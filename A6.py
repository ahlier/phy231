import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('Keller1986interpolated.xls', header = 0, index_col=None)
# header = 0 is to make the program start reading from the first line,
# index_col = None is to remove to index label for column
header = list(data)


def plot_withhist(x, y, title, threshold):
    fig, [ax1, ax2] = plt.subplots(figsize=(15, 4), nrows=1, ncols=2)
    # This will create a subplot with 1 rwo 2 columns

    ax1.set(xlabel='time(ms)', ylabel='current(pA)', title=title)
    ax1.plot(x, y)
    ax1.axhline(y=threshold*0.75, color='g', label='25% From Threshold')
    ax1.axhline(y=threshold, color='b', label='Threshold')
    ax1.axhline(y=threshold * 1.25, color='g')
    # This creates 3 horizontal lines showing where the threshold is, and 75% and 125% of the threshold
    ax1.legend(loc='lower right')

    ax2.set(xlabel='count', ylabel='current(pA)')
    ax2.hist(y, bins=30, orientation='horizontal')  # This plots the data as a histogram
    ax2.axhline(y=threshold, color='b', label='Threshold')
    ax2.legend(loc='lower right')


def calc_prob(data, threshold):
    Tclosed = sum(data>threshold)  # count number of being close
    Topen = sum(data<=threshold)   # count number of being open
    p_open = Topen/(Topen+Tclosed)  # The probability of being open
    return p_open


threshold = [-1.8, -1.4, -1.4, -1.25, -1.1, -1, -0.85, -0.7, -0.5]
# These threshold are the mean of max and min values of current for each data set
voltage = np.arange(-135, -54, 10)  # this will create a list ranging from -135 and -54 with interval of 10
popenl = []
popenbig = []
popensm = []
for i in range(len(header)-1):
    # Time is in header, but it is not taking into account, so -1
    plot_withhist(data.iloc[:, 0], data.iloc[:, i+1], str(header[i+1]), threshold[i])
    # plot_withhist takes in the data.iloc[:, 0], first column of data set, which is time
    # It also takes in data.iloc[:, i+1], column of current
    # str(header[i+1]) will pass the title of each column as title of the graph
    # threshold[i] is the mean of max/min values
    plt.show()

    print('the probability of being open with threshold {} is {}'
          .format(threshold[i], calc_prob(data.iloc[:,i+1], threshold[i])))
    '''
    This will print:
    the probability of being open with threshold -1.8 is 0.010529743812418585
    the probability of being open with threshold -1.4 is 0.04087060356057316
    the probability of being open with threshold -1.4 is 0.07289405123751629
    the probability of being open with threshold -1.25 is 0.2629179331306991
    the probability of being open with threshold -1.1 is 0.4995115067303517
    the probability of being open with threshold -1 is 0.7890794615718628
    the probability of being open with threshold -0.85 is 0.8265848892748588
    the probability of being open with threshold -0.7 is 0.8133955709943552
    the probability of being open with threshold -0.5 is 0.9735128093790708
    '''

    print('the probability of being open with 125% of threshold {} is {}'
          .format(threshold[i]*1.25, calc_prob(data.iloc[:, i + 1], threshold[i]*1.25)))
    '''
    the probability of being open with 125% of threshold -2.25 is 0.008304385584020843
    the probability of being open with 125% of threshold -1.75 is 0.032837603126356925
    the probability of being open with 125% of threshold -1.75 is 0.051291793313069906
    the probability of being open with 125% of threshold -1.5625 is 0.2217216673903604
    the probability of being open with 125% of threshold -1.375 is 0.44577724706904037
    the probability of being open with 125% of threshold -1.25 is 0.7255210594876248
    the probability of being open with 125% of threshold -1.0625 is 0.7857685627442467
    the probability of being open with 125% of threshold -0.875 is 0.7869083803734259
    the probability of being open with 125% of threshold -0.625 is 0.9532132001736865
    '''

    print('the probability of being open with 75% of threshold {} is {}'
          .format(threshold[i] * 0.75,
                  calc_prob(data.iloc[:, i + 1], threshold[i] * 0.75)))

    '''
    the probability of being open with 75% of threshold -1.35 is 0.012592270950933565
    the probability of being open with 75% of threshold -1.0499999999999998 is 0.044941380807642206
    the probability of being open with 75% of threshold -1.0499999999999998 is 0.08309813287016934
    the probability of being open with 75% of threshold -0.9375 is 0.3052540165002171
    the probability of being open with 75% of threshold -0.8250000000000001 is 0.576476335214937
    the probability of being open with 75% of threshold -0.75 is 0.8404798089448545
    the probability of being open with 75% of threshold -0.6375 is 0.8622448979591837
    the probability of being open with 75% of threshold -0.5249999999999999 is 0.8400455927051672
    the probability of being open with 75% of threshold -0.375 is 0.9803517151541468
    '''



    popensm.append(calc_prob(data.iloc[:, i+1], threshold[i]*0.75))
    popenl.append(calc_prob(data.iloc[:, i + 1], threshold[i] ))
    popenbig.append(calc_prob(data.iloc[:, i + 1], threshold[i] * 1.25))
    # These three lists are the probability of 75%, 100% and 125% of threshold
    # being open for different voltages


plt.plot(voltage, popenl, '-ob', label='100% of threshold')
plt.plot(voltage, popenbig, '--og', label='125% of threshold')
plt.plot(voltage, popensm, '--og', label='75% of threshold')
plt.xlabel('Voltage (mV)')
plt.ylabel('Probability')
plt.title('Change in Probability of Threshold Being Open With Change in Voltage')
plt.legend()
plt.show()
# This plots the relation between voltage and probability of threshold being open





