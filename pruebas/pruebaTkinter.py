import tkinter as tk
from tkinter import ttk

'''
    Idea: que aquello con lo que poblemos el frame que se escrollea sean Frames con botones dentro
    y no botones directamente. Su propia clase y asi podemos añadir ahi logica luego cuando cada
    frame de estos sea para un parametro concreto.
'''

class Boton(tk.Button):
    def __init__(self, master, text):
        super().__init__(master=master, justify='center', text=text, command=self.clicked)
        self.pack(fill='x')
        
    def clicked(self):
        print('Se ha pulsado el boton:', self.cget('text'))


class ParamFrame(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)

        self.count = 0

        self._scroll_canvas = tk.Canvas(self, borderwidth=0, border=0, background='black')
        self._param_container = tk.Frame(self._scroll_canvas, background='white')
        self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self._scroll_canvas.yview)
        self._scroll_canvas.configure(yscrollcommand=self._scrollbar.set)

        self._scrollbar.pack(side=tk.RIGHT, fill='y')
        self._scroll_canvas.pack(side=tk.LEFT, fill='both', expand=True)
        self._scroll_canvas.create_window((0,0), window=self._param_container, anchor='nw', tags='self._param_container')
        self._param_container.bind('<Configure>', self.onFrameConfigure)
        
        self.populate()
        

    def onFrameConfigure(self, evet):
        '''Reset the scroll region to encompass the inner frame'''
        self._scroll_canvas.configure(scrollregion=self._scroll_canvas.bbox('all'))
        print(self.count)
        self.count += 1

    def populate(self):
        for i in range(15):
            Boton(self._param_container, text=f'Boton {i}').pack(fill='x')



if __name__ == '__main__':
    window = tk.Tk()
    window.title("Prueba")
    window.geometry('400x600')
    window.configure(background='red')

    a = ParamFrame(window)
    a.pack(side=tk.TOP, fill='x', expand=True, padx=5, pady=5, anchor='n')

    window.mainloop()

