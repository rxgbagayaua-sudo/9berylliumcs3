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
Senior = Senior_Patient("Maria Santos", 15000)
PhilHealth = PhilHealth_Patient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
print("Patient Name:", Regular.get_name())
print("Patient Type: ", end="")
Regular.display_patient_type()
print(f"Original Bill: {Regular.get_bill_amount()}")
print(f"Final Bill: ₱{Regular.calculate_bill():,.2f}")
print("")
print("Patient Name:", Senior.get_name())
print("Patient Type: ", end="")
Senior.display_patient_type()
print(f"Original Bill: {Senior.get_bill_amount()}")
print(f"Final Bill: ₱{Senior.calculate_bill():,.2f}")
print("")
print("Patient Name:", PhilHealth.get_name())
print("Patient Type: ", end="")
PhilHealth.display_patient_type()
print(f"Original Bill: {PhilHealth.get_bill_amount()}")
print(f"Final Bill: ₱{PhilHealth.calculate_bill():,.2f}")