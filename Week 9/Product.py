from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, type, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.type = type
        self.quantity = quantity
    
    def display_information(self): 
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Type: {self.type}")
        print(f"Quantity: {self.quantity}")

    @abstractmethod
    def get_fulfillment_info(self):
        pass