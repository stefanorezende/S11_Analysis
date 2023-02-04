import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('Data Analysis\Data.xlsx', '2nd_inset_analysis', decimal=',')
df.rename(columns = {'dB(S(1,1))[0, ::]':'dB'}, inplace = True)

x = df['lins'].value_counts().index
highest_freq = 1.5e+10

fig, ax = plt.subplots( layout = 'constrained')

for l in x:
    dB = df.loc[df.dB == l]
    ax.plot(dB['freq'],dB['dB'], label ='ADS')

plt.axhline(y=-10, ls=':', c='r') #Horizontal line
ax.set_xlabel('Frequency')  # Add an x-label to the axes.
ax.set_ylabel('S(1,1) [dB]')  # Add a y-label to the axes.
ax.set(xlim=(0, highest_freq)) #Set limits
ax.set_title('S11_Analysis')  # Add a title to the axes.
ax.grid()
ax.legend()

plt.show
