# Makefile builds each xxx.cc file to xxx executable binary.

SRCS = $(wildcard *.cc )
OBJS = $(foreach src, $(SRCS), $(basename $(src)).o )
TARGETS = $(foreach src, $(SRCS), $(basename $(src)) )

CXX=g++
CXXFLAGS += -pipe -Wall -g -std=gnu++11 -fno-exceptions -Wno-sign-compare -O2

LDFLAGS += -lm -lrt -lpthread 

.PHONY : all clean

all : $(TARGETS)

$(TARGETS) : % : %.o 
	$(CXX) $(CXXFLAGS) -o $@ $< $(LDFLAGS)

clean:
	@rm -f $(TARGETS) $(OBJS)

##################################

.SUFFIXES : .cc
.cc.o :
	    $(CXX) $(CXXFLAGS) -c -o $@ $<
