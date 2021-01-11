import numpy as np
import matplotlib.pyplot as plt

# Q1
def ran_num_gen(n):
    '''
    :param n: number of random number generated from 0 to 1
    :return: n random number generated from 0 to 1
    '''
    ran_array = np.random.rand(n)  # generate n random numbers
    plt.hist(ran_array, rwidth=0.9)
    plt.xlabel('Generated Number')
    plt.ylabel('Frequency')
    plt.title('Frequency of getting random numbers ranging from 0 to 1\n'
              'using np.random.rand() method')
    plt.show()
    return ran_array
ran_num_gen(100)
ran_num_gen(1000)


# Q2
n = 100
p = 0.4
result2 = []

for i in range(n):
    if np.random.rand(1) < p:
        result2.append(0)
    else:
        result2.append(1)
print(result2)


# Q3
def coin_flip(n, p):
    '''
    :param n: number of toss
    :param p: probability of getting tails
    :return: a list of '1' and '0', which representing heads and tails
    '''
    result = []
    for i in range(n):
        if np.random.rand(1) < p:
            result.append(0)
        else:
            result.append(1)
    return result


# Q4
# To show the actual slipping of the cell will get closer to 50-50 as N gets larger

N = 1000
deviation_percentage = []
for i in range(1, N+1):
    cell_one = np.array(coin_flip(i, 0.5))
    deviation_percentage.append(1/2-((np.count_nonzero(cell_one == 1)))/i)
    # deviation_percentage is theoretical probability - (number of protein goes to cell one/total number of protein)
plt.plot(np.arange(1, N+1), deviation_percentage)
plt.plot(np.arange(1, N+1), np.zeros(N))
plt.xlabel('Number of protein')
plt.ylabel('Percent deviation from theoretical value')
plt.title('Change in percent deviation for cell division as \n'
          'number of protein increases')
plt.show()
# the graph converts to 0, therefore the percentage of protein goes to cell one
# approaches 1/2 as number of proteins increases




















