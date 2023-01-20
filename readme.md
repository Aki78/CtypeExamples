how to compile:

gcc -c -fPIC plus.c -o plus.o

gcc plus.o -shared -o plus.so
