from wtforms import Form
from wtforms  import SearchField,TextAreaField,TextField,SelectField,RadioField
from wtforms import EmailField

class UserForm(Form):
    nombre=StringField("nombre")
    email=EmailField("correo")
    apaterno=TextField('apaterno')
    materias=SearchField(choices=[('Español','Esp',('Mat','Matematicas')('Ingles','ING'))])
    radios=RadioField('Curso',choices=[("1","1"),("2","2"),("3","3")])