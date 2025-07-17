
from datetime import datetime, timedelta
import pandas as pd

# === Funzione per chiedere input ===
def chiedi_data(prompt):
    while True:
        try:
            data_str = input(prompt + " (GG/MM/AAAA): ")
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("⚠️ Formato non valido. Riprova.")

def chiedi_float(prompt):
    while True:
        try:
            return float(input(prompt + ": "))
        except ValueError:
            print("⚠️ Inserisci un numero valido.")

def chiedi_int(prompt, minimo=1, massimo=6):
    while True:
        try:
            val = int(input(prompt + f" ({minimo}-{massimo}): "))
            if minimo <= val <= massimo:
                return val
            else:
                print(f"⚠️ Inserisci un numero tra {minimo} e {massimo}.")
        except ValueError:
            print("⚠️ Inserisci un numero intero valido.")

# === INPUT UTENTE ===
print("🧮 SIMULATORE DI INTERESSI COMPOSTI CON PUNTATE GIORNALIERE")
capitale_iniziale = chiedi_float("Inserisci il capitale iniziale")
data_inizio = chiedi_data("Inserisci la data di inizio")
data_fine = chiedi_data("Inserisci la data di fine")
puntate_giornaliere = chiedi_int("Inserisci il numero di puntate al giorno")

# === PARAMETRI FISSI ===
percentuale_scommessa = 0.01
percentuale_guadagno = 0.60
orari_standard = ["12:15", "18:15", "19:15", "10:00", "15:00", "21:00"]

# === SIMULAZIONE ===
capitale = capitale_iniziale
dati = []
giorno_simulazione = 0
data_corrente = data_inizio

while data_corrente <= data_fine:
    giorno_simulazione += 1
    for i in range(puntate_giornaliere):
        ora = orari_standard[i]
        guadagno = capitale * percentuale_scommessa * percentuale_guadagno
        capitale += guadagno
        dati.append({
            "Giorno": data_corrente.day,
            "Mese": data_corrente.month,
            "Anno": data_corrente.year,
            "Ora": ora,
            "Giorno Simulazione": giorno_simulazione,
            "Puntata": i + 1,
            "Guadagno netto": round(guadagno, 2),
            "Capitale": round(capitale, 2)
        })
    data_corrente += timedelta(days=1)

# === ESPORTAZIONE ===
df = pd.DataFrame(dati)
nome_file = f"simulazione_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
df.to_excel(nome_file, index=False)

print(f"✅ Simulazione completata! File creato: {nome_file}")
input("Premi INVIO per uscire.")
