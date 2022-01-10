class _Hats:
    def __init__(self,con):
        self._con = con


    def insert_hat(self,hat):
        self._con.execute("""INSERT INTO hats(id,topping,supplier,quantity)VALUES({},'{}',{},{}) """.format(hat.hat_id,hat.topping,hat.supplier_id,hat.quantity))

    def create_hats_table(self):
        cursor = self._con.cursor()
        cursor.execute("""
                        CREATE TABLE "hats"(
                        "id"       INTEGER  PRIMARY KEY , 
                        "topping"  STRING NOT NULL,   
                        "supplier" INTEGER,
                        "quantity" INTEGER NOT NULL,
                        FOREIGN KEY("supplier") REFERENCES "suppliers"("id")
                        );""")


    def place_order_from_inventory(self,topping_order):
        cursor = self._con.cursor()
        cursor.execute(""" SELECT * 
                FROM hats 
                WHERE hats.topping = topping_order 
                ORDER BY hats.supplier""")
        curr_line = cursor.fetchone()
        if curr_line[3]>1:
            temp = curr_line[3] -1
            cursor.execute("UPDATE hats SET hats.quantity = temp WHERE hats.id = curr_line[0]")
        else:
            cursor.execute("DELETE FROM hats WHERE hats.id = curr_line[0]")

