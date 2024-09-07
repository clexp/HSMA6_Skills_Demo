from datetime import datetime
class Clinic:
    def __init__(self, name:str, staff: list):
        self.name = name
        self.staff = staff
        self.status_open = False


    def display_staff(self):
        print(f"{self.name} is run by: ")
        for staffer in self.staff:
            print(f"{staffer, }")

class Bariatric_clinic(Clinic):
    def __init__(self, name: str, staff: list, lead:str):
        super().__init__(name, staff)
        self.lead = lead
        if self.lead not in self.staff:
            self.staff.append(self.lead)

class Genito_urinary_clinic(Clinic):
    def __init__(self, name: str, staff: list, lead:str):
        super().__init__(name, staff)
        self.ledger = []

    def book_aptmt(self, name: str, _date_time: datetime):
        self.ledger.append((name, _date_time))
        self.ledger.sort(key=lambda apt: apt[1])
    
    def display_ledger(self):
        print("Namea \t\t\t\t Date / Time")
        for apt in self.ledger:
            print(f"{apt[0]}\t\t\t{apt[1]}")

devon_weight_loss = Bariatric_clinic("Devon_Darlings", 
                                     ['bill', 
                                      'amelie', 
                                      'mohamed'],
                                      'connelly')

cornwall_couch_apples = Bariatric_clinic(
    "Cornweight Watchers",
    ['figgis',
     'jason'
     'rodrigo'],
     'beth'
)

cornwall_purity = Genito_urinary_clinic(
    "discharge this",
    ['jeffy',
     'surly',
     'bozzy'],
     'aisha'
)
cornwall_purity.book_aptmt('Jessica Fletcher', datetime(2024, 6, 4, 11, 0, 0))

devon_weight_loss.display_staff()
cornwall_couch_apples.display_staff()
cornwall_purity.display_ledger()