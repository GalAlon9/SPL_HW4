import atexit
import sqlite3
from DAOS.Hats import _Hats
from DAOS.Suppliers import _Suppliers
from DAOS.Orders import _Orders
from DTOS import Order
from DTOS.Hat import Hat
from DTOS.Supplier import Supplier


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect("database.db")
        self.hats = _Hats(self._conn)
        self.orders = _Orders(self._conn)
        self.suppliers = _Suppliers(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self.hats.create_hats_table()
        self.orders.create_orders_table()
        self.suppliers.create_suppliers_table()

    def read_config(self , path):
        file = open(path)
        line = file.readline().split(',')
        num_of_type = line[0]
        num_of_suppliers = line[1]

        for i in range (int(num_of_type)):
            split = file.readline().split(',')
            hat = Hat(split[0],split[1],split[2],split[3])
            self.hats.insert_hat(hat)

        for i in range (int(num_of_suppliers)):
            split = file.readline().split(',')
            supplier = Supplier(split[0],split[1])
            self.suppliers.insert_supplier(supplier)


    def read_orders(self, path):
        file = open(path)

        for line in file:
            split = line.split(',')
            order = Order(split[0],split[1])








rep = _Repository()
atexit.register(rep.close())

