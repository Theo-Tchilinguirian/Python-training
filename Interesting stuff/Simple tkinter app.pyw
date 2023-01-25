from tkinter import * #import tout de tkinter, et sans avoir à faire tkinter.fonction(); juste fonction() (mais les noms peuvent se mélanger avec cex des autres modules)

fenetre = Tk()

label = Label(fenetre, text="Bonjour", width = 80, height = 20)
label.pack()

# bouton de sortie
bouton=Button(fenetre, text="Fermer", command=fenetre.quit, width = 25)
bouton.pack()

fenetre.mainloop()