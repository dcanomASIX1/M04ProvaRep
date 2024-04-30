from flask import Flask , render_template, request 
from xml.dom import minidom
import feedparser

app = Flask(__name__)

@app.route('/ex0')
def f_ex0():
    return '<html> <body><h1>Hola, Flask!</h1> </body> </html> '



@app.route('/ex1')
def f_ex1():
    return render_template('/ex1.html')

@app.route('/ex2')
def f_ex2():
    return render_template('ex2.html', modul='M02', nota=8)



@app.route('/ex3/<modul>/<int:nota>')
def f_ex3(modul, nota):
    return render_template('ex2.html', modul=modul , nota=nota) 

@app.route('/ex4')
def ex4():
    var1 = request.args.get('modul', default = 'No modul' , type=str)
    var2 = request.args.get('nota', default = 0 , type=int)
    var3 = request.args.get('color', type=str)
    var4 = request.args.get('img_gato', default = 0 , type=bool)
    return render_template('ex2.html', modul=var1, nota=var2, color=var3, img_gato=var4 )


@app.route('/ex5')
def ex5():
    return render_template('form.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aaa')
def RSSProv1():
    d = feedparser.parse('xml/provaRSS.xml')
    return render_template("ProvaRSS.html", titol=d.feed.title)

@app.route('/a2')
def RSSProv2():
    d = feedparser.parse('xml/provaRSS.xml')
    return render_template("ProvaRSS _2.html", d=d)

