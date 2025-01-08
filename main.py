from tasks import displayTask, addTasks, deleteTask
from pomodoro import PomodoroManager
from gui import PomodoroGUI

def menu():
    manager = PomodoroManager()

    while True:
        print("\nMenu :")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Démarrer une session Pomodoro")
        print("5. Quitter")

        choice = int(input("Choisissez une option : "))
        if choice == 1:
            displayTask()
        elif choice == 2:
            addTasks()
        elif choice == 3:
            deleteTask()
        elif choice == 4:
            manager.start_pomodoro()
        elif choice == 5:
            print("À bientôt !")
            break
        else:
            print("Option invalide, essayez encore.")

if __name__ == "__main__":
    print("Choisissez votre mode d'utilisation :")
    print("1. Mode texte")
    print("2. Interface graphique")

    mode = input("Entrez le numéro du mode : ")
    if mode == "1":
        menu()
    elif mode == "2":
        PomodoroGUI()
    else:
        print("Option invalide.")
