#Examen XalDigital análisis de datos con Python
#Carlos de la Rosa
import requests
import pandas as pd

url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
#Se verifica que url al menos exista
try:
    req = requests.get(url)
except:
    print("ERROR: url no encontrado")
#Transforma la información obtenida a un objeto JSON.
JSON_object = req.json()
#Se normaliza la información en base a la propiedad 'items' y se transforma a un DataFrame
df = pd.json_normalize(JSON_object['items'])

######PREGUNTA 2
##Cuántas respuestas fueron contestadas y cuántas no.
#Se cuentan los valores de la columna 'is_answered'.
answered = df[ ["is_answered"] ].value_counts()

#######PREGUNTA 3
"""Primero se obtiene el valor máximo del campo requerido y ese mismo valor se vuelve a usar
para poder obtener el n número de registros que tengan el mismo valor.
"""
best_reputation_row = df[df["owner.reputation"] == df["owner.reputation"].max()]
value = best_reputation_row["owner.reputation"].iloc[0]
best_reputation_row = df[df["owner.reputation"] == value]
best_reputation = best_reputation_row[["owner.reputation", "owner.user_id", "owner.display_name"]]


#######PREGUNTA 4

min_view_count_row = df[df["view_count"] == df["view_count"].min()]
value = min_view_count_row["owner.reputation"].iloc[0]
min_view_count_row = df[df["owner.reputation"] == value]
min_view_count = min_view_count_row[["question_id", "view_count", "title", "link"]]

#######PREGUNTA 5
oldest_ans_row = df[df["creation_date"] == df["creation_date"].min()]
value = oldest_ans_row["owner.reputation"].iloc[0]
oldest_ans_row = df[df["owner.reputation"] == value]
oldest_ans = oldest_ans_row[["question_id", "creation_date", "title", "link", "owner.user_id"]]

newest_ans_row = df[df["creation_date"] == df["creation_date"].max()]
value = newest_ans_row["owner.reputation"].iloc[0]
newest_ans_row = df[df["owner.reputation"] == value]
newest_ans = newest_ans_row[["question_id", "creation_date", "title", "link", "owner.user_id"]]
#######
###Display en consola de los resultados para cada pregunta.
print("PREGUNTA 2\nRespuestas que fueron contestadas (True) y las que no (False)")
count = 0
for ele in answered:
    if(answered.index[count][0] == True):
        temp = "contestadas (True)"
    else:
        temp = "no contestadas (False)"
    print("Total %s: %i" % (temp, ele) )
    count += 1


print("\n=====================================\n======================\n")
print("PREGUNTA 3\nOwner con la mejor reputacion:")
for ele in best_reputation.keys():
    print("%s: %s" % (ele, best_reputation[ele].values[0]) )

print("\n=====================================\n======================\n")
print("PREGUNTA 4\nRespuesta con el menor número de vistas:")
for ele in min_view_count.keys():
    print("%s: %s" % (ele, min_view_count[ele].values[0]) )

print("\n=====================================\n======================\n")
print("PREGUNTA 5\nRespuesta 5 con fecha de creación más antigua:")
for ele in oldest_ans.keys():
    print("%s: %s" % (ele, oldest_ans[ele].values[0]) )
print("\n=====================================\n======================\n")
print("Respuesta 5 con fecha de creación más reciente:")
for ele in newest_ans.keys():
    print("%s: %s" % (ele, newest_ans[ele].values[0]) )
