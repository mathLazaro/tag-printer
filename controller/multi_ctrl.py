# arquivos do projeto
import view.multi_view as MPF
from model.etiqueta import Etiqueta
#

# tkinter
from tkinter import filedialog
from tkinter import messagebox
#

import pandas as pd
from win32print import EnumPrinters
from pathlib import Path
import warnings


class MultiController:
    def __init__(self, view:MPF.MultiPrintFrame, main_ctrl):
        self._view = view
        self._main = main_ctrl

        # diretorios necessários para imprimir
        self._folder = None
        self._printer = None

        self._view.add_callbacks('GET_PATH_FOLDER',self._callback_get_path_folder)
        self._view.add_callbacks('GET_PRINTER',self._callback_get_printer)
        self._view.add_callbacks('PRINT',self._callback_print)
        
        self._view.bind_comands()
        self._set_printer()

    # seta a lista de impressoras no combobox
    def _set_printer(self):
        impressoras = EnumPrinters(2)
        self._lista_impressoras = []

        for imp in impressoras:
            self._lista_impressoras.append(str(imp[2]))
        
        self._view.combo_printer['values'] = self._lista_impressoras

    # lê os dados do excel
    def _get_list(self, excel_path, sheet) -> list:
        warnings.simplefilter(action='ignore', category=UserWarning)

        pacientes = []        
        col = ["IMPRIMIR","NOME","HC","LEITO"]

        if excel_path == None:
            raise Exception('Diretório da planilha não definida')
        

        data = pd.read_excel(excel_path, sheet_name=sheet, usecols=col)

        for i in range(len(data)):
            if str(data.loc[i,"IMPRIMIR"]) == 'True':
                nome = str(data.loc[i,"NOME"])
                
                if data.isnull().loc[i,"HC"]:
                    hc = ''
                else:
                    hc = str(int(data.loc[i,"HC"]))

                if data.isnull().loc[i,"LEITO"]:
                    leito = ''
                else:
                    leito = str(data.loc[i,"LEITO"])

                pacientes.append(Etiqueta(nome, hc, leito))
        
        warnings.resetwarnings()
        return pacientes

    # callback para pegar o diretório do excel
    def _callback_get_path_folder(self,event):
        path = filedialog.askopenfile(filetypes=(('Microsoft Excel',['.xlsx','.xls']),('Todos os arquivos','*.')))
        if path != None:
            self._view.folder_path.configure(text=str(path.name))
            self._folder = Path(path.name)
    
    # callback para pegar a impressora
    def _callback_get_printer(self,event):
        printer_selected = self._view.input_printer
        self._printer = printer_selected.get()

    # callback do botão de imprimir
    def _callback_print(self,event):
        try:
            sheet = self._view.input_sheet.get()
            list_folders = self._get_list(self._folder, sheet)

            for fl in list_folders:
                fl.print_file(self._printer, self._main.files)
        except Exception as error:
            messagebox.showerror('Input missing',error)