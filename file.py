import pandas as pd
import matplotlib.pyplot as plt

# lendo
df = pd.read_excel('Pasta3.xlsx')

# espaços em branco
df.columns = df.columns.str.strip()


df = df.dropna(subset=['Serviço Desejado'])
# Corrigir possíveis erros de digitação nos serviços desejados
df['Serviço Desejado'] = df['Serviço Desejado'].str.strip().str.lower()



# Quantidade de serviço desejado abaixo
servicos_contagem = df['Serviço Desejado'].value_counts()

# grafico:
plt.figure(figsize=(24, 18))  # Aumentar o tamanho da figura
servicos_contagem.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuição dos Serviços Desejados')
plt.ylabel('')  # Remover o rótulo do eixo y para clareza

# Mostrar o gráfico
plt.show()
