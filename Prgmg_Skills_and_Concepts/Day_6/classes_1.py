from random import expovariate as exp, uniform as uni

class Patient:
    def __init__(self, name: str, patient_id: int, age: int):
        self.name = name
        self.id = patient_id
        self.age = age
        self.cured = False
        
    
    def attended_ed(self, mean_time : float):
        attendance_duration = exp(1 / mean_time)
        print(f"{self.name} (id: {self.id}),            attended the ED and spent {attendance_duration}            minutes there.")
        
    def receive_treatment(self, prob_cure: float):
        treatment_effectiveness = uni(0,1)
        disease_resistance = 1/ prob_cure
        my_string = ""
        if treatment_effectiveness >= disease_resistance:
            self.cured = True
        else:
            self.cured = False
            my_string = " not"
        
        print(f"{self.name} was{my_string} cured.")

patient1 = Patient("Barney",1,35)
patient1.attended_ed(20.456)
patient1.receive_treatment(0.2322321)
