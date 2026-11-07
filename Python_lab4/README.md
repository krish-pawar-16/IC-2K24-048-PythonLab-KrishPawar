\# Python Lab: Naive vs. Optimized Algorithms



\## Aim

To solve different problems using simple and optimized algorithms and compare their execution times.



\## Introduction

In this lab, I explored how different ways of solving a problem affect program performance. Each problem is first solved using a simple method and then using an optimized method. The execution time of each method is also measured using Python's `time` module.



\## Section B – Sum of All Prime Numbers Below N



\### Aim

To find the sum of all prime numbers smaller than a given number N.



\### Methods

1\. Naive Approach: Checks every possible divisor of each number.

2\. Square Root Approach: Checks divisors only up to the square root of the number.

3\. Sieve of Eratosthenes: Marks multiples of prime numbers as non-prime.



\### Sample Output

```text

10 17 PASS

30 129 PASS

100 1060 PASS

1000 76127 PASS

```



\### Performance Results



\*\*Naive Approach\*\*

```text

N = 50000, sum = 121013308, time = 7.8397 s

N = 100000, sum = 454396537, time = 29.7040 s

```



\*\*Square Root Approach\*\*

```text

N = 2000000, sum = 142913828922, time = 9.0601 s

```



\*\*Sieve of Eratosthenes\*\*

```text

N = 2000000, sum = 142913828922, time = 0.2509 s

```



\## Section C – Count Pairs With a Given Sum



\### Aim

To count the number of pairs in a list whose sum is equal to a given target value.



\### Methods

1\. Naive Approach: Uses two loops to check every possible pair.

2\. Optimized Approach: Uses a dictionary to find the required number.



\### Performance Results



\*\*Naive Approach\*\*

```text

N = 5000, pairs found = 604, time = 0.7824 s

N = 50000, pairs found = 62769, time = 76.2584 s

```



\*\*Optimized Approach\*\*

```text

N = 50000, pairs found = 62769, time = 0.0213 s

```



\## Section D – K-th Smallest Pairwise Sum



\### Aim

To find the K-th smallest sum formed by adding two different elements of a list.



\### Methods

1\. Naive Approach: Creates all possible pair sums and sorts them.

2\. Optimized Approach: Uses sorting, two pointers and binary search.



\### Performance Results



\*\*Naive Approach\*\*

```text

N = 5000, K = 1000000, result = 41514, time = 8.9936 s

```



\*\*Optimized Approach\*\*

```text

N = 5000, K = 1000000, result = 41514, time = 0.0127 s

```



\## Overall Takeaway

From these three problems, I understood that choosing a better algorithm can make a program much faster. The naive methods are easy to understand but take more time for large inputs. The optimized methods reduce repeated work by using techniques like the Sieve of Eratosthenes, dictionaries, two pointers and binary search.



\## Conclusion

Thus, all three problems were solved using naive and optimized approaches. Their outputs and execution times were compared to understand the importance of algorithm efficiency.



\*\*Note:\*\* Execution times may change depending on the computer and Python environment.

