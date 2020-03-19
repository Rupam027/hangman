
class hangman :

    '''HANGMAN  v0.0.1
       Developed By Devops Foundation '''
    
    
    def __init__(self,name1,name2,word) :
        self.name =  name1
        self.opponent = name2 
        self.word =  word
        self.guess = ['_' for x in range(len(word))]


    def start(self):

        word = self.word
        level = 0 
        word_guess = self.guess
        print(f"{opponent} , {name} has set the word\n")
        for i in word_guess :
            print(i , end = ' ')
        print('\n')

        man = ['|' , '--' , 'O' , '--' , '<' , '--<' ]
               
               
               
        
        
        


        while  ''.join(word_guess) != word  :
            choice = input('Enter  g  if you got the word or press any other character -> ')
            print()
            
            if choice == 'g' :
                self.guess_word()
                break 
                
            else :
                letter = input('Guess Letter -> ').upper()
                if (letter in word) and (letter not in word_guess) :
                    
                    for x in range(len(word)) :
                        if word[x] == letter :
                            word_guess[x] = letter


                    for x in word_guess :
                        print(x , end = " ")
                    print()

                elif letter in word_guess :
                    print(f"you have already filled the letter {letter} wherever possible")

                else :
                    level+=1
                    print(f"WRONG GUESS. HANG LEVEL : {level}\n")
                    for i in man[:level:] :
                        print(i , end= '')
                    print("\n")
                    
                    
                    if level == 6:
                        print("GAME OVER")
                        break

                self.guess = ''.join(word_guess)

    def guess_word(self) :
        wd = input('Enter word -> ').upper()
        if wd == self.word :
            self.guess = wd
        else :
            self.guess = wd
            print('Oops ! You guessed it wrong. You lost all your chances')
            for i in man[:level:] :
                print(i , end= '')
            print("\n")
            
            print("Game Over")
            
        
        
        

    def result(self) :
        print("YOUR GUESS -> ", self.guess ,"\n")
        print("ORIGINAL WORD -> ",self.word ,"\n")

        if self.guess == self.word :
            print(f"CONGRATS {self.opponent}! YOU ARE THE WINNER")
        else :
            print("LOST")

    def __del__(self) : 
        print("\nBye ! Have a Nice Day\n")
	
		
        
import getpass

print('HANGMAN    v0.0.1\nDeveloped By Devops Foundation\n')

name = input('Enter word setter name -> ').upper()
opponent = input('Enter opponent name -> ').upper()

word = getpass.getpass('Set word -> ').upper()


obj = hangman(name ,opponent , word)


input("\n PRESS ENTER TO START\n")
obj.start()
obj.result()
input("Press Enter to Quit")







    





    

