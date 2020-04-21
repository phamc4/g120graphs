#! python3
import numpy as np
import pandas as pd


def shaded_alpha_area(p,n, alpha):
    binomial_mean = p * n
    binomial_var = n * p * (1-p)
    normal_approx = stats.norm(binomial_mean, np.sqrt(binomial_var))

    x = np.linspace(0,n,1000)

    fig, ax = plt.subplots(1, figsize=(16, 3))

    ax.plot(x, normal_approx.pdf(x), linewidth=3)
    ax.fill_between(x, normal_approx.pdf(x), 
                where=(x >= normal_approx.ppf(1-alpha)), color="red", alpha=0.5)
    ax.set_title("Significance Region")
    

def graph():
    return 



def scatterplot(x,y):
    return plt.scatter(x,y)
def scatter():
    pass

def eddieplot(df):
    df.plotting.scattermatrix()
    return

def beta_distr():
    fig, ax = plt.subplots(figsize=(10,5))
    x = np.linspace(0,1,100)
    for (a,b,s) in [(1,1,"r-"), (2,1,"g-"), (3,1,"b-"), (2,2,"g--"), (3,2,"b--"), (3,3,"b:")]:
            ax.plot(x,
                    stats.beta(a,b).pdf(x),
                    s,
                    label="({0},{1})".format(a,b))
    ax.legend(title=r"($\alpha,\beta$)", loc="upper left")
    ax.set_xlabel("p")
    ax.set_ylabel("pdf")


import matplotlib.pyplot as plt
x=list(range(10))
fig, ax = plt.subplots()
ax.plot(x,x)

def choropleth():
    return 0


def bootstrap_sample_medians(data, n_bootstrap_samples=10000):
    bootstrap_sample_medians = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_sample_medians.append(np.median(bootstrap_sample))
    return bootstrap_sample_medians

def choropleth():

  #add in plotly express
    return 0



#HI GUYS!!

