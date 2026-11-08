class Patient:
    """Parent class: a regular patient (no discount)."""

    def __init__(self, name, bill_amount):
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
        print("Patient Type: Regular Patient")


class SeniorPatient(Patient):
    """Child class: Senior Citizen gets a 20% discount."""

    def calculate_bill(self):
        return self.get_bill_amount() * 0.80

    def display_patient_type(self):
        print("Patient Type: Senior Citizen")


class PhilhealthPatient(Patient):
    """Child class: PhilHealth Member gets a 15% discount."""

    def calculate_bill(self):
        return self.get_bill_amount() * 0.85
    
    def display_patient_type(self):
        print("Patient Type: PhilHealth Member")


def print_statement(patient):
    """Works for any Patient object; the correct version of each method runs."""
    print(f"Patient Name:  {patient.get_name()}")
    patient.display_patient_type()
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")
    print()


print("Hospital Billing System")
print("-----------------------")

patients = [
    Patient("June Marga", 15000),
    SeniorPatient("Calex Salac", 15000),
    PhilhealthPatient("Chardonnay Liv", 15000),
]

for p in patients:
    print_statement(p)
