from database import Database
from tabla_info_client import Customer

my_db = Database()

my_customer = Customer("Leonel", 888, "leo@gmail.com", "Av Rivadavia 2500", "1500")
my_db.save_customer(customer=my_customer)
customer = my_db.fetchCustomerById(666)
my_db.get_table('info_client')
my_db.fetchByName()