lottery_player = {
    'name': 'Raju',
     'numbers': (22,33,44,55)
}

print(lottery_player['name'])
print(sum(lottery_player['numbers']))
class Lotteryclass:
    def __init__(self):
        self.name = "Raju"
        self.numbers = (22,33,44,55)
    def total(self, number):
        return sum(self.numbers)

player = Lotteryclass()
print(player.name, player.numbers)
res = Lotteryclass()
print(res.total(lottery_player['numbers']))


class student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks =[]
    def average(self):
        return sum(self.marks)/len(self.marks)

Amulya = student("Amulya", "JNNCE, Shimoga")
Amulya.marks.append(98)
Amulya.marks.append(88)
print(Amulya.marks)
print(Amulya.average())


class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name':name, 'price':price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        total =0
        return sum([item['price'] for item in self.items])


stud = Store('Appu')
print(stud.name)
stud.add_item('Annu', 40)
stud.add_item('papu', 80)
res = stud.stock_price()
print(res)