import random
from typing import Callable
import click


class PizzaBase:
    """ Основа для любой пиццы. Описаны методы __init__, __eq__, __hash__, __repr__ и __dict__"""

    def __init__(self, size):
        if size != 'L' and size != 'XL':
            raise ValueError(f'Pizza size can only be L or XL')
        self.__size = size

    @property
    def name(self):
        return None

    @property
    def size(self):
        return self.__size

    @property
    def ingredients(self):
        return {}

    @property
    def time_to_make(self):
        return None

    @property
    def icon(self):
        return None

    def __eq__(self, other):
        if isinstance(other, PizzaBase):
            return type(self) == type(other) and self.size == other.size

    def __hash__(self):
        return hash((type(self), self.size))

    def __repr__(self):
        return f'Pizza {self.name} of size {self.size}'

    def dict(self):
        """Shows recipes with quantities of the ingredients:
        pizza sized XL requires twice as much sauce, cheese and toppings as pizza sized L"""
        qnt_sauce = 100
        qnt_cheese = 150
        qnt_toppings = 200
        qnt = [qnt_sauce, qnt_cheese, qnt_toppings]
        i = 0
        recipe = ''
        if self.size == 'L':
            for ingredient in self.ingredients.values():
                recipe += f'{ingredient}: {qnt[i]}g \n'
                i += 1
        if self.size == 'XL':
            for ingredient in self.ingredients.values():
                recipe += f'{ingredient}: {2 * qnt[i]}g \n'
                i += 1
        return recipe


class Margherita(PizzaBase):

    @property
    def name(self):
        return 'Margherita'

    @property
    def icon(self):
        return '🧀'

    @property
    def average_time_to_make(self):
        return 20

    @property
    def ingredients(self):
        return {'sauce': 'tomato sauce', 'cheese': 'mozzarella', 'toppings': ['tomatoes']}


class Pepperoni(PizzaBase):
    @property
    def name(self):
        return 'Pepperoni'

    @property
    def ingredients(self):
        return {'sauce': 'tomato sauce', 'cheese': 'mozzarella', 'toppings': ['pepperoni']}

    @property
    def average_time_to_make(self):
        return 25

    @property
    def icon(self):
        return '🍕'


class Hawaiian(PizzaBase):

    @property
    def name(self):
        return 'Hawaiian'

    @property
    def ingredients(self):
        return {'sauce': 'tomato sauce', 'cheese': 'mozzarella', 'toppings': ['chicken', 'pineapples']}

    @property
    def average_time_to_make(self):
        return 30

    @property
    def icon(self):
        return '🍍'


class Kitchen:
    """На кухню приходит заказ на изготовление пиццы и она готовится"""

    @staticmethod
    def execute_order(pizza_order: PizzaBase) -> PizzaBase:
        instructions = f'First we\'re making the dough, and cooking the {pizza_order.ingredients["sauce"]};\n' \
                       f'Then we\'re rolling the dough and spreading the {pizza_order.ingredients["sauce"]};\n' \
                       f'Finally we\'re adding {" ".join(pizza_order.ingredients["toppings"])} and sprinkling it with ' \
                       f'{pizza_order.ingredients["cheese"]}; \nYour {pizza_order} is ready'
        print(instructions)
        prepared_pizza = pizza_order  # Эта строка отображает процесс изготовления пиццы
        return prepared_pizza


def log(template: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(pizza, *args, **kwargs):
            func(pizza, *args, **kwargs)
            time = pizza.average_time_to_make
            print(template.replace('{}', f'{random.randint(time - 5, time + 5)}'))
            return pizza
        return wrapper
    return decorator


@log('🍕Приготовили за {}с!')
def bake(pizza_order: PizzaBase) -> PizzaBase:
    """Making the pizza"""
    return Kitchen.execute_order(pizza_order)


@log('🛵 Доставили за {}с!')
def delivering(pizza: PizzaBase) -> PizzaBase:
    """Delivering pizza"""
    print(f'Our delivery man is on the way to deliver your {pizza}')
    return pizza


@log('🏠 Забрали за {}с!')
def pickup(pizza: PizzaBase) -> PizzaBase:
    """Collection by customer"""
    print(f'You can collect your {pizza}')
    return pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True, help='Do you need pizza to be delivered?')
@click.argument('pizza_name', nargs=1)
@click.argument('pizza_size', nargs=1)
def cli_order(pizza_name: str, pizza_size: str, delivery: bool):
    order(pizza_name, pizza_size, delivery)


def order(pizza_name: str, pizza_size: str, delivery: bool):
    """Make pizza and get it to the customer"""
    for i in PizzaBase.__subclasses__():
        pizza_order = i(pizza_size)
        if pizza_order.name == pizza_name:
            prepared_pizza = bake(pizza_order)
            if delivery:
                delivering(prepared_pizza)
            else:
                pickup(prepared_pizza)
            return
    raise ValueError(f'No pizza named {pizza_name}')


@cli.command()
def cli_menu():
    menu()


def menu():
    """Shows all the available types of pizza and their ingredients"""
    for piz_class in PizzaBase.__subclasses__():
        piz = piz_class('L')
        final_list = list(piz.ingredients.values())[:-1]
        for i in list(piz.ingredients.values())[2]:
            final_list.append(i)
        print(f'- {piz.name} {piz.icon}: {final_list}')


if __name__ == '__main__':
    cli()
    pass
