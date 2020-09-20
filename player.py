class Player:
    #class variable
    count = 0
    
    def __init__(self, name = '', isAsker = False, isAnswerer = False, isSelected = False):
        self.name = name
        self.isAsker = isAsker
        self.isAnswerer = isAnswerer
        self.isSelected = isSelected
        Player.count += 1
        self.id = Player.count
        self.screen = 
    
    def getRPS(self):
        cheese = ""
        cheese = input("Choose your fate…enter rock, paper, or scissors.")    
        while (not (cheese == "rock" or cheese == "paper" or cheese == "scissors")):
            print("Player "+ str(self.id) + " invalid input. Please try again")
            cheese = input("Choose your fate…enter rock, paper, or scissors.")    
        return cheese
        
    def reset(self):
        isAsker, isAnswerer, isSelected = False, False, False
        
    def submitQuestion(self):
        return input("Whisper a question to the next player.")
        
    def submitAnswer(self, question):
        return input(question + '\n' + "Please pick a player number.") #returns string
        
    def getName(self):
        return self.name

    def getIsAsker(self):
        return self.isAsker
        
    def getIsAnswerer(self):
        return self.isAnswerer
        
    def getIsSelected(self):
        return self.isSelected
        
    def setIsAsker(self, boo):
        self.isAsker = boo
        
    def setIsAnswerer(self, boo):
        self.isAnswerer = boo
        
    def setIsSelected(self, boo):
        self.isSelected = boo
    
    def setName(self, cheese):
        self.name = cheese