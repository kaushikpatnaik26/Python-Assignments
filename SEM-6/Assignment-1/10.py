class CommissionEmployee:
    def __init__(self, name, employee_id, sales, commission_rate):
        if sales < 0 or commission_rate < 0:
            raise ValueError("Sales and commission rate must be non-negative.")
        
        self.name = name
        self.employee_id = employee_id
        self.sales = sales
        self.commission_rate = commission_rate
    
    def earnings(self):
        return self.sales * self.commission_rate
    
    def __repr__(self):
        return f"CommissionEmployee(name={self.name}, employee_id={self.employee_id}, sales={self.sales}, commission_rate={self.commission_rate})"
    
    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self, value):
        if value < 0:
            raise ValueError("Sales cannot be negative.")
        self._sales = value
    
    @property
    def commission_rate(self):
        return self._commission_rate
    
    @commission_rate.setter
    def commission_rate(self, value):
        if value < 0:
            raise ValueError("Commission rate cannot be negative.")
        self._commission_rate = value
if __name__ == "__main__":
    try:
        employee = CommissionEmployee("John Doe", 101, 5000, 0.1)
        print(employee)
        print("Earnings:", employee.earnings())
        
        employee.sales = 7000
        print("Updated Earnings:", employee.earnings())
        
        employee.sales = -1000
    except ValueError as e:
        print("Error:", e)
