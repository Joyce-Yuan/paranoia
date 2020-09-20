from player import Player
players  = [ ]
nameArray = [ ]

def setup():
    numPlayers = int(input("How many players?"))
    for i in range(numPlayers):
        players.append(Player())

    for i in players:
        #print(name)
        i.setName(input("Player " + str(i.id) + "‘s name?"))
        i.reset() #within __main__ for loop

    nameArray = makeNameArray()

def main():
    setup()
    numRounds = int(input("How many rounds would you like to play?"))

    for i in range(numRounds):
        for j in range(len(players)):
            players[j].setIsAsker(True)
            players[(j+1)% len(players)].setIsAnswerer(True)
            asker = players[j]
            answerer = players[(j+1)% len(players)]

            #getting the question, getting the answerer to submit a player number
            print("Player " + str(asker.id) + " is asking a question to " + "Player " + str(answerer.id))
            question = asker.submitQuestion()
            print("Player " + str(answerer.id) + " is choosing a person")
            chosenPlayerNum = answerer.submitAnswer(question)
            validInput = False

            #bounce back this question if user didn't input valid range or inputted answerer / asker
            
            while not(validInput):
                try:
                    if int(chosenPlayerNum) not in range(1, len(players) + 1):
                        print("Please select a player number between 1 and " + str(len(players)))
                        chosenPlayerNum = answerer.submitAnswer(question)
                    elif int(chosenPlayerNum) == asker.id or int(chosenPlayerNum) == answerer.id:
                        print("You cannot select yourself or the asker")
                        chosenPlayerNum = answerer.submitAnswer(question)
                    else: validInput = True
                except:
                    print("Please enter the player number")
                    chosenPlayerNum = answerer.submitAnswer(question)
            
            players[int(chosenPlayerNum) - 1].setIsSelected(True)
            selected = players[int(chosenPlayerNum) - 1]

            print("Player " + str(selected.id) + " was chosen.")

            #rock paper scissors
            pairplay = ['','']
            pairplay = [answerer.getRPS(), selected.getRPS()]

            while (pairplay[0]==pairplay[1]):
                print("Tie! Please try again")
                pairplay = [answerer.getRPS(), selected.getRPS()]

            if (whoWins(pairplay)):
                print("Player " + str(selected.id) + " won! The question was: " + question)
            else: print("Player " + str(answerer.id) + " won! No question displayed.")
            

def makeNameArray():
    nameArray = [ ]
    for i in players:
        nameArray.append(i.getName())
    return nameArray

def randomize(): #possibly code later
    pass

def getPair(): #returns list, list[0] = answerer, list[1] = selected
    Pair = ['',''] 
for player in players:
        if (player.getIsAnswerer()):
            Pair[0] = player
        if(player.getIsSelected()):
            Pair[1] = player
        
def whoWins(pairplay): #pairplay is like [rock, scissors], guaranteed diff answer. return False if first wins
    '''
    Given a list with two Player “Rock Paper Scissor” attributes, in order Answerer and Selected, return a boolean determining whether or not to display the question. aka return False if the Answerer (aka pairplay[0]) wins.
    '''
    if pairplay[0]=="rock":
        if (pairplay[1]=="scissors"):
            return False
        else: return True

    if pairplay[0]=="paper":
        if (pairplay[1]=="rock"):
            return False
        else: return True

    if (pairplay[0] == "scissors"):
        if (pairplay[1] == "paper"):
            return False
        else: return True

if __name__ == '__main__':
    main()