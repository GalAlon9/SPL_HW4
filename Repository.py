import atexit
import sqlite3
from DAOS.Hats import _Hats
from DAOS.Suppliers import _Suppliers
from DAOS.Orders import _Orders
from DTOS.Order import Order
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

    def read_config(self, path):
        file = open(path)
        line = file.readline().split(',')
        num_of_type = line[0]
        num_of_suppliers = line[1]

        for i in range(int(num_of_type)):
            split = file.readline().split(',')
            hat = Hat(split[0], split[1], split[2], split[3])
            self.hats.insert_hat(hat)

        for i in range(int(num_of_suppliers)):
            split = file.readline().split(',')
            supplier = Supplier(split[0], split[1])
            self.suppliers.insert_supplier(supplier)

    def read_orders(self, orders_path, output_path):
        file = open(orders_path)
        output_file = open(output_path)
        i = 0
        for line in file:
            split = line.split(',')
            location = split[0]
            topping = split[1]
            if self.hats.contains_topping(topping):
                i += 1
                hat = self.hats.place_order_from_inventory(topping)
                order = Order(i, location, hat.id)
                self.orders.insert_order(order)
                supplier_name = self.suppliers.get_name(hat.supplier_id)
                self.update_output_file(output_file, topping, supplier_name, location)
        file.close()
        output_file.close()
        return output_file

    @staticmethod
    def update_output_file(output_file, topping, supplier_name, location):
        output_file.write("{},{},{}\n".format(topping, supplier_name, location))


rep = _Repository()
atexit.register(rep.close)
