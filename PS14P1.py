class Employee:
  def __init__(self, first, last, pay, bonusrate):
      self.first = first
      self.last = last
      self.pay = float(pay)
      self.email = first + '.' + last + '@company.com' 
      self.bonusrate = float(bonusrate)  
      self.bonus = self.calculate_bonus() 

  def fullname(self):
    return ('{} {}'.format(self.first, self.last))
    
  def calculate_bonus(self):
    return self.bonusrate * self.pay

emp_1 = Employee('Corey', 'Schafer', '50000', '0.2')
emp_2 = Employee('Tess', 'Miller', '60000', '0.1')

print(emp_1)
print(emp_2)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.calculate_bonus())
print(emp_2.calculate_bonus())

