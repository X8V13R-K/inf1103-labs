from Product import Product
from OrderLine import OrderLine
from DiscountStrategy import DiscountStrategy
from NoDiscount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount 
        if discount is None : 
            discount = NoDiscount()

    @property
    def order_id(self) -> str:
        return self.__order_id

    @property
    def order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.__order_lines)
        return self.__discount.apply(total)
    
    def remove_order_line(self, product_id: str) -> None:
        for line in self.__order_lines:
            if line.product.product_id == product_id:
                self.__order_lines.remove(line)
                print(f"Removed {line.product.name} from order {self.__order_id}.")
                return
        print("Order line not found.")

    def display_order(self) -> None:
        print(f"Order {self.__order_id}")
        for line in self.__order_lines:
            line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")