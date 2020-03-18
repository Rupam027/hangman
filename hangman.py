
class hangman :

    '''HANGMAN  v0.0.1
       Developed By Devops Foundation '''
    
    
    def __init__(self,name,word) :
        self.name =  name
        self.word =  word
        self.guess = ['_' for x in range(len(word))]


    def start(self):

        word = self.word
        level = 0 
        word_guess = self.guess
        


        while  ''.join(word_guess) != word  :
            letter = input('Guess Letter -> ').upper()
            if (letter in word) and (letter not in word_guess) :
                
                for x in range(len(word)) :
                    if word[x] == letter :
                        word_guess[x] = letter


                for x in word_guess :
                    print(x , end = " ")
                print()

                

            else :
                level+=1
                print(f"WRONG GUESS. HANG LEVEL : {level}")
                if level == 8:
                    print("GAME OVER")
                    break


        self.guess = ''.join(word_guess)

    def result(self) :
        print("YOUR GUESS -> ", self.guess ,"\n")
        print("ORIGINAL WORD -> ",self.word ,"\n")

        if self.guess == self.word :
            print(f"CONGRATS {self.name}! YOU ARE THE WINNER")
        else :
            print("LOST")

    def __del__() :
        print("\nBye ! Have a Nice Day\n")
        


print('HANGMAN    v0.0.1\nDeveloped By Devops Foundation\n')

name = input('Enter player name -> ').upper()
word = input('Set word -> ').upper()

obj = hangman(name , word)

input("\n PRESS ENTER TO START\n")
obj.start()
obj.result()






    





    

