import pandas as pd
import numpy as np
import os

def distance_reader(path="data-ugradert/avstander.csv"):

    if not os.path.exists(path):
        print("Feil: CSV-fil mangler!")
        return None

    df = pd.read_csv(path, index_col=0)

    return df

df = distance_reader()

if df is not None:

    print("tilgjengelige steder: ")
    print(list(df.index))
    print()

    from_location = input("Skriv fra lokasjon: ")
    to_location = input("Skriv til lokasjon: ")

    if from_location in df.index and to_location in df.columns: 
        distance = df.loc[from_location, to_location]
        print(f"Avstanden fra {from_location} til {to_location} er {distance}")
    else:
        print("Feil: En av lokasjonene finnes ikke i matrisen.")

