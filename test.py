import gankboard
gankboard.set_api_key('sk_YmQJD2tn3oBUkOjzg_cph3WVrg9wiTvpGPTCG9YgTuo')

def test_create_project():
    # Exemple de données à envoyer à la méthode create
    project_data = {
        'name': 'Mon Projet Test',
        'description': 'Ceci est une description de test pour le projet'
    }

    # Appel de la méthode gankboard.Project.create
    gankboard_project = gankboard.Project.create(
        name=project_data['name'],
        description=project_data.get('description', '')
    )

    # Affichage de la réponse pour voir ce que retourne la méthode
    print("Réponse de la création de projet :")
    print(gankboard_project)

# Exécution du test
if __name__ == "__main__":
    test_create_project()
