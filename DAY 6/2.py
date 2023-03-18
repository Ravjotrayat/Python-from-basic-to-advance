class Company:
    def __init__(self, company_name, hike_rules):
        self.company_name = company_name
        self.hike_rules = hike_rules
        
    def get_hike_percentage(self, hike_category):
        for category, percentage in self.hike_rules.items():
            if category == hike_category:
                return percentage
        return None

class Employee:
    def __init__(self, name, employee_id, performance_list):
        self.name = name
        self.employee_id = employee_id
        self.performance_list = performance_list
        
    def calculate_salary(self, basic_pay, hike_percentage, incentive):
        hike_amount = basic_pay * hike_percentage
        incentive_amount = basic_pay * incentive
        total_salary = basic_pay + hike_amount + incentive_amount
        return total_salary

class PermanentEmployee(Employee):
    def identify_performance_hike(self):
        if len(self.performance_list) < 3:
            return None
        last_three_years_performance = self.performance_list[-3:]
        if last_three_years_performance == [3, 3, 3]:
            return 0.2
        elif last_three_years_performance == [2, 2, 2] or last_three_years_performance == [3, 3, 2]:
            return 0.1
        elif last_three_years_performance == [1, 1, 1] or last_three_years_performance == [2, 2, 1]:
            return 0.05
        else:
            return None
    
    def identify_job_level_hike(self, job_level):
        hike_category = f"Level{job_level}_hike"
        hike_percentage = company.get_hike_percentage(hike_category)
        return hike_percentage
    
    def identify_incentive(self):
        company_incentive = company.get_hike_percentage("Company_incentive")
        employee_incentive = company.get_hike_percentage("Employee_incentive")
        permanent_employee_incentive = company.get_hike_percentage("Permanent_employee_incentive")
        total_incentive = company_incentive + employee_incentive + permanent_employee_incentive
        return total_incentive
    
    def calculate_salary(self, basic_pay, job_level):
        performance_hike_percentage = self.identify_performance_hike()
        job_level_hike_percentage = self.identify_job_level_hike(job_level)
        total_hike_percentage = 0
        if performance_hike_percentage is not None:
            total_hike_percentage += performance_hike_percentage
        if job_level_hike_percentage is not None:
            total_hike_percentage += job_level_hike_percentage
        incentive = self.identify_incentive()
        total_salary = super().calculate_salary(basic_pay, total_hike_percentage, incentive)
        return total_salary

# Example usage
company_hike_rules = {
    "Level1_hike": 0.05,
    "Level2_hike": 0.1,
    "Level3_hike": 0.15,
    "Company_incentive": 0.02,
    "Employee_incentive": 0.01,
    "Permanent_employee_incentive": 0.03,
}
company = Company("ABC Company", company_hike_rules)

employee_performance_list = [3, 2, 3, 3, 1]
employee = Employee("John Doe", "E001", employee_performance_list)

permanent_employee_performance_list = [3, 2, 3, 3, 1]
permanent_employee = PermanentEmployee("Jane Smith", "PE001", permanent_employee_performance_list)
job_level = 2
# Example usage (continued)
basic_pay = 50000
total_salary = permanent_employee.calculate_salary(basic_pay, job_level)

print(f"Employee Name: {permanent_employee.name}")
print(f"Employee ID: {permanent_employee.employee_id}")
print(f"Basic Pay: {basic_pay}")
print(f"Total Salary: {total_salary}")
