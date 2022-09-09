from django.http import HttpResponse
from django.template import loader

def home(self,name):
    return HttpResponse(f'Hola Soy {name}!!!')

def homepage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data ={'nombre':'Catia','apellido': 'Toledo','lista':lista} 
    planilla = loader.get_template('home.html') #nos ahorramos usar 'open' este comando, carga y busca el archivo directo
    documento = planilla.render(data)
    return HttpResponse(documento)     

def cursos(self):
    planilla = loader.get_template('cursos.html') #nos ahorramos usar 'open' este comando, carga y busca el archivo directo
    documento = planilla.render()
    return HttpResponse(documento)  