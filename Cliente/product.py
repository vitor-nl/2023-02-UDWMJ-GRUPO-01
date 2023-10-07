from category import Category

class Product:
  def __init__(self, name, description, date_fabrication, is_active):
    self.name = name
    self.description = description
    self.date_fabrication = date_fabrication
    self.is_active = is_active