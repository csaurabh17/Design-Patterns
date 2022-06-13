class Animal:
    def __init__(self):
        self.name = None
        self.type = None
        self.runs = None
        self.crawls = None

    def __str__(self):
        return f"{self.name} of type {self.type}"


class AnimalBuilder:
    def __init__(self, animal=None):
        if animal is None:
            self.animal = Animal()
        else:
            self.animal = animal

    @property
    def mammal(self):
        return MammalBuilder(self.animal)

    @property
    def reptile(self):
        return ReptileBuilder(self.animal)

    def build(self):
        return self


class MammalBuilder(AnimalBuilder):
    def __init__(self, animal):
        super(MammalBuilder, self).__init__(animal)

    def type(self, s):
        self.animal.type = s
        return self

    def runs(self, s):
        self.animal.runs = s
        return self


class ReptileBuilder(AnimalBuilder):
    def __init__(self, animal):
        super(ReptileBuilder, self).__init__(animal)

    def crawls(self, s):
        self.animal.crawls = s
        return self

    def name(self, s):
        self.animal.name = s
        return self


animal = AnimalBuilder()
rep = animal \
    .reptile \
    .name("Snake") \
    .crawls("Yes")\
    .build()

print(rep)
