# Implemeting open closed principle
from enum import Enum


class Colour(Enum):
    RED = 1
    GREEN = 2
    YELLOW = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, colour, size):
        self.name = name
        self.colour = colour
        self.size = size

    def __str__(self):
        return self.name
# without open closed principle, changes have to be made to the class defined below
class ProductFilter:
    def filter_by_colour(self, products, colour):
        for p in products:
            if p.colour == colour: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

    # more such definitions such as product and/or colour have to be added everytime changes
    # are introduced to the existing code

# after implementing open closed principle
# 1. adding interfaces
class Specification:
    def __init__(self, item):
        pass

    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

# 2. adding implementations for different criterias
# Colour
class ColorSpecification(Specification):
    def __init__(self, colour):
        self.colour = colour

    def is_satisfied(self, item):
        return self.colour == item.colour

# Size
class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return self.size == item.size

# implementing new filter
class AdvancedFilter(Filter):
    def filter(self, item, spec):
        for i in item:
            if spec.is_satisfied(i):
                yield i

orange = Product('Orange', Colour.YELLOW, Size.LARGE)
apple = Product('Apple', Colour.RED, Size.MEDIUM)

products = [orange, apple]

# using old approach
pf = ProductFilter()
for p in pf.filter_by_colour(products, Colour.RED):
    print(p)

# using Open closed principle
af = AdvancedFilter()
spec = ColorSpecification(Colour.YELLOW)
for i in af.filter(products, spec):
    print(i.name)