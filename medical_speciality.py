'''Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the 
medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT
} 

Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.'''


def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    lst = patient_medical_speciality_list[1::2]
    dic = {}
    for i in lst:
        dic[i] = lst.count(i)
    a = max(dic.values())
    
    for key,value in dic.items():
        if value == a:
            speciality = medical_speciality[key]
    return speciality
  
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
