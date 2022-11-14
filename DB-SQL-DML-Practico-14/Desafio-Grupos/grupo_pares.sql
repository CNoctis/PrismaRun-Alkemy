Consultas Grupo 6 (Pares)

--2.	De la tabla ORDERS obtener los números de las últimas 5 órdenes

select orderNumber
from orders
order by orderNumber desc
limit 5

--4.	Indicar en una misma consulta: la cantidad de registros de la tabla productos, 
--el precio promedio de los mismos, el precio máximo y el precio mínimo y la suma total 
--de productos en stock (sin agrupar por producto)

select count(*) as cantidad_registros,
	avg(buyPrice) as precio_promedio, 
	max(buyPrice) as precio_maximo, 
	min(buyPrice) as precio_minimo,
	sum(quantityInStock) as cantidad_productos
from products

--6.	Obtener la cantidad de clientes por país, ordenado de mayor a menor

select count(customerNumber), country
from customers
group by country
order by count(customerNumber) desc

--8.	Obtener todas las ordenes por número de cliente que hayan sido emitidas 
--en el año 2005. Solo mostrar aquellos clientes con mas de 3 ordenes

select customerNumber as cliente, count(customerNumber) as cantidad_clientes
from orders
where year(orderDate) = '2005'
group by customerNumber 
having count(customerNumber) > 3


--10.	Obtener los nombres de los clientes y el monto (amount) de aquellos que realizaron 
--compras en los meses de Marzo de cada año. Ordenar por monto de mayor a menor

select c.customerName ,p.customerNumber as cliente, p.amount as monto_total, year(p.paymentDate) as año
from customers c 
inner join payments p 
on c.customerNumber = p.customerNumber 
where month(p.paymentDate) = '03'
order by p.amount desc


--11 . Obtener los registros de los productos cuyo codigo inicie con la secuencia " S10_ "

select productCode, productName
from products
where productCode like "S10_%"


--14.	Obtenga los codigos de los pagos (payments) , fecha y monto de aquellos que 
--comienzan con la secuencia "IP" y son mayores o iguales a 1000

select checkNumber as codigo, paymentDate as fecha, amount as monto
from payments
where checkNumber like "IP%" and amount >= 1000


--16.	Obtener la cantidad de cheques emitidos por año desde el mas actual hasta el mas antiguo, 
--el importe promedio de los mismos, el máximo importe y el mínimo importe

select 	year(paymentDate) as año,
		count(checkNumber) as cantidad_cheques, 
		avg(amount) as importe_promedio, 
		max(amount) as maximo_importe,
		min(amount) as importe_minimo 
from payments
group by año 
order by año desc

--18.	Obtener el listado de clientes que sean USA o España cuyo límite de crédito sea mayor a 
--50000 que no tengan ningun representante de ventas (salesRepEmployeeNumber)  asignado


--PARA REVISAR--

select salesRepEmployeeNumber
from customers
where ((country = 'USA' or country = 'Spain') and creditLimit > 50000) or salesRepEmployeeNumber is null