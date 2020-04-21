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
    