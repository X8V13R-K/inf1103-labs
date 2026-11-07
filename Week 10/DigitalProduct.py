from abc import ABC, abstractmethod
from Product import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, type, quantity, download_size): 
        super().__init__(product_id, name, price, type, quantity)
        self.download_size = download_size

    def display_information(self):
        super().display_information()
        print(f"Download size: {self.download_size}MB")

    def get_fulfillment_info(self):
        print(f"{self.name} is a Digital Product which will be delivered digitally.")