PREFIX ?= /usr
OPTDIR ?= /opt

BINDIR = $(PREFIX)/bin
DATDIR = $(OPTDIR)/openai

all: build install

build:
	termux-fix-shebang PyGPT.py
	termux-fix-shebang pygpt

install:
	mkdir -p $(DATDIR)
	install -Dm755 -t $(BINDIR) ./pygpt
	install -Dm755 -t $(DATDIR) ./PyGPT.py

uninstall:
	rm $(BINDIR)/openai
	rm -r $(DATDIR)

.PHONY: all build install uninstall