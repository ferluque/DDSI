from easygui import *
import datetime
import pyodbc

def inicializar():
    cursor.execute("create table vehiculo (num_bastidor varchar2(17) constraint num_bastidor_CP primary key,\
marca varchar2(15) not null,modelo varchar2(20) not null,tipo_vehiculo varchar2(15) not null,\
disponibilidad varchar(15) check (disponibilidad in('alquiler', 'venta', 'no disponible')) not null,\
fecha_llegada date not null,fecha_matriculacion date,matricula varchar2(7))")
    cursor.commit()

def dar_de_alta():
    seguir=1
    cursor.execute("savepoint sin_crear")
    while seguir !=0:
        print("Introduzca los datos del vehículo: ")
        print("1. Número de bastidor:")
        num_bastidor = input()
        print("2. Marca:")
        marca = input()
        print("3. Modelo:")
        modelo = input()
        print("4. Tipo de vehículo:")
        tipo = input()
        print("5. Disponibilidad (alquiler, venta, no disponible):")
        disponibilidad=input()
        print("6. Fecha de llegada:")
        fecha_llegada=input()
        print("7. Matrícula (dejar en blanco si no está matriculado):")
        matricula=input()

        if matricula!="":
            print("8. Fecha de matriculación:")
            fecha_matriculacion=input()
            # Insertar sin matrícula ni fecha de matriculación
        if matricula=="":
            orden = "insert into vehiculo (num_bastidor, marca, modelo, tipo_vehiculo, disponibilidad, fecha_llegada)\
values ('"+num_bastidor+"','"+marca+"','"+modelo+"','"+tipo+"','"+disponibilidad+"',to_date('"+fecha_llegada+"','dd/mm/yyyy'))"
            # print(orden)
            try:
                cursor.execute(orden)
            except pyodbc.Error as ex:
                print("ERROR - no se ha insertado el vehículo\n" + ex.args[1].split("\n")[0]+"\n")
        # Insertar con matrícula
        else:
            orden = "insert into vehiculo values ('"+num_bastidor+"','"+marca+"','"+modelo+"','"+tipo+"','"+disponibilidad+\
"',to_date('"+fecha_llegada+"','dd/mm/yyyy'),to_date('"+fecha_matriculacion+"','dd/mm/yyyy'),'"+matricula+"')"
            # print(orden)
            try:
                cursor.execute(orden)
            except pyodbc.Error as ex:
                print("ERROR - no se ha insertado el vehículo\n" + ex.args[1].split("\n")[0]+"\n")
        print("Quiere insertar otro vehículo? (1=Si/0=No)")
        seguir = int(input())

    print("Confirmar los cambios? (1=Si/0=No)")
    confirmar = int(input())
    if confirmar==0:
        cursor.execute("rollback to savepoint sin_crear")
    else:
        cursor.commit()

def retirar():
    seguir = 1
    cursor.execute("savepoint sin_borrar")
    while seguir:
        print("¿Desea mostrar los vehículos disponibles? (1=Si/0=No)")
        mostrar = bool(input())
        if mostrar:
            cursor.execute("select * from vehiculo")
            row = cursor.fetchone()
            while row:
                print(row)
                row = cursor.fetchone()

            print("Introduzca el número de bastidor del vehículo que desea retirar")
            nb = input()
            cursor.execute("delete from vehiculo where num_bastidor="+nb)
        print("Desea eliminar más vehículos?")
        seguir=int(input())
        # print(seguir)
    print("Confirmar cambios?")
    confirm = int(input())
    if confirm:
        cursor.commit()
    else:
        cursor.execute("rollback to savepoint sin_borrar")

def consultar_disponibilidad():
    seguir=1
    while seguir:
        print("Introduzca una marca (dejar en blanco si no quiere especificar)")
        marca=input()
        print("Introduzca un modelo (dejar en blanco si no quiere especificar)")
        modelo=input()

        if marca=="" and modelo=="":
            cursor.execute("select marca,modelo,tipo_vehiculo,fecha_llegada,disponibilidad from vehiculo")
        if marca=="" and modelo!="":
            cursor.execute("select marca,modelo,tipo_vehiculo,fecha_llegada,disponibilidad from vehiculo where modelo='"+modelo+"'")
        if marca!="" and modelo!="":
            cursor.execute("select marca,modelo,tipo_vehiculo,fecha_llegada,disponibilidad from vehiculo where modelo='"+modelo+"'"+" and marca='"+ marca+"'")
        if marca!="" and modelo=="":
            cursor.execute("select marca,modelo,tipo_vehiculo,fecha_llegada,disponibilidad from vehiculo where marca='"+marca+"'")

        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()

        print("Desea realizar otra consulta?")
        seguir=int(input())

def consultar_caracteristicas():
    seguir=1
    while seguir:
        print("Introduzca un número de bastidor")
        nb=input()
        cursor.execute("select * from vehiculo where num_bastidor='"+nb+"'")

        row = cursor.fetchone()
        print(row)

        print("Desea realizar otra consulta?")
        seguir=int(input())

def modificar_caracteristicas():
    cursor.execute("savepoint sin_modificar")
    print("Desea mostrar los vehículos disponibles?")
    mostrar = int(input())
    if mostrar:
        cursor.execute("select * from vehiculo")
        row = cursor.fetchone()
        i=0
        while row:
            print(row)
            row = cursor.fetchone()
    seguir = True
    while seguir:
        print("Qué vehículo desea modificar? (Introduzca el número de bastidor)")
        nb = input()
        print("Qué característica desea modificar?")
        print("1. Disponibilidad")
        print("2. Matrícula")
        print("3. Fecha de matriculación")
        select = int(input())
        print("Nuevo valor")
        nv = input()
        if select==1:
            try:
                cursor.execute("update vehiculo set disponibilidad='"+nv+"' where num_bastidor='"+nb+"'")
            except pyodbc.Error as ex:
                print("ERROR - no se han modificado datos del vehículo\n"+ex.args[1].split("\n")[0]+"\n")

        if select==2:
            try:
                cursor.execute("update vehiculo set matricula='"+nv+"' where num_bastidor='"+nb+"'")
            except pyodbc.Error as ex:
                print("ERROR - no se han modificado datos del vehículo\n"+ex.args[1].split("\n")[0]+"\n")
        if select==3:
            try:
                cursor.execute("update vehiculo set fecha_matriculacion=to_date('"+nv+"', 'dd/mm/yyyy') where num_bastidor='"+nb+"'")
            except pyodbc.Error as ex:
                print("ERROR - no se han modificado datos del vehículo\n"+ex.args[1].split("\n")[0]+"\n")
        print("Desea realizar otra modificación?")
        seguir = int(input())
    print("Desea confirmar los cambios?")
    confirm = int(input())
    if confirm:
        cursor.commit
    else:
        cursor.execute("rollback to savepoint sin_modificar")

def menu():
    print("Escoja una opción:")
    print("1. Dar de alta vehículo")
    print("2. Retirar vehículo")
    print("3. Consultar disponibilidad")
    print("4. Consultar características")
    print("5. Modificar características")
    print("6. Salir")
    choice = int(input())
    return choice

cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=oracle0.ugr.es;Service Name=practbd.oracle0.ugr.es;User ID=x0953877;Password=x0953877')
cursor = cnxn.cursor()
# inicializar()
choice = menu()

while (choice != 6):
    if choice==1:
        dar_de_alta()
    if choice==2:
        retirar()
    if choice==3:
        consultar_disponibilidad()
    if choice==4:
        consultar_caracteristicas()
    if choice==5:
        modificar_caracteristicas()
    choice=menu()