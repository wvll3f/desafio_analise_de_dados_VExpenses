# Relatorio Teste lógico Estagio em analise de dados


## Objetivo
Este relatório documenta o processo realizado para a execução do teste técnico, que visa a criação de um modelo de previsão de compra para um site imobiliário, as variaveis para análise foram: *Idade, Renda Anual, Gênero, Tempo no Site (min), Anúncio Clicado.*

**Ferramentas utilizadas:** python 3 com as bibliotecas, Pandas, matplotlib, seaborn, scikit-learn.

### Etapa 1 - Análise exploratória dos dados:
|  Métricas         | Idade | Renda Anual  | Tempo no Site | Compra (0 ou 1) |
|-------------------|-------|--------------|---------------|-----------------|
| *Média*         | 38,5  | 58253.9      | 17.3          | 0.33            |
| *Desvio Padrão* | 12,6  | 25612        | 7.7           | 0.47            | 
| *Mínimo*        | 18    | 30000        | -1            | 0               |
| *Máximo*        | 59    | 100000       | 29.8          | 1               |

**Idade:** Numérica, com 10 valores ausentes.

**Renda Anual (em $):** Numérica, com 11 valores ausentes.

**Gênero:** Categórica, com 7 valores ausentes.

**Tempo no Site (min):** Numérica, sem valores ausentes, porém com valores inválidos  como -1 .

**Anúncio Clicado:** Categórica (provavelmente "Sim" ou "Não"), com 10 valores ausentes.

**Compra (0 ou 1):** Variável alvo (binária).

Foi identificado nas colunas de *Idade, Renda Anual, Gênero, Anúncio Clicado,* a falta de valores em algumas linhas.

Na coluna de *Tempo no site,* foi identificado a presença valores inválidos  (-1).

### Etapa 2 - Pré-processamento dos dados
**Valores ausentes foram tratados da seguinte forma:**

~ Idade e Renda Anual (em $): Substituídos pela média da coluna.
~ Tempo no Site (min): Substituídos pela média da coluna.
~ Anúncio Clicado: Substituído pelo valor mais frequente (Sim ou Não).
~ Variáveis categóricas foram codificadas:

**Normalização de valores:**

~ Gênero: Feminino = O, Masculino = 1.
~ Anúncio Clicado: Sim = 1, Não = 0.
~ Foi realizada a normalização das variáveis numéricas para escalas comparáveis.

**O dataset foi dividido em conjuntos de treino (80%) e teste (20%).**

### Etapa 3 - Construção do modelo de classificação:
Optei por utilizar o modelo de classificação baseado em árvores de decisão, por ser um modelo que pode lidar bem com ambos os tipos de variáveis e pela forma como lida com essas árvores de decisão, podendo gerar uma modelo com maior confiabilidade.

Utilizado também o cross validation onde tivemos resultados bem proximos utilizando 5 versões de testes, e com um desvio padrão de 5% e uma media de 63% de acurácia.

E com isso os resultados usando o modelo de arvore de decisão se demonstraram bem proximos ao resultado após usar o cross validation.

### Etapa 4 - Interpretação dos resultados:

|               Class               | Precision | Recall | F1-Score | Support |
|-----------------------------------|-----------|--------|----------|---------|
| **0**                             | 0.62      | 0.96   | 0.75     | 24      |
| **1**                             | 0.67      | 0.12   | 0.21     | 16      |
| **Accuracy**                      |           |        | 0.62     | 40      |
| **Macro Avg**                     | 0.64      | 0.54   | 0.48     | 40      |
| **Weighted Avg**                  | 0.64      | 0.62   | 0.54     | 40      |

**Classe 0:** Não houve compra
**Classe 1:** Houve Compra

Para a classe 0 (não compra), o modelo está indo muito bem. Ele consegue identificar corretamente quase todos os casos reais dessa classe, já que o recall é bem alto (96%). Isso significa que o modelo raramente deixa passar um caso de "não compra".

Já para a classe 1 (compra), o desempenho é preocupante. O modelo consegue identificar corretamente apenas 12% dos casos reais dessa classe, o que é muito baixo. Em outras palavras, ele está deixando passar a maioria das pessoas que realmente compram.

Acredito que esse resultado se deu pela maior quantidade de dados sendo como classe 0 (não compra) e/ou pela variedade de dados que chegam a finalidade de compra.
