class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare() 
        maintenance_charge = total_fare * 0.10  
        final_amount = total_fare + maintenance_charge
        return final_amount


vehicle = Vehicle("Car", 4)
bus = Bus("School Bus", 50)

print(f"Fare for vehicle: {vehicle.fare()}")
print(f"Fare for bus: {bus.fare()}")
