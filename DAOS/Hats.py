from DTOS.Hat import Hat


class _Hats:
    def __init__(self, con):
        self._con = con

    def insert_hat(self, hat):
        self._con.execute(
            """INSERT INTO hats(id,topping,supplier,quantity)VALUES(?,?,?,?) """,[hat.id, hat.topping,
                                                                                              hat.supplier_id,
                                                                                              hat.quantity])

    def create_hats_table(self):
        cursor = self._con.cursor()
        cursor.execute("""
                        CREATE TABLE hats (
                        "id"       INTEGER  PRIMARY KEY , 
                        "topping"  TEXT NOT NULL,   
                        "supplier" INTEGER,
                        "quantity" INTEGER NOT NULL,
                        FOREIGN KEY("supplier") REFERENCES "suppliers"("id")
                        );""")

    def place_order_from_inventory(self, topping_order):
        cursor = self._con.cursor()
        cursor.execute(""" SELECT * 
                FROM hats 
                WHERE topping = ?
                ORDER BY supplier""", [topping_order])
        hat = Hat(*cursor.fetchone())
        self.update_quantity(hat, cursor)
        return hat

    def contains_topping(self,topping):
        cursor = self._con.cursor()
        cursor.execute(""" SELECT id 
                       FROM hats 
                       WHERE topping = ?
                      """, [topping])
        hat_id = cursor.fetchone()
        # returns true if topping exist , else returns false
        return hat_id is not None

    def update_quantity(self, hat, cursor):
        if hat.quantity > 1:
            temp = hat.quantity - 1
            cursor.execute("UPDATE hats SET quantity = temp WHERE id = ?", [hat.id])
        else:
            cursor.execute("DELETE FROM hats WHERE id = ?", [hat.id])
