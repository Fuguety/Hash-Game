from random import randint

class Game():

    x = "x"
    o = "o"
    player = False
    computer = False
    
    def __init__(self):
        
        pos = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        running = True
    
        print("Welcome to the game \n\n")
        
        while True:
            print("\nWould you like to play as X or O?\n x -- 1 \n o -- 0\n")

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



        while running:

            print(f"\n{pos[0]}|{pos[1]}|{pos[2]} \n_____\n{pos[3]}|{pos[4]}|{pos[5]}\n______\n{pos[6]}|{pos[7]}|{pos[8]}\n")


            print("r - restart\nq - quit\nChoose the position you wish to insert:")


            getPos = input()

            if getPos == "q":
                running = False

            elif getPos == "r":
                pos = [0, 1, 2, 3, 4, 5, 6, 7, 8] 

            else:
                self.validAnswer(getPos, pos)

                # check win condition
                if pos[0] == pos[1] == pos[2] or pos[0] == pos[4] == pos[8] or pos[0] == pos[3] == pos[6] or pos[3] == pos[4] == pos [5] or pos[6] == pos[7] == pos[8] or pos[2] == pos[4] == pos[6] or pos[1] == pos[4] == pos[7] or pos[2] == pos[5] == pos[8]:
            
                    print(f"\n{pos[0]}|{pos[1]}|{pos[2]} \n_____\n{pos[3]}|{pos[4]}|{pos[5]}\n______\n{pos[6]}|{pos[7]}|{pos[8]}\n")
                    print("Game ended")
                    break

    

    def validAnswer(self, getPos, pos):

        try:
            getPos = int(getPos)

            if pos[getPos]== self.computer:
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

    

Game()
