CC = gcc
TARGET = run

run: main.o hex_to_base64.o fixed_xor.o
	$(CC) main.o hex_to_base64.o fixed_xor.o -o run

main.o: main.c modules.h
	$(CC) -c main.c

hex_to_base64.o: hex_to_base64.c modules.h
	$(CC) -c hex_to_base64.c

fixed_xor.o: fixed_xor.c modules.h
	$(CC) -c fixed_xor.c

clean:
	$(RM) $(TARGET) *.o run
