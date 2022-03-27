class Train:
    def __init__(self, name, seats, fair):
        self.name= name
        self.seats = seats
        self.fair = fair
        
    def status(self):
        print("Welcome to indian railways!")
        print("Train name is", self.name)
        print("seats availability is", self.seats)
        print("Train fair is",self.fair) 
        print("Thank you for using indian railways!")

    def bookTicket(self):
        if (self.seats>0):
            print(f"your ticket is booked and your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Train is full")

# a = input("enter train name:")
# b= input("enter train time:")
# c= int(input("enter train fair:")) # by this we can input the train details
n = Train("gitanjali express", 2, 1200)
# n.status()
n.bookTicket()       
n.bookTicket()
n.bookTicket()
n.status()