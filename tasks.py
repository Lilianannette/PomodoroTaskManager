import json

FICHIER_JSON = "data/sessions.json"

def loadData():
    try:
        with open(FICHIER_JSON, "r") as fichier:
            return json.load(fichier)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"sessions": [], "tâches": []}

def saveData(data):
    with open(FICHIER_JSON, "w") as fichier:
        json.dump(data, fichier, indent=4)

def displayTask():
    data = loadData()
    tasks = data.get("tasks", [])
    if not tasks:
        print("Aucun tâche enregistrée.")
    else:
        print("\n--- Liste des tâches ---")
        for i, task in enumerate(tasks, 1):
            print(f"{i}, {task}")

def addTasks():
    data = loadData()
    tasks = data.get("tasks", [])
    task = input("Entrez une nouvelle tâche : ")
    tasks.append(task)
    data["Task"] = tasks
    saveData(data)
    print(f"Tâche '{task}' ajouté avec succès.")

def deleteTask():
    data = loadData
    tasks = data.get("Tasks", [])
    if not tasks:
        print("Aucun tâche a supprimer")
        return

        displayTask()
    try:
        choice = int(input("Entrez le numéro de la tâche à supprimer : "))
        if 1 <= choice <= len(tasks):
            taskToBeDeleted = tasks.pop(choice - 1)
            data["taches"] = tasks
            loadData(data)
            print(f"Tâche '{taskToBeDeleted}' supprimée avec succès.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Veuillez entrer un numéro valide.")
