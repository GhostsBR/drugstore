import pymongo


class Database:
    dbclient = pymongo.MongoClient("mongodb+srv://system:vD1TyTbZuwz2XI29@cluster0.8ehcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = dbclient["drugstore"]
    stock = db["stock"]

    def get_stock(self):
        return self.stock.find()

    def get_one_stock(self, drug_name):
        return self.stock.find_one({"name":drug_name})

    def update_stock(self, drug_name, drug_quantity):
        result = self.stock.find_one({"name":drug_name})
        resultQuantity = result['quantity']
        if resultQuantity >= drug_quantity:
            try:
                self.stock.update_one({"name":drug_name}, {"$set": {"quantity": resultQuantity - drug_quantity}})
                return True
            except:
                return False
        return False