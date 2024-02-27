# arquivos do projeto
from view.interface_view import InterfaceView
#

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

class MultiPrintFrame(Frame, InterfaceView):
    def __init__(self,win:Tk):
        Frame.__init__(self,win)
        InterfaceView.__init__(self)

        folder_icon = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(),'icon','folder_icon.png')).resize((12,12)))
        
        excel_field = Frame(self)
        printer_field = Frame(self)
        button_field = Frame(self)

        # Label de informação

        Label(excel_field,text="Arquivo de planilha:").pack(side=TOP,anchor=W,pady=5)
        label_field = Frame(printer_field)
        Label(label_field,text="Impressora:").pack(side=LEFT,anchor=W,pady=5)
        Label(label_field,text='Sheet:').pack(side=RIGHT,anchor=E,padx=6,pady=5,ipadx=115)
        label_field.pack(side=TOP,fill=X)

        # Campo do caminho de arquivo

        self.folder_path = Label(excel_field,
                               text='Diretório',
                               background='white',
                               borderwidth=2,
                               relief='sunken',
                               width=60,
                               anchor=W)
        self.folder_path.pack(side=LEFT,anchor=W)

        # botão para inserir caminho do arquivo

        self.folder_path_button = Button(excel_field,
                                  image=folder_icon,
                                  width=15,
                                  height=15)
        
        self.folder_path_button.image = folder_icon
        self.folder_path_button.pack(side=LEFT,anchor=W)

        # Campo para inserir a Impressora

        self.input_printer = StringVar()
        self.combo_printer = ttk.Combobox(printer_field,
                                  width=45
                                  ,textvariable=self.input_printer
                                  ,state='readonly')
        self.combo_printer.pack(side=LEFT,anchor=W)
        
        # Campo para selecionar o tamanho da fonte

        self.input_sheet = StringVar()
        self._combo_sheet = ttk.Combobox(printer_field,
                                  width=22
                                  ,textvariable=self.input_sheet
                                  ,state='readonly')
        self._combo_sheet.pack(side=LEFT,anchor=W,padx=3)
        self._combo_sheet['values'] = ['PACIENTES AGUDOS','TX','CONTÍNUAS','EM DIALISE','CONSERVADOR']
        self._combo_sheet.current(0)

        ## Botão de imprimir
    
        self._button_print = Button(button_field,
                             text='Imprimir',
                             width=10)
        self._button_print.pack(side=TOP)

        # Frame pack
        
        Frame(self).pack(pady=5)
        excel_field.pack(side=TOP,fill=X,padx=30,pady=5)
        printer_field.pack(side=TOP,fill=X,padx=30,pady=5)
        Frame(self).pack(pady=5)
        button_field.pack(side=TOP,fill=X,padx=35,pady=5 )

    # bind dos callbacks
    def bind_comands(self):
        self.folder_path_button.bind('<Button>',self.getCallbacks['GET_PATH_FOLDER'])
        self.combo_printer.bind('<<ComboboxSelected>>',self.getCallbacks['GET_PRINTER'])
        self._button_print.bind('<Button>',self.getCallbacks['PRINT'])