
# arquivos do projeto
from view.single_view import SinglePrintFrame
from model.etiqueta import Etiqueta
#

from tkinter import messagebox
import win32print


class SingleController:
    def __init__(self, view: SinglePrintFrame, main_ctrl):
        self._view = view
        self._main = main_ctrl
        
        self._folder = None
        self._printer = None

        self._view.add_callbacks('GET_PRINTER',self._callback_get_printer)
        self._view.add_callbacks('PRINT',self._callback_print)

        self._view.bind_comands()
        self._set_printer()

    # seta a lista de impressoras no combobox
    def _set_printer(self):
        impressoras = win32print.EnumPrinters(2)
        self._lista_impressoras = []

        for imp in impressoras:
            self._lista_impressoras.append(str(imp[2]))
        
        self._view.comboPrinter['values'] = self._lista_impressoras

    # callback para pegar a impressora
    def _callback_get_printer(self,event):
        printer_selected = self._view.inputPrinter
        self._printer = printer_selected.get()

    # callback do botão de imprimir
    def _callback_print(self,event):
        nome = str(self._view.inputNome.get())
        usuario = str(self._view.inputUsuario.get())
        leito = str(self._view.inputLeito.get())

        try:
            et = Etiqueta(nome, usuario, leito)
            et.print_file(self._printer, self._main.files)
        except ValueError as error:
            messagebox.showerror('Input missing', error)
        except Exception as error:
            messagebox.showerror('Input missing', error)