from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, type: str, quantity: int, supplier: Supplier) -> None:
        self.__product_id: str = product_id
        self.__name: str  = name
        self.__price: float = price
        self.__type: str = type
        self.__quantity: int = quantity
        self.__supplier: Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:   
        return self.__price

    @property
    def type(self) -> str:
        return self.__type

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    def display_information(self): 
        print(f"ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Type: {self.type}")
        print(f"Quantity: {self.quantity}")
        print(f"Supplier: {self.supplier.name}")

    @abstractmethod
    def get_fulfillment_info(self):
        pass