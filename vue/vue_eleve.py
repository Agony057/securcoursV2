
from tkinter import *
from tkinter import ttk

fenetre = Tk()
fenetre.resizable(width=TRUE, height=TRUE)

div = Frame(fenetre)
div.pack(padx=20,pady=10)  # Ajout du padding à gauche et à droite de 20 pixels
div2 = Frame(fenetre)
div2.pack(pady=25)
div3 = Frame(fenetre)
div3.pack(pady=10)

sous_div1 = Frame(div2, height=200)
sous_div1.grid(row=0, column=0, sticky="nsew")

sous_div2 = Frame(div2)
sous_div2.grid(row=0, column=1, sticky="nsew",pady=25)

# Fonction de mise à jour des données de la liste de gauche en fonction de la classe sélectionnée
def update_data():
    selected_class = variable.get()
    # Mettez à jour les données de la liste de gauche en fonction de la classe sélectionnée
    if selected_class == "2AMA Seconde Bac Pro TMA":
        # Efface les anciennes données
        my_tree.delete(*my_tree.get_children())
        # Insère de nouvelles données
        my_tree.insert(parent='', index='end', iid=0, values=(1, "tijou", "allan"))
        my_tree.insert(parent='', index='end', iid=1, values=(2, "viardot", "tibo"))
    elif selected_class == "1TMA Première Bac Pro TMA":
        # Efface les anciennes données
        my_tree.delete(*my_tree.get_children())
        # Insère de nouvelles données
        my_tree.insert(parent='', index='end', iid=0, values=(3, "dupont", "pierre"))
        my_tree.insert(parent='', index='end', iid=1, values=(4, "martin", "sophie"))
    # Ajoutez des conditions pour les autres classes

# Fonction appelée lorsque vous sélectionnez un élément de la liste de gauche
def on_tree_select(event):
    selected_item = my_tree.focus()  # Récupère l'élément sélectionné
    values = my_tree.item(selected_item, 'values')  # Récupère les valeurs de l'élément sélectionné
    display_options_modif()


def display_options_modif():
    # Efface l ancien DropDownMenu
    for widget in sous_div2.winfo_children():
        widget.destroy()

    # Crée le nouveau DropDownMenu
    variable_modif = StringVar(sous_div2)
    variable_modif.set("Modifier")  # Valeur par défaut

    options_modif = ["Modifier", "Supprimer", "Echanger"]
    select_modif = ttk.Combobox(sous_div2, textvariable=variable_modif, values=options_modif, width=30)
    select_modif.pack(side=LEFT)

    # BtnValider
    BtnValider = Button(sous_div2, text="Valider")
    BtnValider.pack(side=LEFT)



# DropDownMenu
variable = StringVar(div)
variable.set("Sélectionner une classe")  # Valeur par défaut

options = [ "2AMA Seconde Bac Pro TMA", "1TMA Première Bac Pro TMA", "1MEN 1ère CAP MF", "TMEN Terminale CAP MF"]

# Fonction de mise à jour des données de la liste de gauche lors du changement de classe sélectionnée
def on_class_select(*args):
    update_data()


select_classes = ttk.Combobox(div, textvariable=variable, values=options,width=30)
select_classes.pack(side=LEFT)
select_classes.bind("<<ComboboxSelected>>", on_class_select)

# BLANK
blank_label = Label(div, width=50)
blank_label.pack(side=LEFT)

# BtnEleve
button1 = Button(div, text="Elèves")
button1.pack(side=LEFT)

# BLANK
blank_label = Label(div, width=10)
blank_label.pack(side=LEFT)

# BtnQuitter
button2 = Button(div, text="Quitter")
button2.pack(side=LEFT)

# BtnAjouter
button3 = Button(div3, text="Ajouter")
button3.pack(side=LEFT)

# Liste de gauche
my_tree = ttk.Treeview(sous_div1)
my_tree['columns'] = ("Id", "nom", "prenom")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Id", anchor=W, width=80)
my_tree.column("nom", anchor=W, width=150)
my_tree.column("prenom", anchor=W, width=150)
my_tree.heading("Id", text="Id")
my_tree.heading("nom", text="Nom")
my_tree.heading("prenom", text="Prenom")
my_tree.bind("<<TreeviewSelect>>", on_tree_select)  # Appelle la fonction lorsqu'un élément est sélectionné
my_tree.pack(side=LEFT)

fenetre.mainloop()
