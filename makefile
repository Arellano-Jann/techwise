COMPILER = python3
FLAGS = 
FILES = 1.py
DIR = assignment02

all: main

main: $(DIR)/$(FILES)
	$(COMPILER) $(FLAGS) $^

clean:
	rm -rf __pycache__

.PHONY: clean all