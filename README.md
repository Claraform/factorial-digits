# Factorial-Digits 

Clara Esther Stassen

A script developed for Corigine Inc. to compute the factorial of an input 
integer and sum the digitals of the result. The script is packaged and 
executable as a Docker container.

I. File Structure
------------------
src/ - Folder containing source code

src/factorial-digits.py - python script responsible for computation

Dockerfile - file to build Docker image

requirements.txt - lists dependencies

README.md - this file

III. How To Run
----------------
- To build docker image:

    $ docker build -t factorial-digits .
    
- To run:

   $ docker run --rm factorial-digits $1

IV. Arguments
--------------
1. $1  -  Integer to compute factorial and digital sum on


V. Outputs
--------------
1. result    -    Integer result printed to terminal

