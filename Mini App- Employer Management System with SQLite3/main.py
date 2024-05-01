import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import customtkinter
import database as db

customtkinter.set_appearance_mode("dark")
customtkinter.set_appearance_mode("dark-blue")

def centerWindow(w, h):
    screenW = root.winfo_screenwidth()
    screenH = root.winfo_screenheight()

    x = (screenW/2) - (w/2)
    y = (screenH/2.2) - (h/2)

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

def addToTree():
    employees = db.fetchWorker()
    myTree.delete(*myTree.get_children())
    for employee in employees:
        myTree.insert('', END, values=employee)

def insert():
    id = idEntry.get()
    name = nameEntry.get()
    teilnehmer_ID = teilnehmerIdEntry.get()
    benutzer_ID = benutzerIdEntry.get()
    pin = pinEntry.get()
    svnr = svnrEntry.get()
    status = statusEntry.get()
    geld = geldEntry.get()
    details = detailsEntry.get()
    if not(id and name and teilnehmer_ID and benutzer_ID and pin and 
           svnr and status and geld and details):
        messagebox.showerror('Error!', 'Bitte, füll alle Felder aus!')
    elif db.idExists(id):
        messagebox.showerror('Error!', 'Die ID existiert schon!')
    else:
        db.insertWorker(id, name, teilnehmer_ID, benutzer_ID, pin, svnr, status, geld, details)
        addToTree()
        messagebox.showinfo('Erfolg!', 'Die Daten wurden erfolgreich eingefügt!')

def clear(*clicked):
    if clicked:
        myTree.selection_remove(myTree.focus())
    idEntry.delete(0, END)
    nameEntry.delete(0, END)
    teilnehmerIdEntry.delete(0, END)
    benutzerIdEntry.delete(0, END)
    pinEntry.delete(0, END)
    svnrEntry.delete(0, END)
    statusEntry.delete(0, END)
    geldEntry.delete(0, END)
    detailsEntry.delete(0, END)

def displayData(event):
    selEmployee = myTree.focus()
    if selEmployee:
        row = myTree.item(selEmployee)['values'] 
        clear()
        idEntry.insert(0, row[0])
        nameEntry.insert(0, row[1])
        teilnehmerIdEntry.insert(0, row[2])
        benutzerIdEntry.insert(0, row[3])
        pinEntry.insert(0, row[4])
        svnrEntry.insert(0, row[5])
        statusEntry.insert(0, row[6])
        geldEntry.insert(0, row[7])
        detailsEntry.insert(0, row[8])
    else:
        pass

def update():
    selEmployee = myTree.focus()
    if not selEmployee:
        messagebox.showerror('Error!', 'Bitte wählen Sie einen Arbeiter, der aktualisiert wird!')
    else:
        id = idEntry.get()
        name = nameEntry.get()
        teilnehmer_ID = teilnehmerIdEntry.get()
        benutzer_ID = benutzerIdEntry.get()
        pin = pinEntry.get()
        svnr = svnrEntry.get()
        status = statusEntry.get()
        geld = geldEntry.get()
        details = detailsEntry.get()
        db.updateWorker(name, teilnehmer_ID, benutzer_ID, pin, svnr, status, geld, details, id)
        addToTree()
        clear()
        messagebox.showinfo('Erfolg!', 'Die Datei wurden erfolgriech aktualisiert!')

def delete():
    selEmployee = myTree.focus()
    if not selEmployee:
        messagebox.showerror('Error!', 'Bitte wählen Sie einen Arbeiter, der gelöscht wird!')
    else:
        id = idEntry.get()
        db.deleteWorker(id)
        addToTree()
        clear()
        messagebox.showinfo('Erfolg!', 'Die Datei wurden erfolgriech gelöscht!')

root = customtkinter.CTk()
root.title("Emin Hodzic <> Mini Employee Management System")
root.iconbitmap("Assets//e.ico")
centerWindow(1480, 700)
root.resizable(False, False)

font1 = ('Helvetica', 25, "bold")
font2 = ('Helvetica', 12, "bold")

#########################################################
idLabel = customtkinter.CTkLabel(root, font=font1, text="ID:", text_color="#fff")
idLabel.place(x=30, y=30)

idEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
idEntry.place(x=210, y=28)

nameLabel = customtkinter.CTkLabel(root, font=font1, text="Name:", text_color="#fff")
nameLabel.place(x=30, y=90)

nameEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
nameEntry.place(x=210, y=88)

teilnehmerIdLabel = customtkinter.CTkLabel(root, font=font1, text="Teilnehmer ID:", text_color="#fff")
teilnehmerIdLabel.place(x=30, y=150)

teilnehmerIdEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
teilnehmerIdEntry.place(x=210, y=148)

benutzerIdLabel = customtkinter.CTkLabel(root, font=font1, text="Benutzer ID:", text_color="#fff")
benutzerIdLabel.place(x=30, y=210)

benutzerIdEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
benutzerIdEntry.place(x=210, y=208)

pinLabel = customtkinter.CTkLabel(root, font=font1, text="P I N:", text_color="#fff")
pinLabel.place(x=30, y=270)

pinEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
pinEntry.place(x=210, y=268)

svnrLabel = customtkinter.CTkLabel(root, font=font1, text="S V N R:", text_color="#fff")
svnrLabel.place(x=30, y=330)

svnrEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
svnrEntry.place(x=210, y=328)

statusLabel = customtkinter.CTkLabel(root, font=font1, text="Status:", text_color="#fff")
statusLabel.place(x=30, y=390)

statusEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
statusEntry.place(x=210, y=388)

geldLabel = customtkinter.CTkLabel(root, font=font1, text="Geld:", text_color="#fff")
geldLabel.place(x=30, y=450)

geldEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
geldEntry.place(x=210, y=448)

detailsLabel = customtkinter.CTkLabel(root, font=font1, text="Details:", text_color="#fff")
detailsLabel.place(x=30, y=510)

detailsEntry = customtkinter.CTkEntry(root, font=font1, text_color="#fff", border_color="#fff", border_width=3, width=200)
detailsEntry.place(x=210, y=508)
#########################################################

#########################################################
insertEmployee = customtkinter.CTkButton(root, command=insert,font=font1, text_color="#fff", text='Hinzufügen', fg_color='#242424',
                                         border_width=1, border_color="#144870", cursor='hand2', corner_radius=5, width=170)
insertEmployee.place(x=25, y=570)

clearEmployee = customtkinter.CTkButton(root, command=lambda:clear(True),font=font1, text_color="#fff", text='Neu', fg_color='#242424',
                                         border_width=1, border_color="#144870", cursor='hand2', corner_radius=5, width=170)
clearEmployee.place(x=241, y=570)

deleteEmployee = customtkinter.CTkButton(root, command=delete, font=font1, text_color="#fff", text='Löschen', fg_color='#242424',
                                         border_color='#B80F0A', hover_color='#B80F0A', border_width=1, cursor='hand2', corner_radius=5, width=170)
deleteEmployee.place(x=25, y=620)

updateEmployee = customtkinter.CTkButton(root, command=update, font=font1, text_color="#fff", text='Aktualisieren', fg_color='#242424', 
                                         border_width=1, border_color="#144870", cursor='hand2', corner_radius=5, width=170)
updateEmployee.place(x=241, y=620)

style = ttk.Style(root)
style.theme_use('clam')
style.configure('Treeview', font=font2, foreground='#000', fieldbackground='"#242424')
style.map('Treeview', backgorund=[('selected', '#144870')])

treeFrame = Frame(root)
treeFrame.place(x=550, y=25)

scrollBar = Scrollbar(treeFrame)
scrollBar.pack(side=RIGHT, fill=Y)

myTree = ttk.Treeview(treeFrame, height=39, yscrollcommand=scrollBar.set)

scrollBar.config(command=myTree.yview)

myTree['columns'] = ('ID', 'Name', 'Teilnehmer-ID', 'Benutzer-ID', 'PIN', 'SVNR', 'Status', 'Geld', 'Details')

myTree.column('#0', width=0, stretch=tk.NO) #hide the default 1. column
myTree.column('ID', anchor=tk.CENTER, width=120)
myTree.column('Name', anchor=tk.CENTER, width=160)
myTree.column('Teilnehmer-ID', anchor=tk.CENTER, width=160)
myTree.column('Benutzer-ID', anchor=tk.CENTER, width=115)
myTree.column('PIN', anchor=tk.CENTER, width=150)
myTree.column('SVNR', anchor=tk.CENTER, width=160)
myTree.column('Status', anchor=tk.CENTER, width=160)
myTree.column('Geld', anchor=tk.CENTER, width=80)
myTree.column('Details', anchor=tk.CENTER, width=150)

myTree.heading('ID', text='ID')
myTree.heading('Name', text='Name')
myTree.heading('Teilnehmer-ID', text='Teilnehmer-ID')
myTree.heading('Benutzer-ID', text='Benutzer-ID')
myTree.heading('PIN', text='PIN')
myTree.heading('SVNR', text='SVNR')
myTree.heading('Status', text='Status')
myTree.heading('Geld', text='Geld')
myTree.heading('Details', text='Details')

myTree.pack()
###########################################

###########################################
addToTree()

myTree.bind('<ButtonRelease>', displayData)

root.mainloop()