import csv

musicas_ano = {}

with open("spotify-2023.csv", "r", encoding="latin-1") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            year = int(row['released_year'])
            streams = int(row['streams'])
            track_name = row['track_name']
            artist_name = row["artist(s)_name"]
        except:
            continue  # Ignora linhas inválidas ou com múltiplos artistas
        
        if 2012 <= year <= 2022:
            if year not in musicas_ano or streams > musicas_ano[year][3]:
                musicas_ano[year] = [track_name, artist_name, year, streams]

lista_final = [musicas_ano[ano] for ano in range(2012, 2023)]
print(lista_final)
