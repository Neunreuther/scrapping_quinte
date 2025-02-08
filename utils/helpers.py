import os
from datetime import datetime
import locale

def creer_dossier_course(path_dossier):
    """
    Dans cette fonction je créer un dossier pour les courses qu'on sort aujourd'hui

    à vérifier si necessaire
    """
    date_actuelle = datetime.now().strftime("%Y-%m-%d")
    nom_dossier = f"scrapping_{date_actuelle}"
    chemin_dossier = os.path.join(path_dossier, nom_dossier)
    try:
        os.mkdir(chemin_dossier)
        print(f"Dossier créé : {nom_dossier}")
    except FileExistsError:
        print(f"Le dossier {nom_dossier} existe déjà.")


def date_auj():
    """
    Retourne la date du jour au format 'jour semaine, jour mois année' en français.
    """
    date_du_jour_global = None
    
    if date_du_jour_global is None:

        try:
            locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        except locale.Error:
            print("Locale française non disponible, utilisation du format par défaut.")
        
        date_du_jour = datetime.now()
        date_du_jour_formatee = date_du_jour.strftime("%A %d %B %Y")
        date_du_jour_global = ' '.join([word.capitalize() for word in date_du_jour_formatee.split()])
    
    return date_du_jour_global