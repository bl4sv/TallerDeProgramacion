#Jonathan David Mendoza Sanchez
#Me costo demasiado esta etapa, es mucho para una sola persona (Aqui va mi mejor esfuerzo)
#Por favor cuando agregue imagenes que sean pequeñas de 400x400 ó 500x500 (Asi se ve mejor
"""De antemanos le pido disculpas, no tuve suficiente tiempo para hacerlo bien, estoy solo en Funda y taller y en ambos tenia que entregar proyectos"""

"""De antemanos le pido disculpas, no tuve suficiente tiempo para hacerlo bien, estoy solo en Funda y taller y en ambos tenia que entregar proyectos"""

"""De antemanos le pido disculpas, no tuve suficiente tiempo para hacerlo bien, estoy solo en Funda y taller y en ambos tenia que entregar proyectos"""

"""De antemanos le pido disculpas, no tuve suficiente tiempo para hacerlo bien, estoy solo en Funda y taller y en ambos tenia que entregar proyectos"""


import cv2
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import random
import tkinter
from tkinter import filedialog
from tkinter import simpledialog
import datetime
import os,io
from google.cloud import vision
from google.cloud.vision import types
import datetime
from tkinter.ttk import Combobox
import numpy as np
from tkinter import messagebox
import operator

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r'Jkey.json'
client=vision.ImageAnnotatorClient()

"""Clases Utilizadas"""

class Personas:
    def __init__(self):
        self.Nombre=""
        self.Lista=[]
    def setinfo(self,nombre,lista):
        self.Nombre=nombre
        self.Lista=lista

class Rostros:
    def __init__(self):
        self.Vectores=0

class Reconocimiento:
    def __init__(self):
        self.fecha=""
        self.RutaImagen=""
        self.ListaDeRostros=[]

"""Codigo de arbol"""
"""Codigo de arbol"""
"""Codigo de arbol"""

class registroAsistencia():
    """Registro de asistencia
    """
    fecha = None
    emociones = None
    sig = None
    def _init_(self,fecha,emociones,cedula):
        """Constructor de los registros de emociones

        Args:
            fecha (dict): Fecha del registro
            emociones (dict): Emociones reconocidas por el API google-cloud-vision
        """
        self.fecha = fecha
        self.emociones = emociones
        self.cedula=cedula

    def insertaRegistro(self,fecha,emociones):
        if self.sig == None:
            self.sig = registroAsistencia(fecha,emociones)
        else:
            self.sig.insertaRegistro(fecha,emociones)

class asistencia():
    cedula = None
    iz = None
    der = None
    asistencia = None
    def _init_(self,cedula):
        self.cedula = cedula

    def crearRegistroAsistencia (self,cedula,fecha,emociones):
        if self.cedula == cedula:
            if self.asistencia == None:
                self.asistencia = registroAsistencia(fecha,emociones)
            else:
                self.asistencia.insertaRegistro(fecha,emociones)
        elif self.cedula>cedula:
            if self.iz == None:
                self.iz = asistencia(cedula)
                self.iz.asistencia = registroAsistencia(fecha,emociones)
            else:
                self.iz.crearRegistroAsistencia(cedula,fecha,emociones)
        else:
            if self.der == None:
                self.der = asistencia(cedula)
                self.der.asistencia = registroAsistencia(fecha,emociones)
            else:
                self.der.crearRegistroAsistencia(cedula,fecha,emociones)


listaCursos={"taller52":None,"intro52":None,"comunicacion51":None}


def registrarAsistencia (curso,cedula,fecha,emociones):
    raizAsistencia = listaCursos[curso]
    if raizAsistencia == None:
        listaCursos[curso] = asistencia(cedula)
        listaCursos[curso].crearRegistroAsistencia(cedula,fecha,emociones)
    else:
        raizAsistencia.crearRegistroAsistencia(cedula,fecha,emociones)



ListaNombres = ["Manuel Zapata","Billie Joe Armstrong" ,"Michael Joseph Jackson ", "Abel Makkonen Tesfaye", "Jonathan David Mendoza","Emma Watson"]
ListaCedula=[298742561,37237653,43238765,228945465,232143543,589855721]
RegistroActual=0
ListaDeGoogle={}
GuardoDatosEnLista=[]
diccionario={}
ListaDeImagenesParaLaAPI = ["ManuelZapata.jpg", "greenday.jpg","Jackson.jpg", "Weekend.jpg", "jonathan.PNG","EmmaWatson.jpg"]
ListaDeCursos=["Introduccion a la programación","Taller de Programacón","Introduccion a la programación","Taller de Programacón","Introduccion a la programación","Taller de Programacón"]
ventana=Tk()
ventana.title("TERCERA ETAPA || Imagen de Estudiante")

imagen1= ImageTk.PhotoImage(Image.open("ManuelZapata.jpg"))
imagen2 = ImageTk.PhotoImage(Image.open("greenday.jpg"))
imagen3 = ImageTk.PhotoImage(Image.open("Jackson.jpg"))
imagen4 = ImageTk.PhotoImage(Image.open("Weekend.jpg"))
imagen5 = ImageTk.PhotoImage(Image.open("jonathan.PNG"))
imagen6= ImageTk.PhotoImage(Image.open("EmmaWatson.jpg"))

ListaDeImagenesParaLaAPI = ["ManuelZapata.jpg", "greenday.jpg","Jackson.jpg", "Weekend.jpg", "jonathan.PNG","EmmaWatson.jpg"]
ListaDeImagenes=[imagen1,imagen2,imagen3,imagen4,imagen5,imagen6]



status = Label(ventana, text="Imagen 1 de " + str(len(ListaDeImagenes)), bd=1, relief=SUNKEN)


my_label = Label(image = imagen1)
my_label.grid(row=0,column=0, columnspan=3)

"""API DE GOOGLE"""
"""API DE GOOGLE"""
"""API DE GOOGLE"""

def reconocer_caras(url):
    global diccionario
    global GuardoDatosEnLista
    global ListaDeGoogle

    with io.open(url, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.face_detection(image=image)

    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('DESCONOCIDO', 'MUY POCO PROBABLE', 'IMPROBABLE', 'POSIBLE', 'PROBABLE', 'MUY PROBABLE')

    # lista simplificada de rostros con datos simplificados
    faces_list = []
    for face in faces:
        # dicccionario con los angulos asociados a la detección de la cara
        face_angles = dict(roll_angle=face.roll_angle, pan_angle=face.pan_angle, tilt_angle=face.tilt_angle)

        # confianza de detección (tipo float)
        detection_confidence = face.detection_confidence

        # Probabilidad de Expresiones
        face_expressions = dict(
            joy_likelihood=likelihood_name[face.joy_likelihood],
            sorrow_likelihood=likelihood_name[face.sorrow_likelihood],
            anger_likelihood=likelihood_name[face.anger_likelihood],
            surprise_likelihood=likelihood_name[face.surprise_likelihood],
            under_exposed_likelihood=likelihood_name[face.under_exposed_likelihood],
            blurred_likelihood=likelihood_name[face.blurred_likelihood],
            headwear_likelihood=likelihood_name[face.headwear_likelihood])

        # polígono de marco de cara
        vertices = []
        for vertex in face.bounding_poly.vertices:
            vertices.append(dict(x=vertex.x, y=vertex.y))

        face_dict = dict(face_angles=face_angles,
                         detection_confidence=detection_confidence,
                         face_expressions=face_expressions,
                         vertices=vertices
                         )
        faces_list.append(face_dict)
        ListaDeGoogle=face_dict
        diccionario=face_dict


Expone=["surprise_likelihood","anger_likelihood","joy_likelihood","joy_likelihood","joy_likelihood","surprise_likelihood","surprise_likelihood",
        "joy_likelihood","joy_likelihood"]

"""Para achivar imagen y sus respectivos datos"""
"""Para achivar imagen y sus respectivos datos"""
"""Para achivar imagen y sus respectivos datos"""

def ArchivarImagen(imagen,nombre,cedula,curso):
    """ Agrega al archivo datos de una persona existente o datos y la etiqueta de una nueva"""

    reconocer_caras(imagen)
    global GuardoDatosEnLista

    # nombre=input("Digita el nombre de la persona que deseas buscar : ")
    try:
        with open('reconocimientos.dat', 'r') as archi:
            lineas = [linea.split("[]") for linea in archi]
            for x in lineas:
                x[0] = eval(x[0])
                if x[0][0]==nombre and len(x[0]) == 4:
                    archi = open("reconocimientos.dat","a")
                    ahora = datetime.datetime.now()
                    fechaMejorada = ahora.strftime("%d/%m/%Y %H:%M:%S")
                    GuardoDatosEnLista = []
                    GuardoDatosEnLista.append(nombre)
                    GuardoDatosEnLista.append(diccionario)
                    GuardoDatosEnLista.append(fechaMejorada)
                    GuardoDatosEnLista.append(imagen)
                    GuardoDatosEnLista.append(cedula)
                    GuardoDatosEnLista.append(curso)
                    archi.write(GuardoDatosEnLista.__str__())
                    archi.write("\n")
                    archi.close()
                    GuardoDatosEnLista = []
                    break
            else:
                archi = open("reconocimientos.dat", "a")
                ahora = datetime.datetime.now()
                fechaMejorada = ahora.strftime("%d/%m/%Y %H:%M:%S")
                GuardoDatosEnLista = []
                GuardoDatosEnLista.append(nombre)
                GuardoDatosEnLista.append(diccionario)
                GuardoDatosEnLista.append(fechaMejorada)
                GuardoDatosEnLista.append(imagen)
                GuardoDatosEnLista.append(cedula)
                GuardoDatosEnLista.append(curso)
                archi.write(GuardoDatosEnLista.__str__())
                archi.write("\n")
                archi.close()
                GuardoDatosEnLista = []
    except:
        print("Algo salio mal")

"""Necesario para que la segunda ventana, vaya mostrando información que recolecta de la API"""
"""Necesario para que la segunda ventana, vaya mostrando información que recolecta de la API"""
"""Necesario para que la segunda ventana, vaya mostrando información que recolecta de la API"""

def VerRegistroActual():
    global RegistroActual
    global ListaDeGoogle
    sr = random.SystemRandom()
    ahora2 = datetime.datetime.now()
    fechaMejorada2 = ahora2.strftime("%d/%m/%Y %H:%M:%S")
    sv_nombre.set(ListaNombres[RegistroActual])
    sv_cedula.set(ListaCedula[RegistroActual])
    sv_curso.set(ListaDeCursos[RegistroActual])
    reconocer_caras(ListaDeImagenesParaLaAPI[RegistroActual])
    sv_joy.set(ListaDeGoogle.get("face_expressions").get("joy_likelihood"))
    sv_sorrow.set(ListaDeGoogle.get("face_expressions").get("sorrow_likelihood"))
    sv_anger.set(ListaDeGoogle.get("face_expressions").get("anger_likelihood"))
    sv_surprise.set(ListaDeGoogle.get("face_expressions").get("surprise_likelihood"))
    sv_under_exposed.set(ListaDeGoogle.get("face_expressions").get("under_exposed_likelihood"))
    sv_blurred.set(ListaDeGoogle.get("face_expressions").get("blurred_likelihood"))
    sv_headwear.set(ListaDeGoogle.get("face_expressions").get("headwear_likelihood"))
    sv_horactual.set(fechaMejorada2)
    sv_promedio.set(Expone[RegistroActual])

ventana_menu=0

"""Cuando el estudiante marca el curso de introduccion"""
"""Cuando el estudiante marca el curso de introduccion"""
"""Cuando el estudiante marca el curso de introduccion"""

def IntroPrograCurso():
    global ventana_menu
    ListaDeCursos.append("Introduccion a la programación")
    ventana_menu.destroy()

"""Cuando el estudiante marca el curso de taller"""
"""Cuando el estudiante marca el curso de taller"""

def TallerPrograCurso():
    global ventana_menu
    ListaDeCursos.append("Taller de Programacón")
    print("DX")
    ventana_menu.destroy()

def SeleccionaUnCurso():
    global ventana_menu
    ventana_menu = Tk()
    # ventana_menu.geometry("500x500")
    ventana_menu.title("Menu Principal")
    ventana_menu.configure(bg="#00CED1")

    lb_nombre2 = tk.Label(ventana_menu, text="Estudiante: " + str(ListaNombres[-1]), pady=10)
    lb_nombre2.grid(column=1, row=0, pady=3, columnspan=2, padx=(0, 100))
    lb_nombre2.configure(bg="#00CED1")

    lb_nombre3 = tk.Label(ventana_menu, text="Selecciona el grupo al cual asistiras :", pady=10)
    lb_nombre3.grid(column=1, row=2, pady=3, columnspan=2, padx=(0, 100))
    lb_nombre3.configure(bg="#00CED1")

    button_I = Button(ventana_menu, text="Introducción a la Programación GR 52",
                      command=lambda: IntroPrograCurso())  # Boton de incio de sesion
    button_I.grid(column=0, row=3, pady=6, columnspan=2, padx=(0, 250))
    button_I.configure(bg="#20B2AA")

    button_S = Button(ventana_menu, text="Taller de Programación GR 52", command=lambda :TallerPrograCurso())  # Boton de salirse
    button_S.grid(column=1, row=3, pady=6, columnspan=2, padx=(90, 0))
    button_S.configure(bg="#BA55D3")
    ventana_menu.mainloop()

def AddFoto():
    """Esta función agrega una nueva imagen a la interfaz grafica"""

    ventana.filename = filedialog.askopenfilename(initialdir="/", title="Selecciona una imagen",filetypes=(("jpeg files", ".jpg"), ("all files", ".*")))
    my_label = Label(ventana, text=lambda :ventana.filename)
    print(ventana.filename)
    my_image= ImageTk.PhotoImage(Image.open(ventana.filename))
    NuevoUsuario=simpledialog.askstring("Nuevo Miembro", "Ingresa Tú Nombre Completo :")
    NuevaCedula=simpledialog.askstring("Nuevo Miembre","Ingresa Tú Número de Cédula")
    ListaCedula.append(NuevaCedula)
    ListaNombres.append(NuevoUsuario)
    ListaDeImagenesParaLaAPI.append(str(ventana.filename))
    ListaDeImagenes.append(my_image)
    SeleccionaUnCurso()

def CapturarImagen():
    # Captura de fotografía basado en la cámara
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        titulo=simpledialog.askstring("IMPORTANTE", "Título de imagen (yo agrego el png):")
        NuevoUsuario = simpledialog.askstring("Nuevo Miembro", "Ingresa Tú Nombre Completo :")
        NuevaCedula = simpledialog.askstring("Nuevo Miembre", "Ingresa Tú Número de Cédula")
        ListaCedula.append(NuevaCedula)
        ListaNombres.append(NuevoUsuario)
        cv2.imwrite(titulo+".png", frame)
        url = titulo+".png"
        my_user = ImageTk.PhotoImage(Image.open(titulo+".png"))
        ListaDeImagenesParaLaAPI.append(url)
        ListaDeImagenes.append(my_user)
        print("Foto tomada correctamente")
        SeleccionaUnCurso()



def Siguiente(Image_number):
    """Se activa cuando el usuario presiona (>>) en la interfaz"""

    global my_label
    global button_N
    global button_B
    global RegistroActual


    my_label.grid_forget()
    my_label = Label(image=ListaDeImagenes[Image_number-1])
    button_N = Button(ventana, text=">>", command=lambda: Siguiente(Image_number + 1))
    button_B = Button(ventana, text="<<",command= lambda: Anterior(Image_number - 1))

    RegistroActual = Image_number-1
    VerRegistroActual()

    if Image_number == len(ListaDeImagenes):
        button_N = Button(ventana, text=">>", state= DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_B.grid(row=1, column=0)
    button_N.grid(row=1, column=2)

    lb_asistencia = tk.Label(ventana, text="Para Registrar tú Asistencia Selecciona una de las Siguientes Opciones :",
                             pady=10)
    lb_asistencia.grid(column=0, row=3, pady=3, columnspan=2, padx=(0, 0))
    lb_asistencia.configure(bg="#FFFACD")

    button_TF = Button(ventana, text="Tomar Foto", command=lambda: CapturarImagen())
    button_TF.grid(row=4, column=1, pady=10)

    button_ADD = Button(ventana, text="Cargar Foto", command=lambda: AddFoto())
    button_ADD.grid(row=4, column=0)

    button_TF.configure(bg="#ADFF2F")
    button_ADD.configure(bg="#00FA9A")


    status = Label(ventana, text="Imagen " + str(Image_number)+ " de " + str(len(ListaDeImagenes)), bd=1, relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3, sticky=W + E)


def Anterior(Image_number):
    """Se activa cuando el usuario presiona (<<) en la interfaz"""

    global RegistroActual
    global my_label
    global button_N
    global button_B
    global RegistroActual


    my_label.grid_forget()
    my_label = Label(image=ListaDeImagenes[Image_number - 1])
    button_N = Button(ventana, text=">>", command=lambda: Siguiente(Image_number + 1))
    button_B = Button(ventana, text="<<", command=lambda: Anterior(Image_number - 1))

    RegistroActual = Image_number-1
    VerRegistroActual()

    if Image_number == 1:
        button_B = Button(ventana, text="<<", state=DISABLED)


    my_label.grid(row=0, column=0, columnspan=3)
    button_B.grid(row=1, column=0)
    button_N.grid(row=1, column=2)

    lb_asistencia = tk.Label(ventana, text="Para Registrar tú Asistencia Selecciona una de las Siguientes Opciones :",
                             pady=10)
    lb_asistencia.grid(column=0, row=3, pady=3, columnspan=2, padx=(0, 0))
    lb_asistencia.configure(bg="#FFFACD")

    button_TF = Button(ventana, text="Tomar Foto", command=lambda: CapturarImagen())
    button_TF.grid(row=4, column=1, pady=10)

    button_ADD = Button(ventana, text="Cargar Foto", command=lambda: AddFoto())
    button_ADD.grid(row=4, column=0)

    button_TF.configure(bg="#ADFF2F")
    button_ADD.configure(bg="#00FA9A")


    status = Label(ventana, text="Imagen " + str(Image_number) + " de " + str(len(ListaDeImagenes)), bd=1,relief=SUNKEN)
    status.grid(row=5, column=0, columnspan=3, sticky=W + E)


"""FUNCIONES PARA CUANDO EL USUARIO DESEE VER LAS IMAGENES ARCHIVADAS"""
"""FUNCIONES PARA CUANDO EL USUARIO DESEE VER LAS IMAGENES ARCHIVADAS"""
"""FUNCIONES PARA CUANDO EL USUARIO DESEE VER LAS IMAGENES ARCHIVADAS"""

def DarleVidaAVerInfo():
    global ListaParaVerInfoImagenArchivada
    global sv_nombre2, sv_joy2, sv_sorrow2, sv_anger2, sv_surprise2, sv_under_exposed2, sv_blurred2, sv_headwear2, sv_fecha2,sv_curso2,sv_cedula2
    global MomentoExactoParaImprimir
    #print(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("joy_likelihood"))
    sv_nombre2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][0])
    sv_curso2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][5])
    sv_cedula2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][4])
    sv_joy2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("joy_likelihood"))
    sv_sorrow2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("sorrow_likelihood"))
    sv_anger2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("anger_likelihood"))
    sv_surprise2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("surprise_likelihood"))
    sv_under_exposed2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("under_exposed_likelihood"))
    sv_blurred2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("blurred_likelihood"))
    sv_headwear2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][1].get("face_expressions").get("headwear_likelihood"))
    sv_fecha2.set(ListaParaVerInfoImagenArchivada[MomentoExactoParaImprimir][2])

def VerInfoImagenArchivada():
    global ListaDeImagenesSegundaVentana
    global ListaAyudaNombres
    global RegistroMomento
    global root
    global ListaParaVerInfoImagenArchivada
    global sv_nombre2,sv_joy2,sv_sorrow2,sv_anger2,sv_surprise2,sv_under_exposed2,sv_blurred2,sv_headwear2,sv_fecha2,sv_curso2,sv_cedula2

    ListaParaVerInfoImagenArchivada=[]

    """Recorrido en archivos para sacar los datos necesarios"""

    archi = open("reconocimientos.dat", "r")
    lineas = [linea.split("[]") for linea in archi]
    for x in lineas:
        x[0] = eval(x[0])
        ListaParaVerInfoImagenArchivada.append(x[0])

    """CAUNDO se presiona ver info de la imagen se despliega esta iformación"""
    segundav = Toplevel()
    segundav.title("Información del Estudiante")
    segundav.minsize(400, 300)

    lb_nombre2 = tk.Label(segundav, text="Nombre: ")
    lb_cedula2 = tk.Label(segundav,text="Cédula: ")
    lb_curso2 = tk.Label(segundav, text="Curso en el que se encuentra :")
    lb_joy2 = tk.Label(segundav, text="Joy: ")
    lb_sorrow2 = tk.Label(segundav, text="Sorrow: ")
    lb_anger2 = tk.Label(segundav, text="Anger: ")
    lb_surprise2 = tk.Label(segundav, text="Surprise: ")
    lb_under_exposed2 = tk.Label(segundav, text="Under Exposed: ")
    lb_blurred2 = tk.Label(segundav, text="Blurred: ")
    lb_headwear2 = tk.Label(segundav, text="Headwear: ")
    lb_fecha2 = tk.Label(segundav,text="Guardada el:")

    sv_cedula2 = tk.StringVar()
    tb_cedula2 = ttk.Entry(segundav, textvariable=sv_cedula2, width=40)

    sv_curso2 = tk.StringVar()
    tb_curso2 = ttk.Entry(segundav, textvariable=sv_curso2, width=40)


    sv_nombre2 = tk.StringVar()
    tb_nombre2 = ttk.Entry(segundav, textvariable=sv_nombre2, width=40)

    sv_joy2 = tk.StringVar()
    tb_joy2 = ttk.Entry(segundav, textvariable=sv_joy2, width=40)

    sv_sorrow2 = tk.StringVar()
    tb_sorrow2 = ttk.Entry(segundav, textvariable=sv_sorrow2, width=40)

    sv_anger2 = tk.StringVar()
    tb_anger2 = ttk.Entry(segundav, textvariable=sv_anger2, width=40)

    sv_surprise2 = tk.StringVar()
    tb_surprise2 = ttk.Entry(segundav, textvariable=sv_surprise2, width=40)

    sv_under_exposed2 = tk.StringVar()
    tb_under_exposed2 = ttk.Entry(segundav, textvariable=sv_under_exposed2, width=40)

    sv_blurred2 = tk.StringVar()
    tb_blurred2 = ttk.Entry(segundav, textvariable=sv_blurred2, width=40)

    sv_headwear2 = tk.StringVar()
    tb_headwear2 = ttk.Entry(segundav, textvariable=sv_headwear2, width=40)

    sv_fecha2 = tk.StringVar()
    tb_fecha2 = ttk.Entry(segundav, textvariable=sv_fecha2, width=40)

    lb_nombre2.grid(column=0, row=0, padx=(20, 10))
    lb_cedula2.grid(column=0, row=1, padx=(20, 10))
    lb_curso2.grid(column=0, row=2, padx=(20, 10))
    lb_joy2.grid(column=0, row=3, padx=(20, 10))
    lb_sorrow2.grid(column=0, row=4, padx=(20, 10))
    lb_anger2.grid(column=0, row=5, padx=(20, 10))
    lb_surprise2.grid(column=0, row=6, padx=(20, 10))
    lb_under_exposed2.grid(column=0, row=7, padx=(20, 10))
    lb_blurred2.grid(column=0, row=8, padx=(20, 10))
    lb_headwear2.grid(column=0, row=9, padx=(20, 10))
    lb_fecha2.grid(column=0, row=10, padx=(20,10))

    tb_nombre2.grid(column=1, row=0, pady=5, columnspan=2, padx=(0, 20))
    tb_cedula2.grid(column=1, row=1, pady=5, columnspan=2, padx=(0, 20))
    tb_curso2.grid(column=1, row=2, pady=5, columnspan=2, padx=(0, 20))
    tb_joy2.grid(column=1, row=3, pady=5, columnspan=2, padx=(0, 20))
    tb_sorrow2.grid(column=1, row=4, pady=5, columnspan=2, padx=(0, 20))
    tb_anger2.grid(column=1, row=5, pady=5, columnspan=2, padx=(0, 20))
    tb_surprise2.grid(column=1, row=6, pady=5, columnspan=2, padx=(0, 20))
    tb_under_exposed2.grid(column=1, row=7, pady=5, columnspan=2, padx=(0, 20))
    tb_blurred2.grid(column=1, row=8, pady=5, columnspan=2, padx=(0, 20))
    tb_headwear2.grid(column=1, row=9, pady=5, columnspan=2, padx=(0, 20))
    tb_fecha2.grid(column=1, row=10, pady=5, columnspan=2, padx=(0,20))

    button_ANI = Button(segundav, text="Cerrar", command=lambda: segundav.destroy())
    button_ANI.grid(row=11, column=2, columnspan=3)



ListaAyudaNombres,ListaAyuda,ListaAyudaReal,RegistroMomento,cmb,ListaDeImagenesSegundaVentana,button_b,button_n=[],[],0,0,[],0,0,[]
my_label2,image_list,root,segundav,ListaParaVerInfoImagenArchivada,MomentoExactoParaImprimir="",[],"","",[],0
sv_nombre2,sv_joy2,sv_sorrow2,sv_anger2,sv_surprise2,sv_under_exposed2,sv_blurred2,sv_headwear2,sv_fecha2,sv_curso2,sv_cedula2="","","","","","","","","","",""

def BotonSiguiente(Image_number):
    global root
    global image_list
    global my_label2
    global RegistroMomento
    global MomentoExactoParaImprimir
    RegistroMomento = RegistroMomento +1

    my_label2.grid_forget()
    my_label2= Label(image=image_list[Image_number-1])
    button_n = Button(root, text="Siguiente", command=lambda : BotonSiguiente(Image_number+1))
    button_b = Button(root,text="Atrás",command=lambda : BotonRegreso(Image_number-1))

    my_label2.grid(row=1,column=0, columnspan=4)
    button_b.grid(row=2, column=0)
    button_n.grid(row=2, column=2)


    if Image_number == len(image_list):
        button_n = Button(root, text="Siguiente", state=DISABLED)
        button_n.grid(row=2, column=2)
    MomentoExactoParaImprimir = MomentoExactoParaImprimir +1
    DarleVidaAVerInfo()

def BotonRegreso(Image_number):
    global root
    global image_list
    global my_label2
    global RegistroMomento
    global MomentoExactoParaImprimir
    global segundav


    RegistroMomento = RegistroMomento -1
    my_label2.grid_forget()
    my_label2 = Label(image=image_list[Image_number - 1])
    button_n = Button(root, text="Siguiente", command=lambda: BotonSiguiente(Image_number + 1))
    button_b = Button(root, text="Atrás", command=lambda: BotonRegreso(Image_number - 1))

    my_label2.grid(row=1, column=0, columnspan=4)
    button_b.grid(row=2, column=0)
    button_n.grid(row=2, column=2)

    if Image_number == 1:
        button_b = Button(root, text="Atrás", state=DISABLED)
        button_b.grid(row=2, column=0)

    MomentoExactoParaImprimir = MomentoExactoParaImprimir -1
    DarleVidaAVerInfo()

def Espejo():
    print("Presiona [Q]  para salir")

    cap = cv2.VideoCapture(0)
    faceClassif = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    while True:
        ret, frame = cap.read()
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def May():
    global root
    global my_label2
    global RegistroMomento
    global ListaAyudaReal
    global ListaDeImagenesSegundaVentana
    global cmb
    global image_list
    global ListaAyuda
    global ListaAyudaNombres
    image_list = []
    ListaAyuda = []
    ListaAyudaReal = []
    ListaDeImagenesSegundaVentana=[]
    ListaAyudaNombres=[]

    """Primero cierro la ventana principal"""
    ventana.destroy()

    archi = open("reconocimientos.dat", "r")
    lineas = [linea.split("[]") for linea in archi]
    for x in lineas:
        x[0] = eval(x[0])
        ImagenG = x[0][3]
        ListaAyudaNombres.append(x[0][0])
        ListaDeImagenesSegundaVentana.append(ImagenG)
        if x[0][0] not in ListaAyuda:
            ListaAyuda.append(x[0][0])
    for i in ListaAyuda:
        ListaAyudaReal.append(i)
    """Nueva Pestaña cuando quieren ver las imagenes archivadas"""


    root = Tk()
    root.title("Imagenes Archivadas")

    imagen00 = ImageTk.PhotoImage(Image.open(ListaDeImagenesSegundaVentana[0]))

    for x in ListaDeImagenesSegundaVentana:
        Nueva= ImageTk.PhotoImage(Image.open(x))
        image_list.append(Nueva)

    my_label2 = Label(image=imagen00)
    my_label2.grid(column=0, row=1, columnspan=4)

    """Posicion en donde aparece el combobox"""

    cmb = ttk.Combobox(root, width="20", values=ListaAyudaReal)
    cmb.grid(row=0, column=1)

    """Personas Archivadas"""
    lb_nombre = tk.Label(root, text="Nombres Guardados: ")
    lb_nombre.grid(column=0, row=0)

    VerInfoImagenArchivada()

    """Botones que aparecen en la interfaz grafica y un lamba para hacer uso de una función"""

    button_b = Button(root, text="Atrás", command=BotonRegreso)
    button_n = Button(root, text="Siguiente",command=lambda : BotonSiguiente(2))
    button_exit = Button(root, text="Salir", command=root.quit)
    btn = ttk.Button(root, text="Ver Fecha", command=lambda :print("Fecha"))


    # Orden en los botones

    button_b.grid(row=2, column=0)
    button_exit.grid(row=2, column=1)
    button_n.grid(row=2, column=2)

    btn.grid(row=0, column=3, columnspan=4)
    DarleVidaAVerInfo()
    root.mainloop()


top= Toplevel()
top.title("Información del Estudiante")
top.minsize(400, 300)

lb_nombre = tk.Label(top, text="Nombre: ")
lb_cedula= tk.Label(top,text="Cedula : ")
lb_curso= tk.Label(top,text="Curso en el que se encuentra :")
lb_joy = tk.Label(top, text="Joy: ")
lb_sorrow = tk.Label(top, text="Sorrow: ")
lb_anger = tk.Label(top, text="Anger: ")
lb_surprise = tk.Label(top, text="Surprise: ")
lb_under_exposed = tk.Label(top, text="Under Exposed: ")
lb_blurred = tk.Label(top, text="Blurred: ")
lb_headwear = tk.Label(top, text="Headwear: ")
lb_horactual= tk.Label(top,text="Hora Actual :")
lb_promedio= tk.Label(top,text="Emoción Característica:")

sv_promedio= tk.StringVar()
tb_promedio= ttk.Entry(top,textvariable=sv_promedio,width=40)

sv_nombre = tk.StringVar()
tb_nombre = ttk.Entry(top, textvariable=sv_nombre, width=40)

sv_cedula = tk.StringVar()
tb_cedula = ttk.Entry(top, textvariable=sv_cedula, width=40)

sv_curso = tk.StringVar()
tb_curso = ttk.Entry(top, textvariable=sv_curso, width=40)

sv_joy = tk.StringVar()
tb_joy = ttk.Entry(top, textvariable=sv_joy, width=40)

sv_sorrow = tk.StringVar()
tb_sorrow = ttk.Entry(top, textvariable=sv_sorrow, width=40)

sv_anger = tk.StringVar()
tb_anger = ttk.Entry(top, textvariable=sv_anger, width=40)

sv_surprise = tk.StringVar()
tb_surprise = ttk.Entry(top, textvariable=sv_surprise, width=40)

sv_under_exposed = tk.StringVar()
tb_under_exposed = ttk.Entry(top, textvariable=sv_under_exposed, width=40)

sv_blurred = tk.StringVar()
tb_blurred = ttk.Entry(top, textvariable=sv_blurred, width=40)

sv_headwear = tk.StringVar()
tb_headwear = ttk.Entry(top, textvariable=sv_headwear, width=40)

sv_horactual = tk.StringVar()
tb_horactual = ttk.Entry(top, textvariable=sv_horactual, width=40)


lb_nombre.grid(column=0, row=0, padx=(20, 10))
lb_cedula.grid(column=0,row=1,padx=(20,10))
lb_curso.grid(column=0,row=2,padx=(20,10))
lb_joy.grid(column=0,row=3, padx=(20,10))
lb_sorrow.grid(column=0, row=4, padx=(20, 10))
lb_anger.grid(column=0, row=5, padx=(20, 10))
lb_surprise.grid(column=0, row=6, padx=(20, 10))
lb_under_exposed.grid(column=0, row=7, padx=(20, 10))
lb_blurred.grid(column=0, row=8, padx=(20, 10))
lb_headwear.grid(column=0, row=9, padx=(20, 10))
lb_horactual.grid(column=0,row=10,padx=(20,10))
lb_promedio.grid(column=0,row=11,padx=(20,10))

tb_nombre.grid(column=1, row=0, pady=5, columnspan=2, padx=(0, 20))
tb_cedula.grid(column=1,row=1,pady=5,columnspan=2,padx=(0,20))
tb_curso.grid(column=1,row=2,pady=5,columnspan=2,padx=(0,20))
tb_joy.grid(column=1, row=3, pady=5, columnspan=2, padx=(0, 20))
tb_sorrow.grid(column=1, row=4, pady=5, columnspan=2, padx=(0, 20))
tb_anger.grid(column=1, row=5, pady=5, columnspan=2, padx=(0, 20))
tb_surprise.grid(column=1, row=6, pady=5, columnspan=2, padx=(0, 20))
tb_under_exposed.grid(column=1, row=7, pady=5, columnspan=2, padx=(0, 20))
tb_blurred.grid(column=1, row=8, pady=5, columnspan=2, padx=(0, 20))
tb_headwear.grid(column=1, row=9, pady=5, columnspan=2, padx=(0, 20))
tb_horactual.grid(column=1,row=10,pady=5,columnspan=2,padx=(0,20))
tb_promedio.grid(column=1,row=11,pady=5,columnspan=2,padx=(0,20))

button_ANI= Button(top,text="Cerrar", command= lambda :top.destroy())
button_ANI.grid(row=12, column=2, columnspan=3)


button_B= Button(ventana,text="<<")
button_N= Button(ventana,text=">>", command= lambda : Siguiente(2))
button_L= Button(ventana,text="Salir", command= ventana.quit)
button_A = Button(ventana,text="Archivar", command=lambda : ArchivarImagen(ListaDeImagenesParaLaAPI[RegistroActual],ListaNombres[RegistroActual],ListaCedula[RegistroActual],ListaDeCursos[RegistroActual]))
button_ADD = Button(ventana,text="Cargar Foto", command= lambda : AddFoto())
button_AV = Button(ventana,text="Ver Imagenes Archivadas", command= lambda : May())
button_TF = Button(ventana,text="Tomar Foto", command=lambda :CapturarImagen())
button_Prueba= Button(ventana,text="Modo Espejo",command=lambda :Espejo())

"""Seccion de asistencia"""

lb_asistencia = tk.Label(ventana, text="Para Registrar tú Asistencia Selecciona una de las Siguientes Opciones :",pady=10)
lb_asistencia.grid(column=0, row=3, pady=3, columnspan=2, padx=(0, 0))
lb_asistencia.configure(bg="#FFFACD")

#Orden en los botones

button_B.grid(row=1, column=0)
button_L.grid(row=1, column=1)
button_Prueba.grid(row=2, column=0)
button_N.grid(row=1, column=2)
button_A.grid(row=2, column=2, pady=10)
button_TF.grid(row=4,column=1,pady=10)
status.grid(row=5, column=0, columnspan=3, sticky=W+E)
button_ADD.grid(row=4, column=0)
button_AV.grid(row=2, column=1)




#Colores en los botones
button_TF.configure(bg="#ADFF2F")
button_ADD.configure(bg="#00FA9A")


VerRegistroActual()
ventana.mainloop()