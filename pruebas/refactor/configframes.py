import tkinter as tk
from tkinter import ttk

class ConfigFrame(tk.Frame):
    def __init__(self, *arg, savePath = None, **args):
        tk.Frame.__init__(self, *arg, **args)

        self.savePath = savePath