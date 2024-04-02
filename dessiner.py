"""Ce fichier permet de dessiner deux formes à l'aide des deux fonctions suivantes
 
+ triangle_equilateral(cote, info_feutre, coordonnees)
+ arc_de_cercle(rayon, angle, info_feutre, coordonnees)
 
Exemples d'utilisation :
>>> informations_feutre = {'écriture':'blue', 'fond':'#FF88FF', 'épaisseur':5}
>>> triangle_equilateral(50, informations_feutre, (50,100))
>>> arc_de_cercle(75, 360, informations_feutre, (200,-200))
 
"""
 
# Importation
 
import turtle as trt
import random as rd

# Fond de couleur

trt.Screen().bgcolor("paleturquoise")  
 
# Déclaration des fonctions privées
 
def nouveau_stylo(ecriture, fond, largeur):
    """Renvoie la référence d'un stylo configuré
 
    :: param ecriture(str)  :: la couleur d'écriture ('red', '#FF0000')
    :: param fond(str)      :: la couleur de fond pour ce stylo
    :: param largeur(int)   :: la largeur du trait
    :: return (Turtle)      :: renvoie un objet de la classe Turtle
 
    """
    feutre = trt.Turtle()
    feutre.color(ecriture)
    feutre.fillcolor(fond)
    feutre.pensize(largeur)
    feutre.speed(0)
    return feutre
 
def deplacer(feutre, x, y):
    """Lève le feutre, déplace le feutre et abaisse le feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param x(int)         :: coordonnée horizontale (abscisse)
    :: param y(int)         :: coordonnée verticale (ordonnée)
    :: return (None)        :: c'est une fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.penup()       # On lève la pointe
    feutre.goto(x, y)    # On déplace le crayon
    feutre.pendown()     # On abaisse la pointe
 
 
def trace_triangle_iso(feutre,cote , x, y ):
    """Trace un triangle (isocele) à l'aide du crayon feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param cote(int)     :: la valeur en pixel du rayon
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.begin_fill()
    feutre.goto(x + cote, y)
    feutre.goto(x + cote//2 , y + cote//3)
    feutre.goto(x , y)
    feutre.end_fill()
    feutre.hideturtle()


def trace_triangle_equilateral(feutre, cote):
    """Trace un triangle (equilatéral) à l'aide du crayon feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur en pixel des côtés 
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.begin_fill()
    for x in range(3):
        feutre.forward(cote)
        feutre.left(120)
    feutre.end_fill()
    feutre.hideturtle()
 

def trace_rectangle(feutre):
    """Trace un rectangle à l'aide du crayon feutre
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    """
    feutre.begin_fill()
    for x in range (2):
        feutre.forward(140)
        feutre.left(90)
        feutre.forward(12)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()
 
 
def trace_arc(feutre, rayon, angle):
    """Trace un arc de cercle à l'aide du crayon feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.begin_fill()
    feutre.circle(rayon, angle)
    feutre.end_fill()
    feutre.hideturtle()
    

def trace_rectangle_paysage(feutre):
    """Trace une facade à l'aide du crayon feutre
    
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    
    """
    feutre.begin_fill()
    for x in range (2):
        feutre.forward(140)
        feutre.left(90)
        feutre.forward(80)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()

def trace_carre(feutre):
    """Trace un carré à l'aide du crayon feutre
    
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    
    """
    feutre.begin_fill()
    for x in range (2):
        feutre.forward(30)
        feutre.left(90)
        feutre.forward(30)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()


def trace_rectangle_portrait(feutre):
    """Trace un rectangle vertical à l'aide du crayon feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle 
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    """
    feutre.begin_fill()
    for x in range(2):
        feutre.forward(30)
        feutre.left(90)
        feutre.forward(50)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()
    
def trace_long_rectangle(feutre):
    """Trace un long rectangle horizontal à l'aide du crayon feutre

    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: return (None):: fonction sans retour
    .. effet de bord:: modifie l'état de feutre
    """
    feutre.begin_fill()
    for x in range(2):
        feutre.forward(3000)
        feutre.right(90)
        feutre.forward(20)
        feutre.right(90)
    feutre.end_fill()
    feutre.hideturtle()
 
# Déclarations des fonctions publiques
 
 
def triangle_equilateral(cote, info_feutre, coordonnees):
    """Trace un triangle (equilatéral) à partir des info_feutre et aux bonnees coordonnées
 
    :: param cote(int)                     :: la valeur en pixel des côtés
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle_equilateral(feutre, cote)
 
    return feutre
 

def triangle_iso(info_feutre, cote, coordonnees):
    """Trace un rectangle (isocele) à partir des info_feutre et aux bonnees coordonnées
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle_iso(feutre, cote, x, y )


def rectangle(info_feutre, coordonnees):
    """Trace un rectangle en mode paysage à partir des info_feutre et aux bonnees coordonnées
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle(feutre)


def arc_de_cercle(rayon, angle, info_feutre, coordonnees):
    """Trace un arc de cercle à partir des info_feutre et aux bonnees coordonnées
 
    :: param rayon(int)                    :: la valeur en pixel du rayon
    :: param angle(int)                    :: la valeur en ° de l'angle
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_arc(feutre, rayon, angle)
 
    return feutre


def rectangle_paysage(info_feutre, coordonnees):
    """Trace une façade à partir des info_feutre et aux bonnees coordonnées

    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle_paysage(feutre)
 
def carre(info_feutre, coordonnees):
    """Trace une fenetre à partir des info_feutre et aux bonnees coordonnées

    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_carre(feutre)
 
def rectangle_portrait(info_feutre, coordonnees):
    """Trace une porte à partir des info_feutre et aux bonnees coordonnées
 
    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees (par désempaquetage)
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle_portrait(feutre)
 
    return feutre
    
def long_rectangle(info_feutre, coordonnees):
    """Trace un trottoir à partir des info_feutre et aux bonnees coordonnées

    :: param info_feutre(dict)             :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple[int,int])   :: un tuple (x,y)
 
    """
    ecriture = info_feutre['écriture']
    fond = info_feutre['fond']
    epaisseur = info_feutre['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_long_rectangle(feutre)
    
# Instructions du programme principal
 
if __name__ == '__main__':
 
    informations_feutre = {'écriture':"blue", 'fond':'#FF88FF', 'épaisseur':5}
    triangle_equilateral(50, informations_feutre, (50,100))
    arc_de_cercle(75, 360, informations_feutre, (200,-200))
    rectangle_paysage(informations_feutre, (50,-50))
    rectangle_portrait(informations_feutre, (50,-120))
    carre(informations_feutre, (50, -200))
    triangle_iso(informations_feutre, 140,(50, 30))
    rectangle(informations_feutre, (-20,-100))
    long_rectangle(informations_feutre, (-750, -300))