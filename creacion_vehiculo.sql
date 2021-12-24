create table vehiculo (
    num_bastidor char(17) constraint num_bastidor_CP primary key,
    marca varchar2(15) not null,
    modelo varchar2(20) not null,
    tipo_vehiculo varchar2(15) not null,
    fecha_llegada date,
    fecha_matriculacion date,
    matricula varchar2(7)
)