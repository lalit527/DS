class ShippingConatiner:

  HEIGHT_FT = 8.5
  WIDTH_FT = 8.0
  next_serial = 1337

  @staticmethod
  def _make_bic_coe(owner_code, serial):
    return 'Shipping {x} Container {y}'.format(x=owner_code, y=serial)

  @classmethod
  def _get_next_serial():
    result = ShippingConatiner.next_serial
    ShippingConatiner.next_serial += 1
    return result

  @classmethod
  def _get_current_serial(cls):
    result = cls.next_serial
    cls.next_serial += 1
    return result

  @classmethod
  def create_empty(cls, owner_code, *args, **kwargs):
    return cls(owner_code, contents=None, *args, **kwargs)
  
  @classmethod
  def create_with_items(cls, owner_code, items, *args, **kwargs):
    return cls(owner_code, contents=list(items), *args, **kwargs)

  def __init__(self, owner_code, contents):
    self.owner_code = owner_code
    self.contents = contents
    self.bic = self._make_bic_coe(owner_code, contents)
    self.serial = ShippingConatiner.next_serial
    ShippingConatiner.next_serial += 1

  @property
  def volume_ft3(self):
    return ShippingConatiner.HEIGHT_FT * ShippingConatiner.WIDTH_FT * self.length_ft

class RegisteredShippingContainer(ShippingConatiner):

  MAX_CELCIUS = 4.0

  @staticmethod
  def _make_bic_coe(owner_code, serial):
    return 'Registered {x} Container {y}'.format(x=owner_code, y=serial)

  @staticmethod
  def _c_to_f(celcius):
    return celcius * 9/5 + 32

  @staticmethod
  def _f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9


  def __init__(self, owner_code, contents, celcius):
    super().__init__(owner_code, contents)
    if celcius > RegisteredShippingContainer.MAX_CELCIUS:
      raise ValueError("Temperature too hot!")
    self.celsius = celcius

  @property
  def celcius(self):
    return self._celsius
  
  @celcius.setter
  def celcius(self, value):
    if value > RegisteredShippingContainer.MAX_CELCIUS:
      raise ValueError("Temperature too hot!")
    self._celcius = value
  
  @property
  def fahrenheit(self):
    return self._fahrenheit
  
  @fahrenheit.setter
  def fahrenheit(self, value):
    self._celcius = RegisteredShippingContainer.celcius.setter

  @property
  def fahrenheit(self):
    return super().volume_ft3 - RegisteredShippingContainer.FRIDGE_VOLUME_FT3

class HeatedRefrigeratedShippingContainer(RegisteredShippingContainer):
  MIN_CELCIUS = -20.0

  @RegisteredShippingContainer.celcius.setter
  def celcius(self, value):
    if value < HeatedRefrigeratedShippingContainer.MIN_CELCIUS:
      raise ValueError("Temperature too cold!")
    RefrigeratedShippingContainer.celsius.fset(self, value)

  

