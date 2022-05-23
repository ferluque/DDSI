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

CREATE OR REPLACE TRIGGER num_bastidor
	BEFORE  
	INSERT on vehiculo
	FOR EACH ROW
DECLARE
    existe INTEGER;
BEGIN
	SELECT count(*) INTO existe FROM vehiculo WHERE num_bastidor = :new.num_bastidor;
	IF (existe > 0) THEN 
		raise_application_error(-20600, :new.num_bastidor || ' no pueden existir dos vehículos con el mismo número de bastidor');
	END IF;
END;

CREATE OR REPLACE TRIGGER disponibilidad
    BEFORE
    INSERT on vehiculo
    FOR EACH ROW
BEGIN
    IF (:new.disponibilidad != 'alquiler' or :new.disponibilidad != 'venta' or :new.disponibilidad != 'no disponible' THEN
        raise_application_error(-20601, :new.disponibilidad || ' la disponibilidad debe ser venta, alquiler o no disponible');
    END IF;
END;