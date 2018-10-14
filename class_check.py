class Animal:
    def __init__(self, name):
        self.name = name
        print('init')

    def __new__(self, weight):
        self.weight = weight
        return self

class Cat (Animal):
    def __init__(self):
        super().__init__()
        self.age = 15

    def __getitem__(self, i):
        return 5


def main():
    print(Animal(133).weight, )

if __name__ == '__main__':
    main()