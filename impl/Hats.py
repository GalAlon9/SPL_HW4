class _Hats:
    def __init__(self,con):
        self._con = con


    def insert_hat(self,hat):
        self._con.exacute("""INSERT INTO hats(id,topping,supplier,quantity)VALUES({},'{}',{},{}) """.format(hat.hat_id,hat.topping,hat.supplier_id,hat.quantity))

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