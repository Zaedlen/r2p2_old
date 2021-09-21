from controllerP import ControllerP
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

class ConfigFrame(tk.Frame):
    '''
        ConfigFrame de prueba:
        -   En la versión final no llevara especificamente un atributo ControllerP
            en __init__ sino algo más general.
    '''

    def __init__(self, *arg, controller: ControllerP = ControllerP(), **args):

        # Inicializacion del frame
        tk.Frame.__init__(self, *arg, **args)

        # Obtenemos un controlador para las pruebas
        self.controller = controller

        # Configuracion del grid para este frame
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Frame que contendra la lista de parametros
        self.listaParam = tk.Frame(self, bg='yellow')
        self.listaParam.grid(column=0, row=0, padx=5, pady=5, sticky='nesw')

        # Frame que contendra los botones. Zona de botones
        self.botones = tk.Frame(self)
        self.botones.grid(column=0, row=1, sticky='nesw')
        self.botones.grid_anchor('center')

        # Botones basicos de guardar y cargar
        self.guardarBoton = tk.Button(self.botones, text='Guardar', command=self.onGuardar)
        self.guardarBoton.grid(column=0, row=0,padx=10, sticky='w')
        self.cargarBoton = tk.Button(self.botones, text='Cargar', command=self.onCargar)
        self.cargarBoton.grid(column=1, row=0, padx=10, sticky='w')
    
    def onGuardar(self):
        print(fd.asksaveasfilename())
        # self.controller.guardar_datos(fd.asksaveasfilename())

    def onCargar(self):
        print(fd.askopenfilename())
        # self.controller.cargar_datos(fd.askopenfilename())

    def leerParametros(self):
        pass



if __name__ == '__main__':
    window = tk.Tk()
    window.title("Prueba")
    window.geometry('400x600')
    window.configure(background='red')

    ConfigFrame(window).pack(fill='both', expand=True)

    window.mainloop()

