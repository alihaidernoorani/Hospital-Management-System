class Hospital:
  # Initialize empty lists to store doctors and patients
  def __init__(self):
    self.doctors = []
    self.patients = []

  # Add a doctor to the hospital's doctor list
  def add_doctor(self, doctor):
    self.doctors.append(doctor)
    print(f"{doctor} has been successfully added as a doctor to the system.\n")
  
  # Remove a doctor from the list if they exist
  def remove_doctor(self, doctor):
    if doctor in self.doctors:
      self.doctors.remove(doctor)
      print(f"{doctor} has been successfully removed as a doctor from the system.\n")
    else:
      print(f"{doctor} was not found in the system.\n")

  # Add a patient to the hospital's patient list
  def add_patient(self, patient):
    self.patients.append(patient)
    print(f"{patient} has been successfully added as a patient to the system.\n")
  
  # Remove a patient from the list if they exist
  def remove_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"{patient} has been successfully removed as a patient from the system.\n")
        else:
            print(f"{patient} was not found in the system.\n")

  # Print all doctors currently in the system
  def display_doctors(self):
    if self.doctors:
        print("List of Doctors:")
        for doctor in self.doctors:
            print(f" - {doctor}")
        print()
    else:
        print("No doctors in the system.\n")

  # Print all patients currently in the system
  def display_patients(self):
    if self.patients:
        print("List of Patients:")
        for patient in self.patients:
            print(f" - {patient}")
        print()
    else:
        print("No patients in the system.\n")

class Doctor:
    def __init__(self, name, speciality):
        self.name = name
        self.speciality = speciality
    
    def __str__(self):
        return f"Dr. {self.name} ({self.speciality})"

class Patient:
    def __init__(self, name, age, ward, ailment):
        self.name = name
        self.age = age
        self.ward = ward
        self.ailment = ailment
    
    def __str__(self):
        return f"{self.name}, {self.age} (Ward: {self.ward}, Ailment: {self.ailment})"

# --- Example usage of the Hospital class ---
my_hospital = Hospital()

# Create and add doctors
dr_ali = Doctor("Ali", "Cardiology")
my_hospital.add_doctor(dr_ali)

# Create and add patients
muhammad_farooq = Patient("Muhammad Farooq", 45, "East Wing", "Heart Disease")
my_hospital.add_patient(muhammad_farooq)

# Display lists
my_hospital.display_doctors()            # Show all current doctors
my_hospital.display_patients()           # Show all current patients

# Remove a patient
my_hospital.remove_patient(muhammad_farooq)     # Remove a patient from the hospital
my_hospital.display_patients()           # Show updated patient list