import os
import getpass

# Funktion, um ein Passwort zu setzen
def set_password():
    password = input("Bitte wähle ein Passwort: ")
    with open("password.txt", 'w') as f:
        f.write(password)
    print("Passwort gesetzt!")

# Funktion, um das gespeicherte Passwort zu überprüfen
def check_password():
    try:
        with open("password.txt", 'r') as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("Kein Passwort gesetzt. Bitte setze ein Passwort.")
        set_password()
        return False

    entered_password = getpass.getpass("Gib dein Passwort ein: ")

    if entered_password == stored_password:
        return True
    else:
        print("Falsches Passwort!")
        return False

# Funktion, um das Passwort zu ändern
def change_password():
    print("\n--- Passwort ändern ---")
    
    # Aktuelles Passwort überprüfen
    if check_password():
        new_password = input("Gib dein neues Passwort ein: ")
        with open("password.txt", 'w') as f:
            f.write(new_password)
        print("Passwort erfolgreich geändert!")
    else:
        print("Passwort konnte nicht geändert werden.")

# Funktion, um eine neue Datei zu erstellen
def create_new_file():
    filename = input("Gib den Namen der neuen Datei (mit .txt Erweiterung) ein: ")
    with open(filename, 'w') as f:
        print(f"Neue Datei '{filename}' erstellt. Du kannst jetzt schreiben.")
        while True:
            content = input("Schreibe deinen Inhalt (tippe 'exit' um zu stoppen): ")
            if content.lower() == 'exit':
                break
            f.write(content + '\n')
        print(f"Inhalt in '{filename}' gespeichert.")

# Funktion, um in eine bestehende Datei zu schreiben
def continue_existing_file():
    filename = input("Gib den Namen der bestehenden Datei (mit .txt Erweiterung) ein: ")
    if os.path.exists(filename):
        with open(filename, 'a') as f:
            print(f"Öffne Datei '{filename}' zum Schreiben.")
            while True:
                content = input("Schreibe deinen Inhalt (tippe 'exit' um zu stoppen): ")
                if content.lower() == 'exit':
                    break
                f.write(content + '\n')
            print(f"Inhalt in '{filename}' hinzugefügt.")
    else:
        print(f"Die Datei '{filename}' existiert nicht.")

# Hauptprogramm
def main():
    if not check_password():
        return  # Beendet das Programm, wenn das Passwort falsch ist

    while True:
        print("\n--- Menü ---")
        print("1. Neue Datei erstellen")
        print("2. In eine bestehende Datei weiterschreiben")
        print("3. Passwort ändern")
        print("4. Programm beenden")
        choice = input("Wähle eine Option (1/2/3/4): ")

        if choice == '1':
            create_new_file()
        elif choice == '2':
            continue_existing_file()
        elif choice == '3':
            change_password()
        elif choice == '4':
            print("Programm wird beendet...")
            break
        else:
            print("Ungültige Wahl, bitte wähle erneut.")

if __name__ == "__main__":
    main()
