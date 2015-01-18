from tkinter import *

def message(titre,texte):
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