class Uber:
    def __init__(self, distance: int, is_hot: bool):
        self.distance = distance
        self.is_hot = is_hot

    def fare(self, pricepermile: int, people: int):
        if self.is_hot:
            cost = (self.distance * pricepermile) * 2
            return cost / people
        cost = self.distance * pricepermile
        return cost / people

    def capacity_check(self, capacity: int, people: int):
        if capacity >= people:
            return True
        raise ValueError("Does not have enough capacity for fare.")


class XL(Uber):
    def __init__(self, distance: int, is_hot: bool):
        super().__init__(distance, is_hot)
        self.capacity = 6


class Van(Uber):
    def __init__(self, distance: int, is_hot: bool):
        super().__init__(distance, is_hot)
        self.capacity = 8


class Car(Uber):
    def __init__(self, distance: int, is_hot: bool):
        super().__init__(distance, is_hot)
        self.capacity = 4
