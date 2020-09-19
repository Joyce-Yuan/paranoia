class Player:
	#class variable
	id = 0

	def __init__(self, name = ‘’, isAsker = False, isAnswerer = False, isSelected = False)
        self.name = name
        #avatar = py.file (??)
        self.isAsker = isAsker
        self.isAnswerer = isAnswerer
        self.isSelected = isSelected
        Player.id += 1

	def getRPS():
		cheese = “”
		while (cheese != “rock” or cheese!= “paper” or cheese != “scissors”):
			cheese = input(“Choose your fate…enter rock, paper, or scissors.”)
		return cheese
	
	def reset():
		isAsker, isAnswerer, isSelected = False, False, False

	def submitQuestion():
		return input(“Whisper a question to the next player.”)

	def submitAnswer(question):
		return input(question + “Please pick a player number.”) #returns string

	def getIsAsker(self):
		return self.isAsker
	def getIsAnswerer(self):
		return self.isAnswerer
	def getIsSelected(self):
		return self.isSelected
	def setIsAsker(self, bool):
		self.isAsker = a
	def setIsAnswerer(self, bool):
		self.isAnswerer = a
	def setIsSelected(self, bool):
		self.isSelected = a
	def setName(string cheese):
		self.name = cheese
__________________________________________________________________

players  = [ ]
nameArray = [ ]

def setup():
	numPlayers = int(input(“How many players?”))
	for i in range(numPlayers):
		players.append(new Player())

	for i in players:
		i.setName(input(“Player “ + player.id + “‘s name?”))
		i.reset() //within __main__ for loop

	nameArray = makeNameArray()

def __main__():
	setup()
	numRounds = input(“How many rounds would you like to play?”)

	for i in range(numRounds):
		for j in range(len(players)):
			players[j].setAsker(True)
			players[(j+1)% len(players)].setAnswerer(True)
			asker = players[j]
			answerer = players[(j+1)% len(players)]

			#getting the question, getting the answerer to submit a player number
			question = asker.submitQuestion()
			chosenPlayerNum = 0
			while chosenPlayerNum not in range(1, len(players)):
				chosenPlayerNum = int(answerer.submitAnswer(question))

			players[chosenPlayerNum].setIsSelected(True)

			#for k in players:
				#if (k.getID() == chosenPlayerNum):
					#k.setIsSelected(True)

#rock paper scissors, answerer vs. selected
			while (pairplay[0]==pairplay[1]):
				pairplay = [getPair()[0].getRPS(), getPair()[1].getRPS()]
			if (whoWins(pairplay)):
				print(question)
			else print(“The Answerer won! No question displayed.”)
			

def makeNameArray():
	nameArray = [ ]
	for i in players:
		nameArray.append(i.getName())
	return nameArray

def randomize(): //possibly code later

def getPair(): // returns list, list[0] = answerer, list[1] = selected
	Pair = [ , ] 
for player in players:
		if (player.getIsAnswerer()):
			Pair[0] = player
		if(player.getIsSelected()):
			Pair[1] = player
		
def whoWins(pairplay): // pairplay is like [rock, scissors], guaranteed diff answer. return False if first wins
	‘’’
	Given a list with two Player “Rock Paper Scissor” attributes, in order Answerer and Selected, return a boolean determining whether or not to display the question. aka return False if the Answerer (aka pairplay[0]) wins.
	‘’’
	if (pairplay[0]==”rock”):
		if (pairplay[1]==”scissors”):
			return False
		else return True

	if (pairplay[0]==”paper”):
		if (pairplay[1]==”rock”):
			return False
		else return True

	if (pairplay[0] == “scissors”):
		if (pairplay[1] == “paper”):
			return False
		else return True
