
class Facility:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
          return f'{self.name}'
class Laboratory:
    def __init__(self,Lab_name, cost):
        self.Lab_name = Lab_name
        self.cost = cost
    def __repr__(self):
          return f'{self.Lab_name} {self.cost}'
class Patient:
    def __init__(self,pid,name, disease, gender, age ):
         self.pid = pid
         self.name = name
         self.disease = disease
         self.gender = gender
         self.age =age
    def __repr__(self):
          return f'{self.pid} {self.name} {self.disease} {self.gender} {self.age}'


class Doctor:
    def __init__(self,id, name, specialization, working_time, qualification, room_number):
         self.id = id
         self.name = name
         self.specialization = specialization
         self.working_time = working_time
         self.qualification = qualification
         self.room_number = room_number


    def __repr__(self):
          return f'{self.id} {self.name} {self.specialization} {self.working_time} {self.qualification} {self.room_number}'
#Hospital Functions

def Hospital_Menu_options():
    Hospital_Menu_Input = input('Welcome to Alberta Hospital (AH) Managment system\n1 -    Doctors\n2 - 	Facilities\n3 - 	Laboratories\n4 - 	Patients\n')
    if int(Hospital_Menu_Input) > 4 or int(Hospital_Menu_Input) < 1 or Hospital_Menu_Input.isnumeric() == False:
        Hospital_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
    return Hospital_Menu_Input

# Doctor Functions
new_doctor = []
def enterDrInfo():
    new_doctor.append (input("Enter the doctor’s ID:"))
    new_doctor.append (input("Enter the doctor’s name:"))
    new_doctor.append (input("Enter the doctor’s speciality:"))
    new_doctor.append (input("Enter the doctor’s timing (e.g., 7am-10pm):"))
    new_doctor.append (input("Enter the doctor’s qualification:"))
    new_doctor.append (input("Enter the doctor’s room number:"))
    return new_doctor

def readDoctorsFile():
    Doctors_file = open('doctors.txt','r')
    for Doctors_file_line in Doctors_file:
            DoctorList.append(Doctor(*Doctors_file_line.split('_')))
    return DoctorList

def writeListOfDoctorsToFile():
    DoctorList_File_Data = []
    Doctors_file = open('doctors.txt','r')
    DoctorList_File_Data=Doctors_file.readlines()

    for Line_Number, Doctor_Details in enumerate(DoctorList_File_Data):
        if str(Input_Doctor_ID_Edit) in Doctor_Details :
            DoctorList_File_Data[Line_Number] = updated_current_doctor_str + '\n'
    return DoctorList_File_Data

def displayDoctorInfo():
    DoctorList = []
    Doctors_file = open('doctors.txt','r')
    for Doctors_file_line in Doctors_file:
        DoctorList.append(Doctor(*Doctors_file_line.split('_')))
    return DoctorList

def displayDoctorsList():
    print("Id        Name       Speciality     Timing    Qualification   Room Number")
    for i in range(1, len(DoctorList)):
        print(f'{DoctorList[i].id:<10} {DoctorList[i].name:<12} {DoctorList[i].specialization:<12} {DoctorList[i].working_time:<10} {DoctorList[i].qualification:<10}  {DoctorList[i].room_number:<10}'.format(DoctorList[i]))



def addDrToFile():
    Doctors_file = open('doctors.txt','a')
    Doctors_file.write('\n' + new_doctor_str)
    Doctors_file.close()

current_doctor = []
def editDoctorInfo():
    current_doctor.append (input("Enter the doctor’s ID:"))
    current_doctor.append (input("Enter the doctor’s name:"))
    current_doctor.append (input("Enter the doctor’s speciality:"))
    current_doctor.append (input("Enter the doctor’s timing (e.g., 7am-10pm):"))
    current_doctor.append (input("Enter the doctor’s qualification:"))
    current_doctor.append (input("Enter the doctor’s room number:"))
    return current_doctor

def searchDoctorById():
    Input_Doctor_ID = input('Enter the Doctor ID:')
    for i in range(1, len(DoctorList)):
        if str(Input_Doctor_ID) == str(DoctorList[i].id):
                print(DoctorList[i])
                break
    else:
            print("Can't find the doctor with the same ID on the system")

def searchDoctorByName():
    Input_Doctor_Name = input('Enter the Doctor Name:')
    for i in range(0, len(DoctorList)):
        if Input_Doctor_Name.strip()== DoctorList[i].name.strip():
            print (DoctorList [i])
            break
    else:
            print("Can't find the doctor with the same name on the system")

new_line = []
def formatDrInfo():
    Underline_Char = "_"
    for i in range(0, len(new_line)):
      new_doctor_str = Underline_Char.join(new_line)
    return new_doctor_str

def Doctors_Menu_options():
    print('Doctors Menu:')
    Doctor_Menu_Input1 = input('1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')
    if int(Doctor_Menu_Input1) > 6 or int(Doctor_Menu_Input1) < 1 or Doctor_Menu_Input1.isnumeric() == False:
        Doctor_Menu_Input1 = input('Your selection is invalid, please re-enter:\n ')
    return Doctor_Menu_Input1


# Facilites Functions

def addFacility():
    new_facility  = input("Enter Facility name: ")
    return new_facility

def writeListOffacilitiesToFile():
    Facilities_file = open('facilities.txt','a')
    Facilities_file.write('\n' + str(new_facility))
    Facilities_file.close()

def facilites_Menu_options():
    print('Facilities Menu:')
    facilites_Menu_Input1 = input('1 - Display Facilities list\n2 - Add Facilities\n3 - Back to the Main Menu\n')
    if int(facilites_Menu_Input1) > 3 or int(facilites_Menu_Input1) < 1 or facilites_Menu_Input1.isnumeric() == False:
        facilites_Menu_Input1 = input('Your selection is invalid, please re-enter:\n ')
    return facilites_Menu_Input1

# Laboratory Functions
new_Laboratory = []
def enterLaboratoryInfo():
    new_Laboratory.append (input("Enter the Lab’s Name:"))
    new_Laboratory.append (input("Enter the Lab’s Cost:"))
    return new_Laboratory

def readLaboratoriesFile():
    Labs_file = open('laboratories.txt','r')
    for Labs_file_line in Labs_file:
            LaboratoryList.append(Laboratory(*Labs_file_line.split('_')))
    return LaboratoryList

def writeListOfLabsToFile():
    Laboratorys_file = open('laboratories.txt','r')
    LaboratoryList_File.write(str(new_Laboratory))
    LaboratoryList_File = Laboratorys_file.readlines()




def displayLaboratorysList():
    print("Lab_Name   Cost       ")
    for i in range(1, len(LaboratoryList)):
        print(f'{LaboratoryList[i].Lab_name:<20} {LaboratoryList[i].cost:<20}'.format(LaboratoryList[i]))


new_Laboratory = []
def addLabToFile():
    Lab_file = open('laboratories.txt','a')
    Lab_file.write('\n' + new_Laboratory)
    Lab_file.close()

def Laboratorys_Menu_options():
    print('Laboratorys Menu:')
    Laboratory_Menu_Input1 = input('1 - Display Laboratorys list\n2  - Add Laboratory\n3 - Back to the Main Menu\n')
    if int(Laboratory_Menu_Input1) > 3 or int(Laboratory_Menu_Input1) < 1 or Laboratory_Menu_Input1.isnumeric() == False:
        Laboratory_Menu_Input1 = int(input('Your selection is invalid, please re-enter:\n '))
    return Laboratory_Menu_Input1


# Patient Functions
new_Patient = []
def enterPatientInfo():
    new_Patient.append (input("Enter the Patient’s ID:"))
    new_Patient.append (input("Enter the Patient’s name:"))
    new_Patient.append (input("Enter the Patient’s Disease:"))
    new_Patient.append (input("Enter the Patient’s Gender:"))
    new_Patient.append (input("Enter the Patient’s Age:"))
    return new_Patient

PatientList = []
def readPatientsFile():
    Patients_file = open('patients.txt','r')
    for Patients_file_line in Patients_file:
            PatientList.append(Patient(*Patients_file_line.split('_')))
    return PatientList

def writeListOfPatientsToFile():
    PatientList_File_Data = []
    Patients_file = open('patients.txt','r')
    PatientList_File_Data=Patients_file.readlines()

    for Line_Number, Patient_Details in enumerate(PatientList_File_Data):
        if str(Input_Patient_PID_Edit) in Patient_Details :
            PatientList_File_Data[Line_Number] = updated_current_Patient_str + '\n'
    return PatientList_File_Data

def displayPatientInfo():
    PatientList = []
    Patients_file = open('patients.txt','r')
    for Patients_file_line in Patients_file:
        PatientList.append(Patient(*Patients_file_line.split('_')))
    return PatientList

def displayPatientsList():
    print("Id        Name       Disease     Gender    Age   ")
    for i in range(1, len(PatientList)):
        print(f'{PatientList[i].pid:<10} {PatientList[i].name:<12} {PatientList[i].disease:<12} {PatientList[i].gender:<10} {PatientList[i].age:<10} '.format(PatientList[i]))



def addPatientToFile():
    Patients_file = open('patients.txt','a')
    Patients_file.write('\n' + new_Patient_str)
    Patients_file.close()

current_Patient = []
def editPatientInfo():
    current_Patient.append (input("Enter the Patient’s ID:"))
    current_Patient.append (input("Enter the Patient’s name:"))
    current_Patient.append (input("Enter the Patient’s Disease:"))
    current_Patient.append (input("Enter the Patient’s Gender:"))
    current_Patient.append (input("Enter the Patient’s Age:"))
    return current_Patient

def searchPatientById():
    Input_Patient_ID = input('Enter the Patient ID:')
    for i in range(1, len(PatientList)):
        if str(Input_Patient_ID) == str(PatientList[i].pid):
                print(PatientList[i])
                break
    else:
            print("Can't find the Patient with the same ID on the system")




def formatPatientInfo():
    Underline_Char = "_"
    for i in range(0, len(new_Patient)):
      new_Patient_str = Underline_Char.join(new_Patient)
    return new_Patient_str

def Patients_Menu_options():
    print('Patients Menu:')
    Patient_Menu_Input1 = input('1 - Display Patients list\n2 - Search for Patient by ID\n3 - Add Patient\n4 - Edit Patient info\n5 - Back to the Main Menu\n')
    if int(Patient_Menu_Input1) > 6 or int(Patient_Menu_Input1) < 1 or Patient_Menu_Input1.isnumeric() == False:
        Patient_Menu_Input1 = input('Your selection is invalid, please re-enter:\n ')
    return Patient_Menu_Input1



#Start

Hospital_Input_value = Hospital_Menu_options()
while int(Hospital_Input_value) != 0:
 if int(Hospital_Input_value) > 4 or int(Hospital_Input_value) < 1:
    Hospital_Input_value = input('Your selection is invalid, please re-enter:\n ')
        
#print ('Doctors Menu:')
#Doctor_Menu_Input = input('1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')
 if int(Hospital_Input_value) == 1:
    Doctor_Menu_Input = Doctors_Menu_options()
    while int(Doctor_Menu_Input) != 6:
        if int(Doctor_Menu_Input) > 6 or int(Doctor_Menu_Input) < 1 or Doctor_Menu_Input.isnumeric() == False:
            Doctor_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Doctors  #####
        if int(Doctor_Menu_Input) == 1:
            DoctorList = []
            DoctorList = readDoctorsFile()
 
            displayDoctorsList()
            
            print('Back to the prevoius Menu')
            Doctor_Menu_Input = Doctors_Menu_options()

    ### Search for a Doctor  by ID #####

        elif int(Doctor_Menu_Input) == 2:
                DoctorList = []
                DoctorList = displayDoctorInfo()
    
                searchDoctorById()

                print('Back to the previous Menu')
                Doctor_Menu_Input = Doctors_Menu_options()

    ### Search for a Doctor  by Name #####
        elif int(Doctor_Menu_Input) == 3:
                DoctorList = []
                DoctorList = displayDoctorInfo()

                searchDoctorByName()

                print('Back to the previous Menu')
                Doctor_Menu_Input = Doctors_Menu_options()

    #### Entering new Doctor   #####
        elif int(Doctor_Menu_Input) == 4:
                new_line = enterDrInfo()
                print (new_line)
                Underline_Char = "_"
                formatDrInfo()
                new_doctor_str = formatDrInfo()
                print(new_doctor_str)

                addDrToFile()


                print('Back to the previous Menu')
                Doctor_Menu_Input = Doctors_Menu_options()
                


    ####   Edit current Doctor  ####
        elif int(Doctor_Menu_Input) == 5:
                DoctorList = []
                Doctors_file = open('doctors.txt','r')
                for Doctors_file_line in Doctors_file:
                    DoctorList.append(Doctor(*Doctors_file_line.split('_')))


                Input_Doctor_ID_Edit = input('Please enter the id of the doctor that you want to edit their information: ')
                Input_Doctor_ID_Edit = int(Input_Doctor_ID_Edit)
                for i in range(1, len(DoctorList)):
                    if int(Input_Doctor_ID_Edit) == int(DoctorList[i].id):
                        print (DoctorList [i])
                        break
                else:
                 print("Can't find the doctor with the same ID on the system")

                editDoctorInfo()
                print (current_doctor)
                Underline_Char = "_"
                for i in range(0, len(current_doctor)):
                    updated_current_doctor_str = Underline_Char.join(current_doctor)

                print(updated_current_doctor_str)

                DoctorList_File_Data = writeListOfDoctorsToFile()

                print(DoctorList_File_Data)

                Doctors_File_Update = open('doctors.txt','w')
                for i in range(0, len(DoctorList_File_Data)):
                    Doctors_File_Update.write(DoctorList_File_Data[i])
                print('Back to the previous Menu')
                Doctors_File_Update.close()
                Doctor_Menu_Input = Doctors_Menu_options()
                
    
    
    Hospital_Input_value = int(Hospital_Menu_options())



 if int(Hospital_Input_value) == 2:
    Facilities_Menu_Input = facilites_Menu_options()
    while int(Facilities_Menu_Input) != 3:
        if int(Facilities_Menu_Input) > 3 or int(Facilities_Menu_Input) < 1 or Facilities_Menu_Input.isnumeric() == False:
            Facilities_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Facilities  #####
        if int(Facilities_Menu_Input) == 1:
            FacilitiesList = []
            Facilities_file = open('facilities.txt','r')
            FacilitiesList = Facilities_file.read()

            for i in range(1,5, len(FacilitiesList)):
                print(FacilitiesList)
                Facilities_file.close
                    

            print('Back to the prevoius Menu')
            Facilities_Menu_Input = facilites_Menu_options()

    #### Entering new Facility   #####
        elif int(Facilities_Menu_Input) == 2:
                new_facility = addFacility()
                print (new_facility)

                writeListOffacilitiesToFile()

                print('Back to the previous Menu')
                
                Facilities_Menu_Input = facilites_Menu_options()     
    Hospital_Input_value = int(Hospital_Menu_options())

#Laboratory
 if int(Hospital_Input_value) == 3:
    Laboratory_Menu_Input = Laboratorys_Menu_options()
    while int(Laboratory_Menu_Input) != 3:
        if int(Laboratory_Menu_Input) > 3 or int(Laboratory_Menu_Input) < 1 or Laboratory_Menu_Input.isnumeric() == False:
            Laboratory_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Laboratorys  #####
        if int(Laboratory_Menu_Input) == 1:
            LaboratoryList = []
            LaboratoryList = readLaboratoriesFile()
 
            displayLaboratorysList()
            
            print('Back to the prevoius Menu')
            Laboratory_Menu_Input = Laboratorys_Menu_options()



    #### Entering new Laboratory   #####
        elif int(Laboratory_Menu_Input) == 2:
                new_line = enterLaboratoryInfo()
                print (new_line)
                Underline_Char = "_"
                formatDrInfo()
                new_Laboratory = formatDrInfo()
                print(new_Laboratory)

                addLabToFile()


                print('Back to the previous Menu')
                Laboratory_Menu_Input = Laboratorys_Menu_options()
                

                
    Hospital_Input_value = int(Hospital_Menu_options())


 elif Hospital_Input_value == '2':
    Facilities_Menu_Input = facilites_Menu_options()
    while Facilities_Menu_Input != '3':
        if Facilities_Menu_Input > '3' or Facilities_Menu_Input < '1' or Facilities_Menu_Input.isnumeric() == False:
            Facilities_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Laboratorys  #####
        if int(Facilities_Menu_Input) == 1:
            FacilitiesList = []
            Facilities_file = open('facilities.txt','r')
            FacilitiesList = Facilities_file.read()

            for i in range(1,5, len(FacilitiesList)):
                print(FacilitiesList)
                Facilities_file.close
                    

            print('Back to the prevoius Menu')
            Facilities_Menu_Input = facilites_Menu_options()

    #### Entering new Facility   #####
        elif int(Facilities_Menu_Input) == 2:
                new_facility = addFacility()
                print (new_facility)

                writeListOffacilitiesToFile()

                print('Back to the previous Menu')
                
                Facilities_Menu_Input = facilites_Menu_options()     
    Hospital_Input_value = int(Hospital_Menu_options())
#Patients
 if int(Hospital_Input_value) == 4:
    Patient_Menu_Input = Patients_Menu_options()
    while int(Patient_Menu_Input) != 5:
        if int(Patient_Menu_Input) > 5 or int(Patient_Menu_Input) < 1 or Patient_Menu_Input.isnumeric() == False:
            Patient_Menu_Input = input('Your selection is invalid, please re-enter:\n ')
        
        
    ##### List All Patients  #####
        if int(Patient_Menu_Input) == 1:
            PatientList = []
            PatientList = readPatientsFile()
 
            displayPatientsList()
            
            print('Back to the prevoius Menu')
            Patient_Menu_Input = Patients_Menu_options()

    ### Search for a Patient  by ID #####

        elif int(Patient_Menu_Input) == 2:
                PatientList = []
                PatientList = displayPatientInfo()
    
                searchPatientById()

                print('Back to the previous Menu')
                Patient_Menu_Input = Patients_Menu_options()

    #### Entering new Patient   #####
        elif int(Patient_Menu_Input) == 3:
                enterPatientInfo()
                print (new_Patient)
                Underline_Char = "_"
                formatPatientInfo()
                new_Patient_str = formatPatientInfo()
                print(new_Patient_str)

                addPatientToFile()


                print('Back to the previous Menu')
                Patient_Menu_Input = Patients_Menu_options()
                


    ####   Edit current Patient  ####
        elif int(Patient_Menu_Input) == 4:
                PatientList = []
                Patients_file = open('Patients.txt','r')
                for Patients_file_line in Patients_file:
                    PatientList.append(Patient(*Patients_file_line.split('_')))


                Input_Patient_PID_Edit = input('Please enter the id of the Patient that you want to edit their information: ')
                Input_Patient_PID_Edit = int(Input_Patient_PID_Edit)
                for i in range(1, len(PatientList)):
                    if int(Input_Patient_PID_Edit) == int(PatientList[i].pid):
                        print (PatientList [i])
                        break
                else:
                 print("Can't find the Patient with the same ID on the system")

                editPatientInfo()
                print (current_Patient)
                Underline_Char = "_"
                for i in range(0, len(current_Patient)):
                    updated_current_Patient_str = Underline_Char.join(current_Patient)

                print(updated_current_Patient_str)

                PatientList_File_Data = writeListOfPatientsToFile()

                print(PatientList_File_Data)

                Patients_File_Update = open('Patients.txt','w')
                for i in range(0, len(PatientList_File_Data)):
                    Patients_File_Update.write(PatientList_File_Data[i])
                print('Back to the previous Menu')
                Patients_File_Update.close()
                Patient_Menu_Input = Patients_Menu_options()
                
    Hospital_Input_value = int(Hospital_Menu_options())
