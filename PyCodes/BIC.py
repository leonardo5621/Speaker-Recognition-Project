import numpy as np
from sklearn.mixture import GMM
from matplotlib import pyplot as plt

def BIC(Model,N):

    n_components=np.arange(1,N,5)

    Models=[ GMM(n,'tied').fit(Model) for n in n_components]

    plt.plot(n_components, [M.bic(Model) for M in Models], label='BIC')
    plt.legend(loc='best')
    plt.xlabel('n_components');
    plt.ylabel('BIC');

    plt.show()
