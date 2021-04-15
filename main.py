import databaseController
import drugstore

db = databaseController.Database()
pt1 = drugstore.Patient("Carlos Santos", drugstore.Prescription("Paracetamol", "15/04/2021", 1, "Carlos Santos"),
                        drugstore.Document("Carlos Santos"))
drugstore.Pharmaceutical().receive_prescription(pt1)

