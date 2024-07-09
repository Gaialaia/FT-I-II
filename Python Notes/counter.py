import notes
class Counter(object):
        counter = 0
        id = counter

        with open('notesfile.txt') as file:
            for counter, line in enumerate(file):
                id = counter + 1




