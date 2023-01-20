how to compile:

gcc -c -fPIC example.c -o example.o

gcc example.o -shared -o example.so


or for the array case:


gcc -c -fPIC array_example.c -o array_example.o

gcc array_example.o -shared -o array_example.so


for the rust example:

rustc --crate-type cdylib -o cfile.so cfile.rs
 
