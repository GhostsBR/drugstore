import databaseController

db = databaseController.Database()
# db.start_database("mongodb+srv://system:vD1TyTbZuwz2XI29@cluster0.8ehcf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", "drugstore")

import drugstore

pt1 = drugstore.Patient("Carlos Santos", drugstore.Prescription("Paracetamol", "15/04/2021", 1, "Carlos Santos"), drugstore.Document("Carlos Santos"))
ds = drugstore.Pharmaceutical()

ds.receive_prescription(pt1)

