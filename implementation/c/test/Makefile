CC=gcc
OTHERDIR=../src
CFLAGS=-Wall -Wextra -g
CPPFLAGS=-I$(OTHERDIR)
LDFLAGS=
TARGET=demo


all: $(TARGET)

$(TARGET): demo.o $(OTHERDIR)/cpu.c $(OTHERDIR)/cpu.h
	$(CC) -o $@ $^ $(LDFLAGS)

%.o: %.c
	$(CC) -o $@ -c $< $(CFLAGS) $(CPPFLAGS)

clean:
	@rm -f *.o

mrproper: clean
	@rm -f $(TARGET)

.PHONY: clean mrproper
