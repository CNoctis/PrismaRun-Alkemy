# Exercise 1
# Mostrar el precio máximo de los productos de la 
# tabla PRODUCTS por línea de producto y renombrar ese campo como Precio_Maximo
SELECT productLine, MAX(buyPrice) AS Precio_Maximo 
FROM products
GROUP BY productLine;

# Exercise 3
# De la tabla EMPLOYEES mostrar cuanta cantidad de representantes de ventas hay 
# en cada oficina que no sea la 4. Hicimos dos versiones.
SELECT officeCode, COUNT(employeeNumber) 
FROM employees e 
WHERE officeCode <> 4 AND jobTitle = 'Sales Rep'
GROUP BY officeCode ;

# Exercise 5
# Mostrar en una tabla el número de cada orden, la cantidad y la fecha de envío (shippedDate)
SELECT od.orderNumber, quantityordered, shippeddate 
FROM orderdetails od
LEFT JOIN orders o ON od.ordernumber=o.ordernumber;

# Exercise 7
# Obtener la cantidad de clientes por país, ordenado de mayor a menor. Solo mostrar 
# aquellos países con mas de 5 clientes.
SELECT country, COUNT(*) Total
FROM customers c
GROUP BY country
HAVING COUNT(*) > 5
ORDER BY Total DESC
LIMIT 5;

# Exercise 9
# Obtener una lista con los nombres de clientes y 
# la cantidad de ordenes que se emitieron para ellos.
SELECT customerName, COUNT(o.customerNumber) AS cantidad 
FROM customers c LEFT JOIN orders o on c.customerNumber = o.customerNumber 
GROUP BY c.customerNumber 

# Exercise 11
#Aplicar un descuento del 10% (buyPrice) a los productos cuya cantidad en stock sea 
#mayor a 8000 (quantityInStock)
SELECT quantityInStock ,((buyPrice -(buyPrice*10)/100)) AS buyPriceDesc, buyPrice
FROM products p
WHERE quantityInStock > 8000;

# Exercise 13
# Obtenga los codigos de producto, nombre, linea a la que pertenecen y descripción de 
# aquellos en los cuales la descripción del producto contenga la palabra "features"
SELECT productCode, productname, productLine, productDescription  
FROM products
WHERE productDescription LIKE '%features%'

# Exercise 15
# Obtener los nombres de las líneas de producto que tengan más de una palabra
SELECT productLine FROM productlines p
WHERE productLine LIKE '% %';

# Exercise 17
# Obtener un listado de ordenes emitidas a clientes de USA mostrando el valor total de 
# cada orden si se le aplicará un aumento del 10%
SELECT o.orderNumber, (SUM(quantityOrdered * priceEach) * 1.1) AS price
FROM orders o 
LEFT JOIN orderdetails od ON o.orderNumber = od.orderNumber  
LEFT JOIN customers c ON o.customerNumber = c.customerNumber 
WHERE c.country = 'USA'
GROUP BY o.orderNumber;