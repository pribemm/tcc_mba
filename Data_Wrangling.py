import seaborn as sns
import pandas as pd
import numpy as np

df_enem_2023 = pd.read_parquet("C://Users//prisc//Documents//enem_2023.parquet")

#Seleção das observações identificadas como treineiro
treineiros=df_enem_2023.loc[df_enem_2023['IN_TREINEIRO']==1]
df_enem_2023=df_enem_2023.drop(treineiros.index) #Exclusão dos treineiros
df_enem_2023=df_enem_2023.drop(columns='IN_TREINEIRO') #Exclusão da coluna que identifica os treineiros

variaveis_excluidas=['NU_ANO',
                     'TP_PRESENCA_CN',
                      'TP_PRESENCA_LC',
                      'TP_ESCOLA',
                      'TP_ENSINO',
                      'CO_MUNICIPIO_ESC',
                      'CO_UF_ESC',
                      'TP_SIT_FUNC_ESC',
                      'CO_MUNICIPIO_PROVA',
                      'NO_MUNICIPIO_PROVA',
                      'CO_UF_PROVA',
                      'SG_UF_PROVA',
                      'CO_PROVA_CN',
                      'CO_PROVA_CH',
                      'CO_PROVA_LC',
                      'CO_PROVA_MT',
                      'TX_RESPOSTAS_CN',
                      'TX_RESPOSTAS_CH',
                      'TX_RESPOSTAS_LC',
                      'TX_RESPOSTAS_MT',
                      'TP_LINGUA',
                      'TX_GABARITO_CN',
                      'TX_GABARITO_CH',
                      'TX_GABARITO_LC',
                      'TX_GABARITO_MT',
                      'TP_LINGUA',
                      'TX_GABARITO_CN',
                      'TX_GABARITO_CH',
                      'TX_GABARITO_LC',
                      'TX_GABARITO_MT',
                      'TP_STATUS_REDACAO',
                      'Q003',
                      'Q004',
                      'Q005',
                      'Q009',
                      'Q011',
                      'Q013',
                      'Q014',
                      'Q015',
                      'Q016',
                      'Q017',
                      'Q018',
                      'Q020',
                      'Q021',
                      'Q022',
                      'Q023']

df_enem_2023=df_enem_2023.drop(columns=variaveis_excluidas)

# Detecção dos candidatos ausentes

dados_presenca=['INSCRICAO',
                'PRESENCA_CH_LC',
                'PRESENCA_MT_CN']

# Seleção dos candidatos eliminados nas provas. Motivos que podem levar um candidato a ser eliminado:
# (https://www.gov.br/inep/pt-br/acesso-a-informacao/perguntas-frequentes/exame-nacional-do-ensino-medio-enem/no-dia-do-exame-orientacoes/motivos-de-eliminacao-do-enem)
eliminados_mt = df_enem_2023.loc[df_enem_2023['TP_PRESENCA_MT'] == 2]['NU_INSCRICAO']
eliminados_ch = df_enem_2023.loc[df_enem_2023['TP_PRESENCA_CH'] == 2]['NU_INSCRICAO']
print(f'Total de eliminados na prova de matemática/Ciências naturais: {len(eliminados_mt)}')
print(f'Total de elimiandos na prova de Linguagens e códigos/Ciências humanas: {len(eliminados_ch)}')

# Seleção dos candidatos presentes nas provas
presentes_mt = df_enem_2023.loc[df_enem_2023['TP_PRESENCA_MT'] == 1]['NU_INSCRICAO']
presentes_ch = df_enem_2023.loc[df_enem_2023['TP_PRESENCA_CH'] == 1]['NU_INSCRICAO']
print(f'Total de presentes na prova de matemática/Ciências naturais: {len(presentes_mt)}')
print(f'Total de presentes na prova de Linguagens e códigos/Ciências humanas: {len(presentes_ch)}')

ausentes_mt = df_enem_2023.loc[df_enem_2023['TP_PRESENCA_MT'] == 0]['NU_INSCRICAO']
ausentes_ch = df_enem_2023.loc[df_enem_2023['TP_PRESENCA_CH'] == 0]['NU_INSCRICAO']
ausentes_geral= pd.Series(list(set(ausentes_ch).intersection(set(ausentes_mt))))
presentes_geral=pd.Series(list(set(presentes_ch).intersection(set(presentes_mt))))
print(f'Total de ausentes em todas as provas do enem: {len(ausentes_geral)}')
print(f'Total de presentes em todas as provas do enem: {len(presentes_geral)}')
print(f'{len(df_enem_2023)-len(ausentes_geral)-len(presentes_geral)} faltaram em apenas um dia de prova')

# Tranformação dos dados

colunas_selecionadas=['NU_INSCRICAO',
                        'TP_FAIXA_ETARIA',
                        'TP_SEXO',
                        'TP_ESTADO_CIVIL',
                        'TP_COR_RACA',
                        'TP_NACIONALIDADE',
                        'TP_ST_CONCLUSAO',
                        'TP_ANO_CONCLUIU',
                        'TP_ESCOLA', 'TP_ENSINO',
                        'IN_TREINEIRO',
                        'TP_PRESENCA_CN',
                        'TP_PRESENCA_CH',
                        'TP_PRESENCA_LC',
                        'TP_PRESENCA_MT',
                        'NU_NOTA_CN',
                        'NU_NOTA_CH',
                        'NU_NOTA_LC',
                        'NU_NOTA_MT',
                        'TP_LINGUA',
                        'TP_STATUS_REDACAO',
                        'NU_NOTA_COMP1',
                        'NU_NOTA_COMP2',
                        'NU_NOTA_COMP3',
                        'NU_NOTA_COMP4',
                        'NU_NOTA_COMP5',
                        'NU_NOTA_REDACAO',
                        'Q001', 'Q002', 'Q003', 'Q004',
                        'Q005', 'Q006', 'Q007', 'Q008', 'Q009', 'Q010', 'Q011', 'Q012', 'Q013',
                        'Q014', 'Q015', 'Q016', 'Q017', 'Q018', 'Q019', 'Q020', 'Q021', 'Q022',
                        'Q023', 'Q024', 'Q025']

#'NU_INSCRICAO': 'INSCRICAO',
#'TP_PRESENCA_CH': 'PRESENCA_CH_LC',
#'TP_PRESENCA_MT': 'PRESENCA_MT_CN',
                
renome_colunas={'NU_NOTA_CN': 'NOTA_CN',
                'NU_NOTA_CH': 'NOTA_CH',
                'NU_NOTA_LC': 'NOTA_LC',
                'NU_NOTA_MT': 'NOTA_MT',
                'TP_FAIXA_ETARIA': 'FAIXA_ETARIA',
                'TP_SEXO': 'SEXO',
                'TP_ESTADO_CIVIL': 'ESTADO_CIVIL',
                'TP_COR_RACA': 'COR',
                'TP_NACIONALIDADE':'NACIONALIDADE',
                'TP_ST_CONCLUSAO':'ST_CONCLUSAO',
                'IN_TREINEIRO':'TREINEIRO',
                'TP_ANO_CONCLUIU':'ANO_CONCLUSAO',
                'NU_INSCRICAO':'INSCRICAO',
                'NO_MUNICIPIO_ESC':'MUNICIPIO',
                'SG_UF_ESC':'UF',
                'TP_DEPENDENCIA_ADM_ESC': 'ADM_ESC',
                'TP_LOCALIZACAO_ESC':'TP_URBANA_RURAL',
                'NU_NOTA_COMP1': 'NOTA_COMP1_REDACAO' ,
                'NU_NOTA_COMP2': 'NOTA_COMP2_REDACAO',
                'NU_NOTA_COMP3': 'NOTA_COMP3_REDACAO',
                'NU_NOTA_COMP4': 'NOTA_COMP4_REDACAO',
                'NU_NOTA_COMP5': 'NOTA_COMP5_REDACAO',
                'NU_NOTA_REDACAO': 'NOTA_REDACAO',
                'Q001': 'ESCOLARIDADE_PATERNA',
                'Q002': 'ESCOLARIDADE_MATERNA',
                'Q006': 'RENDA_FAMILIAR',
                'Q007': 'POSSUI_DIARISTA',
                'Q008': 'QTD_BANHEIROS',
                'Q010': 'QTD_CARROS',
                'Q012': 'QTD_GELADEIRA',
                'Q019': 'QTD_TV_COLORIDA',
                'Q024': 'QTD_COMPUTADOR',
                'Q025': 'ACESSO_INTERNET'}

df_enem_2023.rename(columns=renome_colunas, inplace=True)

## Renomeando as categorias de cada variável categórica

label_cores={0: 'Nao_declarado',
                1: 'Branca',
                2: 'Preta',
                3: 'Parda',
                4: 'Amarela',
                5: 'Indígena'}

df_enem_2023['COR']=df_enem_2023['COR'].map(label_cores)
df_enem_2023['COR'].value_counts().reset_index()

label_sexo={"F": "Feminino", "M": "Masculino"}
df_enem_2023['SEXO']=df_enem_2023['SEXO'].map(label_sexo)
df_enem_2023['SEXO'].value_counts().reset_index()

label_estado_civil={0:'Nao_informado',
                        1:	'Solteiro(a)',
                        2:	'Casado_Mora_com_companheiro',
                        3:	'Divorciado_Desquitado_Separado',
                        4:	'Viuvo'}
df_enem_2023['ESTADO_CIVIL']=df_enem_2023['ESTADO_CIVIL'].map(label_estado_civil)
df_enem_2023['ESTADO_CIVIL'].value_counts().reset_index()

label_tp_escola={1:	'Nao_Respondeu',
                     2:	'Publica',
                     3:	'Privada'}

df_enem_2023['ADM_ESC']=df_enem_2023['ADM_ESC'].map(label_tp_escola)
df_enem_2023['ADM_ESC'].value_counts().reset_index()

label_nacionalidade={0:	'Nao_informado',
                         1:	'Brasileiro',
                         2:	'Brasileiro_Naturalizado',
                         3:	'Estrangeiro',
                         4:	'Brasileiro_Nato_nascido_no_exterior'}

df_enem_2023['NACIONALIDADE']=df_enem_2023['NACIONALIDADE'].map(label_nacionalidade)
df_enem_2023['NACIONALIDADE'].value_counts().reset_index()

label_st_conclusao={1:	'Ja_conclui_Ensino_Medio',
                        2:	'Estou_cursando_concluirei_Ensino_Medio_em_2023',
                        3:	'Estou_cursando_e_concluirei_o_Ensino_Medio_apos_2023',
                        4:	'Nao_conclui_e_nao_estou_cursando_o_Ensino_Medio'}

df_enem_2023['ST_CONCLUSAO']=df_enem_2023['ST_CONCLUSAO'].map(label_st_conclusao)
df_enem_2023['ST_CONCLUSAO'].value_counts().reset_index()

label_faixa_etaria={1: "menor_que_17",
                        2:	"17",
                        3:	"18",
                        4:	"19",
                        5:	"20",
                        6:	"21",
                        7:	"22",
                        8:	"23",
                        9:	"24",
                        10:	"25",
                        11:	"26_30",
                        12: "31_35",
                        13:	"36_40",
                        14:	"41_45",
                        15:	"46_50",
                        16:	"51_55",
                        17:	"56_60",
                        18:	"61_65",
                        19:	"66_70",
                        20:	"maior_que_70"}

df_enem_2023['FAIXA_ETARIA']=df_enem_2023['FAIXA_ETARIA'].map(label_faixa_etaria)
df_enem_2023['FAIXA_ETARIA'].value_counts().reset_index()

label_tp_urbana_rural={1:'urbana',2:"rural"}

df_enem_2023['TP_URBANA_RURAL']=df_enem_2023['TP_URBANA_RURAL'].map(label_tp_urbana_rural)
df_enem_2023['TP_URBANA_RURAL'].value_counts().reset_index()

label_escolaridade_paterna={'A':'sem_escoladidade',
                            'B':'4ano_incompleto',
                            'C':'9ano_incompleto',
                            'D':'ensino_medio_incompleto',
                            'E': 'ensino_medio_completo',
                            'F': 'ensino_superior',
                            'G': 'pos_graducao_completa',
                            'H':'nao_sabe_responder'}

df_enem_2023['ESCOLARIDADE_PATERNA']=df_enem_2023['ESCOLARIDADE_PATERNA'].map(label_escolaridade_paterna)
df_enem_2023['ESCOLARIDADE_PATERNA'].value_counts().reset_index()

label_escolaridade_materna={'A':'sem_escoladidade',
                            'B':'4ano_incompleto',
                            'C':'9ano_incompleto',
                            'D':'ensino_medio_incompleto',
                            'E': 'ensino_medio_completo',
                            'F': 'ensino_superior',
                            'G': 'pos_graducao_completa',
                            'H':'nao_sabe_responder'}

df_enem_2023['ESCOLARIDADE_MATERNA']=df_enem_2023['ESCOLARIDADE_MATERNA'].map(label_escolaridade_materna)
df_enem_2023['ESCOLARIDADE_MATERNA'].value_counts().reset_index()

label_diarista={'A':'nao',
                'B': 'ate_2_vezes_semanais',
                'C': '3_a_4_vezes_semanais',
                'D': 'mais_5_vezes_semanais'}

df_enem_2023['POSSUI_DIARISTA']=df_enem_2023['POSSUI_DIARISTA'].map(label_diarista)
df_enem_2023['POSSUI_DIARISTA'].value_counts().reset_index()

label_banheiros={'A':'nao',
                'B': '1',
                'C': '2',
                'D': '3',
                'E':'mais_que_4'}

df_enem_2023['QTD_BANHEIROS']=df_enem_2023['QTD_BANHEIROS'].map(label_banheiros)
df_enem_2023['QTD_BANHEIROS'].value_counts().reset_index()

label_carros={'A':'nao',
            'B': '1',
            'C': '2',
            'D': '3',
            'E':'mais_que_4'}

df_enem_2023['QTD_CARROS']=df_enem_2023['QTD_CARROS'].map(label_carros)
df_enem_2023['QTD_CARROS'].value_counts().reset_index()

label_computador={'A':'nao',
                'B': '1',
                'C': '2',
                'D': '3',
                'E':'mais_que_4'}

df_enem_2023['QTD_COMPUTADOR']=df_enem_2023['QTD_COMPUTADOR'].map(label_computador)
df_enem_2023['QTD_COMPUTADOR'].value_counts().reset_index()

label_geladeira={'A':'nao',
                'B': '1',
                'C': '2',
                'D': '3',
                'E':'mais_que_4'}

df_enem_2023['QTD_GELADEIRA']=df_enem_2023['QTD_GELADEIRA'].map(label_geladeira)
df_enem_2023['QTD_GELADEIRA'].value_counts().reset_index()

label_tv={'A':'nao',
          'B': '1',
          'C': '2',
          'D': '3',
          'E':'mais_que_4'}

df_enem_2023['QTD_TV_COLORIDA']=df_enem_2023['QTD_TV_COLORIDA'].map(label_tv)
df_enem_2023['QTD_TV_COLORIDA'].value_counts().reset_index()

label_internet={'A':'nao',
                'B': 'sim'}

df_enem_2023['ACESSO_INTERNET']=df_enem_2023['ACESSO_INTERNET'].map(label_internet)
df_enem_2023['ACESSO_INTERNET'].value_counts().reset_index()

label_renda={'A': 'nenhuma_renda',
             'B': 'renda_ate_1320',
             'C': 'renda_1320_1980',
             'D': 'renda_1980_2640',
             'E': 'renda_2640_3300',
             'F': 'renda_3300_3960',
             'G': 'renda_3960_5280',
             'H': 'renda_5280_6600',
             'I': 'renda_6600_7920',
             'J': 'renda_7920_9240',
             'K': 'renda_9240_10560',
             'L': 'renda_10560_11880',
             'M': 'renda_11880_13200',
             'N': 'renda_13200_15840',
             'O': 'renda_15840_19800',
             'P': 'renda_19800_26400',
             'Q': 'renda_acima_26400'}

df_enem_2023['RENDA_FAMILIAR']=df_enem_2023['RENDA_FAMILIAR'].map(label_renda)
df_enem_2023['RENDA_FAMILIAR'].value_counts().reset_index()

## Tranformando dados categóricos

categoricas=['INSCRICAO',
              'FAIXA_ETARIA',
              'SEXO',
              'ESTADO_CIVIL',
              'COR',
              'NACIONALIDADE',
              'ST_CONCLUSAO',
              'ANO_CONCLUSAO',
              'MUNICIPIO',
              'UF',
              'ADM_ESC',
             'TP_URBANA_RURAL',
             'TP_PRESENCA_CH',
             'TP_PRESENCA_MT',
             'ESCOLARIDADE_PATERNA',
              'ESCOLARIDADE_MATERNA',
              'RENDA_FAMILIAR',
              'POSSUI_DIARISTA',
              'QTD_BANHEIROS',
              'QTD_CARROS',
              'QTD_GELADEIRA',
              'QTD_TV_COLORIDA',
              'QTD_COMPUTADOR',
              'ACESSO_INTERNET']

for cat in categoricas:
  df_enem_2023[cat] = df_enem_2023[cat].astype('category')

# Criação da variável região

#Devido ao grande número de estados brasileiros, é inviável computacionalmente dummizar a variável UF, sendo assim criaremos uma coluna que indica qual é a região do brasil que está localizada a escola.
regioes = {
    'AC': 'Norte', 'AP': 'Norte', 'AM': 'Norte', 'PA': 'Norte', 'RO': 'Norte', 'RR': 'Norte', 'TO': 'Norte',
    'AL': 'Nordeste', 'BA': 'Nordeste', 'CE': 'Nordeste', 'MA': 'Nordeste', 'PB': 'Nordeste', 
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RN': 'Nordeste', 'SE': 'Nordeste',
    'DF': 'Centro_Oeste', 'GO': 'Centro_Oeste', 'MT': 'Centro_Oeste', 'MS': 'Centro_Oeste',
    'ES': 'Sudeste', 'MG': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'RS': 'Sul', 'SC': 'Sul'
}

df_enem_2023['REGIAO']=df_enem_2023['UF'].map(regioes).astype('category')

#df_enem_2023['REGIAO']=df_enem_2023['REGIAO'].astype('category')

## Criação da variável média final

df_enem_2023['MEDIA']=(df_enem_2023['NOTA_CH']+df_enem_2023['NOTA_CN']+df_enem_2023['NOTA_LC']+df_enem_2023['NOTA_MT']+df_enem_2023['NOTA_REDACAO'])/5


#Tratamento dos dados faltantes

# Colunas do tipo float são as notas e recebem zero no lugar de NaN
colunas_float= ['NOTA_CN', 'NOTA_CH', 'NOTA_LC', 'NOTA_MT', 'NOTA_COMP1_REDACAO', 'NOTA_COMP2_REDACAO', 'NOTA_COMP3_REDACAO', 'NOTA_COMP4_REDACAO', 'NOTA_COMP5_REDACAO', 'NOTA_REDACAO']
for cate in colunas_float:
    df_enem_2023[cate].fillna(0, inplace=True)

# As colunas do tipo categóricas trocarão NaN por 'Desconhecido'
categorical_columns = ['MUNICIPIO','UF','ADM_ESC','TP_URBANA_RURAL','REGIAO']
for cate in categorical_columns:
    # Adiciona categoria e preenche NAs em uma única operação
    df_enem_2023[cate] = (
        df_enem_2023[cate]
        .cat.add_categories('Desconhecido')
        .fillna('Desconhecido')
    )

# Seleção dos candidatos que estavam presentes na prova de matemática

presentes_mt_df_enem_2023=df_enem_2023[df_enem_2023['INSCRICAO'].isin(presentes_mt)]

# Criação dos top_20. Entre as 20% maiores notas de matemática

nota_minima_top20=presentes_mt_df_enem_2023['NOTA_MT'].quantile(0.8)
df_enem_2023['IS_TOP20'] = np.where(df_enem_2023['NOTA_MT'] >= nota_minima_top20, 1, 0)
df_enem_2023['IS_TOP20'].value_counts(normalize=True)

# Observe que muitos candidatos podem compartilhar da mesma nota, por exemplo, vários candidatos podem tirar 0. 
# Por isso, ter nota acima de 645 não implica que voce está entre os 20% melhores candidatos. 
# Para que se mantenha a proporção e pegue exatamente os 20% dos melhores candidatos com maiores notas, 
# everíamos ter ordenado os candidatos por ordem decrescente de nota de matemática e ter selecionado os primeiros 20% de todos os candidatos.
# Observe a seguir que 136, dos 198, candidatos tiraram zero, ou seja, 68% zeraram.

# Seleção dos candidatos que estavam presentes em pelo menos uma prova
presentes_df_enem_2023=df_enem_2023[df_enem_2023['INSCRICAO'].isin(presentes_geral)]

# Seleção dos candidatos que estavam entre as 20% das maiores notas
candidatos_top20=df_enem_2023.loc[df_enem_2023['NOTA_MT']>nota_minima_top20].INSCRICAO
print(f'O total de candidatos que tiraram acima de {nota_minima_top20} é {len(candidatos_top20)}.')

top_20=df_enem_2023[df_enem_2023['INSCRICAO'].isin(candidatos_top20)]

print(f' Foram selecionadas {len(df_enem_2023.columns)} colunas  e {len(df_enem_2023)} observações. Destes {len(presentes_df_enem_2023)} presentes em pelo menos uma prova e {len(top_20)} entre os 20% melhores candidatos.')

print(f'As colunas selecionadas foram: {df_enem_2023.columns.tolist()}')

#Dumização das variáveis categóricas
colunas_dummies=['FAIXA_ETARIA', 
                'SEXO', 
                'COR', 
                'NACIONALIDADE',
                'REGIAO',       
                'ADM_ESC', 
                'TP_URBANA_RURAL', 
                'ESCOLARIDADE_PATERNA',       
                'ESCOLARIDADE_MATERNA', 
                'RENDA_FAMILIAR']

dados_analise=presentes_df_enem_2023[['INSCRICAO','FAIXA_ETARIA', 
                'SEXO', 
                'COR', 
                'NACIONALIDADE',
                'REGIAO',       
                'ADM_ESC', 
                'TP_URBANA_RURAL', 
                'ESCOLARIDADE_PATERNA',       
                'ESCOLARIDADE_MATERNA', 
                'RENDA_FAMILIAR', 'IS_TOP20']]

presentes_df_enem_2023_dummies = pd.get_dummies(dados_analise, columns=colunas_dummies, drop_first=True)

# Salvando os dataframes, que serão analisados e para algoritmos de machine learning, em um arquivo parquet
presentes_df_enem_2023.to_parquet('G://Meu Drive//ciencia de dados//Pos//TCC//TCC//presentes_df_enem_2023.csv', index=False)
top_20.to_parquet('G://Meu Drive//ciencia de dados//Pos//TCC//TCC//top_20.csv', index=False)
df_enem_2023.to_parquet('G://Meu Drive//ciencia de dados//Pos//TCC//TCC//df_enem_2023.csv', index=False)
presentes_df_enem_2023_dummies.to_parquet('G://Meu Drive//ciencia de dados//Pos//TCC//TCC//presentes_df_enem_2023_dummies.csv', index=False)