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
