CC = gcc
TARGET = run

run: main.o hex_to_base64.o
	$(CC) main.o hex_to_base64.o -o run

main.o: main.c modules.h
	$(CC) -c main.c

hex_to_base64.o: hex_to_base64.c modules.h
	$(CC) -c hex_to_base64.c

clean:
	$(RM) $(TARGET) *.o
