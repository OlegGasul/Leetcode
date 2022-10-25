class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.places = [0, big, medium, small]
    
    def addCar(self, carType: int) -> bool:
        if not self.places[carType]:
            return False
        
        self.places[carType] -= 1
        return True

parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))