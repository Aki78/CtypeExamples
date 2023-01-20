how to compile:

gcc -c -fPIC example.c -o example.o

gcc example.o -shared -o example.so


or for the array case:


gcc -c -fPIC array_example.c -o array_example.o

gcc array_example.o -shared -o array_example.so


for the rust example:

rustc --crate-type cdylib -o array_example.so array_example.rs
 
or in Haskell

 ghc -shared -o array_example.so array_example.hs

