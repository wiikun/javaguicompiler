import os
import compf
import tkinter
import tkinter.filedialog
import tkinter.ttk
root = tkinter.Tk()
root.title("javaコンパイラgui")
root.geometry(u"1600x1000")
cpb = tkinter.ttk.Button(root,text = 'file',command=lambda:compf.compilejava())
quitb = tkinter.ttk.Button(root,text='exit',command=lambda:quit())
quitb.pack()
cpb.pack()
root.mainloop()