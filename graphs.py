#! python3


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

def bootstrap_sample_medians(data, n_bootstrap_samples=10000):
    bootstrap_sample_medians = []
    for i in range(n_bootstrap_samples):
        bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
        bootstrap_sample_medians.append(np.median(bootstrap_sample))
    return bootstrap_sample_medians

def choropleth():
    return 0

