import pdb

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
       
    def drive(self):
        return "Brum brum"

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def passenger_count(self):
        return len(self.passengers)
    
    def empty_bus(self):
        self.passengers.clear()

#EXTENSION
    def pick_up_from_stop(self, bus_stop):
        # pdb.set_trace()
        for person in bus_stop.queue:
            self.passengers.append(person)
        bus_stop.clear_queue()

        
        
        # self.pick_up(bus_stop.queue)
        # self.passengers.pick_up(bus_stop.queue)
        # bus_stop.clear_queue()



    #  def sell_pet_to_cusomer(self, pet_name, customer):
    #     pet = self.find_pet_by_name(pet_name)
    #     customer.reduce_cash(pet.price)
    #     self.increase_total_cash(pet.price)
    #     self.remove_pet(pet)
    #     self.increase_pets_sold()
    #     customer.add_pet(pet)
        