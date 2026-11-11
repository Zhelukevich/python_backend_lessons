class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} работает")


class TesterQA(Employee):
    def work(self):
        print(f"{self.name} тестирует код")


class Developer(Employee):
    def __init__(self, name, salary, language: str) -> None:
        super().__init__(name, salary)
        self.language = language

    def work(self) -> None:
        print(f"{self.name} пишет код {self.language}")


class Designer(Employee):
    def work(self):
        print(f"{self.name} Рисует интерфейс")


tester = TesterQA("Pasha", "1500$")
tester.work()

developer = Developer("Pasha", 2000, "Python")
developer.work()


designer = Designer("Pasha", "1500$")
designer.work()
