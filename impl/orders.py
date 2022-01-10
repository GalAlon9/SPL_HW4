class orders:
    def __init__(self,con):
        self._con = con

    def create_orders_table(self):
        cursor = self._con.cursor()
        cursor.execute("""
            CREATE TABLE orders(
                id INTEGER PRIMARY KEY,
                location STRING NOT NULL,
                hat INTEGER,
                FOREIGN KEY("hat") REFERENCES "hats"("id") 
        );""")