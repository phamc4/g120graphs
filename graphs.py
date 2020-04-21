#! python3

def graph():
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

def choropleth():
    return 0

