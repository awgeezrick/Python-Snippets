"""
4 demo class components (subframes) on one window;
there are 5 Quitter buttons on this one window too, and each kills entire gui;
GUIs can be reused as frames in container, independent windows, or processes;
"""

from Tkinter import *
from quitter import Quitter

demoModules = ['demoDlg', 'demoCheck', 'demoRadio', 'demoScale']
parts = []


def addComponents(root):
    for demo in demoModules:
        module = __import__(demo)  # import by name string
        part = module.Demo(root, bd=6, relief=RIDGE)  # attach an instance and pass config options (i.e. **options)
#        part = module.Demo(root)  # attach an instance
#        part.config(bd=2, relief=GROOVE)  # or pass config
        part.pack(side=LEFT, expand=YES, fill=BOTH)
        parts.append(part)


def dumpState():
    for part in parts:
        print part.__module__ + ':'
        if hasattr(part, 'report'):
            part.report()
        else:
            print 'none'

root = Tk()  # make explicit root first
root.title('Frames')
Label(root, text='Mulitple Frame Demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()
