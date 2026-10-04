import pandas as pd

# Carregar o join
df = pd.read_csv("vendas_lojas.csv")

# Extrair o mês da coluna data
df['mes'] = pd.to_datetime(df['data']).dt.to_period('M').astype(str)

# Criar o pivot: receita por região × mês
pivot = df.pivot_table(
    index='regiao',
    columns='mes',
    values='receita_brl',
    aggfunc='sum'
)

# Reordenar os meses
pivot = pivot[['2026-01','2026-02','2026-03','2026-04','2026-05','2026-06']]

# Salvar no formato correto
pivot.to_csv("pivot_receita.csv", float_format="%.2f")
