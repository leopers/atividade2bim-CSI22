# Pizza example using decorators

class PizzaComponent:  # Component
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Massa(PizzaComponent):  # Concrete Component
    cost = 15.00


class Decorator(PizzaComponent):  # Decorator
    def __init__(self, pizzaComponent):
        self.component = pizzaComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' + PizzaComponent.getDescription(self)


class Calabresa(Decorator):  # Concrete DecoratorA
    cost = 5.00

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Queijo(Decorator): # Concrete DecoratorB
    cost = 4.00

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class MolhoDeTomate(Decorator): # Concrete DecoratorC
    cost = 3.00

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


class Pepperoni(Decorator):
    cost = 2.00

    def __init__(self, pizzaComponent):
        Decorator.__init__(self, pizzaComponent)


pepperoni_pizza = Pepperoni(Queijo(MolhoDeTomate(Massa())))
print(pepperoni_pizza.getDescription() + ": $" + str(pepperoni_pizza.getTotalCost()))

calabresa_pizza = Calabresa(Queijo(MolhoDeTomate(Massa())))
print(calabresa_pizza.getDescription() + ": $" + str(calabresa_pizza.getTotalCost()))

cheese_pizza = Queijo(MolhoDeTomate(Massa()))
print(cheese_pizza.getDescription() + ": $" + str(cheese_pizza.getTotalCost()))