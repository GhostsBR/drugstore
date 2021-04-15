class Drugstore:
    def receive_prescription(self):
        pass

    def valid_prescription(self):
        pass

    def verify_stock(self):
        pass

    def delivery_drug(self):
        pass

    def take_from_stock(self):
        pass


class Prescription:
    def __init__(self, drug_name, expiration_date, quantity, patient_name):
        self.drug_name = drug_name
        self.expiration_date = expiration_date
        self.quantity = quantity
        self.patient_name = patient_name


class Document:
    def __init__(self, fullname, birth):
        pass


class Patient:
    def __init__(self, prescription, document):
        self.prescription = prescription
        self.document = document
