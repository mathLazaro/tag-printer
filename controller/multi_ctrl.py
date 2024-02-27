import view.multi_view as MPF
from model.tag import Tag

from tkinter import filedialog
from tkinter import messagebox

import pandas as pd
from win32print import EnumPrinters
from pathlib import Path
import warnings


class MultiController:
    def __init__(self, view:MPF.MultiPrintFrame, main_ctrl):
        self._view = view
        self._main = main_ctrl

        # paths needed to print file
        self._folder = None
        self._printer = None

        self._view.add_callbacks('GET_PATH_FOLDER',self._callback_get_path_folder)
        self._view.add_callbacks('GET_PRINTER',self._callback_get_printer)
        self._view.add_callbacks('PRINT',self._callback_print)
        
        self._view.bind_comands()
        self._set_printer()

    # bind printer names to combobox
    def _set_printer(self):
        printers = EnumPrinters(2)
        self._printer_list = []

        for imp in printers:
            self._printer_list.append(str(imp[2]))
        
        self._view.combo_printer['values'] = self._printer_list

    # read data on excel file
    def _get_list(self, excel_path, sheet) -> list:
        warnings.simplefilter(action='ignore', category=UserWarning)

        patient_list = []        
        col = ["IMPRIMIR","NOME","HC","LEITO"]

        if excel_path == None:
            raise Exception('Diretório da planilha não definida')
        

        data = pd.read_excel(excel_path, sheet_name=sheet, usecols=col)

        for i in range(len(data)):
            if str(data.loc[i,"IMPRIMIR"]) == 'True':
                name = str(data.loc[i,"NOME"])
                
                if data.isnull().loc[i,"HC"]:
                    hc = ''
                else:
                    hc = str(int(data.loc[i,"HC"]))

                if data.isnull().loc[i,"LEITO"]:
                    room = ''
                else:
                    room = str(data.loc[i,"LEITO"])

                patient_list.append(Tag(name, hc, room))
        
        warnings.resetwarnings()
        return patient_list

    def _callback_get_path_folder(self,event):
        path = filedialog.askopenfile(filetypes=(('Microsoft Excel',['.xlsx','.xls']),('Todos os arquivos','*.')))
        if path != None:
            self._view.folder_path.configure(text=str(path.name))
            self._folder = Path(path.name)

    def _callback_get_printer(self,event):
        printer_selected = self._view.input_printer
        self._printer = printer_selected.get()

    def _callback_print(self, event):
        try:
            sheet = self._view.input_sheet.get()
            list_folders = self._get_list(self._folder, sheet)

            for fl in list_folders:
                fl.print_file(self._printer, self._main.files)
        except Exception as error:
            messagebox.showerror('Input missing',error)