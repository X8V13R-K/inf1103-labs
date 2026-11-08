from abc import ABC, abstractmethod
from Product import Product
from CanBeShipped import CanBeShipped
from Supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, type: str, quantity: int, supplier: Supplier, weight: float) -> None:
        super().__init__(product_id, name, price, type, quantity, supplier)
        self.__weight: float = weight

    @property
    def weight(self) -> float:
        return self.__weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self.weight}")

    def get_fulfillment_info(self) -> str:
        return (f"{self.name} is a Physical Product which requires physical shipping. "f"Shipping cost: ${self.calculate_shipping_cost():.2f}")

    def calculate_shipping_cost(self) -> float:
        return self.weight * 5

    def to_dict(self) -> dict:
        product_dict = super().to_dict()
        product_dict["weight"] = self.__weight
        return product_dict