#Elevator can take multiple passengers and
#remember the current floor for the passengers.
#With more time I would've added the ability for
#The elevator to remove passengers when it passes their
#Selected floor.  But I wanted to get it in before the time Limit.
#Thanks for the opportunity, this was really fun.

import time

class Elevator():
    def __init__(self, starting_floor=1, capacity=10):
        self.NUM_FLOORS = 10
        self.passengers = []
        self.starting_floor = starting_floor
        self.capacity = capacity
        self.current_floor = 1
        self.queue = []

    def add_passenger(self):
        if len(self.passengers) < self.capacity:
            name = str(input("Enter passenger name: "))
            p = Passenger(name)
            self.passengers.append(p)
        else:
            print("The capacity is over the limit")

    def push_button(self):
        print(self.get_name_list())
        name = str(input("Enter name of passenger selecting button: "))
        for item in self.passengers:
            if item.name == name:
                item.get_input()
                selection = item.floor_selection
                self.queue.append(selection)
                self.move_floor(selection, item)
                self.passengers.remove(item)
    
    def get_name_list(self):
        name_list = [name.name for name in self.passengers]
        return name_list

    def move_floor(self, selection, passenger):
        if len(self.queue) > 0:
            print("Moving through the selected floors!")
            if self.current_floor == selection:
                print("***")
                print("We are already at this passengers designated floor!")
                print("***")
                time.sleep(1)
            elif self.current_floor > selection:
                for floor in range(self.current_floor, selection, -1):
                    self.check_floor(passenger)
                    print(f'Now on floor {self.current_floor}')
                    self.current_floor-=1
                    time.sleep(1)
                print("****")
                print(f'You have arrived at floor number {self.current_floor}!!!')
                time.sleep(1)
                print("The doors open abroad to a whole new world")
                time.sleep(1)
                print("You look back and wave, with some gusto and a smirk on your face..")
                print("****")
                time.sleep(1.5)
            else:
                if self.current_floor < selection:
                    for floor in range(self.current_floor, selection):
                        self.check_floor(passenger)
                        print(f'Now on floor {self.current_floor}')
                        self.current_floor+=1
                        time.sleep(1)
                    print("****")
                    print(f'You have arrived at {self.current_floor}')
                    time.sleep(1)
                    print("The doors open abroad to a whole new world")
                    time.sleep(1)
                    print("You look back and wave, with some gusto and a smirk on your face..")
                    print("****")
                    time.sleep(1.5)
        else:
            self.queue.append(selection)
            print(self.queue)

    def check_floor(self, current_passenger):
        if current_passenger.floor_selection == self.current_floor:
            self.passengers.remove(passenger)

class Passenger():
    def __init__(self, name):
        self.floor_selection = 0
        self.name = name

    def get_input(self):
        selection = int(input("Enter floor number: "))
        if selection <= Elevator().NUM_FLOORS and selection >= 1:
            self.floor_selection = selection
        else:
            print("You must select a floor less than or equal to 10")

def start():
    while True:
        print("Welcome to the elevator.\n")
        print("This elevator takes multiple passengers\n")
        print("and is equipped to know when your designated floor has arrived!")
        print("")
        print("We have already created the elevator for you.")
        print("Simply select an option from the menu to use the elevator.")
        print("***************")
        print("1: Add a Passenger")
        print("2: Push a button to move the elevator")
        print("3: List Passengers")
        print("***************")
        choice = str(input("Enter your choice---> "))
        if choice == '1':
            e.add_passenger()
        elif choice == '2':
            e.push_button()
        elif choice == '3':
            print("Current Passengers")
            print(e.get_name_list())
            time.sleep(1)


e = Elevator()
start()