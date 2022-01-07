import vehiculos
"""""
import clientes
import empleados
import ventas
import alquileres
import citas
"""
import easygui
import pyodbc

cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name=practbd.oracle0.ugr.es;User ID=x0953877;Password=x0953877')
cursor = cnxn.cursor()
print("Conectado a la BD")

msg = "Elija un subsistema"
title = "Selector de subsistema"
choices = ["Clientes", "Empleados", "Vehículos",
           "Ventas", "Alquileres", "Citas", "Salir"]



choice = easygui.choicebox(msg, title, choices)

while (choice != choices[6]):
    """"    
    if choice==choices[0]:
        clientes.menu()
    if choice==choices[1]:
        empleados.menu()
    """
    if choice == choices[2]:
        vehiculos.menu(cnxn)
    """""
    if choice==choices[3]:
        ventas.menu()
    if choice==choices[4]:
        alquileres.menu()
    if choice==choices[5]:
        citas.menu()"""    
    choice = easygui.choicebox(msg, title, choices)

