import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('Pasta3.xlsx')

# Função para padronizar os nomes dos serviços
def padronizar_nomes(nome):
    return ' '.join(palavra.capitalize() for palavra in nome.lower().split())

# Aplicar a função à coluna que contém os nomes dos serviços
df['Serviço Desejado'] = df['Serviço Desejado'].apply(padronizar_nomes)

# Salvar de volta no Excel, se necessário
df.to_excel('Pasta3_padronizado.xlsx', index=False)
