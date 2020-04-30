from operator import attrgetter
class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area;

    def __repr__(self):
        return repr((self.name, self.population, self.area))

countries = [Country('India', 1200, 100),
             Country('USA', 120, 120),
             Country('Canada', 100, 80)]

countries.sort(key=attrgetter('name'), reverse=True)
print(countries)

