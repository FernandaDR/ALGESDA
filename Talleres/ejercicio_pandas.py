import pandas as pd

lista_mercado =pd.Series({"Frijol":3300,
                  "carne":15600,
                  "arroz":4900,
                  "papa":2200,
                  "aceite":9800,
                  "limones":2500,
                  "azucar":6400,
                  "sal":3300,
                  "cilantro":1000,
                  "huevos":8700})
print(lista_mercado)

lista_mercado_frame= pd.DataFrame({"enero":[3300,15600,4900,2200,9800],
                  "febrero":[3800,21000,5300,2700,11000],
                  "marzo":[4300,26000,5900,3100,12500],
                  "abril":[4900,30000,6200,3600,13400]},index=["frijol","carne","arroz","papa","aceite"])
print(lista_mercado_frame)
print(lista_mercado_frame[["febrero","marzo"]])
print(lista_mercado_frame[["abril"]])

