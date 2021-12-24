from easygui import *

def menu():
    msg = "Elija una de las siguientes opciones"
    title = "Subsistema de vehículos"
    choices = ["Dar de alta", "Retirar", "Consultar disponibilidad", "Consultar características", "Modificar características", "Volver atrás"]
    choice = choicebox(msg, title, choices)

    while (choice != choices[5]):
        """"
        if choice==choices[0]:
            dar_de_alta()
        if choice==choices[1]:
            retirar()
        if choice==choices[2]:
            consultar_disponibilidad()
        if choice==choices[3]:
            consultar_caracteristicas()
        if choice==choices[4]:
            modificar_caracteristicas()
        choice = choicebox(msg, title, choices)

def dar_de_alta():

def retirar():

def consultar_disponibilidad():

def consultar_caracteristicas():

def modificar_caracteristicas():"""