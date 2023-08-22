from tkinter import *
from tkinter import filedialog

root = Tk()
root.iconbitmap("C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects\\pythonicon.ico")
root.title('Text Editor')

global file_saved_name
file_saved_name = False

global selected_data
selected_data = False



def newfile():
    text.delete('1.0', END)
    root.title('New Text Pad')
    statusbar.config(text='New File       ')


def openfile():
    text.delete('1.0',END)

    textfile = filedialog.askopenfilename(initialdir='C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects', filetypes=(('textfiles','*.txt'),('python files','*.py'),('All files','*.*')))
    if textfile:
        global file_saved_name
        file_saved_name = textfile
    
    filename = textfile
    statusbar.config(text=filename)


    textfile = open(textfile, 'r')
    textdata = textfile.read()
    text.insert(END,textdata)
    textfile.close()


def saveasfile():
    global file_saved_name
    textfile = filedialog.asksaveasfilename(defaultextension='.*', initialdir='C:\\Users\\smuna\\OneDrive\\Documents\\python swathi\\codeclausepythonprojects', filetypes=(('textfiles','*.txt'),('python files','*.py'),('All files','*.*')))
    if textfile:
        filename = textfile
        statusbar.config(text='saved: '+filename)

        textfile = open(textfile, 'w')
        textfile.write(text.get('1.0',END))
        textfile.close()    


def savefile():
    global file_saved_name
    if file_saved_name:
        textfile = open(file_saved_name, 'w')
        textfile.write(text.get('1.0',END))
        textfile.close()
        filename = textfile
        statusbar.config(text='Saved: '+file_saved_name)

    else:
        saveasfile()


def cut_text(e):
    global selected_data
    selected_data = text.selection_get()

    text.delete('sel.first','sel.last')

def copy_text(e):
    global selected_data
    selected_data = text.selection_get()
    

def paste_text(e):

    cursor_position = text.index(INSERT)
    text.insert(cursor_position,selected_data)


frame = Frame(root)
frame.pack(pady=5)

scroll = Scrollbar(frame)
scroll.pack(side=RIGHT, fill=Y)

text = Text(frame, width=60, height=30, font=('Times New Roman', 12), selectbackground='yellow', selectforeground='black', undo=True, yscrollcommand=scroll)
text.pack(pady=5)

scroll.config(command=text)

menubar = Menu(root)
root.config(menu = menubar)

filemenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = 'New', command=newfile)
filemenu.add_command(label = 'Open', command=openfile)
filemenu.add_command(label = 'Save', command=savefile)
filemenu.add_command(label = 'Save as', command=saveasfile)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command=root.quit)

editmenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = 'Cut', command=lambda: cut_text(False))
editmenu.add_command(label = 'Copy',command=lambda: copy_text(False))
editmenu.add_command(label = 'Paste',command=lambda: paste_text(False))
editmenu.add_command(label = 'Undo', command=text.edit_undo)
editmenu.add_command(label = 'Redo', command=text.edit_redo)


statusbar = Label(root, text='Ready      ', anchor=E)
statusbar.pack(fill=X, side=BOTTOM)




root.mainloop()