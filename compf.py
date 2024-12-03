import os
import subprocess
import tkinter
import time
def compilejava():
    Static1 = tkinter.Label(text="")
    Static2 = tkinter.Label(text="")
    fTyp = [("javaソースファイル", "*.java")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    file_name = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)
    command = ["javac", file_name]
    try:
        subprocess.check_call(command)
    except:
        Static1 = tkinter.Label(text=u'eroor')
        Static1.pack()
        time.sleep(3)
        Static1.destroy
        return(0)
    Static2 = tkinter.Label(text=u'compile,sucsess')
    Static2.pack()
    time.sleep(3)
    Static2.destroy
    return(0)
