from datetime import datetime
import counter
import notes_console
class Notes(object):
        date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

        def add_note(self):
                notes = []
                id = counter.Counter.id
                id = str(id)
                notes.append(id)
                self.title = input('enter title to add a note or q to star over: ')
                if self.title == 'q':
                    notes_console.notes_console()
                notes.append(self.title)
                self.content = input('enter content: ')
                notes.append(self.content)
                notes.append(self.date)
                notesfile = open('notesfile.txt', "a")
                print(notes)
                print("Do you want to save note added?")
                reply = input()
                if reply == 'no':
                        print(notes)
                else:
                        print(','.join(notes), file=notesfile)

        def edit_note(self):
                note_to_edit = input("Enter text to edit or q to start over: ")

                with open('notesfile.txt', 'r+') as file: #2
                    content = file.readlines()
                    for line in content:
                        if note_to_edit in line:
                            print(line, end='')

                    d = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
                    date_cut = line[-19:]
                    new_content = input('\n'"Enter new content for this note:")
                    content = file.readline()

                    updated_contents = line.replace(date_cut, d).replace(note_to_edit, new_content)

                    print(updated_contents)
                    file.write(updated_contents + '\n')

                    with open('notesfile.txt', 'r') as fw:
                        content = fw.readlines()
                        with open('notesfile.txt', 'w') as fw:
                            for line in content:
                                if line.find(note_to_edit) == -1:
                                    fw.write(line)


        def delete_note(self):
            note_to_delete = input("Enter title or content to delete a note: ")
            # if note_to_delete == 'q':
            #     notes_console.notes_console()

            with open('notesfile.txt', 'r') as fw:
                lines = fw.readlines()
                with open('notesfile.txt', 'w') as fw:
                    for line in lines:
                        if note_to_delete in line:
                            print(line, end='')
                        if line.find(note_to_delete) == -1:
                            fw.write(line)


        def show_notes(self):
            with open('notesfile.txt', 'r') as fr:
                print(fr.read())
            notes_console.notes_console()





















