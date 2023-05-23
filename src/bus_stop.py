class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def queue_length(self):
        return len(self.queue)
    
    def add_to_queue(self, passenger):
        self.queue.append(passenger)

    def clear_queue(self):
        self.queue.clear()
        return len(self.queue)
    

    


    #  def sell_pet_to_cusomer(self, pet_name, customer):
    #     pet = self.find_pet_by_name(pet_name)
    #     customer.reduce_cash(pet.price)
    #     self.increase_total_cash(pet.price)
    #     self.remove_pet(pet)
    #     self.increase_pets_sold()
    #     customer.add_pet(pet)

