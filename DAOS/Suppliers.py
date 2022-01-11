class _Suppliers:
    def __init__(self,con):
        self._con = con

    def create_suppliers_table(self):
        cursor = self._con.cursor()
        cursor.execute("""
            CREATE TABLE suppliers(
                id   INTEGER PRIMARY KEY, 
                name STRING NOT NULL
                );""")


    def insert_supplier(self,supplier):
        self._con.execute("""INSERT INTO suppliers(id,name) 
                VALUES({},'{}')""".format(supplier.id, supplier.name))

    def get_name(self,supplier_id):
        cursor = self._con.cursor()
        cursor.execute(""" SELECT name 
                      FROM suppliers 
                      WHERE id = {}
                      """.format(supplier_id))
        supplier_name = cursor.fetchone()
        return supplier_name