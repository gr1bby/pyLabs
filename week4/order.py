from dataclasses import dataclass


@dataclass
class Dish:
    count: int
    name: str
    price: float
    weight: float


class Order:
    def __init__(self, *dishes: Dish):
        self.__order = list()
        self.__count = 0
        self.__price = 0
        self.__weight = 0

        for dish in dishes:
            self.__order.append(dish.name)
            self.__count += dish.count
            self.__price += dish.price
            self.__weight += dish.weight

        self.__left_to_pay = self.__price


    def __str__(self) -> str:
        return ', '.join(self.__order)


    @property
    def count(self) -> int:
        return self.__count

    
    @property
    def price(self) -> float:
        return self.__price


    @property
    def weight(self) -> float:
        return self.__weight


    @property
    def left_to_pay(self) -> float:
        return self.__left_to_pay


    # Add a new dish to the order
    def add_dish(self, *dishes: Dish):
        for dish in dishes:
            self.__order.append(dish.name)
            self.__count += dish.count
            self.__price += dish.price
            self.__weight += dish.weight
            self.__left_to_pay += dish.price


    def pay(self, amount: float):
        if amount < self.__left_to_pay:
            self.__left_to_pay -= amount
        else:
            self.__left_to_pay = 0


if __name__ == '__main__':
    chicken = Dish(
        count=2,
        name='Chicken',
        price=89.99,
        weight=300
    )
    pasta = Dish(
        count=1,
        name='Pasta',
        price=45.59,
        weight=245.5
    )
    tomatoes = Dish(
        count=3,
        name='Tomatoes',
        price=20,
        weight=60.6
    )

    order = Order(pasta, chicken, tomatoes)
    order.pay(100)
    print(order.left_to_pay)
    order.add_dish(chicken, tomatoes)
    print(order, order.left_to_pay)
    order.pay(200)
    print(order.left_to_pay)
