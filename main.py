# from tasks import displayTask, addTask, recoverTask
# from pomodoro import startPomodoro

def menu():
    while True:
        print("\nMenu :")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Démarrer une session pomodoro")
        print("5. Quitter")

        choice = int(input("Choissisez une option: \n "))
        if choice == 1:
            displayTask()
        elif choice == 2:
            addTask()
        elif choice == 3:
            deleteTask()
        elif choice == 4:
            startPomodoro()
        elif choice == 5:
            print("A bientôt !")
            break
        else:
            print("Option Invalide, Essayez encore")

if __name__ == "__main__":
    menu()
