# imports necessarios para rodar o codigo
import pandas as pd
import json

df = pd.read_excel("Taco-4a-Edicao.xlsx") # está lendo a planilha

df = df.loc[:, ~df.columns.str.contains('^Unnamed')] # aqui está retirando tudo que está com Unnamed

df = df.dropna(axis=1, how='all') #Retirando valores nulos

df = df[~((df['name'].isna()) | (df['name'] == 'Descrição dos alimentos'))] #retirando qualquer coisa que você queira q retire baseado no header que você deseja (ou coluna sei la)

df["calories"] = df["calories"].apply(lambda x: x if x == "*" or x == "Tr" else float(f"{float(x):.2f}")) # Aqui está virando tudo float com apenas 2 digitos depois da virgula ou ponto.

df["fat"] = df["fat"].apply(lambda x: x if x == "*" or x == "Tr" else float(f"{float(x):.2f}")) # Aqui está virando tudo float com apenas 2 digitos depois da virgula ou ponto.

df["carbs"] = df["carbs"].apply(lambda x: x if x == "*" or x == "Tr" else float(f"{float(x):.2f}")) # Aqui está virando tudo float com apenas 2 digitos depois da virgula ou ponto.

df["protein"] = df["protein"].apply(lambda x: x if x == "*" or x == "Tr" else float(f"{float(x):.2f}")) # Aqui está virando tudo float com apenas 2 digitos depois da virgula ou ponto.

dados = json.loads(df.to_json(orient='records', force_ascii=False, indent=4)) #Aqui inicia minha logica para inserir dados, mas vale resaltar que meu force_ascii está deixando que apareça com acentuação correta sem dar erro e uma identação de 4
for d in dados:
    d["name"] = {"en-US": "", "pt-BR": d["name"], "es-ES": ""}
    d["category"] = ""
    d["metricUnity"] = "grams"
    d["quantity"] = 100

    # Um loopzinho para adicionar categorias ou qualquer coisa que você queria

json.dump(dados, open("arquivo.json", "w"))
# Aqui retorna o arquivo e você pode ser feliz com seu arquivo.json!