from controllerP import ControllerP
import tkinter as tk
from tkinter import ttk

class ConfigFrame(tk.Frame):
    def __init__(self, *arg, controller: ControllerP = ControllerP(), **args):
        '''
            ConfigFrame de prueba:
            -   En la versión final no llevara especificamente un atributo ControllerP sino algo más
                general.
        '''
        tk.Frame.__init__(self, *arg, **args)

        self.controller = controller
        self.guardarBoton = tk.Button(self, )
    
    def onGuardar():
        pass