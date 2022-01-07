/* creación de tabla */
create table vehiculo (
    num_bastidor varchar2(17) constraint num_bastidor_CP primary key,
    marca varchar2(15) not null,
    modelo varchar2(20) not null,
    tipo_vehiculo varchar2(15) not null,
    disponibilidad varchar(15) check (disponibilidad in('alquiler', 'venta', 'no disponible')) not null,
    fecha_llegada date not null,
    fecha_matriculacion date,
    matricula varchar2(7)
);

drop table vehiculo;

/* dar de alta vehículo con matricula */
insert into vehiculo values (1,2,3,4,'alquiler',to_date('10/06/2001','dd/mm/yyyy'),to_date('10/07/2001','dd/mm/yyyy'),'9');

select * from vehiculo;

delete from vehiculo where num_bastidor=1;