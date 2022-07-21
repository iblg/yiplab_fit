import pandas as pd
# from scipy.odr import OD
import scipy.odr as odr
#R
import csv
import statistics as st
import matplotlib.pyplot as plt


def f(B,x):
    return B[0] * x + B[1]

def odr_fit(x, y, xerr = None, yerr = None, filepath = None, pprint = False):

    linear = odr.Model(f)

    data = odr.RealData(x, y, xerr, yerr)
    fit = odr.ODR(data, linear, beta0 = [1.,-2.])
    output = fit.run()

    # calculate R^2:

    B0 = output.beta[0]
    B1 = output.beta[1]

    sum_res = 0
    for i in range(len(x)):
        sum_res += (y[i] - (B0 * x[i] + B1))**2

    y_mean = st.mean(y)
    sum_mean = 0
    for i in range(len(x)):
        sum_mean += (y[i] - y_mean)**2

    rsq = 1 - sum_res / sum_mean
    if not filepath is None:
        write_results_to_file(output, rsq, filepath)

    if pprint == True:
        print('Results:\n')
        output.pprint()
        print('\n R**2 is: {:1.5f}'.format(rsq))

    return output


def write_results_to_file(output, rsq, filepath):

    try:
        with open(filepath, 'w') as f:
            f.write('Best fit equation: y = {:2.5f} x + {:2.5f} \n'.format(output.beta[0], output.beta[1]))
            f.write('Slope: {:2.5f} +- {:2.5f} \n'.format(output.beta[0], output.sd_beta[0]))
            f.write('Y-int: {:2.5f} +- {:2.5f} \n'.format(output.beta[1], output.sd_beta[1]))
            f.write('R^2: {:2.5f}\n'.format(rsq))
    except:
        print('There was an error saving fit results to file.')
    return
