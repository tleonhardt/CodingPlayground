# Test for zlog logging library
t_zlog: t_zlog.o
	g++ -o t_zlog t_zlog.o -lzlog

t_zlog.o: t_zlog.cpp
	g++ -g3 -Wall -W t_zlog.cpp -c
clean:
	rm t_zlog.o t_zlog
