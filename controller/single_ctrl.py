from view.single_view import SinglePrintFrame
from model.tag import Tag

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

     # bind printer names to combobox
    def _set_printer(self):
        printers = win32print.EnumPrinters(2)
        self._printer_list = []

        for imp in printers:
            self._printer_list.append(str(imp[2]))
        
        self._view.comboPrinter['values'] = self._printer_list

    def _callback_get_printer(self,event):
        printer_selected = self._view.inputPrinter
        self._printer = printer_selected.get()

    def _callback_print(self,event):
        name = str(self._view.inputNome.get())
        user = str(self._view.inputUsuario.get())
        room = str(self._view.inputLeito.get())

        try:
            et = Tag(name, user, room)
            et.print_file(self._printer, self._main.files)
        except ValueError as error:
            messagebox.showerror('Input missing', error)
        except Exception as error:
            messagebox.showerror('Input missing', error)