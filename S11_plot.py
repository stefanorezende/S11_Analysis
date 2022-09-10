import matplotlib.pyplot as plt
import pandas as pd

xl = pd.ExcelFile('S11_ADS.xlsx')
sh_names = xl.sheet_names

for name in sh_names:

    df_ads = pd.read_excel('S11_ADS.xlsx', name, decimal=',')
    df_ads.dtypes
    df_ads.rename(columns = {'dB(S11_fitted)':'S11_ADS'}, inplace = True)

    df_cst = pd.read_excel('S11_CST.xlsx', name, decimal=',')
    df_cst.dtypes
    df_cst.rename(columns = {'Frequency / GHz':'freq', 'S1,1/abs,dB':'S11_CST'}, inplace = True)

    df_cst['freq'] = round(df_cst['freq'],2)*10**9

    fig, ax = plt.subplots( layout = 'constrained')
    ax.plot(df_ads['freq'], df_ads['S11_ADS'], label ='ADS')
    ax.plot(df_cst['freq'], df_cst['S11_CST'], label ='CST')

    ax.set_xlabel('Frequency')  # Add an x-label to the axes.
    ax.set_ylabel('S(1,1) [dB]')  # Add a y-label to the axes.
    ax.set_title('S11_Analysis')  # Add a title to the axes.
    ax.legend()


    plt.savefig(name+'.png')