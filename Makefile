CC = g++
CFLAGS = -Wall -Wextra -pedantic -std=c++11
SRCS = HashGame.cpp
TARGET = HashGame

all: $(SRCS)
	$(CC) $(CFLAGS) $< -o $(TARGET)

clean:
	rm -f $(TARGET)
	

