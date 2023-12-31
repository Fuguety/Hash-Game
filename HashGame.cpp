#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

class Game {
    char x = 'x';
    char o = 'o';
    char player;
    char computer;
    
public:
    Game() {
        char pos[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8'};
        bool running = true;
        
        cout << "Welcome to the game" << endl;
        
        // Who's playing
        int playerChoice;
        while (true) {
            cout << "\nHow would you like to play? \nPlayer x Computer -- 1\nPlayer x Player -- 2\n";
            try {
                cin >> playerChoice;
                
                if (playerChoice == 1 || playerChoice == 2) {
                    break;
                } else {
                    cout << "Please choose a valid option\n";
                }
            } catch(...) {
                cout << "Please insert a number\n";
            }
        }
        
        // Choose x or o
        while (true) {
            cout << "\nWould you like to play as X or O?\n x -- 1 \n o -- 0\n";

            if (playerChoice == 2) {
                cout << "Player 2 will receive the remaining option\n";
            }
            
            int pp;
            cin >> pp;
            cout << endl;
            
            if (pp == 1) {
                player = x;
                computer = o;
                break;
            } else if (pp == 0) {
                player = o;
                computer = x;
                break;
            } else {
                cout << "\nPlease insert a valid option\n";
            }
        }
        
        // Game loop
        while (running) {
            cout << pos[0] << "|" << pos[1] << "|" << pos[2] << endl;
            cout << "_____" << endl;
            cout << pos[3] << "|" << pos[4] << "|" << pos[5] << endl;
            cout << "_____" << endl;
            cout << pos[6] << "|" << pos[7] << "|" << pos[8] << endl;
            
            cout << "\nr - restart\nq - quit\nChoose the position you wish to insert: ";
            string getPos;
            cin >> getPos;
            
            if (getPos == "q") {
                running = false;
            } else if (getPos == "r") {
                char resetPos[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8'};
                for (int i = 0; i < 9; i++) {
                    pos[i] = resetPos[i];
                }
            } else {
                validAnswer(getPos, pos, playerChoice);
                
                // check win condition
                if ((pos[0] == pos[1] && pos[1] == pos[2]) ||
                    (pos[0] == pos[4] && pos[4] == pos[8]) ||
                    (pos[0] == pos[3] && pos[3] == pos[6]) ||
                    (pos[3] == pos[4] && pos[4] == pos[5]) ||
                    (pos[6] == pos[7] && pos[7] == pos[8]) ||
                    (pos[2] == pos[4] && pos[4] == pos[6]) ||
                    (pos[1] == pos[4] && pos[4] == pos[7]) ||
                    (pos[2] == pos[5] && pos[5] == pos[8])) {
                    cout << pos[0] << "|" << pos[1] << "|" << pos[2] << endl;
                    cout << "_____" << endl;
                    cout << pos[3] << "|" << pos[4] << "|" << pos[5] << endl;
                    cout << "_____" << endl;
                    cout << pos[6] << "|" << pos[7] << "|" << pos[8] << endl;
                    cout << "Game ended" << endl;
                    break;
                }
            }
        }
    }
    
    void validAnswer(string getPos, char* pos, int playerChoice) {
        try {
            int position = stoi(getPos);
            
            if (pos[position] == computer || pos[position] == player) {
                cout << "\nPlease choose a position that has not been occupied!\n";
            } else {
                pos[position] = player;
                
                if (playerChoice == 2) {
                    while (true) {
                        cout << pos[0] << "|" << pos[1] << "|" << pos[2] << endl;
                        cout << "_____" << endl;
                        cout << pos[3] << "|" << pos[4] << "|" << pos[5] << endl;
                        cout << "_____" << endl;
                        cout << pos[6] << "|" << pos[7] << "|" << pos[8] << endl;
                        
                        cout << "\nPlease choose a place: ";
                        int playerTwo;
                        cin >> playerTwo;
                        
                        if (pos[playerTwo] == computer || pos[playerTwo] == player) {
                            cout << "\nPlease choose a position that has not been occupied!\n";
                        } else {
                            pos[playerTwo] = computer;
                            break;
                        }
                    }
                } else {
                    while (true) {
                        int inList = rand() % 9;
                        
                        if (pos[inList] != 'x' && pos[inList] != 'o') {
                            pos[inList] = computer;
                            break;
                        } else {
                            continue;
                        }
                    }
                }
            }
        } catch (const invalid_argument& e) {
            cout << "\nPlease insert a valid position\n";
        }
    }
};

int main() {
    srand(time(0));
    Game game;
    return 0;
}
