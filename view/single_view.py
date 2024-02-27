# arquivos do projeto
from view.interface_view import InterfaceView
#

from tkinter import *
from tkinter import ttk


class SinglePrintFrame(Frame, InterfaceView):
    def __init__(self, win:Tk):
        Frame.__init__(self, win)
        InterfaceView.__init__(self)
        
        entry_field = Frame(self)
        printer_field = Frame(self)
        button_field = Frame(self)

        # Label de informação

        Label(entry_field,text="Etiqueta: ").pack(side=TOP,anchor=W,pady=2)
        Label(printer_field,text="Impressora: ").pack(side=TOP,anchor=W,pady=2)

        # Input das informações da etiqueta

            ## Label
        nome = Frame(entry_field)
        usuario = Frame(entry_field)
        leito = Frame(entry_field)

        Label(nome,text='Nome').pack(side=LEFT,anchor=W,padx=5,pady=1)
        Label(usuario,text='Usuário').pack(side=LEFT,anchor=W,padx=5,pady=1)
        Label(leito,text='Leito').pack(side=LEFT,anchor=W,padx=5,pady=1)

        nome.pack(anchor=W)
        usuario.pack(anchor=W)
        leito.pack(anchor=W)
            ##

            ## Entry
        self.inputNome = Entry(nome,width=65)
        self.inputUsuario = Entry(usuario,width=64)
        self.inputLeito = Entry(leito,width=66)

        self.inputNome.pack(side=LEFT,anchor=E)
        self.inputUsuario.pack(side=LEFT,anchor=E)
        self.inputLeito.pack(side=LEFT,anchor=E,padx=1)
            #
        
        # Campo para inserir a Impressora
        
        self.inputPrinter = StringVar()
        self.comboPrinter = ttk.Combobox(printer_field,
                                  width=73
                                  ,textvariable=self.inputPrinter
                                  ,state='readonly')
        self.comboPrinter.pack(side=LEFT,anchor=W)
        
        ## Botão de imprimir

        self._buttonPrint = Button(button_field,
                             text='Imprimir',
                             width=10)
        self._buttonPrint.pack(side=TOP)

        entry_field.pack(side=TOP,fill=X,padx=30,pady=5)
        printer_field.pack(side=TOP,fill=X,padx=30,pady=5)
        button_field.pack(side=TOP,fill=X,padx=35,pady=5)

    # bind dos calbacks
    def bind_comands(self):
        self.comboPrinter.bind('<<ComboboxSelected>>',self.getCallbacks['GET_PRINTER'])
        self._buttonPrint.bind('<Button>',self.getCallbacks['PRINT'])
    
