from abc import ABC, abstractmethod
from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, type, quantity, weight): 
        super().__init__(product_id, name, price, type, quantity)
        self.weight = weight

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.weight}")

    def get_fulfillment_info(self):
        print(f"{self.name} is a Physical Product which requires physical shipping.")
        self.calculate_shipping_cost()

    def calculate_shipping_cost(self):
        print(f"Shipping cost for {self.name}: ${self.weight * 5:.2f}")