import tkinter as tk
from tkinter import ttk


class Boton(tk.Button):
    def __init__(self, master, text):
        super().__init__(master=master, justify='center', text=text, command=self.clicked)
        
    def clicked(self):
        print('Se ha pulsado el boton:', self.cget('text'))

class Canvas(tk.Canvas):

    def __init__(self, master, height, width):
        
        super().__init__(master=master, border=5, borderwidth=0, height=height, width=width, background='yellow')

        self.scroll = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.scroll.pack(side=tk.RIGHT, fill='y')

        self.configure(yscrollcommand=self.scroll.set)

        self.panel = ttk.PanedWindow(self, orient=tk.VERTICAL, name='prueba', width=340)
        self.panel.pack(fill='x', padx=5)


        self.pack(side=tk.LEFT, fill='x', expand=True)

        self.create_window((4,4), window=self.panel, anchor='nw', tags='self.panel')

        self.panel.bind('<Configure>', lambda: self.configure(scrollregion=self.bbox('all')))

        for i in range(15):
            self.panel.add(Boton(self.panel, text=f'Boton {i}'))




window = tk.Tk()
window.title("Prueba")
window.geometry('350x500')
window.configure(background='red')

# p = ttk.PanedWindow(window, orient=tk.VERTICAL, name='prueba', width=340, height=400)
# p.pack(fill='x', padx=5)
# for i in range(15):
#     p.add(Boton(p, text=f'Boton {i}'))

a = Canvas(window, height=400, width=345)

window.mainloop()

