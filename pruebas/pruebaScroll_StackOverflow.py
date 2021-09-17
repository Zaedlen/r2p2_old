# import tkinter as tk

# RWIDTH = 400
# RHEIGHT = 600


# class Example(tk.Frame):
#     def __init__(self, parent, rwidth, rheight):

#         tk.Frame.__init__(self, parent)

#         self.canvas = tk.Canvas(self, borderwidth=0, background="black")
#         self.frame = tk.Frame(self.canvas, background="yellow")
#         self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.canvas.configure(yscrollcommand=self.vsb.set)

#         self.vsb.pack(side="right", fill="y")
#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.canvas.create_window((4,4), window=self.frame, anchor="nw",
#                                   tags="self.frame")

#         self.frame.bind("<Configure>", self.onFrameConfigure)
#         # self.canvas.bind('<Configure>', self.onCanvasConfigure)

#         self.populate()

#     def populate(self):
#         '''Put in some fake data'''
#         for row in range(100):
#             tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
#                      relief="solid").grid(row=row, column=0)
#             t="this is the second column for row %s" %row
#             tk.Label(self.frame, text=t).grid(row=row, column=1)
        

#     def onFrameConfigure(self, event):
#         '''Reset the scroll region to encompass the inner frame'''
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def onCanvasConfigure(self, event):
#         self.frame.configure(width=self.canvas.winfo_width())


# if __name__ == "__main__":
#     root=tk.Tk()
#     root.configure(background='red')
#     root.geometry(str(RWIDTH)+'x'+str(RHEIGHT))
#     example = Example(root, RWIDTH, RHEIGHT)
#     example.pack(side="top", fill="both", expand=True)
#     root.mainloop()








# import tkinter as tk
# from tkinter import ttk

# class ScrolledList(ttk.)

# class Example(tk.Frame):
#     def __init__(self, parent):

#         tk.Frame.__init__(self, parent)
#         self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
#         self.frame = tk.Frame(self.canvas, background="#ffffff")
#         self.vsb = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
#         self.canvas.configure(yscrollcommand=self.vsb.set)

#         self.vsb.pack(side="right", fill="y")
#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.canvas.create_window((4,4), window=self.frame, anchor="nw",
#                                   tags="self.frame")

#         self.frame.bind("<Configure>", self.onFrameConfigure)

#         self.populate()

#     def populate(self):
#         '''Put in some fake data'''
#         for row in range(100):
#             tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1",
#                      relief="solid").grid(row=row, column=0)
#             t="this is the second column for row %s" %row
#             tk.Label(self.frame, text=t).grid(row=row, column=1)

#     def onFrameConfigure(self, event):
#         '''Reset the scroll region to encompass the inner frame'''
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

# if __name__ == "__main__":
#     root=tk.Tk()
#     example = Example(root)
#     example.pack(side="top", fill="both", expand=True)
#     root.mainloop()






from tkinter import *

class Scrollable_frame(Frame):

    def __init__(self, parent, title, values):

        self.parent = parent

        Frame.__init__(self, self.parent, background='green')

        self.canvas = Canvas(self, borderwidth=0, background="black")
        self.scrollbar = Scrollbar(self, command=self.canvas.yview)
        self.innerFrame = Radiobutton_frame(self.canvas,title,values)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky= N+S)
        self.scrollbar.grid(row=0, column=1, sticky = N+S)
        self.canvas.create_window((0,0),window = self.innerFrame,anchor="nw",
                                                                tags="my_tag")

        self.canvas.bind("<Configure>", self.set_canvas_scrollregion)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


    def set_canvas_scrollregion(self, event):

        width = event.width - 4
        self.canvas.itemconfigure("my_tag", width=width)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


class Radiobutton_frame(LabelFrame):

    def __init__(self, parent, title, values):

        """            
        In: parent - Canvas
            title - String
            values - List of Int
        """

        self.radiobuttons = {}
        self.parent = parent

        self.selection = StringVar()
        self.selection.set("init")

        LabelFrame.__init__(self, self.parent, text = title, background='yellow')

        for value in values:
            self.add_radiobutton(value)


    def add_radiobutton(self, value):

        """
        Adds a radiobutton to the frame.

        In: item - String
        """

        # Associate to same variable to make them function as a group
        self.radiobuttons[value] = Radiobutton(master = self,
                                                variable = self.selection,
                                                text = value,
                                                value = value)
        self.radiobuttons[value].pack(anchor=W)

# Usage example

root = Tk()
root.configure(background='red')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
scrollableFrame = Scrollable_frame(root, "Canvas not resizing", range(30))
scrollableFrame.grid(row=0, column=0, sticky=N+S+E+W)

if __name__ == '__main__':
    root.mainloop()