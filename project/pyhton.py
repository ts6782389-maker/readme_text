class car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class toyotacar(car):
    def __init__(self, name , type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = toyotacar("pirus" , "electric")
print(car1.type)