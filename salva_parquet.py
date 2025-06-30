# Arquivos Parquet, normalmente ocupa menos espaço em disco que o formato csv e, por isso, é indicado quando se lida com grande volume de dados.
# Esse arquivo, especificamente, ocupa 1,65GB no formato csv e, 416 MB no formato parquet.
# O formato parquet foi desenvolvido pelo Apache e o dados são salvos em colunas. Ao contrário do formato CSV, o formato parquet salva as colunas 
# separadamente e carrega apenas as colunas que serão utilizadas. Esse formato é indicado para ambiente de big data e datalakes e, é compatível com 
# Apache Spark, Hive, AWS Athena, Google BigQuery e Pandas.

#Encontra o encoding do arquivo csv
import chardet

with open("G://Meu Drive//ciencia de dados//Pos//TCC//TCC//dados//enem//microdados_enem_2023//DADOS//MICRODADOS_ENEM_2023.csv", 'rb') as f:
    result = chardet.detect(f.read(1000))  # Lê todo o arquivo para detectar a codificação

print(result)  # Exibe a codificação detectada

#Banco de dados real, completo
df = pd.read_csv("G://Meu Drive//ciencia de dados//Pos//TCC//TCC//dados//enem//microdados_enem_2023//DADOS//MICRODADOS_ENEM_2023.csv", encoding= result['encoding'], sep=';')

#Salva df no formato parque com o nome enem_2023.parquet
df.to_parquet('enem_2023.parquet')

df.shape