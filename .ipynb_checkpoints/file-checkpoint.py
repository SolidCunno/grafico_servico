import pandas as pd
import matplotlib.pyplot as plt

# Ler a planilha
df = pd.read_excel('Pasta3.xlsx')

# Remover espaços em branco das colunas
df.columns = df.columns.str.strip()

# Remover linhas com dados faltando em 'Serviço Desejado'
df = df.dropna(subset=['Serviço Desejado'])

# Corrigir possíveis erros de digitação nos serviços desejados
df['Serviço Desejado'] = df['Serviço Desejado'].str.strip().str.lower()

# Agrupar serviços desejados em categorias mais amplas (se necessário)
# Exemplo: df['Serviço Desejado'] = df['Serviço Desejado'].replace({'crochê': 'artesanato', 'massoterapeuta': 'saúde', ...})

# Contar a frequência de cada serviço desejado
servicos_contagem = df['Serviço Desejado'].value_counts()

# Criar o gráfico de pizza com tamanho ainda maior
plt.figure(figsize=(24, 18))  # Aumentar o tamanho da figura
servicos_contagem.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribuição dos Serviços Desejados')
plt.ylabel('')  # Remover o rótulo do eixo y para clareza

# Mostrar o gráfico
plt.show()
