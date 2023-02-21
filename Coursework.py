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
            print("Here are the flavours we have available: \n{flavours.values()}")

def select_tin_flavours():
            user_choice = int(input("If you would like to view our available flavours, press 1. If you are ready to choose the flavours you want, press 2."):
                if user_choice = 1:
                      view_flavours()
                      return select_tin_flavours()
                elif user_choice = 2:
                        return select_tin_flavours()

            valid = False
            while valid == False:
                              try:
                              flavour_to_add = input("Please either enter the corresponding number or name of the flavour to add: ")
                              if flavour_to_add.title() not in flavours.values():
                              print("Sorry, we don't recognsie that flavour. Please try again.")
                              raise ValueError
                        
           
