import vehiculos
"""""
import clientes
import empleados
import ventas
import alquileres
import citas
"""
from easygui import *

msg = "Elija un subsistema"
title = "Selector de subsistema"
choices = ["Clientes", "Empleados", "Vehículos",
           "Ventas", "Alquileres", "Citas", "Salir"]

choice = choicebox(msg, title, choices)

while (choice != choices[6]):
    """"    
    if choice==choices[0]:
        clientes.menu()
    if choice==choices[1]:
        empleados.menu()
    """
    if choice == choices[2]:
        vehiculos.menu()
    """""
    if choice==choices[3]:
        ventas.menu()
    if choice==choices[4]:
        alquileres.menu()
    if choice==choices[5]:
        citas.menu()"""    
    choice = choicebox(msg, title, choices)

