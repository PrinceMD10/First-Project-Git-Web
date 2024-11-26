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
