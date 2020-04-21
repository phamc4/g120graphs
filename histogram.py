#! python3

# Import Libraries
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mplcyberpunk
import seaborn as sns

# Cyberpunk Histogram with KDE

"""
Base graph is Seaborn distplot object with Histogram and Kernel Density Estimate Distribution

REQUIRED MODULES (outside of normal DS imports):
- mplcyberpunk
- seaborn
"""

# Draw Plot
plt.figure(figsize=(12,6), dpi= 80)

# Plot Points
mpg_kde_plot_5 = sns.distplot(auto_df.loc[auto_df['Cylinders'] == 5, "Gas Mileage (Combined)"],
             color="red",
             kde_kws={
                 "color":'white',
                 "shade":True,
                 "alpha":0.7,
             }
            )


# Decoration
plt.title('\nHistogram of MPG by 5-Cylinder Engines with KDE/Dist\n', fontsize=22)
plt.xlabel("MPG\n", fontsize=18)
plt.ylabel("Density (KDE)\n", fontsize=18)
mplcyberpunk.add_underglow()
mplcyberpunk.add_glow_effects()


# Show Plot
plt.subplots_adjust(left=0, bottom=0, right=1.1, top=1, wspace=1, hspace=0)
plt.show()

