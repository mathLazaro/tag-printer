# arquivos do projeto
from view.main_view import *
from controller.multi_ctrl import MultiController
from controller.single_ctrl import SingleController
# 

import os
from shutil import rmtree

class MainController:
    def __init__(self):
        # Create a new folder to place temp pdf files
        try:
            os.mkdir(os.path.join(os.getcwd(),'pdfs_gerados'))
        except:
            pass

        self.__files = str(os.path.join(os.getcwd(),'pdfs_gerados'))

        root = Tk()

        view = MainView(root)

        MultiController(view.multi_print_frame, self)
        SingleController(view.single_print_frame, self)        

        view.run()

    @property
    def files(self):
        return self.__files

    def __del__(self):
        rmtree(self.__files)