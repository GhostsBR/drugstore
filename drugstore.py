import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import databaseController
class Pharmaceutical:
    def receive_prescription(self, patient):
        drug_name = patient.prescription.drug_name
        drug_quantity = patient.prescription.drug_quantity
        if not patient.prescription:
            print(f"{bcolors.WARNING}O paciente precisa ter uma receita!{bcolors.ENDC}")
            return
        if not self.valid_prescription(patient):
            print(f"{bcolors.WARNING}A receita do paciente não é válida!{bcolors.ENDC}")
            return
        if not self.verify_stock(drug_name, drug_quantity):
            print(f"{bcolors.WARNING}Não remédio solicitado não existe no estoque!{bcolors.ENDC}")
            return
        if not self.take_from_stock(drug_name, drug_quantity):
            print(f"{bcolors.WARNING}Não foi possível pegar o remédio no estoque{bcolors.ENDC}")
        self.delivery_drug(patient)


    def valid_prescription(self, patient):
        date_now = [datetime.datetime.now().day, datetime.datetime.now().month, datetime.datetime.now().year]
        date_expire = patient.prescription.expiration_date.split("/")
        if int(date_expire[0]) >= date_now[0]:
            if int(date_expire[1]) >= date_now[1]:
                if not int(date_expire[2]) >= date_now[2]:
                    return False
            else:
                return False
        else:
            return False
        if not patient.name == patient.prescription.patient_name or not patient.name == patient.document.fullname:
            return False
        return True

    def verify_stock(self, drug_name, drug_quantity):
        database_find = databaseController.Database().get_one_stock(drug_name)
        if database_find:
            if database_find["quantity"] >= drug_quantity:
                return True
        return False

    def delivery_drug(self, patient):
        print(f"{bcolors.OKGREEN}-{bcolors.ENDC}"*100)
        print(f"{bcolors.OKGREEN}MEDICAMENTO ENTREGUE{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}O medicamento {patient.prescription.drug_name} foi entregue ao paciente {patient.name}{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}-{bcolors.ENDC}" *100)

    def take_from_stock(self, drug_name, drug_quantity):
        return databaseController.Database().update_stock(drug_name, drug_quantity)


class Prescription:
    def __init__(self, drug_name, expiration_date, drug_quantity, patient_name):
        self.drug_name = drug_name
        self.expiration_date = expiration_date
        self.drug_quantity = drug_quantity
        self.patient_name = patient_name


class Document:
    def __init__(self, fullname):
        self.fullname = fullname


class Patient:
    def __init__(self, name, prescription, document):
        self.name = name
        self.prescription = prescription
        self.document = document

    def get_name(self):
        return self.name
