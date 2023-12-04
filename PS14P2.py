class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code
      self.enrolled_credits = enrolled_credits

  def compute_tuition(self):
      if self.district_code == 'I':
          tuition_owed = self.enrolled_credits * 250.00
      else:
          tuition_owed = self.enrolled_credits * 500.00
      return tuition_owed

student1 = Student('John', 'Doe', 'I', 12)
student2 = Student('Jane', 'Smith', 'O', 15)

print(f"{student1.first_name} {student1.last_name}")
print(f"District Code: {student1.district_code}")
print(f"Enrolled Credits: {student1.enrolled_credits}")
print(f"Tuition Owed: ${student1.compute_tuition():,.2f}\n")

print(f"{student2.first_name} {student2.last_name}")
print(f"District Code: {student2.district_code}")
print(f"Enrolled Credits: {student2.enrolled_credits}")
print(f"Tuition Owed: ${student2.compute_tuition():,.2f}")

