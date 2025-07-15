# tcc_mba
Este projeto tem como objetivo analisar os microdados do ENEM 2023 e desenvolver um modelo preditivo para identificar os alunos com melhor desempenho na prova de Matemática.

Objetivos:
- Identificar padrões entre os alunos com notas acima do percentil 80 em Matemática.
- Desenvolver um modelo de machine learning para prever alunos com alto desempenho.
- Extrair insights sobre fatores socioeconômicos e de estudo que influenciam o desempenho. 

Dados tratados e filtrados para análise (disponíveis em https://drive.google.com/drive/folders/1LcwhWErhcjsZhMAzxCsPRIzZ2-Cw3isY?usp=drive_link)

As principais análises envolvem:
- Distribuição das notas de Matemática e da média geral, histogramas e boxplots, dos candidatos presentes na prova de matemática.
- Correlação entre notas de Matemática e outras notas.
- Impacto de variáveis socioeconômicas (renda, escolaridade dos pais, tipo de escola) no desempenho na prova de matemática.
- Modelos de classificação: Random Forest, XGBoost, LightGBM para prever alunos que tiram as notas acima do percentil 80 em Matemática no ENEM de 2023.
- Ranking das variáveis socieconômicas que mais influenciam os modelos a prever os alunos que tiram as notas acima do percentil 80 em Matemática no ENEM de 2023.

Este projeto é dividido em 5 arquivos:
- **salva_parquet** : código que faz a alteração do formato csv para o formato parquet.
- **Data_Wragling** : usado para limpeza e transformação dos dados.
- **Analise_dados_enem_2023** : arquivo contendo toda a análise dos dados.
- **previsao_top20** : algoritmos de machine learning, de ensemble models, para prever quais as candidatos estão mais propensos a 
estar entre as 20% das melhores notas para que, com isso, seja possível avaliar a importância de cada variável para essa decisão. 

Próximo passos:

- Criar um dashboard interatidos dos dados
- Incorporar dados de edições anteriores
