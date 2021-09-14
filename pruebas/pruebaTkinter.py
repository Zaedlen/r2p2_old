import tkinter as tk

def clicked():
    lbl.configure(text='Button was clicked')


window = tk.Tk()
window.title("Prueba")
window.geometry('350x200')

lbl = tk.Label(window, text='mi etiqueta', font=('Arial Bold', 12)); lbl.grid(column=0, row=0)

btn = tk.Button(window, text='click me', command=clicked); btn.grid(column=1, row=1)

window.mainloop()


