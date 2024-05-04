class PythonNotes():
    def __init__(self,title, content, date, id):
        self.title = title
        self.content = content
        self.date = date
        self.id = id
    
    def noteTitle(self):
        return self.title
    
    def noteContent (self):
        return self.content
    
    def noteDate (self):
        return self.date
    
    def noteID (self):
        return self.id
    

note1 = PythonNotes('sky', 'blue', date='', id=0)





