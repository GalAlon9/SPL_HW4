class _Orders:
    def __init__(self,con):
        self._con = con

    def create_orders_table(self):
        cursor = self._con.cursor()
        cursor.execute("""
            CREATE TABLE orders(
                id INTEGER PRIMARY KEY,
                location STRING NOT NULL,
                hat_id INTEGER,
                FOREIGN KEY("hat_id") REFERENCES "hats"("id") 
        );""")

    def insert_order(self,order):
        self._con.execute("""INSERT INTO orders(id,location,hat_id)
                VALUES (?,?,?)""", [order.id,order.location,order.hat_id])