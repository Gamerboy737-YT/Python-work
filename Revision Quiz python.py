def hardware_quiz():
           
    score = 0
   
    answer = input("What does the R in ROM stand for?").lower()
    while answer != "read":
        print("Wrong! Try again")
        answer = input("What does the R in ROM stand for?").lower()
    if answer == "read":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What does the R in RAM stand for?").lower()
    while answer != "random":
        print("Wrong! Try again")
        answer = input("What does the R in RAM stand for?").lower()
    if answer == "random":
        print("Correct!")
        score += 1
        print("Your score is" ,score)
       
    answer = input("Which type of main memory storage is closest to the CPU?").lower()
    while answer != "register" and answer != "registers":
        print("Wrong! Try again")
        answer = input("Which type of main memory storage is closest to the CPU?").lower()
    if answer == "register" or answer == "registers":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What is the fastest type of Cache?").lower()
    while answer != "l1":
        print("Wrong! Try again")
        answer = input("What is the fastest type of Cache?").lower()
    if answer == "l1":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What is the main circuit board of computers?").lower()
    while answer != "motherboard":
        print("Wrong! Try again")
        answer = input("What is the main circuit board of computers?").lower()
    if answer == "motherboard":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What does ALU stand for?").lower()
    while answer != "arithmetic logic unit":
        print("Wrong! Try again")
        answer = input("What does ALU stand for?").lower()
    if answer == "arithmetic logic unit":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What part of the computer is the BIOS stored?").lower()
    while answer != "rom":
        print("Wrong! Try again")
        answer = input("What part of the computer is the BIOS stored?").lower()
    if answer == "rom":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What word describes RAM losing it's data when the computer is powered off?").lower()
    while answer != "volatile":
        print("Wrong! Try again")
        answer = input("What word describes RAM losing it's data when the computer is powered off?").lower()
    if answer == "volatile":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What does FDE stand for?").lower()
    while answer != "fetch decode execute":
        print("Wrong! Try again")
        answer = input("What word d2escribes RAM losing it's data when the computer is powered off?").lower()
    if answer == "fetch decode execute":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("Which component performs the FDE cycle?").lower()
    while answer != "cpu":
        print("Wrong! Try again")
        answer = input("Which component performs the FDE cycle?").lower()
    if answer == "cpu":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    final_score = score
    print("Congratulations, you scored", final_score,)
       
def networks_quiz():
           
    score = 0
   
    answer = input("What represents the devices in a network?").lower()
    while answer != "nodes":
        print("Wrong! Try again")
        answer = input("What represents the devices in a network?").lower()
    if answer == "nodes":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What represents the connections in a network?").lower()
    while answer != "edges":
        print("Wrong! Try again")
        answer = input("What represents the connections in a network?").lower()
    if answer == "edges":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("True or False: In a peer-to-peer network, devices can act as the client and the server").lower()
    while answer != "true":
        print("Wrong! Try again")
        answer = input("True or False: In a peer-to-peer network, devices can act as the client and the server").lower()
    if answer == "true":
        print("Correct!")
        score += 1
        print("Your score is" ,score)
       
    answer = input("What does the L in LAN stand for?").lower()
    while answer != "local":
        print("Wrong! Try again")
        answer = input("What does the L in LAN stand for?").lower()
    if answer == "local":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What is the most common network topology?").lower()
    while answer != "mesh":
        print("Wrong! Try again")
        answer = input("What is the most common network topology?").lower()
    if answer == "mesh":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What is the top layer of the TCP/IP model?").lower()
    while answer != "application":
        print("Wrong! Try again")
        answer = input("What is the top layer of the TCP/IP model?").lower()
    if answer == "application":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("Which type of cable has the higher bandwidth, copper or fibreoptic?").lower()
    while answer != "fibreoptic":
        print("Wrong! Try again")
        answer = input("Which type of cable has the higher bandwidth, copper or fibreoptic?").lower()
    if answer == "fibreoptic":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("Which protocol splits data into packets and reassembles them at the destination?").lower()
    while answer != "tcp":
        print("Wrong! Try again")
        answer = input("Which protocol splits data into packets and reassembles them at the destination?").lower()
    if answer == "tcp":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("The area networks types are PAN, LAN and ...?").lower()
    while answer != "wan":
        print("Wrong! Try again")
        answer = input("What is the most common network topology?").lower()
    if answer == "wan":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("How many layers are in the TCP/IP model (word answer)?")
    while answer != "five":
        print("Wrong! Try again")
        answer = input("How many layers are in the TCP/IP model (word answer)?")
    if answer == "five":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

def networks_quiz22():
           
    score = 0
   
    answer = input("What represents the devices in a network?").lower()
    while answer != "nodes":
        print("Wrong! Try again")
        answer = input("What represents the devices in a network?").lower()
    if answer == "nodes":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What represents the connections in a network?").lower()
    while answer != "edges":
        print("Wrong! Try again")
        answer = input("What represents the connections in a network?").lower()
    if answer == "edges":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("True or False: In a peer-to-peer network, devices can act as the client and the server").lower()
    while answer != "true":
        print("Wrong! Try again")
        answer = input("True or False: In a peer-to-peer network, devices can act as the client and the server").lower()
    if answer == "true":
        print("Correct!")
        score += 1
        print("Your score is" ,score)
       
    answer = input("What does the L in LAN stand for?").lower()
    while answer != "local":
        print("Wrong! Try again")
        answer = input("What does the L in LAN stand for?").lower()
    if answer == "local":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What is the most common network topology?").lower()
    while answer != "mesh":
        print("Wrong! Try again")
        answer = input("What is the most common network topology?").lower()
    if answer == "mesh":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("The 4 topologies are bus, star, mesh and...").lower()
    while answer != "ring":
        print("Wrong! Try again")
        answer = input("The 4 topologies are bus, star, mesh and...").lower()
    if answer == "ring":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    answer = input("What is the cheapest network topology?").lower()
    while answer != "star":
        print("Wrong! Try again")
        answer = input("What is the cheapest network topology?").lower()
    if answer == "star":
        print("Correct!")
        score += 1
        print("Your score is" ,score)

    final_score = score
    print("Congratulations, you scored", final_score,)

print("Hello, and welcome to the revision quiz")
def menu():
    choice = int(input("What would you like to study, press 1 for hardware, 2 for networks, or 3 for (networks)?"))
    if choice == 1:
        hardware_quiz()
    elif choice == 2:
        networks_quiz()
    elif choice == 3:
        networks_quiz()
    else:
        print("Please input 1, 2 or 3")
        int(input("What would you like to study, press 1 for hardware, 2 for networks or 3 for (networks)?"))

    again = input("Would you like to do another quiz? Please type yes or no").lower()
    if again == "yes":
        menu()
    elif again == "no":
        print("Goodbye")
    else:
        print("Please input yes or no")
        again = input("Would you like to do another quiz? Please type yes or no").lower()    

menu()