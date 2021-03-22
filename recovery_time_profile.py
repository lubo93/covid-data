import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MultipleLocator

latest_data = pd.read_csv("singapore_data.csv")

# process data
status = np.asarray(latest_data['status'].to_list())
age = np.asarray(latest_data['age'].to_list())
days_prior = np.asarray(latest_data['symptomatic to confirmation'].to_list())
days_resolve = np.asarray(latest_data['days to recover'].to_list())

age = np.copy(age[status == 'Recovered'])
recovered_days_prior = np.copy(days_prior[status == 'Recovered'])
recovered_days_resolve = np.copy(days_prior[status == 'Recovered'])

# time between onset of symptoms and recovery
delta_arr = [float(recovered_days_prior[i])+float(recovered_days_resolve[i]) \
            for i in range(len(recovered_days_prior)) if \
            recovered_days_prior[i] != '-' and \
            recovered_days_resolve[i] != '-']

# age data may be used to stratify recovery times on age
age_arr = [float(age[i]) for i in range(len(age)) if \
          recovered_days_prior[i] != '-' and recovered_days_resolve[i] != '-']

fig, ax = plt.subplots()

ax.hist(delta_arr, 
        weights=np.zeros_like(delta_arr) + 1. / len(delta_arr), 
        bins = 17, 
        alpha = 0.5, 
        histtype='bar', 
        color='steelblue',
        edgecolor='k',
        rwidth = 0.7,
        density = True)

ax.set_xlabel(r'recovery time [days]')
ax.set_ylabel(r'PDF')
ax.set_xlim([0,50])
ax.set_ylim([0,0.1])
ax.xaxis.set_minor_locator(MultipleLocator(2))
plt.legend(loc = 1, frameon = False, fontsize = 8)
plt.tight_layout()
plt.margins(0,0)
plt.savefig('recovery_data.png', 
            dpi=300, 
            bbox_inches = 'tight',
            pad_inches = 0.05)
plt.show()