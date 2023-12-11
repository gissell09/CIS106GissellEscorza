class Employee:
  def __init__(self, first, last, pay, bonusrate):
      self.first = first
      self.last = last
      self.pay = float(pay)
      self.email = f"{first}.{last}@company.com"
      self.bonusrate = float(bonusrate)
      self.bonus = self.calculate_bonus()

  def fullname(self):
      return f"{self.first} {self.last}"

  def calculate_bonus(self):
      return self.bonusrate * self.pay


class Manager(Employee):
  def __init__(self, first, last, pay, bonusrate, salary):
      super().__init__(first, last, pay, bonusrate)
      self.salary = float(salary)

  def long_term_bonus(self):
      return 0.4 * self.salary



emp_1 = Employee('Corey', 'Schafer', '50000', '0.2')
emp_2 = Employee('Tess', 'Miller', '60000', '0.1')

manager_1 = Manager('Alice', 'Johnson', '80000', '0.15', '100000')
manager_2 = Manager('Bob', 'Williams', '70000', '0.12', '90000')

print("Manager 1 Long Term Bonus:", manager_1.long_term_bonus())
print("Manager 2 Long Term Bonus:", manager_2.long_term_bonus())

