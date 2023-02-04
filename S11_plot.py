import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

xl = pd.ExcelFile('S11_ADS.xlsx')
sh_ads = xl.sheet_names

xl = pd.ExcelFile('S11_CST.xlsx')
sh_cst = xl.sheet_names

for name in sh_cst:

    df_ads = pd.read_excel('S11_ADS.xlsx', name, decimal=',')
    # df_ads.dtypes
    df_ads.rename(columns = {'dB(S11_fitted)':'S11_ADS'}, inplace = True)

    df_cst = pd.read_excel('S11_CST.xlsx', name, decimal=',')
    # df_cst.dtypes
    df_cst.rename(columns = {'Frequency / GHz':'freq', 'S1,1/abs,dB':'S11_CST'}, inplace = True)

    df_cst['freq'] = round(df_cst['freq'],2)*10**9

    highest_freq = max([max(df_cst['freq']),max(df_ads['freq'])])

    fig, ax = plt.subplots( layout = 'constrained')
    ax.plot(df_ads['freq'], df_ads['S11_ADS'], label ='ADS')
    ax.plot(df_cst['freq'], df_cst['S11_CST'], label ='CST')

    if name == 'MLIN_Disc_Monopole' or name == 'CPW_Disc_Monopole':
        df_ads2 = pd.read_excel('S11_ADS.xlsx', name+'_FEM', decimal=',')
        df_ads2.rename(columns = {'dB(S11_fitted)':'S11_ADS_FEM'}, inplace = True)
        ax.plot(df_ads2['freq'], df_ads2['S11_ADS_FEM'], label ='ADS_FEM')

    plt.axhline(y=-10, ls=':', c='r') #Horizontal line
    ax.set_xlabel('Frequency')  # Add an x-label to the axes.
    ax.set_ylabel('S(1,1) [dB]')  # Add a y-label to the axes.
    ax.set(xlim=(0, highest_freq)) #Set limits
    ax.set_title('S11_Analysis')  # Add a title to the axes.
    ax.grid()
    ax.legend()


    plt.savefig('Figures/'+name+'.png')



    df = df_ads.merge(df_cst, how= 'outer', on='freq')
    df.sort_values(by='freq', inplace=True)
    corr = df.corr()

    if name == 'MLIN_Disc_Monopole' or name == 'CPW_Disc_Monopole':
        df = df.merge(df_ads2, how= 'outer', on='freq')
        df.sort_values(by='freq', inplace=True)
        corr = df.corr()
    
    with pd.ExcelWriter('Correlations.xlsx', mode= 'a') as writer:        
        corr.to_excel(writer, sheet_name= name)
        