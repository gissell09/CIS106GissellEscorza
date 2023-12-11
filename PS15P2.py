class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = float(sticker_price)
      self.discount_price = self.calculate_discount_price()

  def calculate_discount_price(self):
      return 0.9 * self.sticker_price

  def display_info(self):
      print(f"{self.make} {self.model}")
      print(f"Sticker Price: ${self.sticker_price:.2f}")
      print(f"Discount Price: ${self.discount_price:.2f}")


class Sport(Car):
  def __init__(self, make, model, sticker_price, sport_wheels='N', sport_engine='N', sport_interior='N'):
      super().__init__(make, model, sticker_price)
      self.sport_wheels = sport_wheels
      self.sport_engine = sport_engine
      self.sport_interior = sport_interior
      self.pricewithoptions = self.calculate_price_with_options()

  def calculate_price_with_options(self):
      updated_price = self.discount_price
      if self.sport_wheels == 'Y':
          updated_price += 1000.00
      if self.sport_engine == 'Y':
          updated_price += 3000.00
      if self.sport_interior == 'Y':
          updated_price += 2000.00
      return updated_price

  def display_info(self):
      super().display_info()
      print(f"Sport Wheels: {self.sport_wheels}")
      print(f"Sport Engine: {self.sport_engine}")
      print(f"Sport Interior: {self.sport_interior}")
      print(f"Updated Price with Options: ${self.pricewithoptions:.2f}")


car1 = Sport('Toyota', 'Camry', 25000, sport_wheels='Y', sport_engine='N', sport_interior='Y')
car2 = Sport('Ford', 'Mustang', 40000, sport_wheels='N', sport_engine='Y', sport_interior='N')

car1.display_info()
print("\n")
car2.display_info()
