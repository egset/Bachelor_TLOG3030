import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.linalg import eigh


def distance_reader(path="data-ugradert/avstander.csv"):
    if not os.path.exists(path):
        print("Feil: CSV-fil mangler!")
        return None
    df = pd.read_csv(path, index_col=0)
    return df



def classical_mds(D, n_components=2):
    """
    Classical MDS: gjør om en avstandsmatrise D (nxn) til 2D-koordinater.
    """
    D = np.array(D, dtype=float)
    n = D.shape[0]

    # Kvadrer avstandene
    D2 = D ** 2

    # Sentreringsmatrise
    J = np.eye(n) - np.ones((n, n)) / n

    # Double centering
    B = -0.5 * J @ D2 @ J

    # Egenverdier/-vektorer
    evals, evecs = eigh(B)

    # Sorter synkende
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:, idx]

    # Unngå negative små egenverdier pga numerikk
    evals = np.maximum(evals, 0)

    # Koordinater: V * sqrt(L)
    L = np.diag(np.sqrt(evals[:n_components]))
    V = evecs[:, :n_components]
    X = V @ L
    return X




def plot_map(df, highlight=None):
    """
    df: DataFrame med avstander (index=steder, columns=steder)
    highlight: tuple (from_location, to_location) for å tegne linje
    """
    # Rydd opp navn og sørg for samme rekkefølge
    df.index = df.index.astype(str).str.strip()
    df.columns = df.columns.astype(str).str.strip()
    df = df.loc[df.index, df.index]  # samme rekkefølge rad/kolonne
    df = df.apply(pd.to_numeric, errors="raise")

    places = list(df.index)
    coords = classical_mds(df.to_numpy(), n_components=2)

    plt.figure()
    plt.scatter(coords[:, 0], coords[:, 1])

    for i, name in enumerate(places):
        plt.text(coords[i, 0], coords[i, 1], name)

    # Tegn linje mellom valgt fra/til hvis ønsket
    if highlight is not None:
        a, b = highlight
        a = str(a).strip()
        b = str(b).strip()
        if a in places and b in places:
            ia = places.index(a)
            ib = places.index(b)
            plt.plot(
                [coords[ia, 0], coords[ib, 0]],
                [coords[ia, 1], coords[ib, 1]],
                linewidth=2
            )

    plt.title("Kart generert fra avstandsmatrise (MDS)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()




# --- HOVEDPROGRAM ---
df = distance_reader()

if df is not None:
    print("tilgjengelige steder:")
    print(list(df.index))
    print()

    from_location = input("Skriv fra lokasjon: ").strip()
    to_location = input("Skriv til lokasjon: ").strip()

    if from_location in df.index and to_location in df.columns:
        distance = df.loc[from_location, to_location]
        print(f"Avstanden fra {from_location} til {to_location} er {distance}")
        # Tegn kart og marker ruten
        plot_map(df, highlight=(from_location, to_location))
    else:
        print("Feil: En av lokasjonene finnes ikke i matrisen.")
        # Tegn kart uansett (uten highlight)
        plot_map(df)



