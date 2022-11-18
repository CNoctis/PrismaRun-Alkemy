from sqlalchemy import Column
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.orm import Session
from tabla_info_client import Customer
from db import engine

class Database():
    """Manipulador de la base de datos info_client"""
    # Conexión
    engine = engine

    def __init__(self) -> None:
        self.connection = self.engine.connect()
        print("DB instance create")

    def get_table(self, query: str) -> None:
        """Consulta todos los datos de una tabla
        :param query: tabla a consultar
        :type query: str"""
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery:
            print(data)

    def save_customer(self, customer: Customer) -> None:
        """Realiza la inserción de datos
        :param customer: Objeto Customer a cagar(Dupla de datos)
        :type customer: Customer"""
        self.connection.execute(f"""INSERT INTO info_client( name, age, email, address, zip_code)
                                    VALUES('{customer.name}',
                                            '{customer.age}',
                                            '{customer.email}',
                                            '{customer.address}',
                                            '{customer.zip_code}')""")


    def fetchByName(self) -> None:
        """Retorna todos los nombres en la tabla info_client"""
        meta = MetaData()
        customer = Table('info_client', meta, Column('name'))
        data = self.connection.execute(customer.select())
        for cust in data:
            print(cust)

    def fetchCustomerById(self, id_client: int) -> None:
        """Consulta ID"""
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter(Customer.id == id_client)
        return customerData

    def save_data(self, customer) -> None:
        """ Guardado de dato"""
        session = Session(bind=self.connection)
        session.add(customer)
        session.commit()

    def updateCustomer(self, name: str, address: str) -> None:
        """Actualización de datos"""
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.address: address}
        customerData = session.query(Customer).filter(Customer.name == name)
        customerData.update(dataToUpdate)
        session.commit()

    def deleteCustomer(self, id_client):
        """Borrado de datos"""
        session = Session(bind=self.connection)
        customerData = session.query(Customer).filter(Customer.id == id_client).first()
        session.delete(customerData)
        session.commit()

    



