import time
class hangmanword():
    def _init_(self):
        print("WELCOME to Hangman- The word guess game")
        print("Guess the coreect word, or be ready to be hanged!")
        print("(1) START GUESSING \n(2) QUIT, I DON'T WANT TO BE HANGED!")
        user_choice = raw_input("->")
		
        if user_choice == '1':
            print ("Loading The word that can save your life!")
            self.start_game()
        elif user_choice == '2':
            print ("Bye bye now...")
            exit()

    def start_game(self):
        print ("A crowd begins to gather, they are all here to see some fun")
        print ("and judge you on your skills.... All are selfish peeps near you")
        print ("And yes you are in a Risky Situation!!!!")
        print ("All are here to enjoy seeing you hanged.")
        print ("got a chance to outwit others")
        print ("guess the RIGHT WORD and you can live to see another day.\n GOOD LUCK!")
        print ("Starting game...")
        time.sleep(1)
        self.core_game()

    def core_game(self):
        guesses = 0
        letters_used = ""
        the_word = "pizza"
        progress = ['*','*','*','*','*']

        while guesses < 6:
            guess = raw_input("Guess a letter ->")

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
                print ("You already typed this letter")
                print ("Try again!")
            if ''.join(progress) == the_word:
                print ("You Guessed the word:" + the_word)
                print ("You Won")
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
            else:
                i += 1

        return "".join(progress)
game = hangmanword()
		
