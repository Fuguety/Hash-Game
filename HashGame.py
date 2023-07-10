from random import randint

class Game():

    x = "x"
    o = "o"
    player = False
    computer = False
    
    def __init__(self):
        
        pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        running = True
    
        print("Welcome to the game \n\n")

        # Who's playing
        while True:
            print("\nHow would you like to play? \nPlayer x Computer -- 1\nPlayer x Player -- 2\n")
            try:

                playerChoice = int(input())
                
                if playerChoice == 1:
                    break
                elif playerChoice == 2:
                    break
                else:
                    print("Please choose a valid option")

            except:
                print("Please insert a number")
        
        # Choose x or o
        while True:
            print("\nWould you like to play as X or O?\n x -- 1 \n o -- 0\n")

            if playerChoice == 2:
                print("Player 2 will recieve the remaining option\n")

            try:
                pp = int(input())


                print("\n")
    
                if  pp == 1:
                    self.player = self.x
                    self.computer = self.o
                    break

                elif pp == 0:
                    self.player = self.o
                    self.computer = self.x
                    break
                else:
                    print("\nPlease insert a valid option\n")
            except:
                print("\nPlease choose a valid option\n")


        # Main Game
        while running:

            print(f"\n{pos[0]}|{pos[1]}|{pos[2]} \n_____\n{pos[3]}|{pos[4]}|{pos[5]}\n______\n{pos[6]}|{pos[7]}|{pos[8]}\n")


            print("r - restart\nq - quit\n\nChoose the position you wish to insert:\n")


            getPos = input()

            if getPos == "q":
                running = False

            elif getPos == "r":
                pos = [1, 2,  3, 4, 5, 6, 7, 8, 9] 

            else:
                self.validAnswer(getPos, pos, playerChoice)

                # check win condition
                if pos[0] == pos[1] == pos[2] or pos[0] == pos[4] == pos[8] or pos[0] == pos[3] == pos[6] or pos[3] == pos[4] == pos [5] or pos[6] == pos[7] == pos[8] or pos[2] == pos[4] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8]:
            
                    print(f"\n{pos[0]}|{pos[1]}|{pos[2]} \n_____\n{pos[3]}|{pos[4]}|{pos[5]}\n______\n{pos[6]}|{pos[7]}|{pos[8]}\n")
                    print("Game ended")
                    break

    

    def validAnswer(self, getPos, pos, playerChoice):


        if playerChoice == 1:
    
            try:
    
                getPos = int(getPos)
                getPos = getPos - 1

                if pos[getPos]== self.computer or pos[getPos] == self.player:
                    print("\nPlease choose a position that has not been occupied!\n")

                else:
    
                    pos[getPos] = self.player

                    while True:
                
                        inList = randint(0, 8)

                        if inList in pos:
                            pos[inList] = self.computer
                            break
        
                        else:
                            continue

            except:
                
                    print("\nPlease insert a valuable postition\n")
    




        elif playerChoice == 2:
        
            try:
                getPos = int(getPos)
                getPos -= 1

                if pos[getPos] == self.computer or pos[getPos] == self.player:
                    print("\nPlease choose a position that has not been occupied!\n")

                else:
                    pos[getPos] = self.player
    
    

                    while True:
                    
                        try:
                            print(f"\n{pos[0]}|{pos[1]}|{pos[2]} \n_____\n{pos[3]}|{pos[4]}|{pos[5]}\n______\n{pos[6]}|{pos[7]}|{pos[8]}\n")
                        
                            print("\nPlease choose a place:\n")
                            playerTwo = int(input())
                            playerTwo -= 1

                            if pos[playerTwo] == self.computer or pos[playerTwo] == self.player:
                        
                                print("\nPlease choose a position that has not been occupied!\n")

                            else:
                                pos[playerTwo] = self.computer
                                break
                        except:
                            print("Please insert a valid number")


            except:
                print("\nPlease insert a valuable postition\n")

    

Game()
