import view.multi_view as MPF
from model.etiqueta import Etiqueta

from tkinter import filedialog
from tkinter import messagebox

import pandas as pd

from win32print import EnumPrinters
from pathlib import Path


class MultiController:
    def __init__(self, view:MPF.MultiPrintFrame, mainCtrl):
        self._view = view
        self._main = mainCtrl

        self._folder = None
        self._printer = None

        self._view.add_callbacks('GET_PATH_FOLDER',self._get_path_folder)
        self._view.add_callbacks('GET_PRINTER',self._get_printer)
        self._view.add_callbacks('PRINT',self._print)
        self._view.bind_comands()
        self._set_printer()

    def _get_path_folder(self,event):
        path = filedialog.askopenfile(filetypes=(('Microsoft Excel',['.xlsx','.xls']),('Todos os arquivos','*.')))
        if path != None:
            self._view.folder_path.configure(text=str(path.name))
            self._folder = Path(path.name)

    def _set_printer(self):
        impressoras = EnumPrinters(2)
        self._lista_impressoras = []

        for imp in impressoras:
            self._lista_impressoras.append(str(imp[2]))
        
        self._view.combo_printer['values'] = self._lista_impressoras

    def _get_printer(self,event):
        printerSelected = self._view.input_printer
        self._printer = printerSelected.get()
    
    def _get_list(self, path) -> list:
        if path == None:
            raise Exception('Diretório da planilha não definida')
        
        col = []
        for i in range(1,21):
            col.append("p"+str(i).zfill(2))

        data = pd.read_excel(path,usecols=col)

        pacientes = []        

        for c in col:
            if data.notnull().loc[0,c]:
                if data.isnull().loc[1,c]:
                    usuario = ''
                else:
                    usuario = str(data.loc[1,c])

                if data.isnull().loc[2,c]:
                    leito = ''
                else:
                    leito = str(data.loc[2,c])
                
                pacientes.append(Etiqueta(data.loc[0,c],usuario,leito))
                
        return pacientes

    def _print(self,event):
        try:
            list_folders = self._get_list(self._folder)
            size = self._view.input_sheet.get()
            for fl in list_folders:
                self._main.files.append(fl.print_file(self._printer,size))
        except Exception as error:
            messagebox.showerror('Input missing',error)