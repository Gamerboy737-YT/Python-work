from time import sleep

flavours = {1: "Caramel Twist",
            2: "Orange Crush",
            3: "Chocolate Bar",
            4: "Brazil Nut in Chocolate",
            5: "Cornish Fudge", 
            6: "Strawberry Treat",
            7: "Orange Smoothie", 
            8: "Toffee Bar", 
            9: "Hazelnut Triangle", 
            10: "Coconut Dream"
            }

def view_flavours():
    print("Here are the flavours we have available:")
    for i in flavours:
        print(f"{i}. {flavours[i]}")

def select_tin_flavours():
    order = {}
    user_choice = int(input("If you would like to view our available flavours, press 1. If you are ready to choose the flavours you want, press 2."))
    if user_choice == 1:
        view_flavours()
        return select_tin_flavours()
    elif user_choice == 2:
        pass

    while sum(order.values()) < 1000:
        valid = False
        flavour_to_add = ""
        while valid == False:
            try:
                flavour_to_add = input(
                "Please either enter the corresponding number or name of the flavour to add:"
                ).title()
                if flavour_to_add.isdigit():
                    if int(flavour_to_add) in flavours:
                        if int(flavour_to_add) in order:
                            print("You have already added this flavour to your tin")
                            raise ValueError
                    valid = True
                elif flavours in flavour_to_add.values():
                    if flavour_to_add in order:
                        print("You have already added this flavour to your tin")
                        raise ValueError
                    valid = True    
                else:
                    print("Sorry, we don't recognise that flavour. Please try again.")
                    raise ValueError        
            except ValueError:                           
                pass
        
        valid = False
        amount_to_add = 0
        while valid == False:
            try:    
                amount_to_add = int(input("Please enter the ammount of chocolate you would like (must be divisible by 100 and less than 500)"))
                if not 100 <= amount_to_add <= 500:
                    print("You must enter an amount between 100g and 500g")
                    raise ValueError
                if sum(order.values()) + amount_to_add > 1000:
                    print("You can't have more than 1000g of chocolate total")
                if amount_to_add % 100 == 0:
                    print("You have chosen to add" ,amount_to_add, "g of " , flavours.values())
                    confirm = input("To confirm, press y, otherwise any key")
                    if confirm == "y":
                        valid = True
                    else:
                        raise ValueError
                else:
                    print("Please enter a valid amount of chocolate.")
                    raise ValueError
                
                valid = True
            except ValueError:
                pass
        order[flavour_to_add] = amount_to_add

    if 3 <= len(order) <= 6:
        print("Order complete")
        return order
    else:
        print("You're order must contain between 3 and 6 flavours, resetting...")
        return select_tin_flavours
        sleep(1)

def create_message():
    print("You can choose to add your own personalised message to your tin")
    print("'Merry Christmas' will be added for free, and every other character, excluding spaces, costs 10p")
    message = None
    if input("Would you like to add your own message? Please type y if you would, otherwise continue.").lower() == "y":
        message = input("Please type your message.")
        return "Merry Christmas" + message
    else:
        return ""


def menu():
    if int(input("")):
        select_tin_flavours()
