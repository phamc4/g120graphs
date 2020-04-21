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


def bootstrap_sample_medians(data, n_bootstrap_samples=10000):
    bootstrap_sample_medians = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_sample_medians.append(np.median(bootstrap_sample))
    return bootstrap_sample_medians

def choropleth():
    return 0

