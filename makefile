COMPILER = python3
FLAGS = 
FILES = 1.py
DIR = assignment05
# FILES = zoombot.py
# DIR = zoombot

all: main

main: $(DIR)/$(FILES)
	$(COMPILER) $(FLAGS) $^

clean:
	rm -rf $(DIR)/__pycache__

.PHONY: clean all