import pandas as pd

krotkiNormal = []

def wczytajDane():
    global krotkiNormal
    # 1. Wczytujemy surowe dane pobrane z API
    df = pd.read_csv('dota_heroes.csv')
    
    # 2. Najpierw usuwamy bohaterów z brakującymi danymi (Kez, Largo)
    df = df.dropna()
    
    # 3. Oddzielamy tekst od liczb
    kolumny_tekstowe = df[['localized_name', 'primary_attr']]
    kolumny_liczbowe = df.drop(columns=['localized_name', 'primary_attr'])
    
    # 4. Bezpieczna normalizacja (unikamy dzielenia przez 0!)
    rozstep = kolumny_liczbowe.max() - kolumny_liczbowe.min()
    # Jeśli max-min wynosi 0, zamieniamy to na 1, żeby uniknąć błędu
    rozstep = rozstep.replace(0, 1) 
    
    df_znormalizowane = (kolumny_liczbowe - kolumny_liczbowe.min()) / rozstep
    
    # 5. Łączymy z powrotem tekst z liczbami
    df_gotowe = pd.concat([kolumny_tekstowe, df_znormalizowane], axis=1)
    
    # 6. Pakujemy do listy dla algorytmu K-means
    krotkiNormal.clear()
    for _, row in df_gotowe.iterrows():
        krotka = list(row)
        krotka.append(0) # Dodajemy miejsce na numer klastra na końcu (indeks 11)
        krotkiNormal.append(krotka)
        
    print(f"Dane wczytane! Liczba gotowych bohaterów: {len(krotkiNormal)}")

def normalizujDane():
    # Zostawiamy puste, bo normalizacja robi się automatycznie w wczytajDane()
    pass