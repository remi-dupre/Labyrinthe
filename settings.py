"""Pour modifier certain parametres"""

from tkinter import *
from PIL import Image, ImageTk


def choixMode() :
    """Lance une fenetre qui permet de selectionner differents types de parties"""
    
    def rapide():
        commencer(5, 12)
        Fen.destroy()
    def normal():
        commencer(7, 25)
        Fen.destroy()
    def long():
        commencer(11, 25)
        Fen.destroy()
    
    Fen = Tk()
    btn_rapide = Button(Fen, text="Partie rapide", command=rapide)
    btn_rapide.pack()
    btn_normal = Button(Fen, text="Partie classique", command=normal)
    btn_normal.pack()
    btn_long = Button(Fen, text="Partie longue", command=long)
    btn_long.pack()
    Fen.mainloop()
    

def message(titre,texte) :
    """Affiche une fenetre pop up avec comme titre titre et texte texte
    S'efface au bout d'un court instant
    Fermable en appuyant sur Ok"""
    
    f_pop=Toplevel()
    f_pop.title(titre)
    f_pop.geometry("250x120+500+300")
       
    l_Message=Label(f_pop, text='\n'+'\n'+texte+'\n', font="Verdana 10 bold")
    l_Message.pack()
        
    b_Stop=Button(f_pop, text="Ok", command=f_pop.destroy)
    b_Stop.pack()
    b_Stop.after(4000, f_pop.destroy)
        
    f_pop.mainloop()


def settingsNoms():
    """Fonction renvoyant une liste de noms rentrée par l'utilisateur.
        - Il doit forcément y avoir un premier nom
        - Il peut y avoir maximum quatre noms
        - Les redondances sont proscrites
    Structure à désirer.
    
    Petites subtilitées:
        - D, W et C rentrent respectivement DreadBonney, Whopping et Chapodfail
        - Echap ferme la fenêtre (par procédure normale)
        - Saisie possible avec Entrer"""
        
    liste=[0]*4
    
    def valider(*event):
        if saisie()!="":
            if dans(liste,saisie()):
                message("Erreur","Nom déjà utilisé")
                return
            liste[i[0]-1]=saisie()
            i[0]+=1
            if i==[5]:
                Fenetre.destroy()
            else:
                l_Nom['text']="\tNom joueur {}".format(i[0])
        else:
            message("Erreur","Anneau nul: erreur")
            
    def lancer(*event):
        if liste[0]!=0:
            Fenetre.destroy()
        else:
            message("Erreur",'Il faut au moins un joueur')

    def dans(L,e):
        for i in L:
            if i==e: return True
        return False
    
    def saisie():
        n=nom.get()
        if n=="D": return 'DreadBonney'
        if n=="W": return 'Whopping'
        if n=="C": return 'Chapodfail'
        return n
    
    Fenetre=Tk()
    Fenetre.title("Sélection des noms")
    Fenetre.geometry("370x120+450+300")
    
    i=[1]
    l_Nom=Label(Fenetre, text='\tNom joueur 1')
    l_Nom.grid(row=1, column=0)
    
    nom=StringVar()
    e_Nom=Entry(Fenetre, textvariable=nom, width=30)
    e_Nom.bind("<Return>",valider)
    e_Nom.bind("<Escape>",lancer)
    e_Nom.grid(row=1, column=1, columnspan=3)
    
    b_Lancer=Button(Fenetre, text='Lancer!', command=lancer)
    b_Lancer.grid(row=2, column=2)
    
    b_Valider=Button(Fenetre, text='Valider', command=valider)
    b_Valider.grid(row=2, column=1)
    
    Label(Fenetre, text='\n').grid(row=0)
    Label(Fenetre, text='\n').grid(row=3)
    
    
    
    Fenetre.mainloop()
    
    
    return(liste)
    
    
def settingsTextures():
    
    Fenetre=Tk()
    Fenetre.title("Sélection des textures packs")
    Fenetre.geometry("500x400+400+220")
    
    l_Message=Label(Fenetre, text='\n\t\t\tVeuillez sélectionner un texture pack')
    l_Message.grid(row=0, column=1, columnspan=2)
    
    valeur=IntVar()
    valeur.set(1)
    r_Choix1=Radiobutton(Fenetre, variable=valeur, value=1)
    r_Choix2=Radiobutton(Fenetre, variable=valeur, value=2)
    r_Choix3=Radiobutton(Fenetre, variable=valeur, value=3)
    r_Choix4=Radiobutton(Fenetre, variable=valeur, value=4)
    r_Choix1.grid(row=1, column=1)
    r_Choix2.grid(row=2, column=1)
    r_Choix3.grid(row=3, column=1)
    r_Choix4.grid(row=4, column=1)
    
    f_1=Frame(Fenetre, relief=GROOVE, border=3)
    img1 = Image.open("img/patern/1/1.png").resize((50,50))
    img1 = ImageTk.PhotoImage(img1)
    lbl1 = Label(Fenetre, image=img1)
    lbl1.image = img1
    lbl1.grid(row=1, column=2)
    
    f_2=Frame(Fenetre, relief=GROOVE, border=3)
    img2 = Image.open("img/patern/2/1.png").resize((50,50))
    img2 = ImageTk.PhotoImage(img2)
    lbl2 = Label(Fenetre, image=img2)
    lbl2.image = img2
    lbl2.grid(row=2, column=2)
    
    f_3=Frame(Fenetre, relief=GROOVE, border=3)
    img3 = Image.open("img/patern/3/1.png").resize((50,50))
    img3 = ImageTk.PhotoImage(img3)
    lbl3 = Label(Fenetre, image=img3)
    lbl3.image = img3
    lbl3.grid(row=3, column=2)
    
    f_4=Frame(Fenetre, relief=GROOVE, border=3)
    img4 = Image.open("img/patern/4/1.png").resize((50,50))
    img4 = ImageTk.PhotoImage(img4)
    lbl4 = Label(Fenetre, image=img4)
    lbl4.image = img4
    lbl4.grid(row=4, column=2)
    
    #todo: insérer dans chaque Frame l'image de la case en T
    
    b_Valider=Button(Fenetre, text='Valider', command=Fenetre.destroy)
    b_Valider.grid(row=5, column=1)
    
    Fenetre.mainloop()
    
    a=valeur.get()
    return(a)