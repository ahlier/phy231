import numpy as np
import matplotlib.pyplot as plt

# Q1
def F(n, p, d):
    '''
    This function will create a random walk situation in 1-D world
    :param n: How many steps did the cell take
    :param p: The probability of taking a right step
    :param d: The distance of each step
    :return: A 1xn matrix, with each element being the position of cell
    '''

    count = 0
    a = [0]
    while count < n:
        # this while-loop goes through each step
        if np.random.rand(1) < p:
            a.append(a[-1] + d)  # adding one step based on the previous position
        else:
            a.append(a[-1] - d)
        count += 1
    return np.array(a[1:])  # this matrix excludes the initial position, which is 0.




# Q2
def random_walk(n, p, d):
    '''
    This function will do the same thing as function F, but using numpy array
    functions instead. Inputs and outputs are the same as previous one
    '''
    random_matrix = np.random.uniform(size=n)
    # This creates a 1xn matrix with random float ranging from 0 to 1

    ran_walk_matrix = (((random_matrix > p).astype('int')) - 0.5) * 2 * d
    # (random_matrix > p) will creates a 1-D matrix consists of True/False,
    # astype('int') will convert True/False into 1 and 0
    # ran_walk_matrix is a matrix consists of d and -d

    result = np.cumsum(ran_walk_matrix)
    # result is a matrix which each element indicates the position of the cell
    return result


# Q3
trail = 100
step = 100
p = 0.5
d = 1  # assume the cell moves 1 unit per second

all_trial = random_walk(step, p, d) # this stores data for all trial
_ = plt.plot(all_trial) # this plots the random walk for the first trial
for i in range(trail-1):
    # one trial is plotted before for-loop, so trail-1 is needed to be plotted
    a = random_walk(step, p, d)
    _ = plt.plot(a)
    all_trial = np.vstack((all_trial, a))

aver_position = np.mean(all_trial**2, axis=0)
# Calculate the average mean square distance for all trials.

plt.xlabel('time (s)')
plt.ylabel('position (x)')
plt.title('Random walk for 100 trails of 100 steps')

plt.show()

_ = plt.plot(aver_position)
plt.xlabel('time (s)')
plt.ylabel('mean square distance (<x^2>)')
plt.title('average of mean square distance of 100 trials')
plt.show()


# Q4

np.savetxt('data.txt', all_trial)  # using all_trail from Q3
