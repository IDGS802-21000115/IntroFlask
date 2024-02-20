from flask import Flask, render_template,request,Response
import forms

from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash

app = Flask(__name__)
app.secret_key='esta es la clave secreta'
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
@app.before_request
def before_request():
   g.prueba='hola'
   print('antes de ruta 1')



@app.route("/")
def index():
    return render_template("index.html")
@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    print('dentro 2')
    valor=g.prueba
    print('el dato es:{}'.format(valor))
    nom=""
    apaterno=""
    correo=""
    alum_form=forms.UserForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        correo = alum_form.email.data
        apaterno = alum_form.apaterno.data
        mensaje='Bienvenido: {}'.format(nom)
        flash(mensaje)
        print("nombre: {}".format(nom))
        print("correo: {}".format(correo))
        print("apaterno: {}".format(apaterno))
    return render_template("alumnos.html", form=alum_form, nom=nom, apaterno=apaterno,correo=correo)
@app.after_request
def alfter_request(response):
   print('despues de la ruta 3')
   return response

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

 
@app.route("/")
def hola():
    return "<p> Hola Mundo <p>"

@app.route("/hola")
def func():
    return "<h1>Saludo desde Hola-UTL<h1>"
@app.route("/saludo")
def func1():
    return "<h1>Saludo desde saludito<h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
     return "<h1>Hola<h1>"+nom 
 
@app.route("/numero/<int:n1>")
def numero(n1):
     return "<h1>El valor es: {}<h1>".format(n1)
 
@app.route("/user/<string:nom>/<int:id>")
def user(id,nom):
     return "<h1>ID: {} Nombre {}<h1>".format(id,nom)
 
@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
     return "<h1>la suma de {} + {}= {}<h1>".format(n1,n2,n1+n2)
 
@app.route("/multiplica",methods=["GET","POST"])
def mul():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        
        return "<h1> el resultado es {}</h1>".format(str(int(num1)*int(num2)))
    else:
        
      return '''
            <form action="/multiplica" method="POST">
            <label>N1:<lable>
            <input type="text" name="n1"/>
            <label>N2:</label>
            <input type="text" name="n2"/>
            <input type="submit"/>
            </form>
            '''
 
@app.route("/formulario1>",methods=["GET","POST"])
def calculo():
     return render_template("formulario1.html")
 
@app.route("/resultado",methods=["GET","POST"])
def multi():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        
        return "<h1> el resultado es {}</h1>".format(str(int(num1)*int(num2)))

if __name__ == "__main__":
    app.run(debug=True)