import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import database

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

#### Function to center the window ####
def centerWindow(w, h):
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()

    x = (screenW/2) - (w/2)
    y = (screenH/2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def addToTree():
    employees = database.fetchEmployees()
    myTree.delete(*myTree.get_children())
    for employee in employees:
        myTree.insert('', END, values=employee)


def insert():
    id = idEntry.get()
    name = nameEntry.get()
    nachname = nachnameEntry.get()
    jahre = jahreEntry.get()
    status = var1.get()
    if not(id and name and nachname and jahre and status):
        messagebox.showerror('Error!', 'Fill out all of the fields!')
    elif database.idExistent(id):
        messagebox.showerror('Error!', 'The ID already exists!')
    else:
        database.insertEmployees(id, name, nachname, jahre, status)
        addToTree()
        messagebox.showinfo('Success!', 'Data has been successfully inserted!')

def clear(*clicked):
    if clicked:
# This removes the highlight on the employee that is selected in the treeview #
        myTree.selection_remove(myTree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    nachnameEntry.delete(0, END)
    jahreEntry.delete(0, END)
    var1.set('Active')

def displayData(event):
    selectedEmp = myTree.focus()
    if selectedEmp:
        row = myTree.item(selectedEmp)['values']
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        nachnameEntry.insert(0, row[2])
        jahreEntry.insert(0, row[3])
        var1.set(row[4])
    else:
        pass

def update():
    selectedEmp = myTree.focus()
    if not selectedEmp:
        messagebox.showerror('Error!', 'Choose an employee to update them!')
    else:
        id = idEntry.get()
        name = nameEntry.get()
        nachname = nachnameEntry.get()
        jahre = jahreEntry.get()
        status = var1.get()
        database.updateEmployees(name, nachname, jahre, status, id)
        addToTree()
        clear()
        messagebox.showinfo('Success!', 'Data has been successfully updated!')

def delete():
    selectedEmp = myTree.focus()
    if not selectedEmp:
        messagebox.showerror('Error!', 'Choose an employee to delete them!')
    else:
        id = idEntry.get()
        database.deleteEmployees(id)
        addToTree()
        clear()
        messagebox.showinfo('Success!', 'Data has been successfully deleted!')

################### MAIN ###################
root = customtkinter.CTk()
root.title('Emin Hodzic <> Employee Management System mit Tutorial')
import os

icon_path = os.path.join(os.path.dirname(__file__), "Assets", "e.ico")
if os.path.exists(icon_path):
    root.iconbitmap(icon_path)
else:
    print("Warning: Icon file not found. Using default icon.")
centerWindow(1150, 630)
root.resizable(False, False)

font1 = ('Helvetica', 20, 'bold')
font2 = ('Helvetica', 12, 'bold')


##################
idLabel = customtkinter.CTkLabel(root, font=font1, text='ID:', text_color='#fff')
idLabel.place(x=40, y=40)

idEntry = customtkinter.CTkEntry(root, font=font1, text_color='#fff', border_color='#fff', border_width=2, width=180)
idEntry.place(x=150, y=40)

nameLabel = customtkinter.CTkLabel(root, font=font1, text='Name:', text_color='#fff')
nameLabel.place(x=40, y=100)

nameEntry = customtkinter.CTkEntry(root, font=font1, text_color='#fff', border_color='#fff', border_width=2, width=180)
nameEntry.place(x=150, y=100)

nachnameLabel = customtkinter.CTkLabel(root, font=font1, text='Nachname:', text_color='#fff')
nachnameLabel.place(x=40, y=160)

nachnameEntry = customtkinter.CTkEntry(root, font=font1, text_color='#fff', border_color='#fff', border_width=2, width=180)
nachnameEntry.place(x=150, y=160)

jahreLabel = customtkinter.CTkLabel(root, font=font1, text='Jahre:', text_color='#fff')
jahreLabel.place(x=40, y=220)

jahreEntry = customtkinter.CTkEntry(root, font=font1, text_color='#fff', border_color='#fff', border_width=2, width=180)
jahreEntry.place(x=150, y=220)

statusLabel = customtkinter.CTkLabel(root, font=font1, text='Status:', text_color='#fff')
statusLabel.place(x=40, y=280)

option = ['Active', 'Inactive']
var1 = StringVar()

statusOption = customtkinter.CTkComboBox(root, font=font1, text_color='#fff', variable=var1, values=option, state='readonly',width=180)
statusOption.set('Active')
statusOption.place(x=150, y=280)
###################

###################
insertEmployee = customtkinter.CTkButton(root, command=insert, font=font1, text_color='#fff', text='Add Employee', fg_color='#242424', 
                                         border_color='#106a43', border_width=2, cursor='hand2', corner_radius=5, width=290)
insertEmployee.place(x=40, y=370)

clearEmployee = customtkinter.CTkButton(root, command=lambda:clear(True), # <- this will enable the func to stop highlighting the selected employee
                                        font=font1, text_color='#fff', text='New Employee', fg_color='#242424', 
                                        border_color='#106a43', border_width=2, cursor='hand2', corner_radius=5, width=290)
clearEmployee.place(x=40, y=420)

updateEmployee = customtkinter.CTkButton(root, command=update, font=font1, text_color='#fff', text='Update Employee', fg_color='#242424', 
                                         border_color='#106a43', border_width=2, cursor='hand2', corner_radius=5, width=290)
updateEmployee.place(x=40, y=470)

deleteEmployee = customtkinter.CTkButton(root, command=delete, font=font1, text_color='#fff', text='Delete Employee', fg_color='#242424', 
                                         border_color='#B80F0A', hover_color='#B80F0A', border_width=2, cursor='hand2', corner_radius=5, width=290)
deleteEmployee.place(x=40, y=520)
###################

###################
style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#106a43', fieldbackground='#242424')
style.map('Treeview', background=[('selected', '#106a43')])

myTree = ttk.Treeview(root, height=26)

myTree['columns'] = ('ID', 'Name', 'Nachname', 'Jahre', 'Status')

myTree.column('#0', width=0, stretch=tk.NO) #hide the default 1. column
myTree.column('ID', anchor=tk.W, width=120)
myTree.column('Name', anchor=tk.CENTER, width=160)
myTree.column('Nachname', anchor=tk.CENTER, width=160)
myTree.column('Jahre', anchor=tk.CENTER, width=115)
myTree.column('Status', anchor=tk.CENTER, width=150)

myTree.heading('ID', text='ID')
myTree.heading('Name', text='Name')
myTree.heading('Nachname', text='Nachname')
myTree.heading('Jahre', text='Jahre')
myTree.heading('Status', text='Status')

myTree.place(x=380, y=40)
###################

###################
addToTree()

# when pressing on a row in the treeview, we will be able to start this function #
myTree.bind('<ButtonRelease>', displayData)

root.mainloop()