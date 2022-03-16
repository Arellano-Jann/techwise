COMPILER = python3
FLAGS = 
FILES = zoombot.py
DIR = zoombot

all: main

main: $(DIR)/$(FILES)
	$(COMPILER) $(FLAGS) $^

clean:
	rm -rf __pycache__

.PHONY: clean all