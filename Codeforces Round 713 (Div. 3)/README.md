A. Spy Detected!
time limit per test2 seconds
memory limit per test256 megabytes
You are given an array 𝑎
consisting of 𝑛
(𝑛≥3
) positive integers. It is known that in this array, all the numbers except one are the same (for example, in the array [4,11,4,4]
all numbers except one are equal to 4
).

Print the index of the element that does not equal others. The numbers in the array are numbered from one.

Input
The first line contains a single integer 𝑡
(1≤𝑡≤100
). Then 𝑡
test cases follow.

The first line of each test case contains a single integer 𝑛
(3≤𝑛≤100
) — the length of the array 𝑎
.

The second line of each test case contains 𝑛
integers 𝑎1,𝑎2,…,𝑎𝑛
(1≤𝑎𝑖≤100
).

It is guaranteed that all the numbers except one in the 𝑎
array are the same.

Output
For each test case, output a single integer — the index of the element that is not equal to others.

Example
InputCopy
4
4
11 13 11 11
5
1 4 4 4 4
10
3 3 3 3 10 3 3 3 3 3
3
20 20 10
OutputCopy
2
1
5
3
