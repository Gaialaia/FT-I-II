
import notes
def notes_console():
    numbers = int(input("Press \n 1: to add note, \n 2: to show notes, "
                        "\n 3: to edit note, \n 4: delete note \n"))

    if numbers == 1:
        notes.Notes().add_note()
        next_note = input("Do you want to add one more note?")
        if next_note == "yes":
            notes.Notes.add_note()
            if next_note == 'no':
                notes_console()
    elif numbers == 2:
        notes.Notes().show_notes()
    elif numbers == 3:
        notes.Notes().edit_note()
    elif numbers == 4:
        notes.Notes().delete_note()
    else:
        print("press keys 1,2,3 or 4")
        notes_console()
