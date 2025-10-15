from abc import ABC

class Movie(ABC):
    def genre(self):
        pass

class Kantara(Movie):
    def genre (self):
        print("Devotional")

class Padmavat(Movie):
    def genre(self):
        print("Historical")

class Avangers(Movie):
    def genre(self):
        print("Action film")

class HarryPotter(Movie):
    def genre(self):
        print("Magical world")


class StrangersThings(Movie):
    def genre(self):
        print("advanture")

class Housefull(Movie):
    def genre(self):
        print("Humourous")


k = Kantara()
k.genre()

p = Padmavat()
p.genre()

a = Avangers()
a.genre()

h = HarryPotter()
h.genre()

s = StrangersThings()
s.genre()

h = Housefull()
h.genre()