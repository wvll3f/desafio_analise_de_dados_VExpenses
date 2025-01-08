import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
# 1. Carregando o Dataset
df = pd.read_csv('Dataset.csv')
print(df)

# 2. Análise Exploratória
print(df.info())
print(df.describe())
sns.pairplot(df, hue='Compra (0 ou 1)')

# Identificando quantos valores nulos temos
print('| inicio - Tabela de valores nulos |')
print(df.isnull().sum())
print('| fim - Tabela de valores nulos |')

# 3. Pré-processamento
df['Anúncio Clicado'] = df['Anúncio Clicado'].map({'Sim': 1, 'Não': 0})
df['Gênero'] = LabelEncoder().fit_transform(df['Gênero'])

# Preenchendo Valores nulos ou invalidos
media_tempo_site = df[df['Tempo no Site (min)'] != -1]['Tempo no Site (min)'].mean()
df['Tempo no Site (min)'] = df['Tempo no Site (min)'].replace(-1, media_tempo_site)
df['Anúncio Clicado'] = df['Anúncio Clicado'].fillna(0)
df['Idade'] = df['Idade'].fillna(df['Idade'].mean())  
df['Renda Anual (em $)'] = df['Renda Anual (em $)'].fillna(df['Renda Anual (em $)'].mean())  
df['Gênero'] = df['Gênero'].fillna(df['Gênero'].mode()[0])

#Verificação se após o preenchimento se manteve algum valor nulo
print('| Tabela de valores nulos após preenchimento |')
print(df.isnull().sum())

X = df.drop('Compra (0 ou 1)', axis=1)
y = df['Compra (0 ou 1)']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Construção do Modelo
model = RandomForestClassifier(n_estimators=1000,random_state=42)
model.fit(X_train, y_train)

# 5. Teste do modelo 
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d')
plt.show()

metrics = pd.DataFrame({
    'Métrica': ['Accuracy', 'Precision', 'Recall', 'F1-Score'],
    'Valor': [
        accuracy_score(y_test, y_pred),
        precision_score(y_test, y_pred),
        recall_score(y_test, y_pred),
        f1_score(y_test, y_pred)
    ]
})

print(metrics)
sns.barplot(x='Métrica', y='Valor', data=metrics)
plt.title('Desempenho do Modelo')
plt.ylim(0, 1)
plt.show()

