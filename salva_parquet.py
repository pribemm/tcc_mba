#Encontra o encoding do arquivo csv
import chardet

with open("G:\Meu Drive\ciencia de dados\Pos\TCC\TCC\dados\enem\microdados_enem_2023\DADOS\MICRODADOS_ENEM_2023.csv", 'rb') as f:
    result = chardet.detect(f.read(1000))  # Lê todo o arquivo para detectar a codificação

print(result)  # Exibe a codificação detectada

#Banco de dados real, completo
df = pd.read_csv("G://Meu Drive//ciencia de dados//Pos//TCC//TCC//dados//enem//microdados_enem_2023//DADOS//MICRODADOS_ENEM_2023.csv", encoding= 'ISO-8859-1', sep=';')

#Salva df no formato parque com o nome enem_2023.parquet
df.to_parquet('enem_2023.parquet')

df.shape