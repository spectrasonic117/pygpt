PREFIX ?= /usr
OPTDIR ?= /opt

BINDIR = $(PREFIX)/bin
DATDIR = $(OPTDIR)/openai


all: build install

# sudo make build
build:
	termux-fix-shebang PyGPT.py
	termux-fix-shebang pygpt

# sudo make install
install:
	python3 -m pip install -r ./requirements.txt
	mkdir -p $(DATDIR)
	install -Dm755 -t $(BINDIR) ./pygpt
	install -Dm755 -t $(DATDIR) ./PyGPT.py

# sudo make uninstall
uninstall:
	rm $(BINDIR)/openai
	rm -r $(DATDIR)

.PHONY: all build install uninstall