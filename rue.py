"""Ce fichier permet de dessiner une rue à l'aide des fonctions suivantes :
 
+ dessiner_rue_aleatoire()
+ dessiner_rue_decrite(rue:dict)
"""
 
 
# Importation
 
from dessiner import * # importation de dessiner
import random # importation de random
 
 
'''TABLEAUX DES ELEMENTS ALEATOIRE DE L'IMMEUBLE'''
 
LARGEUR_IMMEUBLE = 140 # largeur de IMMEUBLE
colors  = ["red","green","blue","orange","purple","pink","yellow"] # tableau de colors aléatoires
colors_porte  = ["lightslategrey","whitesmoke","lightsteelblue"] # tableau de colors_porte aléatoires
colors_immeuble = ["gainsboro","lightgrey","lightgray","silver","darkgrey","darkgray","grey","gray","dimgrey","dimgray"] # tableau de colors_immeuble aléatoires
colors_fenetre = ["azure","lightcyan"] # tableau de colors_fenetre aléatoires
colors_toit = ["lightslategray","slategrey"] # tableau de colors_toit aléatoires
coordonnees_porte = [12, 52, 92] # tableau de coordonnees_porte aléatoires
coordonnees_fenetres = [52, 95, 15] # tableau de coordonnees_fenetre aléatoires
nbr_aleatoire = [1, 2, 3, 4, 5] # tableau de nbr_aléatoires
 

'''TOUT LES PARAMETRES DE L'IMMEUBLE'''

 
def immeuble_aleatoire(numero:int) -> dict: # fonction qui creer un tableau avec toutes les inforamtions de l'immeuble
    informations = {} # création d'un tableau vide
    informations['couleur_facade'] = couleur_aleatoire_facade() # paramètre de couleur_facade
    informations['couleur_porte'] = couleur_aleatoire_porte() # paramètre de couleur_porte
    informations['couleur_fenetre'] = couleur_aleatoire_fenetre() # paramètre de couleur_fenetre
    informations['couleur_toit'] = couleur_aleatoire_toit() # paramètre de couleur_toit
    informations['numero'] = numero # paramètre de numéro de l'immeuble
    informations['nbr_etage'] = nombre_aleatoire_etages() # paramètre de nbr_etage
    informations['coordonnees_porte'] = coordonnees_aleatoire_porte() # paramètre de coordonnees_porte
    informations['coordonnees_fenetres'] = coordonnees_aleatoire_fenetres() # paramètre de coordonnees_aleatoire_fenetres
    return informations # on renvoie le tableau immeuble avec toutes les informations nécessaires


'''FONCTIONS DES ELEMENTS ALEATOIRE DE L'IMMEUBLE'''

 
def couleur_aleatoire(): # fonction aléatoire pour couleur_aleatoire()
    return colors[random.randint(0,len(colors)-1)] # renvoie aléatoirement l'indice du tableau colors

def couleur_aleatoire_porte(): # fonction aléatoire pour couleur_aleatoire_porte()
    return colors_porte[random.randint(0,len(colors_porte)-1)] # renvoie aléatoirement l'indice du tableau colors_porte

def couleur_aleatoire_facade(): # fonction aléatoire pour couleur_aleatoire_facade()
    return colors_immeuble[random.randint(0,len(colors_immeuble)-1)] # renvoie aléatoirement l'indice du tableau colors_immeuble

def couleur_aleatoire_fenetre(): # fonction aléatoire pour couleur_aleatoire_fenetre()
    return colors_fenetre[random.randint(0,len(colors_fenetre)-1)] # renvoie aléatoirement l'indice du tableau colors_fenetre

def couleur_aleatoire_toit(): # fonction aléatoire pour couleur_aleatoire_toit()
    return colors_toit[random.randint(0,len(colors_toit)-1)] # renvoie aléatoirement l'indice du tableau colors_toit

def coordonnees_aleatoire_porte(): # fonction aléatoire pour coordonnees_aleatoire_porte()
    return coordonnees_porte[random.randint(0,len(coordonnees_porte)-1)] # renvoie aléatoirement l'indice du tableau coordonnees_porte
    
def nombre_aleatoire_etages(): # fonction aléatoire pour nombre_aleatoire_etages()
    return nbr_aleatoire[random.randint(0,len(nbr_aleatoire)-1)] # renvoie aléatoirement l'indice du tableau nbr_aleatoire

def coordonnees_aleatoire_fenetres(): # fonction aléatoire pour coordonnees_aleatoire_fenetres()
    return coordonnees_fenetres[random.randint(0,len(coordonnees_fenetres)-1)] # renvoie aléatoirement l'indice du tableau coordonnees_fenetres

def toit_aleatoire(immeuble): # fonction toit_aleatoire
    cle = random.randint(0 , 1) # cle sera égal à un chiffre entre 0 ET 1
    if cle < 1: # si la cle est plus petit que 1
        return dessiner_toit_plat(immeuble) # on dessine le toit plat
    else: # sinon
        return dessiner_toit_pointu(immeuble) # on dessine le toit pointu
    
'''COORDONNEES DES ELEMENTS DE L'IMMEUBLE'''

 
def coordonnees_facade(immeuble:dict) -> tuple: # fonction de coordonnees_facade qui reçoit un paramètre de immeuble
    x_gauche = 200 * immeuble['numero'] - 460 # coordonnees de x_gauche par rapport au numéro de l'immeuble
    y_bas = 0 # coordonnees de y_bas par rapport au numéro donné
    return (x_gauche, y_bas) # renvoie les coordonnees x_gauche et y_bas

def coordonnees_trottoir(immeuble:dict) -> tuple: # fonction de coordonnees_trottoir qui reçoit un paramètre de immeuble
    x_gauche = -155 * immeuble['numero'] - 999 # coordonnees de x_gauche par rapport au numéro de l'immeuble
    y_bas = 10 # coordonnees de y_bas par rapport au numéro donné
    return (x_gauche, y_bas) # renvoie les coordonnees x_gauche et y_bas

def coordonnees_toit(immeuble:dict) -> tuple: # fonction de coordonnees_toit qui reçoit un paramètre de immeuble
    x_gauche = 200 * immeuble['numero'] - 460 # coordonnees de x_gauche par rapport au numéro de l'immeuble
    y_bas = 80 * immeuble['nbr_etage'] # coordonnees de y_bas par rapport au numbre d'étage
    return (x_gauche, y_bas) # renvoie les coordonnees x_gauche et y_bas

def recuperer_coordonnees_porte(immeuble:dict) -> tuple:
    x, y = coordonnees_facade(immeuble) # x, y sont égal au coordonnees_facade(immeuble)
    x = x + immeuble['coordonnees_porte'] # x est égal à x + le paramètre de "coordonnees_porte" dans immeuble
    return (x, y) # renvoie les coordonnees x, y


'''DESSINER DES ELEMENTS DE L'IMMEUBLE'''


def dessiner_facade(immeuble:dict) -> None: # fonctions dessiner_facade
    for nbr in range(0, immeuble['nbr_etage']): # nbr contient le numero de l'étage, boucle selon le nbr d'étages
        crayon = {}  # création d'un tableau vide crayon
        crayon['écriture'] = "black" # couleur du contour du toit en couleur noir
        crayon['fond'] = immeuble['couleur_facade'] # la couleur de fond est dans le paramètre de "couleur_facade" dans immeuble
        crayon['épaisseur'] = 2 # crayon avec 2 d'épaisseur
        x, y = coordonnees_facade(immeuble)  # désempaquatage du couple
        y = y + 80 * nbr # Permet de faire des étage, 80 étant la hauteur d'un étage, fois la boucle nbr au dessus
        cote = LARGEUR_IMMEUBLE # cote de l'immeuble correspond à LARGEUR_IMMEUBLE
        # Demande d'affichage
        rectangle_paysage(crayon, (x,y)) # dessine un rectangle_paysage qui reprente la porte avec en paramètre le crayon et les coordonnees x, y
 
def dessiner_porte(immeuble:dict) -> None: # fonctions dessiner_porte
    # Traduction des données de rue vers dessiner
    crayon = {} # création d'un tableau vide crayon
    crayon['écriture'] = "black" # couleur du contour du toit en couleur noir
    crayon['fond'] = immeuble["couleur_porte"] # la couleur de fond est dans le paramètre de "couleur_porte" dans immeuble
    crayon['épaisseur'] = 3 # crayon avec 3 d'épaisseur
    x, y = recuperer_coordonnees_porte(immeuble)  # désempaquatage du couple
    # Demande d'affichage
    rectangle_portrait(crayon, (x,y)) # dessine un rectangle_portrait qui reprente la porte avec en paramètre le crayon et les coordonnees x, y
    
    
def dessiner_toit_plat(immeuble:dict) -> None: # fonctions dessiner_toit_plat
    # Traduction des données de rue vers dessiner
    crayon = {} # création d'un tableau vide crayon
    crayon['écriture'] = "black" # couleur du contour du toit en couleur noir
    crayon['fond'] = immeuble['couleur_toit'] # la couleur de fond est dans le paramètre de "couleur_toit" dans immeuble
    crayon['épaisseur'] = 2 # crayon avec 3 d'épaisseur
    x, y = coordonnees_toit(immeuble)  # désempaquatage du couple
    # Demande d'affichage
    rectangle(crayon, (x,y)) # dessine un rectangle qui reprente le toit plat avec en paramètre le crayon et les coordonnees x, y
    
def dessiner_toit_pointu(immeuble:dict) -> None:
    # Traduction des données de rue vers dessiner
    crayon = {} # création d'un tableau vide crayon
    crayon['écriture'] = "black" # couleur du contour du toit en couleur noir
    crayon['fond'] = immeuble['couleur_toit'] # la couleur de fond est dans le paramètre de "couleur_toit" dans immeuble
    crayon['épaisseur'] = 2 # crayon avec 2 d'épaisseur
    x, y = coordonnees_toit(immeuble)  # désempaquatage du couple
    # Demande d'affichage
    triangle_iso(crayon, 140, (x,y)) # dessine un rectangle qui reprente le toit pointu avec en paramètre le crayon et les coordonnees x, y
    
    
def dessiner_fenetre(immeuble:dict) -> None: # fonctions dessiner_fenetre
    # Traduction des données de rue vers dessiner
    v_etage = immeuble['nbr_etage']   
    for etage in range(v_etage):
        for nbr in range(3):
            crayon = {} # création d'un tableau vide crayon
            crayon['écriture'] = "black" # contour du crayon en couleur noir
            crayon['fond'] = immeuble["couleur_fenetre"] # la couleur de fond est dans le paramètre de "couleur_fenetre" dans immeuble
            crayon['épaisseur'] = 3 # crayon avec 3 d'épaisseur
            x, y = coordonnees_facade(immeuble)  # désempaquatage du couple des coordonnées
            x = x + 12 # x + 12 pour décaler les fenetres du mur de gauche
            x = x + 40 * nbr # x + 40 * nbr pour faire 3 fenetres aves un écart de 40
            y = 20 + etage * 80 # y = 20 pour décaler les fenetres vers le haut + le nombre d'étage * 80
          # Demande d'affichage
            carre(crayon, (x,y)) # affichage du carré qui represente des fenetres


def dessiner_trottoir(immeuble:dict) -> None: # fonction qui dessine le trottoir
    crayon = {} # création d'un tableau vide crayon
    crayon['écriture'] = "grey" # contour en gris
    crayon['fond'] = "gray" # fond en gris
    crayon['épaisseur'] = 5 # épaisseur du crayon
    x, y = coordonnees_trottoir(immeuble) # désempaquatage du couple des coordonnées
    y = -3
    long_rectangle(crayon, (x, y)) # dessine le long rectangle avec le crayon et les coordonnées x, y
    
def dessiner_trottoir2(immeuble:dict) -> None: # fonction qui dessine le trottoir d'enface
    crayon = {} # création d'un tableau vide crayon
    crayon['écriture'] = "grey" # contour en gris
    crayon['fond'] = "gray" # fond en gris
    crayon['épaisseur'] = 5 # épaisseur du crayon
    x, y = coordonnees_trottoir(immeuble) # désempaquatage du couple des coordonnées
    y = -180
    long_rectangle(crayon, (x, y)) # dessine le long rectangle avec le crayon et les coordonnées x, y
    
def dessiner_route(immeuble:dict) -> None: # fonction qui dessine la route
    crayon = {} # création d'un tableau vide crayon
    crayon['écriture'] = "black" # contour en vert
    crayon['fond'] = "black" # fond en vert
    crayon['épaisseur'] = 165 # épaisseur du crayon
    x, y = coordonnees_trottoir(immeuble) # désempaquatage du couple des coordonnées
    y = -100
    long_rectangle(crayon, (x, y)) # dessine le long rectangle avec le crayon et les coordonnées x, y

def dessiner_herbe(immeuble:dict) -> None: # fonction qui dessine le trottoir
        crayon = {} # création d'un tableau vide crayon
        crayon['écriture'] = "forestgreen" # contour en vert
        crayon['fond'] = "forestgreen" # fond en vert
        crayon['épaisseur'] = 520 # épaisseur du crayon
        x, y = coordonnees_trottoir(immeuble) # désempaquatage du couple des coordonnées
        y = -450
        long_rectangle(crayon, (x, y)) # dessine le long rectangle avec le crayon et les coordonnées x, y
        
    
'''DESSINER TOUTE LA VILLE'''
 

def dessiner_trot_et_route(immeuble:dict) -> None:
    dessiner_trottoir(immeuble) # Dessine un trottoir en utilisant la fonction dessiner_long_rectangle
    dessiner_herbe(immeuble) # Dessine de l'herbe en utilisant la fonction dessiner_herbe

def dessiner_immeuble(immeuble:dict) -> None:
    dessiner_facade(immeuble) # Dessine la façade en utilisant la fonction dessiner_rectangle_paysage
    dessiner_fenetre(immeuble) # Dessine les fenetres en utilisant la fonction dessiner_carre
    dessiner_porte(immeuble)  # Dessine la porte en utilisant la fonction dessiner_rectangle_portrait
    toit_aleatoire(immeuble) # Dessine un toit aléatoire en utilisant la fonction dessiner_toit_pointu et dessiner toit_plat
    dessiner_herbe(immeuble) # Dessine l'herbe en utilisant la fonction dessiner_long_rectangle
    dessiner_route(immeuble) # Dessine la route en utilisant la fonction dessiner_long_rectangle
    dessiner_trottoir(immeuble) # Dessine un trottoir en utilisant la fonction dessiner_long_rectangle
    dessiner_trottoir2(immeuble) # Dessine un trottoir2 en utilisant la fonction dessiner_long_rectangle
    
def dessiner_rue_aleatoire() -> None: # fonction dessiner_rue_aleatoire
    for n in range(6): # 6 tours de boucles
        informations_immeuble = immeuble_aleatoire(n) # informations_immeuble est immeuble_aleatoire
        dessiner_immeuble(informations_immeuble) # dessine les immeuble avec les paramètrec de informations_immeuble
 
def dessiner_rue_decrite(rue:'?') -> None:
    pass
 
 
# Programme principal
 
if __name__ == '__main__':
    dessiner_rue_aleatoire()
