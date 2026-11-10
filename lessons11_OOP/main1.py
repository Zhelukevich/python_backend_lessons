class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.is_human = True

    def say_hello(self, to_name):
        print(f"Привет {self.name}, я {to_name}")


user1 = User("Pasha", 28)  # Экземпляр
print(user1.__dict__["name"])
user1.say_hello(to_name="TTTT")


class GameCharacter:
    def __init__(self, name, damage, health) -> None:
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self):
        print(f"{self.name} наносит {self.damage} урон")

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"получил {self.name} урон. Осталось здоровья: {self.health}")


character = GameCharacter("Pasha", 5, 100)
character.attack()
character.take_damage(30)
character.take_damage(30)
character.take_damage(30)
character.take_damage(30)


class Card:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.items = []

    def add_item(self, name, price):
        self.items.append(
            {
                "name": name,
                "price": price,
            }
        )

    def get_total(self):
        # total_price = 0

        # for item in self.items:
        #     total_price += item["price"]

        # return total_price
        return sum(item["price"] for item in self.items)

    def show_items(self):
        if not self.items:
            return "Корзина пустая"

        # lines = []
        # for item in self.items:
        #     lines.append(f"{item['name']} - {item['price']}")

        # return "\n".join(lines)
        return "\n".join(f"{item['name']} - {item['price']}" for item in self.items)


card1 = Card("Pasha")
card1.add_item(name="Phone", price=1500)
card1.add_item(name="Pen", price=100)
print(card1.get_total())
print(card1.show_items())
