import random

# Define player attributes
player = {
    "name": "Player",
    "charisma": 0,
    "eloquence": 0,
    "wealth": 0,
    "status": 0,
}
chapter = 1
#end game
endGame = False
# Location
Location = {"Home"}
#time
Time = "Morning"

# Location options
Location_options = {"Home of Patron":{
    "character": "Gaius Aurelius",
    "dialgueIndex": 3,
}, "Thermae": {
    "character": "Ceasar"}}
PatronData = [
    {"initialDialogue": "You greet Gaius Aurelius and introduce yourself. Many of his patron accompany him to forum for a speech. Will you acompany him?", 
    "options": 
        ["yes", "no"], 
    "response": 
        [[
            "You acompany Gaius Aurelius to the forum. As he gives his speech you cheer along with his other clients. You are impressed by his eloquence and charisma. You feel like you have learned a lot from him. +1 eloquence",
             "You decide not to acompany Gaius Aurelius to the forum. You feel like you have missed out on an opportunity to learn from him."
             ],
        ["eloquence", 1, 0]],
    "require": {"charisma": 0, "eloquence": 0, "wealth": 0, "status": 0},
    "correctAnswer": 0,
    },
        #go to a salutatio and ask for a favor in starting a bakery

    {"initialDialogue": "You go to Gaius's salutatio and you ask your fellow \nclients what kind of favors they have asked of Gaius. You hear that Gaius is a powerful patron for many bakeries in Rome.\n You approach Gaius at his desk and you ask for help starting a...",
    "options":["bakery", "tavern", "inn", "brothel"],
    "response":[["Gaius is impressed by your ambition and charisma. He agrees to help you start a bakery and gifts you enough money to start one. +1 wealth\nYou make a note to yourself to make a public inscription thanking Gaius for his generosity.)", "Gaius says that he is unable to help you with your request. Maybe you should ask him for something else."],[ "wealth", 1, 0]],
    "require": {"charisma": 2, "eloquence": 1, "wealth": 0, "status": 0},
    "correctAnswer": 1,
    },
    #go to a salutatio and he asks you to give some bread to some of his clients right answer is yes
    {
        "initialDialogue": "Your bakery is in it's starting phase. You go to Gaius's salutatio and you graciously bow for the support he has given. \n When you meet with him, he says that some of his clients are in dire need of food. He asks you if you can give them some bread.",
        "options": ["yes", "no"],
        "response": [["You agree to give bread to his clients. You feel like you have made a good impression on Gaius. +1 charisma", "You refuse to give bread to his clients. After all he's done to help you, he is disapointed. -1 charisma"], ["charisma", 1, -1]],
        "require": {"charisma": 0, "eloquence": 0, "wealth": 0, "status": 0},
        "correctAnswer": 1,

    },
    #go to a salutatio and ask for help making the bakery more profitable
    {
        "initialDialogue": "Your bakery is in it's starting phase. You go to Gaius's salutatio and you graciously bow for the support he has given. \n When you meet with him, you ask for assistance in imporving your bakery's profits.\n He asks how you would like him to support you.",
        "options": ["give me a knowledgeable slave","give me a loan for more equipment", "help me spread the name of the bakery"],
        "response": [["Gaius says he will give you a slave that is knowledgeable in the art of baking. You think to yourself that Gaius is truely a generous patron. +1 wealth", "Gaius gives you a loan to buy more equipment. You think to yourself that Gaius is truely a generous patron. +1 wealth", "Gaius says he will help you spread the name of your bakery. You think to yourself that Gaius is truely a generous patron. +1 wealth"], ["wealth", 1, 1, 1]],
        "require": {"charisma": 0, "eloquence": 0, "wealth": 0, "status": 0},
        "correctAnswer": 0,
    }, 
    

    ]
# have a variable that stores a boolean value for wehter or not there is a dinner party
# Function to display player status
def show_status():
    #print(f"\n{name}'s Status:")
    print(f"Charisma: {player['charisma']}")
    print(f"Eloquence: {player['eloquence']}")
    print(f"Wealth: {player['wealth']}")
    print(f"Status: {player['status']}\n")
#Funciton to display text for the Thermae
def thermae():
    #print("You are at the Thermae. You can see many people bathing and socializing.")
    if(Time != "Evening"):
        print("It is morning, the Thermae is closed. Try checking other places or waiting until morning.")
        return
    else:#Runs if player is in thermae
        print("You are at the Thermae. You can see many people bathing and socializing.")
        print("You pay someone to watch your clothes and enter the bath. You exercise and get cleaned with perfumed oil.")
        print("Do you want to socialize with others in hopes of making connections?")
        while True:
            command = input("yes/no: ").lower()
            if command == "yes":
                break
            elif command == "no":
                print("You leave the Thermae and go home for the night.")
                changeTime()
                return
            else:
                print("Invalid command. Type 'yes' or 'no'.")
        
        if random.random() < 0.50:
            print("You socialize with a group of people and \na more powerful patron takes an interest in you. \nYou are invited to a dinner party at his home.\nDo you go?")
            while True:
                command = input("yes/no: ").lower()
                if command == "yes":
                    break
                elif command == "no":
                    print("You leave the Thermae and go home for the night.")
                    changeTime()
                    return
                else:
                    print("Invalid command. Type 'yes' or 'no'.")
            #handle dinner party with later chapter
            dinnerParty()
            player["charisma"] += 1
        else:
            print("You socialize with some people, but no one of importance takes \nan interest in you. Better luck next time. +1 charisma")
            player["charisma"] += 1
            print("You leave the Thermae and go home for the night.")
        changeTime()

#Function to check if the player has the required stats to do an action
def checkRequire(require):
    for key in require:
        if player[key] < require[key]:
            return key
    return False
#Reverse time of day
def changeTime():
    global Time
    if(Time == "Morning"):
        Time = "Evening"
    else:
        Time = "Morning"
#Function for dinner party
def dinnerParty():
    global endGame
    print("You arrive at the dinner party and find out that the host is the emperor himself! The emperor has taken a great liking to you and elects you a member of the senate. By a stroke of pure luck you have reached as far as you can in the Roman world. Congratulations!")
    endGame = True
    return
#Function to display home of Gaius Aurelius
def homeOfPatron():
    print("You are at the home of" + Location_options["Home of Patron"]["character"] +". From the entrance, you can see an expansive garden further in the house.")
    if(Time != "Morning" and not dinnerParty):
        print("It is evening, Gaius Aurelius is not home right now. Try checking other places or waiting until morning.")
        return
    
    else:
        
        
        #print("You are talking to Gaius Aurelius")
        index = Location_options["Home of Patron"]["dialgueIndex"]
        if (index >= len(PatronData)):
            print("-----------------------------------")
            print("A few years have passed since you started your bakery, and you have opened many more. You have become a successful bakery owner, and you have a good relationship with Gaius Aurelius.")
            print("lucky for you, a census is being taken, and your bakeries are now worth more than 100,000 denarii. Due to Agustus's law, you are granted the use of the equestrian title.")
            print("Because of your new status, you are no longer allowed to be Gaius' client. You consider yourself lucky that you had such a good patron.")
            print("However, your story does not end here. Your ambition drives you to move further upward in society, and for that, you will need a new patron.")
            stage2()
            return
        print(PatronData[index]["initialDialogue"])
        while True:
            for i in range(len(PatronData[index]["options"])):
                print(f"{i+1}. {PatronData[index]['options'][i]}")
            try:
                response = int(input("choose and option: ").lower())

            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            require = checkRequire(PatronData[index]["require"])
            if (require):
                print("You do not have enough " + require + " to do this action. Try raising your " + require + " by doing other actions first.")
                return
            elif (PatronData[index]["correctAnswer"] != 0):
                if PatronData[index]["correctAnswer"] != response:
                    print(PatronData[index]["response"][0][1])
                    return
                elif PatronData[index]["correctAnswer"] == response:
                    print(PatronData[index]["response"][0][0])
                    player[PatronData[index]["response"][1][0]] += PatronData[index]["response"][1][1]
                    Location_options["Home of Patron"]["dialgueIndex"] += 1
                    break
            else:
                if (response > len(PatronData[index]["options"]) or response < 1):
                    print("Invalid input. Please enter a number between 1 and " + str(len(PatronData[index]["options"])) + ".")
                    continue
                else:
                    print(PatronData[index]["response"][0][response-1])
                    player[PatronData[index]["response"][1][0]] += PatronData[index]["response"][1][response]
                    Location_options["Home of Patron"]["dialgueIndex"] += 1
                    break
                
#Function to move to stage 2 of the game
def stage2():
    global PatronData
    PatronData = [
        {
            "initialDialogue": "In your new position, you search for a new patron.\n Unfortunately, many of those in the senetorial class have so many clients that you are unable to see them.\n However, there is one senator who does not seem to many clients. His name is Lucius Malvolius. You decide to go to his sparse salutatio and after, you approach his office. You greet him formally and introduce yourself. You need to ask for something, what do you ask for?",
            "options": ["Help buying land", "Help finding a wife", "Help getting into public office"],
            "response": [["Lucius begins talking about the prestige that comes with owning land. He continues talking for an hour about his own successes, and finally agrees to help you buy land. You begin to understand why he has so few clients. wealth +1","Lucius Malvolius does not think he can help you with that yet. Come back and try something else."] , ["wealth", 1]],
            "correctAnswer": 1,
            "require": {"wealth": 1}
        },
        {
            "initialDialogue": "You've bought some land outside of Rome, and your wealth begins to grow. You decide to maintain your relationship with Lucius Malvolius, and you go to his salutatio. You approach his office and greet him formally. You don't hace much to ask him, but he asks you to support him in an upcoming election. What do you say?",
            "options": ["Yes", "No"],
            "response": [["You agree to support him in the coming election, but before you can leave he begins to talk about how well suited to the position he is. He then delves into his plans if he does get elected. You are stuck listening to him for an hour before you can leave and manage to keep a smile the whole time. Charisma +1", "You tell him that you will not support him in the election. He is disappointed"], ["charisma", 1]],
            "correctAnswer": 1,
            "require": {"charisma": 1}
        },
        {
            "initialDialogue": "You have been supporting Lucius Malvolius in his election, disaster has struck! Lucius requests that you attend a dinner of his. You can already hear his voice talking about something mundane in your head. Do you go?", 
            "options": ["Yes", "No"],
            "response": [["You get to the dinner party, and are seated far from Lucius. You manage to socialize a little during the dinner. You are pretty happy to get the chance to talk to highly educated people although your wine is a little watery. Eloquence +3", "You don't go, but you feel that you are missing out on something..."],["eloquence", 3, 0]],
            "correctAnswer": 0,
            "require": {"eloquence": 0}
        },
    ]
    global Location_options
    Location_options["Home of Patron"] = {"character": "Lucius Malvolius", "dialgueIndex": 0}



    
# Function to handle the main game logic
def play_game():
    #print("Welcome to the Text-Based Game!")
    print("Welcome to my final project where you will navigate the intricacies of ancient Roman society and embark on a journey of social advancement through the patron-client system. The game is set in the bustling city of Rome during the early Roman Empire, a world of political intrigue, economic opportunity, and social stratification.")
    print("You begin your journey as Lucius, a resourceful and ambitious plebeian living in the Rome. Lucius, driven by a desire for upward mobility, dreams of breaking free from the constraints of his humble origins. The city is abuzz with rumors of a powerful equestrian patron seeking capable individuals to enhance his influence and wealth.")
    print("\nYou hear of a powerful equestrian patron who is looking for capable individuals to work for him")

    while True:
        if (endGame):
            print("You have reached the end of the game. Thanks for playing!")
            break
        # Get user input
        #question = ""
        command = input("Enter a command(or help if you need help): ").lower()

        # Process user commands
        if command == "quit":
            print("Thanks for playing!")
            break
        elif command == "status":
            show_status()
        elif command == "home of patron":
            homeOfPatron()
        elif command == "thermae":
            thermae()
        elif command == "wait":
            changeTime()
            print("You wait until " + Time + ".")
        elif command == "help":
            print("Commands:\n status - check your character's status\n quit- quit the game\n help - get a list of commands\n")
        else:
            print("Invalid command. Type 'status' to check your status.")

# Run the game
if __name__ == "__main__":
    play_game()