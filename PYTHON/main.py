from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/') #decorator
def say_hello():
    return render_template ('index.html', name = "Gaia")


#@app.route('/index') 
#def index():
 #   return 'It is my first project'

if __name__ == '__main__':
    app.run()