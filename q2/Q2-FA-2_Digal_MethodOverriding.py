SENIOR_DISCOUNT = 0.20
PHILHEALTH_DISCOUNT = 0.15

class Patient:
    """A regular patient who pays the full amount."""

    def __init__(self, name, bill_amount):
        self.set_name(name)
        self.set_bill_amount(bill_amount)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        self.__name = name.strip()

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        if not isinstance(bill_amount, (int, float)):
            raise TypeError("Bill amount must be a number.")
        if bill_amount < 0:
            raise ValueError("Bill amount cannot be negative.")
        self.__bill_amount = float(bill_amount)

    def calculate_bill(self):
        """Return the full bill (no discount)."""
        return self.get_bill_amount()

class SeniorPatient(Patient):
    def calculate_bill(self):
        full_bill = super().calculate_bill()
        return full_bill - (full_bill * SENIOR_DISCOUNT)


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        full_bill = super().calculate_bill()
        return full_bill - (full_bill * PHILHEALTH_DISCOUNT)


def display_bill(patient):
    """Print the patient's name, original bill, and final computed bill."""
    print(f"Patient Name:  {patient.get_name()}")
    print(f"Original Bill: ₱{patient.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{patient.calculate_bill():,.2f}")

regular_patient = Patient("June Marga", 15000)
senior_patient = SeniorPatient("Calex Salac", 15000)
philhealth_patient = PhilHealthPatient("Chardonnay Liv", 15000)

patients = [regular_patient, senior_patient, philhealth_patient]

print("Hospital Billing System")
print("-" * 23)
for index, patient in enumerate(patients):
    if index > 0:
        print() 
    display_bill(patient)
