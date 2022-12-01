import matplotlib.image as mpimage

adresse_image = input("Entrez le chemin d'accès à votre image : ")
image = mpimage.imread(adresse_image)

hauteur = len(image)  # hauteur de l'image
largeur = len(image[0])  # largeur de l'image

# calcul du pas idéal :
if hauteur >= largeur:
    maxlong = hauteur

else:
    maxlong = largeur

pas = maxlong//60

max_value = image.max()  # on trouve la valeur du pixel le plus sombre de l'image
# on va du plus clair au plus sombre
asci = " ", " ", ".", ":", "+", "=", "n", "o", "O", "#", "@"

for y in range(0, hauteur, pas):
    # on vide la variable
    image_finale = ""

    for x in range(0, largeur, pas):

        valeur_pixel = image[y][x]
        moyenne_valeur = sum(valeur_pixel)/len(valeur_pixel)
        noirceur = moyenne_valeur/max_value  # On obtient un nombre compris en 0 et 1

        # Je multiplie par 10 et arrondie à l'unité pour avoir des valeurs entières
        noirceur = noirceur*10
        noirceur = round(noirceur)

        # on ajoute 2 fois le caractère pour garder les proportionnalités
        symbole = asci[noirceur]+asci[noirceur]

        # on assemble tous les caractères d'une ligne
        image_finale += symbole

    # on affine la ligne de caractère finit
    print(image_finale)

input("Entrez pour quitter.")
