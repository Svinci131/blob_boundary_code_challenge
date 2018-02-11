# Boundary Challenge

A Blob is a shape in two-dimensional integer coordinate space where all cells have at least one adjoining cell to the right, left, top, or bottom that is also occupied.

## Table of Contents
1. ##### Problem Statement
2. ##### Assumptions
3. ##### Approach
4. ##### Develop
5. ##### Test

## Problem Statement

Given a 10x10 array of boolean values that represents a Blob uniformly selected at random from the set of all possible Blobs that could occupy that array, write a program that will determine the Blob boundaries. Optimize for finding the correct result, performing a minimum number of cell Boolean value reads, and elegance and clarity of the solution.
 
### Sample input: 
_(Please view in a monospaced font)_

```
0000000000
0011100000
0011111000
0010001000
0011111000
0000101000
0000101000
0000111000
0000000000
0000000000
```

### Sample output:

```bash
Cell Reads: 44
Top: 1
Left: 2
Bottom: 7
Right: 6
```

## Assumptions

1. The input will always be a valid 10X10 array.
2. The grid will always contain blob.
3. Cell count starts after top edge is detected.

# Approach

Loop through the rows until you find the top of the blob O(n^2).
Starting from that cell keep checking all the adjacent cells until you reach a 0.

As you are traversing the grid keep check if this is the furthest (Right, Left, Down) you're been and update the boundaries if that's the case.

# Develop

```bash
cd [into_project]
virtualenv -p python3 .venv
source .venv/bin/activate
make
```

# Test

After the steps above: 
_(note: running `make` will also run the tests)_

```bash
make test
```
