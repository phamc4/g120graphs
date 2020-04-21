#! python3

def graph():
    return 


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
    return 0

