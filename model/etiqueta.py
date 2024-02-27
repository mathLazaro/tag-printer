from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import cm
from win32print import SetDefaultPrinter
from win32api import ShellExecute
from pathlib import Path

class Etiqueta:
    def __init__(self, nome, hc, leito):
        self.nome = nome
        self.leito = leito
        self.hc = hc

    # getters

    @property
    def nome(self):
        list_name = (str(self.__nome).rstrip()).split(' ')
        full_name = ''

        for name in list_name:
            if len(full_name) == 0:
                full_name += name.capitalize()
            else:
                full_name += ' ' + name.capitalize()

        return full_name
    
    @property
    def hc(self):
        return self.__hc
    
    @property
    def leito(self):
        return self.__leito

    # setters
        
    @nome.setter
    def nome(self, value):
        if len(value) == 0:
            raise ValueError('Deve ser inserido pelo menos o nome do paciente')
        else:
            self.__nome = value

    @hc.setter
    def hc(self, value):
        if len(value) == 0:
            self.__hc = '---'
            return
        self.__hc = value

    @leito.setter
    def leito(self, value):
        if len(value) == 0:
            self.__leito = '---'
            return
        self.__leito = value

    ##

    # retorna o diretorio do pdf gerado para ser deletado posteriormente
    def print_file(self, printer, parent_path):
        if printer == None:
            raise Exception('Deve ser selecionada a impressora de etiqueta')

        pdf_name = self.hc + '.pdf'

        # criando o pdf
        pdf = Canvas(parent_path + '\\' + pdf_name, (5 * cm,3 * cm))
        pdf.setFont('Times-Bold',10)
        
        # Formando a etiqueta
        if len(self.nome) < 20:
            pdf.drawString(0.20*cm,2.25*cm,'Nome: ' + self.nome)
            pdf.drawString(0.20*cm,1.5*cm,'HC: ' + self.hc)
            pdf.drawString(0.20*cm,0.75*cm,'Leito: ' + self.leito)

        else:
            list_name = self.nome.split(' ')
            first_line = ''
            second_line = ''

            for name in list_name:
                if len(first_line) + len(name) + 1 < 20:
                    if len(first_line) == 0:
                        first_line = name
                    else:
                        first_line += ' ' + name
                else:
                    if len(second_line) == 0:
                        second_line = name
                    else:
                        second_line += ' ' + name
            
            pdf.drawString(0.20*cm,2.25*cm,'Nome: ' + first_line)
            pdf.drawString(0.40*cm,1.85*cm, second_line)
            pdf.drawString(0.20*cm,1.35*cm,'HC: ' + self.hc)
            pdf.drawString(0.20*cm,0.85*cm,'Leito: ' + self.leito)
            


        pdf.save()

        # Imprimindo a etiqueta
        SetDefaultPrinter(printer)
        ShellExecute(0,"print", pdf_name, None, parent_path, 1)