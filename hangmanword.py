import time
class hangmanword():
    def _init_(self):
        print("WELCOME to Hangman- The word guess game")
        print("Guess the coreect word, or get ready to be hung!")
        print("(1) START GUESSING \n(2) QUIT, I DON'T WANT TO BE HANGED!")
        user_choice = input("->")
		
        if user_choice == '1':
            print ("Loading the word that can save your life!")
            self.start_game()
        elif user_choice == '2':
            print ("Bye, bye now...")
            exit()

    def start_game(self):
        print ("A crowd begins to gather, they are all here to see some fun")
        print ("and judge you on your skills … Rapscallions all!")
        print ("And yes, you are in a Risky Situation!!!!")
        print ("They are all here, to enjoy seeing you hung from the post!")
        print ("You have a chance to outwit the hangman!")
        print ("Guess the RIGHT WORD and you’ll live to see another day.\n GOOD LUCK!")
        print ("Starting game …")
        time.sleep(1)
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = "pizza"
        progress = ['*','*','*','*','*']

        while guesses < 6:
            guess = input("Guess a letter ->")

            if (guess in the_word) and (guess not in letters_used):
                print ("Your guess was RIGHT!")
                letters_used +=  guess +","
                self.hangman_graphic(guesses)
                print ("Progress: " + self.progress_updater(guess, the_word, progress))
                print ("Letter used: " + letters_used)
            elif (guess not in the_word) and (guess not in letters_used):
                guesses += 1
                print ("Wrong Guess!")
                letters_used += guess + ","
                self.hangman_graphic(guesses)
                print ("Progress: " + "".join(progress))
                print ("Letter used: " + letters_used)
            else:
                print ("You’ve already typed this letter")
                print ("Try again!")
            if ''.join(progress) == the_word:
                print ("You guessed the word:" + the_word)
                print ("You won!")
                break
    def hangman_graphic(self, guesses):
        if guesses == 0:
            print ("________      ")
            print ("|      |      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif guesses == 1:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|             ")
            print ("|             ")
            print ("|             ")
        elif guesses == 2:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /       ")
            print ("|             ")
            print ("|             ")
        elif guesses == 3:
           print ("________      ")
           print ("|      |      ")
           print ("|      0      ")
           print ("|     /|      ")
           print ("|             ")
           print ("|             ")
        elif guesses == 4:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|             ")
            print ("|             ")
        elif guesses == 5:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     /       ")
            print ("|             ")
        else:
            print ("________      ")
            print ("|      |      ")
            print ("|      0      ")
            print ("|     /|\     ")
            print ("|     / \     ")
            print ("|             ")
            print ("YOU LOST")
            print ("GAME OVER!")
            self.__init__()
    def progress_updater(self, guess, the_word, progress):
        i = 0
        while i < len(the_word):
            if guess == the_word[i]:
                progress[i] = guess
            i += 1

        return "".join(progress)
game = hangmanword()
		
