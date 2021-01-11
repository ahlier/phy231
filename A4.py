import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

# Q1
k = np.arange(6)
n = 50
p = 0.005
# make n*p to be less than 0.5

binomial = sp.binom.pmf(k, n, p)
poisson = sp.poisson.pmf(k, n*p)
plt.plot(k, poisson, label='Poisson Distribution', linewidth=4)
plt.plot(k, binomial, label='Binomial Distribution')
plt.xlabel('Number of Event')
plt.ylabel('Probability')
plt.title('Comparision between poisson and binomial distribution with \n'
          'small n*p value')
plt.legend()
plt.show()

n = 60  # For Gaussian-looking binomial distribution, use large n
k = np.arange(60)
# make k value matches n value, otherwise the range of plot is not showing correctly
p = 0.5

binomial2 = sp.binom.pmf(k, n, p)
plt.plot(k, binomial2, label='Binomial Distribution')
plt.title('Binomial distribution with large n value')
plt.xlabel('Number of Event')
plt.ylabel('Probability')
plt.legend()
plt.show()


# Q2
def two_D_array(n , m):
    # this function return a nxm 2D array
    return np.random.uniform(0, 1, (n, m))

fig, [p1, p2, p3] = plt.subplots(nrows=1, ncols=3)

small_sum = np.sum(two_D_array(100, 10), axis=0)
# axis=0 means summing the column
p1.hist(small_sum)

median_sum = np.sum(two_D_array(100, 200), axis=0)
p2.hist(median_sum)

large_sum = np.sum(two_D_array(100, 1000), axis=0)
p3.hist(large_sum)

p2.set_title('Central Limit Theorem With Small, Median and Large \n'
          'Number of Column')

plt.show()
# the subplot ranging from left to right are plot with small, median and large
# number of random value.




# Q3
total = 10000

def monte_carlo(total):
    count = 0
    for i in range(total):
        if np.random.random() ** 2 + np.random.random() ** 2 < 1:
            # x^2 + y^2 < 1, this is happening in a square with side length of 2
            # this if statement checks if the random point generated on this
            # square is also on the circle with radius of 1.
            count += 1
    return count

inside = monte_carlo(total)
pi = inside/total*4
# the area radio between circle and square is pi*r^2/4*r^2

print('the estimation made using Monte Carlo method is {} using {} trial'
      .format(pi, total))
