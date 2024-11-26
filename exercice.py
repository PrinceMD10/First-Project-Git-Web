Code Python
# Liste pour stocker les todos
todos = []

# Fonction pour lister les todos
def lister_todos():
    if not todos:
        print("Aucun todo disponible.")
    else:
        print("\n===== Liste des todos =====")
        for index, todo in enumerate(todos):
            print(f"{index + 1}. {todo['titre']} - Statut : {todo['statut']}")
        print("===========================")

# Fonction pour créer un todo
def creer_todo():
    titre = input("Entrez le titre du todo : ")
    todo = {
        "titre": titre,
        "statut": "À faire"  # Par défaut, le statut est "À faire"
    }
    todos.append(todo)
    print(f'Todo "{titre}" ajouté avec succès.')

    # Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    if not todos:
        print("Aucun todo disponible à modifier.")
        return

    lister_todos()
    try:
        choix = int(input("Entrez le numéro du todo à modifier : ")) - 1
        if choix < 0 or choix >= len(todos):
            print("Numéro invalide.")
            return

        # Logique de changement de statut
        if todos[choix]["statut"] == "À faire":
            todos[choix]["statut"] = "Fait"
        elif todos[choix]["statut"] == "Fait":
            todos[choix]["statut"] = "À fair"  # Erreur volontaire sans le 'e'
        else:
            print("Statut inconnu, impossible de le changer.")

        print(f'Statut du todo "{todos[choix]["titre"]}" mis à jour : {todos[choix]["statut"]}')
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        # Logique de changement de statut
        if todos[choix]["statut"] == "À faire":
            todos[choix]["statut"] = "Fait"
        elif todos[choix]["statut"] == "Fait":
            todos[choix]["statut"] = "À fair"  # Erreur volontaire sans le 'e'
        else:
            print("Statut inconnu, impossible de le changer.")

        print(f'Statut du todo "{todos[choix]["titre"]}" mis à jour : {todos[choix]["statut"]}')
    except ValueError:
        print("Veuillez entrer un numéro valide.")

