import re
import os
import getpass
import sys

try:
    import requests

except ModuleNotFoundError:
    # si module "requests" pas installé -> l'installe et l'importe
    os.system('cmd /c "pip install requests & cls"')
    import requests


name = input("Entrez le nom du fichier vidéo : ")
link = input("Entrez le lien : ")
path = "C:/Users/"+getpass.getuser()+"/Downloads/"+name


def wifi(link, i):  # vérifie s'il y a accès à Internet tout en envoyant les requêtes GET
    number = 1
    headers = {
        'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    while True:
        try:
            if i == 0:
                return requests.get(link, headers=headers).text
            if i == 1:
                return requests.get(link, headers=headers).content
            break

        except:
            if number == 1:
                print("Pour continuer, connectez-vous à Internet ou vérifiez le lien.")
                # back to previous line and clear
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")


text = wifi(link, 0)
url = re.findall(
    'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

if url == []:
    link = link.rsplit("/", 1)[0] + "/"

    for x in range(len(re.findall('.ts', text))):
        url.append(link+str(x)+".ts")


a, n, it = 0, 1, len(url)
try:
    with open(path + ".tp4", 'wb') as merged:
        os.system('attrib +H "'+path+'".tp4')
        print("\nChargement : 0%")

        for x in url:  # copie les données des fichiers dans un fichier principal

            merged.write(wifi(x, 1))

            loading = round(a/it*100)
            a += 1

            if loading != round(a/it*100):

                # back to previous line and clear
                sys.stdout.write("\033[F")
                sys.stdout.write("\033[K")
                print("Chargement : "+str(round(a/it*100))+"%")

except:
    path = path+"("+str(n)+")"
    n += 1

os.rename(path+".tp4", path+".mp4")
os.system('attrib -H "'+path+'".mp4')
