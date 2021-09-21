import tkinter as tk
from tkinter import ttk

'''
    Idea: que aquello con lo que poblemos el frame que se escrollea sean Frames con botones dentro
    y no botones directamente. Su propia clase y asi podemos añadir ahi logica luego cuando cada
    frame de estos sea para un parametro concreto.
'''

# class MiniFrame(tk.Frame):
#     def __init__(self, size, master=None, cnf={}, **kw):
#         super().__init__(master=master, cnf=cnf, **kw)
#         self._size = size
#         self.configure()
    

# class Boton(tk.Button):
#     def __init__(self, master, num):
#         self._num = num
#         self.frame = tk.Frame(master)
#         super().__init__(master=self.frame, justify='center', text=f'Boton {num}', command=self.clicked)
#         self.pack(fill='x')
        
#     def clicked(self):
#         print('Se ha pulsado el boton:', self.cget('text'))
#         self._num += 1
#         self.configure(text=f'Boton {self._num}')


# class ParamFrame(tk.Frame):

#     def __init__(self, master=None, cnf={}, **kw):
#         super().__init__(master=master, cnf=cnf, **kw)

#         self.count = 0

#         self._scroll_canvas = tk.Canvas(self, borderwidth=0, border=0, background='black')
#         self._param_container = tk.Frame(self._scroll_canvas, background='white')
#         self._scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self._scroll_canvas.yview)
#         self._scroll_canvas.configure(yscrollcommand=self._scrollbar.set)

#         self._scrollbar.pack(side=tk.RIGHT, fill='y')
#         self._scroll_canvas.pack(side=tk.LEFT, fill='both', expand=True)
#         self._scroll_canvas.create_window((0,0), window=self._param_container, anchor='nw', tags='self._param_container')
#         self._param_container.bind('<Configure>', self.onFrameConfigure)
        
#         self.populate()
        

#     def onFrameConfigure(self, evet):
#         '''Reset the scroll region to encompass the inner frame'''
#         self._scroll_canvas.configure(scrollregion=self._scroll_canvas.bbox('all'))
#         print(self.count)
#         self.count += 1

#     def populate(self):
#         for i in range(15):
#             Boton(self._param_container, i).pack(fill='x')



# if __name__ == '__main__':
#     window = tk.Tk()
#     window.title("Prueba")
#     window.geometry('400x600')
#     window.configure(background='red')

#     # a = ParamFrame(window)
#     # a.pack(side=tk.TOP, fill='x', expand=False, padx=5, pady=5, anchor='n')
    
#     # lista = []
#     # for i in range(50):
#     #     lista.append(Boton(window, i).pack(fill='x'))

#     # b = tk.Listbox(window, listvariable=lista)

#     b = tk.Listbox(window)
#     b.pack(side=tk.LEFT, fill='both', expand=True)

#     s = tk.Scrollbar(window, orient=tk.VERTICAL)
#     s.pack(side=tk.RIGHT, fill='y')

#     for i in range(50):
#         b.insert(tk.END, Boton(b, i))

#     b.configure(yscrollcommand=s.set)
#     s.configure(command=b.yview)
    
#     window.mainloop()

# ==================================================================================================================================================================================

class ConfigFrame(tk.Frame):
    def __init__(self, *arg, **args):
        tk.Frame.__init__(self, *arg, **args)



if __name__ == '__main__':
    window = tk.Tk()
    window.title("Prueba")
    window.geometry('400x600')
    window.configure(background='red')
    window.update_idletasks()
    window.grid(baseWidth=100, baseHeight=100, widthInc=window.winfo_width(), heightInc=window.winfo_height())

    a = tk.Frame(window, bg='yellow')
    a.grid(column=0, row=0, sticky='nesw', padx=5, pady=5)
    # tk.Label(a, text='hola').pack(fill='both', expand=True)
    # a.pack(fill='both', expand=True, padx=5, pady=5)
    b = tk.Frame(window, bg='green')
    b.grid(column=0, row=1, sticky='nesw')
    # tk.Label(b, text='hola').pack(fill='both', expand=True)
    # b.pack(fill='both', expand=True, padx=5, pady=5)

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=3)
    window.grid_rowconfigure(1, weight=1)
    # window.grid_anchor('center')
    


    window.mainloop()




