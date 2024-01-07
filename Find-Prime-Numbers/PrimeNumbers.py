#Assignment 2, Question 5
# Created by Natalia Wilson

def findPrime(n):
    #Part A
    primes = [True for i in range(n+1)]
    #Part B
    primeIndex = 2
    while (primeIndex * primeIndex <= n):
        if (primes[primeIndex] == True):
            for i in range(primeIndex * primeIndex, n+1, primeIndex):
                primes[i] = False
                primeIndex += 1
                x = 0
            #Part C
            isPrime = []
            for primeIndex in range(2, n):
                if primes[primeIndex]:
                    isPrime.append(primeIndex)
                    x = x + 1
                if(x == 10):
                    x = 0
            print(isPrime)
findPrime(10000)
