create table empleado (
    dni varchar2(9) constraint empleado_dni_CP primary key,
    nombre varchar2(20) not null,
    apellido varchar2(50) not null,
    telefono varchar2(20) not null,
    correo varchar2(30) not null,
    domicilio varchar2(30) not null,
    rol varchar2(30) not null,
    salario float not null check (salario>0) 
);

create table vehiculo (
    num_bastidor
)