# Análise de Lead Time nas Entregas de Software - WideBTech
# Código extraído do notebook Jupyter

# ===== IMPORTAÇÃO DE BIBLIOTECAS =====
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar o estilo dos gráficos
sns.set_style("whitegrid")

# ===== CARREGAMENTO DOS DADOS =====
# Carregar tabelas do dataset
dim_equipes = pd.read_csv("Dim_Equipes.csv")
dim_desenvolvedores = pd.read_csv("Dim_Desenvolvedores.csv")
fato_sprints = pd.read_csv("Fato_Sprints.csv")
fato_tarefas = pd.read_csv("Fato_Tarefas.csv")
fato_implantacoes = pd.read_csv("Fato_Implantacoes.csv")
fato_defeitos = pd.read_csv("Fato_Defeitos.csv")

print("Dados carregados com sucesso!")

# ===== EXPLORAÇÃO INICIAL DOS DADOS =====
print("\n--- Informações sobre Fato_Tarefas ---")
fato_tarefas.info()

print("\n--- Informações sobre Fato_Sprints ---")
fato_sprints.info()

print("\n--- Informações sobre Fato_Implantacoes ---")
fato_implantacoes.info()

print("\n--- Informações sobre Fato_Defeitos ---")
fato_defeitos.info()

print("\n--- Informações sobre Dim_Equipes ---")
dim_equipes.info()

print("\n--- Informações sobre Dim_Desenvolvedores ---")
dim_desenvolvedores.info()

# ===== VERIFICAÇÃO DE VALORES AUSENTES =====
print("\n--- Valores Ausentes em Fato_Tarefas ---")
print(fato_tarefas.isnull().sum())

print("\n--- Valores Ausentes em Fato_Sprints ---")
print(fato_sprints.isnull().sum())

print("\n--- Valores Ausentes em Fato_Implantacoes ---")
print(fato_implantacoes.isnull().sum())

print("\n--- Valores Ausentes em Fato_Defeitos ---")
print(fato_defeitos.isnull().sum())

print("\n--- Valores Ausentes em Dim_Equipes ---")
print(dim_equipes.isnull().sum())

print("\n--- Valores Ausentes em Dim_Desenvolvedores ---")
print(dim_desenvolvedores.isnull().sum())

# ===== ANÁLISE ESTATÍSTICA DESCRITIVA =====
print("\n--- Distribuição e Outliers em Fato_Tarefas ---")
print(fato_tarefas.describe())

print("\n--- Distribuição e Outliers em Fato_Sprints ---")
print(fato_sprints.describe())

print("\n--- Distribuição e Outliers em Fato_Implantacoes ---")
print(fato_implantacoes.describe())

print("\n--- Distribuição e Outliers em Fato_Defeitos ---")
print(fato_defeitos.describe())

# ===== CONVERSÃO DE TIPOS DE DADOS =====
# Converter colunas de data para o tipo datetime em Fato_Tarefas
fato_tarefas["Data_Criacao"] = pd.to_datetime(fato_tarefas["Data_Criacao"])
fato_tarefas["Data_Inicio_Desenvolvimento"] = pd.to_datetime(fato_tarefas["Data_Inicio_Desenvolvimento"])
fato_tarefas["Data_Conclusao"] = pd.to_datetime(fato_tarefas["Data_Conclusao"])

# Converter colunas de data em Fato_Sprints
fato_sprints["Data_Inicio_Sprint"] = pd.to_datetime(fato_sprints["Data_Inicio_Sprint"])
fato_sprints["Data_Fim_Sprint"] = pd.to_datetime(fato_sprints["Data_Fim_Sprint"])

# Converter colunas de data em Fato_Implantacoes
fato_implantacoes["Data_Implantacao"] = pd.to_datetime(fato_implantacoes["Data_Implantacao"])

# Converter colunas de data em Fato_Defeitos
fato_defeitos["Data_Descoberta"] = pd.to_datetime(fato_defeitos["Data_Descoberta"])
fato_defeitos["Data_Resolucao"] = pd.to_datetime(fato_defeitos["Data_Resolucao"])

print("Colunas de data convertidas com sucesso!")

# ===== VISUALIZAÇÕES - DISTRIBUIÇÕES =====
# Histograma do Lead Time (Fato_Tarefas)
plt.figure(figsize=(10, 6))
sns.histplot(fato_tarefas["Lead_Time_Dias"], kde=True, bins=30)
plt.title("Distribuição do Lead Time (em Dias)")
plt.xlabel("Lead Time (Dias)")
plt.ylabel("Frequência")
plt.show()

# Box Plot do Lead Time por Tipo de Tarefa (Fato_Tarefas)
plt.figure(figsize=(12, 7))
sns.boxplot(x="Tipo_Tarefa", y="Lead_Time_Dias", data=fato_tarefas)
plt.title("Lead Time por Tipo de Tarefa")
plt.xlabel("Tipo de Tarefa")
plt.ylabel("Lead Time (Dias)")
plt.show()

# Box Plot do Lead Time por Complexidade (Fato_Tarefas)
plt.figure(figsize=(12, 7))
sns.boxplot(x="Complexidade", y="Lead_Time_Dias", data=fato_tarefas, order=["Baixa", "Média", "Alta"])
plt.title("Lead Time por Complexidade da Tarefa")
plt.xlabel("Complexidade")
plt.ylabel("Lead Time (Dias)")
plt.show()

# ===== VISUALIZAÇÕES - CONTAGENS =====
# Contagem de tarefas por Status (Fato_Tarefas)
plt.figure(figsize=(10, 6))
sns.countplot(y="Status_Tarefa", data=fato_tarefas, order=fato_tarefas["Status_Tarefa"].value_counts().index)
plt.title("Contagem de Tarefas por Status")
plt.xlabel("Contagem")
plt.ylabel("Status da Tarefa")
plt.show()

# Contagem de equipes por Metodologia Ágil (Dim_Equipes)
plt.figure(figsize=(8, 5))
sns.countplot(x="Metodologia_Agil", data=dim_equipes)
plt.title("Número de Equipes por Metodologia Ágil")
plt.xlabel("Metodologia Ágil")
plt.ylabel("Número de Equipes")
plt.show()

# ===== ANÁLISE DE CORRELAÇÃO =====
# Selecionar colunas numéricas relevantes para correlação em Fato_Tarefas
correlation_data = fato_tarefas[[
    "Lead_Time_Dias",
    "Cycle_Time_Dias",
    "Story_Points",
    "Numero_Defeitos_Associados"
]].copy()

# Calcular a matriz de correlação
correlation_matrix = correlation_data.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlação entre Métricas de Tarefas")
plt.show()

# ===== ANÁLISES DE RELACIONAMENTO =====
# Relação entre Story Points e Lead Time
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Story_Points", y="Lead_Time_Dias", data=fato_tarefas)
plt.title("Relação entre Story Points e Lead Time")
plt.xlabel("Story Points")
plt.ylabel("Lead Time (Dias)")
plt.show()

# Relação entre Numero_Defeitos_Associados e Lead Time
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Numero_Defeitos_Associados", y="Lead_Time_Dias", data=fato_tarefas)
plt.title("Relação entre Número de Defeitos Associados e Lead Time")
plt.xlabel("Número de Defeitos Associados")
plt.ylabel("Lead Time (Dias)")
plt.show()

# ===== ANÁLISES TEMPORAIS =====
# Agrupar tarefas por mês de conclusão e calcular o Lead Time médio
fato_tarefas["Mes_Conclusao"] = fato_tarefas["Data_Conclusao"].dt.to_period("M")
lead_time_mensal = fato_tarefas.groupby("Mes_Conclusao")["Lead_Time_Dias"].mean().reset_index()
lead_time_mensal["Mes_Conclusao"] = lead_time_mensal["Mes_Conclusao"].dt.to_timestamp()

plt.figure(figsize=(14, 7))
sns.lineplot(x="Mes_Conclusao", y="Lead_Time_Dias", data=lead_time_mensal)
plt.title("Tendência Mensal do Lead Time Médio")
plt.xlabel("Mês de Conclusão")
plt.ylabel("Lead Time Médio (Dias)")
plt.xticks(rotation=45)
plt.show()

# Tendência da Velocidade do Sprint
sprints_mensal = fato_sprints.groupby(fato_sprints["Data_Fim_Sprint"].dt.to_period("M"))["Pontos_Concluidos"].sum().reset_index()
sprints_mensal["Data_Fim_Sprint"] = sprints_mensal["Data_Fim_Sprint"].dt.to_timestamp()

plt.figure(figsize=(14, 7))
sns.lineplot(x="Data_Fim_Sprint", y="Pontos_Concluidos", data=sprints_mensal)
plt.title("Tendência Mensal da Velocidade Total dos Sprints")
plt.xlabel("Mês")
plt.ylabel("Pontos Concluídos")
plt.xticks(rotation=45)
plt.show()

# ===== ANÁLISES POR EQUIPE =====
# Juntar Fato_Tarefas com Dim_Equipes para analisar Lead Time por Equipe
dados_com_equipes = pd.merge(fato_tarefas, dim_equipes, on="ID_Equipe", how="left")

plt.figure(figsize=(14, 7))
sns.boxplot(x="Nome_Equipe", y="Lead_Time_Dias", data=dados_com_equipes)
plt.title("Lead Time por Equipe")
plt.xlabel("Nome da Equipe")
plt.ylabel("Lead Time (Dias)")
plt.xticks(rotation=45)
plt.show()

# Juntar Fato_Sprints com Dim_Equipes para analisar Velocidade por Equipe
dados_sprints_equipes = pd.merge(fato_sprints, dim_equipes, on="ID_Equipe", how="left")

plt.figure(figsize=(14, 7))
sns.barplot(x="Nome_Equipe", y="Pontos_Concluidos", data=dados_sprints_equipes, estimator=sum, ci=None)
plt.title("Total de Pontos Concluídos por Equipe")
plt.xlabel("Nome da Equipe")
plt.ylabel("Pontos Concluídos")
plt.xticks(rotation=45)
plt.show()

# ===== VERIFICAÇÃO DE TIPOS DE DADOS =====
# Verificar os tipos de dados após as conversões
print("\n--- Tipos de Dados Após Conversão em Fato_Tarefas ---")
fato_tarefas.info()

print("\n--- Tipos de Dados Após Conversão em Fato_Sprints ---")
fato_sprints.info()

print("\n--- Tipos de Dados Após Conversão em Fato_Implantacoes ---")
fato_implantacoes.info()

print("\n--- Tipos de Dados Após Conversão em Fato_Defeitos ---")
fato_defeitos.info()

# Verificar os tipos das colunas numéricas principais
print("\n--- Tipos de Dados das Colunas Numéricas Relevantes ---")
print("Fato_Tarefas:")
print(fato_tarefas[["Lead_Time_Dias", "Cycle_Time_Dias", "Story_Points", "Numero_Defeitos_Associados"]].dtypes)
print("\nFato_Sprints:")
print(fato_sprints[["Pontos_Concluidos"]].dtypes)

# ===== ANÁLISE DETALHADA DAS MÉTRICAS CHAVE =====
print("\n--- Análise da Distribuição das Métricas Chave ---")

# Lead Time
print("\nAnálise de Lead Time:")
print(fato_tarefas["Lead_Time_Dias"].describe())
plt.figure(figsize=(10, 6))
sns.histplot(fato_tarefas["Lead_Time_Dias"], kde=True, bins=50)
plt.title("Distribuição do Lead Time (em Dias)")
plt.xlabel("Lead Time (Dias)")
plt.ylabel("Frequência")
plt.show()

# Cycle Time
print("\nAnálise de Cycle Time:")
print(fato_tarefas["Cycle_Time_Dias"].describe())
plt.figure(figsize=(10, 6))
sns.histplot(fato_tarefas["Cycle_Time_Dias"], kde=True, bins=50)
plt.title("Distribuição do Cycle Time (em Dias)")
plt.xlabel("Cycle Time (Dias)")
plt.ylabel("Frequência")
plt.show()

# Story Points
print("\nAnálise de Story Points:")
print(fato_tarefas["Story_Points"].describe())
plt.figure(figsize=(10, 6))
sns.histplot(fato_tarefas["Story_Points"], kde=True, bins=fato_tarefas["Story_Points"].nunique() if fato_tarefas["Story_Points"].nunique() < 30 else 30)
plt.title("Distribuição de Story Points")
plt.xlabel("Story Points")
plt.ylabel("Frequência")
plt.xticks(sorted(fato_tarefas["Story_Points"].unique()))
plt.show()

# Pontos Concluídos (em Fato_Sprints)
print("\nAnálise de Pontos Concluídos por Sprint:")
print(fato_sprints["Pontos_Concluidos"].describe())
plt.figure(figsize=(10, 6))
sns.histplot(fato_sprints["Pontos_Concluidos"], kde=True, bins=fato_sprints["Pontos_Concluidos"].nunique() if fato_sprints["Pontos_Concluidos"].nunique() < 30 else 30)
plt.title("Distribuição de Pontos Concluídos por Sprint")
plt.xlabel("Pontos Concluídos")
plt.ylabel("Frequência de Sprints")
plt.xticks(sorted(fato_sprints["Pontos_Concluidos"].unique()))
plt.show()

# ===== INTERPRETAÇÃO DOS RESULTADOS =====
print("\nInterpretação da Razoabilidade:")
print("- A distribuição do Lead Time e Cycle Time parece seguir um padrão esperado (assimetria positiva)")
print("- A distribuição de Story Points mostra uma concentração em valores inteiros, o que é comum")
print("- A distribuição de Pontos Concluídos por Sprint reflete a variação na velocidade")
print("\nPara uma conclusão definitiva sobre a razoabilidade, seria ideal comparar essas distribuições")
print("com benchmarks da indústria ou com o conhecimento específico do contexto de negócio simulado.")

