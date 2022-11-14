/*Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto “Ramos” */
SELECT p.Nombre
FROM Proveedor p
WHERE Ciudad LIKE '%Ramos%';

/*Listar los códigos de los materiales que provea el proveedor 4 
y no los provea el proveedor 5. Se debe resolver de 3 formas.*/
--1
SELECT pp1.CodMat
FROM Provisto_Por pp1
WHERE EXISTS(
	SELECT 1
	FROM Provisto_Por pp2
	WHERE pp1.CodProv = pp2.CodProv AND pp2.CodProv = 4
);
--2
SELECT CodMat
FROM Material
WHERE CodMat IN (
	SELECT CodMat
	FROM Provisto_Por
	WHERE CodProv = 4
);
--3
SELECT CodMat
FROM Provisto_Por
WHERE CodProv = 4 AND CodProv NOT IN (
	SELECT CodMat
	FROM Provisto_Por 
	WHERE CodMat = 5
	);

/* Listar los materiales, código y descripción, provistos por proveedores
de la ciudad de Ramos Mejía.*/
SELECT m.CodMat, m.Descripcion
	FROM Material m
	WHERE EXISTS(
		SELECT 1 
		FROM Provisto_Por pp 
		WHERE m.CodMat = pp.CodMat AND pp.CodProv IN (
			SELECT CodProv
			FROM Proveedor p
			WHERE p.Ciudad = 'Ramos Mejía'
		));

/*Listar los proveedores y materiales que provee. 
La lista resultante debe incluir a aquellos proveedores que no proveen ningún material.*/
SELECT p.Nombre AS Nombre_Proveedor, m.Descripcion AS Material_Provisto
FROM Material m
INNER JOIN Provisto_Por pp
ON m.CodMat = pp.CodMat
RIGHT JOIN Proveedor p
ON p.CodProv = pp.CodProv;

/*Listar los artículos que cuesten más de $30 o que estén
compuestos por el material 2*/
SELECT a.CodArt
FROM Articulo a 
where a.Precio > 30
UNION
SELECT cp.CodArt
FROM Compuesto_Por cp
WHERE cp.CodMat = '2'

/*Listar los artículos de Mayor precio.*/
SELECT CodArt,Descripcion,Precio
FROM Articulo
WHERE Precio = (SELECT max(Precio) FROM Articulo)

/*Listar los proveedores que proveen más de 3 materiales*/
SELECT pp.CodProv, count(pp.CodProv) as 'Cantidad Materiales'
FROM Provisto_Por pp
GROUP BY pp.CodProv
HAVING count(pp.CodProv)> 3

/*Crear una vista para el caso de los proveedores que proveen
más de 4 materiales. Mostrar la forma de invocar esa vista*/
CREATE VIEW proveedores_mas_materiales AS (
	SELECT pp.CodProv, count(pp.CodProv) as 'Cantidad Materiales'
		FROM Provisto_Por pp
        GROUP BY pp.CodProv
        HAVING count(pp.CodProv)> 4
);

SELECT *
FROM proveedores_mas_materiales;