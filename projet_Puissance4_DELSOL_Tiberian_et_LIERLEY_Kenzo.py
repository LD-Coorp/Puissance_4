from random import randint
plateau=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

def checkPlateauFull(plateau):
    '''regarde si le plateau de jeu est plein
       paramètre: la liste du plateau du jeu
    '''
    i=0
    for element in plateau:
        if 0 not in element:
            i+=1  #si il n'y a pas de vide dans la ligne, ajoute 1 au compteur
            if i==6: #au bout de 6 au compteur (quand il n'y a pas de vide sur le plateau) full est égale à True
                full=True
        else: #sinon full est False
            full=False
    return full


def checkLigne(liste):
    '''regarde si un même symbole aparaît 4 fois d'affilé dans toutes les listes de la liste en paramètre (lignes du plateau)
       paramètre: la liste du plateau de jeu
       si il y a une victoire renvoie un tuple avec victoire et le joueur sinon renvoie False et 0
    '''
    rep=(False,0)
    for element in liste:
        for i in range(3,len(element)): #optimise la recherche de victoire en ne regardant que à partir du moment où la victoire est possible (si 4 pion peuvent être placé sur l'intervalle), s'arrête à la fin du tableau et donc vérifie à partir du moment où la longueur est supérieur à 3 car en dessous ou égale à 3 de longueur la victoire est impossible
            if element[i]==element[i-1] and element[i]==element[i-2] and element[i]==element[i-3] and element[i]!=0:
                rep=(True,element[i])
    return rep


def checkColonne(liste):
    '''regarde si un même symbole aparaît 4 fois d'affilé dans toutes les listes de la liste en paramètre (colonnes du plateau)
       paramètre: la liste du plateau de jeu
       si il y a une victoire renvoie un tuple avec victoire et le joueur sinon renvoie False et 0
    '''
    rep=(False,0)
    for i in range(7):
        for e in range(3,6): #optimise la recherche de victoire en ne regardant que à partir du moment où la victoire est possible (si 4 pion peuvent être placé sur l'intervalle), s'arrête à la fin du tableau et donc vérifie à partir du moment où la hauteur est supérieur à 3 car en dessous ou égale à 3 de hauteur la victoire est impossible
            if liste[e][i]==liste[e-1][i]==liste[e-2][i]==liste[e-3][i] and liste[e][i]!=0:
                rep=(True,liste[e][i])
    return rep


def checkDiagonale(liste):
    '''regarde si un même symbole aparaît 4 fois d'affilé dans toutes les listes de la liste en paramètre (diagonales du plateau)
       paramètre: la liste du plateau de jeu
       prends toute les diagonales(sous forme de liste) et les rentrent dans une liste qui sera traité par checkLigne
       si il y a une victoire renvoie un tuple avec victoire et le joueur sinon renvoie False et 0
    '''
    x=0
    y=0
    listeDiag=[] #créer un liste vide qui prendra par la suite toute les diagonales du plateau de jeu sous forme de listes dans listeDiag
    while x>=0 and y<6:     #4 while qui permettent de convertir les diagonales en listes dans une liste pour, par la suite faire vérifier la grande liste par la fonction checkLigne
        for x in range(6):  #permet de pouvoir changer la valeur de x et y afin de les déplacer dans un repère qui est notre plateau de jeu
            Temp=[]    #défini une liste vide temporaire qui viendra par la suite prendre tout les pions des différentes diagonales du plateau et vide la liste temporaire à chaque passage
            for y in range(x+1): #permet de pouvoir changer la valeur de x et y afin de les déplacer dans un repère qui est notre plateau de jeu
                Temp.append(liste[x][y]) #met dans la liste temporaire le pion au coordonnées (x;y) dans le repère
                x-=1
            listeDiag.append(Temp)  #puis met la liste temporaire dans la liste de toutes les diagonales
    while y>1:
        for x in range(6):
            Temp=[]  #vide la liste temporaire
            for e in range(x+1):
                y=6-e
                Temp.append(liste[x][y])
                x-=1
            listeDiag.append(Temp)
    while x<5 and y>0:
        for x in range(6):
            Temp=[]
            for y in range(6-x):
                Temp.append(liste[x][y])
                x+=1
            listeDiag.append(Temp)
            x=0
    while x<5 and y<6:
        for x in range(6):
            Temp=[]
            for e in range(6-x):
                y=6-e
                Temp.append(liste[x][y])
                x+=1
            listeDiag.append(Temp)
        x=5
        if len(listeDiag)==24 and x==5 and y==6:
            return checkLigne(listeDiag)  #à la fin de la conversion des diagonales en listes dans une liste on utilise la fonction checkLigne(la liste des diagonales) afin de vérifier si 4 pion se trouve à la suit sur la même diagonale.

def affichage(l):
    '''
       Permet d'afficher le plateau de jeu sans rien retourner
       : paramètre: l: liste de 6 listes contenant des 0, des 1 et des 2
    '''
    #parcours la liste de listes
    for i in range(len(l)):
        print("\n"+11*" "+"|", end="")
        #parcours induviduellement chaque listes de l, et affiche son contenu sur une ligne
        for element in l[i]:
            if element==1:
                print("@", end="|")
            elif element==2:
                print("¤", end="|")
            else:
                print(' ', end="|")
    print("\n"+11*" "+15*"#","\n"+11*" "+"[1|2|3|4|5|6|7]")


def pion(signe, l,IA=False):
    '''
       demande au joueur de choisir sa colonne et modifie la liste en fonction de la colonne choisi sans rien retourner, pour L'IA le pion est placé aléatoirement
       : paramètre: signe: 1 ou 2 selon le joueur qui joue
                  : l: liste de listes (représentant les lignes du plateau) composées de 1, de 2et de 0 pour les emplacements vides
                  : IA: True si le joueur souhaite jouer avec une IA, False sinon
    '''
    if IA==True:
        coupJoue=False
        # tant que le coup joué est invalide, refait jouer l'IA
        while coupJoue==False:
            coup=randint(0,6) #choisi la colonne de l'IA aléatoirement
            #parcours la liste en sens inverse afin de rechercher la liste la plus basse du plateau où l'indice demandé par le joueur est occupé par un 0 soit vide
            for element in reversed(l):
                if element[coup]==0:
                    element[coup]=signe
                    coupJoue=True
                    break
    else:
        coupJoue=False
        # tant que le coup joué est invalide, redemande au joueur ce qu'il souhaite faire 
        while coupJoue==False: 
            coup=input("\nEntrez votre colonne:  ")
            #le try est ici car la variable coup est une chaine de caractère et non un nombre, suite à une erreur de jeu du joueur, la fonction int() produit une erreur et arrête le jeu
            try: 
                coup=int(coup) 
                coup-=1 
                place=False 
                #parcours la liste en sens inverse afin de rechercher la liste la plus basse du plateau où l'indice demandé par le joueur est occupé par un 0 soit vide 
                for element in reversed(l): 
                    if element[coup]==0: 
                        element[coup]=signe 
                        place=True 
                        coupJoue=True 
                        break 
                #si la colonne est déjà pleine le signal au joueur et lui fait recommencer le choix de colonne 
                if place==False: 
                    print("Votre colonne est déjà pleine") 
            #sinon si la colonne choisi est invalide et dépasse les limites du plateau, le joueur est aussi signalé
            except: 
                print("Votre demande est invalide, veuillez entrer un nombre entier compris entre 1 e t 7")  



def updaterun(plateau):
    '''prend en parmètre la varaible run et le plateau de jeu
       fait le check intégrale du plateau et met fin au pro
    '''
    check=checkLigne(plateau),checkColonne(plateau),checkDiagonale(plateau) #effectue tous les check
    winner=0 
    for i in range(3):
        if check[i][0]==True: #vérifie si un des check est vrai (donc s'il y a victoire)
            winner=check[i][1] #winner prend le pion donc le joueur ayant gagné
            print(35*'=')
            print('manche terminé !\nVictoire du joueur',winner,"!")
            print(35*'=')
        elif check[i][0]!=True and i==2:  #si personne ne gagne, vérifie si le plateau de jeu est plein
            if checkPlateauFull(plateau)==True:
                print(35*'=')
                print('Match nul !')
                print(35*'=')
                winner=-1 #winner prend la valeur -1 car la partie est nul
    return winner

def jeu(IA=False):
    '''paramètre: True ou False qui est la présence ou non de l'IA
       lance la partie jusqu'à ce que run ne soit plus égale à true donc jusqu'à ce que la partie se termine(qui peut être en un nombre de manche infini qui est le nombre de fois ou le joueur veut rejouer)
    '''
    #Nombre de manches gagnées
    j1=0
    j2=0
    run=True
    tourIA=randint(1,2) #défini qui commence en premier entre l'IA et le joueur
    while run==True:
        #Reset de la partie
        plateau=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        winner=0
        if tourIA==1 and IA==True: #signal au joueur qui va commencer à jouer
            print(35*'=')
            print("l'IA est le joueur 1 !")
            print(35*'=')
        elif tourIA==2 and IA==True:
            print(35*'=')
            print("Vous êtes le joueur 1 !")
            print(35*'=')
        #Le deroulement de la partie
        while winner==0:
            for i in range(1,3):
                #Informe le joueur de son pion
                if i==1:  #signal au joueur la personne qui joue et le pion qui va être placé
                    print(35*'=')
                    print('Au tour du joueur',i,'!','\n'+'Le pion actuelle est:  @')
                    print(35*'=')
                else:
                    print(35*'=')
                    print('Au tour du joueur',i,'!','\n'+'Le pion actuelle est :  ¤')
                    print(35*'=')
                #affichage du jeu
                affichage(plateau)
                #regarde si un joueur a gagné ou s'il y a match nul
                winner=updaterun(plateau)
                #sort directement de la boucle si quelqun gagne le jeu ou en cas de match nul
                if winner!=0:
                    if winner==1:
                        j1+=1
                    elif winner==2:
                        j2+=1
                    break
                #tour du joueur, vérifie si c'est une IA ou le joueur qui joue
                if i==tourIA:
                    pion(i,plateau,IA)
                else:
                    pion(i,plateau)
        #Annonce les scores
        print(35*"=")
        print("Le joueur 1 a " + str(j1) + " points")
        print("Le joueur 2 a " + str(j2) + " points")
        print(35*"=")
        #Demande au joueur si il veut refaire une manche
        rejouer=""
        while rejouer!="O" and rejouer!="N":
            rejouer=input('Voulez vous rejouer? Si oui: O, sinon : N\n').upper()
            if rejouer!="O" and rejouer!="N":
                print("Votre réponse n'est pas valide, veuillez répondre par 'O' ou 'N'")
        #Regarde si le joueur veut refaire une manche
        if rejouer=="N":
            run=False
            #Dit quel joueur a gagné
            if j1>j2:
                print(35*"=")
                print("Le joueur 1 à gagné la partie!!")
                print(35*"=")
            elif j1<j2:
                print(35*"=")
                print("Le joueur 2 a gagné la partie!!")
                print(35*"=")
            else:
                print(35*"=")
                print("Egalité")
                print(35*"=")
            print(35*" ")

                
        

#Pour que l'on soit toujours sur l'écran d'acceuil
while 0!=1:
    #Affichage de l'écran d'acceuil
    print(35*"=")
    print(12*" "+"PUISSANCE 4")
    print(35*"=")
    print("Selectionnez votre mode de jeu:\n")
    print(9*" "+"Mode 2 joueurs: 1")
    print(6*" "+"Jeu contre l'ordinateur: 2")
    print(35*"=")
    mode=""
    #Choix du mode de jeu
    while mode !="1" and mode !="2":
        mode=input()
        if mode !="1" and mode !="2":
            print("Veuillez entrer soit 1 soit 2")
    #Lancement du mode de jeu choisi
    if mode=="1":
        jeu()
    else:
        jeu(True)