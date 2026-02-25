class Name:
    def __init__(self, text: str):
        self.text = text

    def __repr__(self):
        return f"Name('{self.text}')"

class Length:
    def __init__(self, meters: float):
        self.meters = meters

    def __repr__(self):
        return f"Length({self.meters})"

class Speed:
    def __init__(self, kmh: float):
        self.kmh = kmh

    def __repr__(self):
        return f"Speed({self.kmh})"

class Capacity:
    def __init__(self, people: int):
        self.people = people

    def __repr__(self):
        return f"Capacity({self.people})"

class Year:
    def __init__(self, year: int):
        self.year = year

    def __repr__(self):
        return f"Year({self.year})"

class SeaBoat:
    def __init__(self, name: Name, length: Length, speed: Speed, capacity: Capacity, year: Year):
        self.name = name
        self.length = length
        self.speed = speed
        self.capacity = capacity
        self.year = year

    def __eq__(self, other):
        return (
            self.name.text == other.name.text and
            self.length.meters == other.length.meters and
            self.speed.kmh == other.speed.kmh and
            self.capacity.people == other.capacity.people and
            self.year.year == other.year.year
        )

    def __repr__(self):
        return (f"SeaBoat(name={self.name}, length={self.length}, "
                f"speed={self.speed}, capacity={self.capacity}, year={self.year})")

    def execute(boats: list):
        print("Початковий масив човнів:")
        for boat in boats:
            print(boat)

        boats.sort(key=lambda b: b.length.meters)
        print("\nМасив після сортування (довжина за зростанням):")
        for boat in boats:
            print(boat)

        boats.sort(key=lambda b: -b.speed.kmh)
        print("\nМасив після сортування (швидкість за спаданням):")
        for boat in boats:
            print(boat)

        target_boat = SeaBoat(Name("Poseidon"), Length(35.0), Speed(55), Capacity(150), Year(2012))
        print("\nПошук заданого об'єкта:")
        found = False
        for boat in boats:
            if boat == target_boat:
                print("Знайдено ідентичний об'єкт:")
                print(boat)
                found = True
                break
        if not found:
            print("Ідентичний об'єкт не знайдено.")

if __name__ == "__main__":
    boats = [
        SeaBoat(Name("Odessa"), Length(30.5), Speed(45), Capacity(120), Year(2010)),
        SeaBoat(Name("Neptune"), Length(25.0), Speed(60), Capacity(80), Year(2015)),
        SeaBoat(Name("BlackSea"), Length(40.2), Speed(50), Capacity(200), Year(2008)),
        SeaBoat(Name("Poseidon"), Length(35.0), Speed(55), Capacity(150), Year(2012)),
        SeaBoat(Name("Atlantis"), Length(28.7), Speed(48), Capacity(100), Year(2018))
    ]
    SeaBoat.execute(boats)
