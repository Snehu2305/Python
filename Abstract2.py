from abc import ABC

class Movie(ABC):
    def __init__(self, genre):
        self.genre = genre
    
    def genreClassify(self):
        pass

class Action(Movie):
    def genreClassify(self):
       print("Avangers")


class Humorous(Movie):
    def genreClassify(self):
        print("Houseful")

class Advanture(Movie):
    def genreClassify(self):
        print("Stranger's Things")

class Devotional(Movie):
    def genreClassify(self):
        print("Kantara")

class Historic(Movie):
    def genreClassify(self):
        print("Padmavat")

genre = input("Enter genre: ")
m = Movie(genre)

a = Action()
h = Humorous()
ad =Advanture()
d = Devotional()
hi = Historic()

match genre:
    case "action":
        a.genreClassify()
    
    case 'humorous':
        h.genreClassify()
    
    case 'advanture':
        ad.genreClassify()

    case 'devontional':
        d.genreClassify()
    
    case 'historic':
        hi.genreClassify()


