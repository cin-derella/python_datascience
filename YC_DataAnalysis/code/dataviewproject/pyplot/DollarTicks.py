import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def DollarTickShow(nparray = 100*np.random.rand(20)):
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    fig, ax = plt.subplots()
    ax.plot(nparray)

    formatter = ticker.FormatStrFormatter('$%1.2f')
    ax.yaxis.set_major_formatter(formatter)

    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_visible(False)
        tick.label2.set_visible(True)
        tick.label2.set_color('green')

    plt.show()

if __name__ == '__main__':

    DollarTickShow()