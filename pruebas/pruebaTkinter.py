import tkinter as tk

window = tk.Tk()
window.title("Prueba")
window.geometry('350x200')

lbl = tk.Label(window, text='mi etiqueta', font=('Arial Bold', 12))
tk.Label(window, text='JA').grid(column=0, row=0)
tk.Label(window, text='JA').grid(column=0, row=1)
tk.Label(window, text='JA').grid(column=1, row=0)
lbl.grid(column=1, row=1)

window.mainloop()

