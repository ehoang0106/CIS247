class Car:
   def __init__(self, make, model, year):
      self._make = make
      self._model = model
      self._year = year
      self._speed = 0

   def __str__(self):
      return f'Make: {_make} Model: {_model} Year: {_year}'