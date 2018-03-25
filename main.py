from Spy_details import spy, Spy
from datetime import datetime

print "Hello!"

print'let\'s get started'
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

def start_chat(spy):
    print "Authentication complete. Welcome " + spy.name + " age: " \
          + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"
    current_status_message=None
    show_menu = True

    while show_menu:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n" \
                       " 3. Send a secret message \n 4. Read a secret message \n" \
                       " 5. Read Chats from a user \n 6. Close Application \n"
        menu_choice = raw_input(menu_choices)

        if len(menu_choice) > 0:
            menu_choice = int(menu_choice)

            if menu_choice == 1:
                spy.current_status_message = add_status()
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print "You have %d friends" % (number_of_friends)
            elif menu_choice == 3:
                send_a_message()
            elif menu_choice == 4:
                read_a_message()
            elif menu_choice == 5:
                read_chat_history()
            else:
                show_menu = False
if existing == "Y":
    start_chat(spy)
else:

    spy = Spy('','',0,0.0)

    spy.name = raw_input("What is your name?")

    if len(spy.name) > 0:
        print "Welcome " + spy.name + ". Glad to have you back with us."
        spy.salutation = raw_input("What should we call you (Mr. or Ms.)?")
        spy.name = spy.salutation + " " + spy.name
        print "Alright " + spy.name + ". I'd like to know a little bit more about you before we proceed..."
        spy.age = 0
        spy.rating = 0.0
        spy.is_online = False
        spy.age = int(raw_input("What is your age?"))
        if 18 < spy.age < 65:
            spy.rating = float(raw_input("What is your spy rating?"))
            if spy.rating > 4.5:
                print "Great ace!"
            elif 3.5 < spy.rating <= 4.5:
                print "You are one of the good ones."
            elif 2.5 <= spy.rating <= 3.5:
                print "You can always do better"
            else:
                print "We can always use somebody to help in the office."
            spy.is_online = True
            start_chat(spy)

        else:
            print "Sorry you are not of the correct age to be a spy"
    else:

        print "A spy needs to have a valid name. Try again please."