from abc import ABC, abstractmethod
from Product import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, type: str, quantity: int, supplier: Supplier, download_size: int) -> None:
        super().__init__(product_id, name, price, type, quantity, supplier)
        self.__download_size: int = download_size

    @property
    def download_size(self) -> int:
        return self.__download_size

    def display_information(self) -> None:
        super().display_information()
        print(f"Download size: {self.download_size}MB")

    def get_fulfillment_info(self) -> str:
        return f"{self.name} is a Digital Product which will be delivered digitally."

    def to_dict(self) -> dict:
        product_dict = super().to_dict()
        product_dict["download_size"] = self.__download_size
        return product_dict
