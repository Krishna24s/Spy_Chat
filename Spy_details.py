from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

spy = Spy('Krishna', 'Mr.', 21, 4.7)


friend_one = Spy('Mohit', 'Mr.', 23, 4.7)
friend_two = Spy('Diksha', 'Mr.', 20, 4.8)
friend_three = Spy('Ridhima', 'Dr.', 19, 4.8)
friend_four = Spy('Prince', 'Mr..', 22, 4.9)
friend_five = Spy('Aashish', 'Ms.', 22, 4.9)
friend_six = Spy('Yash', 'Dr.', 19, 4.9)


friends = [friend_one, friend_two, friend_three,friend_four,friend_five,friend_six]
