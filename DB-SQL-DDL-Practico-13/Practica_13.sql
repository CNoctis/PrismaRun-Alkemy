USE Curso
GO
/*Creación de tabla alumno*/
CREATE TABLE Alumno(Legajo INT PRIMARY KEY NOT NULL,
                    Nombre VARCHAR(30)NOT NULL,
					Apellido VARCHAR(30) NOT NULL,
					Fecha_Nacimiento DATE NOT NULL);
/*Creación de tabla Materia*/
CREATE TABLE Materia(Codigo INT PRIMARY KEY NOT NULL,
                     Descripcion VARCHAR(50) NOT NULL);
/*Creación de tabla Cursa*/
CREATE TABLE Cursa(Legajo_Alumno INT foreign KEY REFERENCES Alumno(Legajo),
                   Codigo_Materia INT foreign KEY REFERENCES Materia(Codigo));
                   
/*Inserción de datos*/
INSERT INTO Alumno VALUES(1,'Cristian','Rosas','1998-12-02'),
						 (2,'Eliana','Dominguez','2000-06-28'),
						 (3,'Claudia','Guaina','1972-12-02'),
						 (4	,'Anthoni','Rosas','2004-08-26'),
						 (5,'Juan','Perez','2000-01-21');
INSERT INTO Materia VALUES(1,'Programacion'),
						  (2,'Estadistica'),
						  (3,'Ingles'),
						  (4,'Metodologia de la investigacion'),
						  (5,'Matematica');
INSERT INTO Cursa VALUES(1,5),
                        (2,4),
						(3,3),
						(4,2),
						(5,1);