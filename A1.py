import math
import matplotlib.pyplot as plt

def P(k, n, p):
    return math.factorial(n)*p**k*(1-p)**(n-k)/\
           (math.factorial(k)*math.factorial(n-k))

# Q1
'''
Question 1 asks the probability of getting 1 and 9 heads in 10 coin flips 
with a fair coin and the probability of getting 5 heads in 10 coin flips with 
the probability of getting heads is 30% 
'''
print('The probability of getting 1 heads in 10 flips with a fair coin is', P(1, 10, 0.5))
print('The probability of getting 9 heads in 10 flips with a fair coin is', P(9, 10, 0.5))
print('The probability of getting 5 heads in 10 flips with an unfair coin is', P(5, 10, 0.3))


# Q2
'''
Question 2 asks us to build a function to ask user to input the number of event,
number of trial and the probability of getting the event. Then output the 
probability of such scenario
'''
# k = int(input('input value of k (number of event)'))
# n = int(input('input value of n (number of trial)'))
# p = float(input('input value of p (the probability of getting the event)'))
# print(P(k, n, p))


# Q3
'''
Question 3 asks us to plot a graph of probability of getting head ranging from 0
to 10 with a fair coin, and plot a graph of probability of getting head ranging 
from 0 to 10 with an unfair coin of 30% getting head. 
 
'''
p_unfair = [P(i, 10, 0.3) for i in range(11)]
p_fair = [P(i, 10, 0.5) for i in range(11)]

unfair_distribution = plt.plot(range(11), p_unfair, label='Unfair Coint')
unfair_dot = plt.plot(range(11), p_unfair, 'o', color='black')
fair_distribtuion = plt.plot(range(11), p_fair, label='Fair Coin')
fair_dot = plt.plot(range(11), p_fair, 'o', color='black')

plt.xlabel('Number of Head')
plt.ylabel('Probability')
plt.title('The Probability Distribution of Getting Heads in 10 Coin Flips\n'
          'Using a Fair and an Unfair Coin')

plt.legend()
plt.show()

def p(a):
    return a
