import pandas as pd

def separar_dataframes(arquivo):
    with open(arquivo, 'r') as file:
        linhas = file.readlines()

    separador = '----------------------------------------------------------------------'
    dataframes = []
    nome_dataframe = None
    dados_dataframe = []

    for linha in linhas:
        if linha.strip() == separador:
            if nome_dataframe and dados_dataframe:
                df = pd.DataFrame(dados_dataframe)
                dataframes.append((nome_dataframe, df))
                dados_dataframe = []
                nome_dataframe = None
        else:
            if nome_dataframe is None:
                nome_dataframe = linha.strip()
            else:
                dados_dataframe.append(linha.strip().split())

    if nome_dataframe and dados_dataframe:
        df = pd.DataFrame(dados_dataframe)
        dataframes.append((nome_dataframe, df))

    for nome, df in dataframes:
        nome_arquivo = f'{nome}.txt'
        df.to_csv('Lgnd\\'+nome_arquivo, index=False, sep='\t')
        print(f'Dataframe "{nome}" salvo em "{nome_arquivo}".')

# Exemplo de uso:
arquivo_txt = 'Simul X Medidas\\Cardioid\\Par Sweep\\Lgnd.txt'
separar_dataframes(arquivo_txt)
