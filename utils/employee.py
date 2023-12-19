class Employee:
    def __init__(self, first_name, last_name, base_salary, bonus_percentage, employment_years, retirement_contribution):
        assert 45000 <= base_salary <= 125000, "Base salary should be between 45000 and 125000"
        self.first_name = first_name
        self.last_name = last_name
        self.base_salary = base_salary
        assert 10 <= bonus_percentage <= 20, "Bonus percentage should be between 10% to 20%" 
        self.bonus_percentage = bonus_percentage
        self.employment_years = employment_years
        self.retirement_contribution = retirement_contribution

    def calculate_bonus(self):
        bonus_amount = self.base_salary * (self.bonus_percentage / 100)
        return bonus_amount
    
    def calculate_vacation_hours(self):
        if self.employment_years == 1:
            total_vacation_hours = (self.employment_years * 52 ) * 1.1
            return total_vacation_hours
        elif self.employment_years == 2:
            total_vacation_hours = (self.employment_years * 52) * 1.2
            return total_vacation_hours
        elif self.employment_years ==3:
            total_vacation_hours = (self.employment_years * 52) * 1.3
            return total_vacation_hours
        elif self.employment_years == 4:
            total_vacation_hours = (self.employment_years * 52) * 1.4
            return total_vacation_hours
        elif self.employment_years == 5:
            total_vacation_hours = (self.employment_years * 52) * 1.5
            return total_vacation_hours
        else:
            raise ValueError("Employment years must be between 1-5")
        
    def calculate_retirement_contribution(self):
        retirement_contribution_per_year = self.base_salary * (self.retirement_contribution / 100)
        total_retirement_contribution = (retirement_contribution_per_year * 0.5 ) / 2 + retirement_contribution_per_year
        return total_retirement_contribution

def main():
    first_name = input("Enter the employee first name")
    last_name = input("Enter the employee last name ")
    base_salary = int(input("Enter the employee's base salary"))
    bonus_percentage = float(input("Enter the employee's bonus in percent"))
    employment_years = int(input("How many years has the employee been employed? Enter a number from 1 to 5."))
    retirement_contribution = float(input("Enter the employee's retirement contribution in percent"))

    employee1 = Employee(first_name, last_name, base_salary, bonus_percentage, employment_years, retirement_contribution)

    bonus = employee1.calculate_bonus()
    vacation_hours = employee1.calculate_vacation_hours()
    retirement_fund = employee1.calculate_retirement_contribution()

    print(f"------------------Report {employee1.first_name}{employee1.last_name}---------------------------")
    print(f"bonus : {bonus}")
    print(f"vacation hours : {vacation_hours}")
    print(f"retirement_fund : {retirement_fund}")
    print(f"----------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
    main()