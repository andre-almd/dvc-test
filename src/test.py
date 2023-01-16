import pandas as pd
import yaml

params = yaml.safe_load(open("params.yaml"))["params"]

dados = pd.read_csv("data/dados.csv", delimiter=";")

texto = f'{dados["nome"].values[0]} é um {dados["Profissao"].values[0]} e mora em {dados["cidade"].values[0]}. O Parametro de teste escolhido foi {params["param1"]}'

f = open("data/generated.txt", "w")
f.write(texto)
f.close()