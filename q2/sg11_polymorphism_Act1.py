class Patient:
    def __init__(self,name:str,bill_amount:float):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount

    def display_patient_type(self):
        print("Regular Patient")

class Senior_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * .80

    def display_patient_type(self):
        print("Senior Citizen")
    
class PhilHealth_Patient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * .85

    def display_patient_type(self):
        print("Philhealth Member")

Regular = Patient("Juan Dela Cruz", 15000)
print("Hospital Billing System")
print("-----------------------")
print(f"Patient Name: {get_name(Patient)}")
