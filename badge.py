# coding: utf-8

from tkinter import *

def accueil():
    fenetre = Tk()

    label = Label(fenetre, text="Veuillez passez votre badge")
    # label.pack(pady=20, padx=20)
    label.pack()
    fenetre.geometry("400x300")
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    fenetre.mainloop()