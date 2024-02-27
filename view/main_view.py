# arquivos do projeto
import view.multi_view as mpf
import view.single_view as spf
from view.interface_view import InterfaceView
#

from tkinter import *
from tkinter import ttk

class MainView(InterfaceView):
    def __init__(self, root:Tk):
        self._win = root
        self._win_config()
        
        self._note= ttk.Notebook(self._win)
        self._note.pack(fill='both')

        self.multi_print_frame = mpf.MultiPrintFrame(self._note)
        self.single_print_frame = spf.SinglePrintFrame(self._note)

        self._note.add(self.multi_print_frame,text="Múltiplas")
        self._note.add(self.single_print_frame,text="Único")

    # configura a janela
    def _win_config(self):
        self._win.title("Impressão de etiquetas")
        self._win.geometry("520x223")
        self._win.resizable(FALSE,FALSE)

    def run(self):
        self._win.mainloop()