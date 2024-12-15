Folosind un ESP32, scrieți un algoritm care generează o parolă random de 64 de caractere folosind alfabetul „9876543210qazwsxedcrfvtgbyhnmikolpQAZWSXEDCRFVTGBYHNUJOLP” și următorul algoritm de generare a numerelor random:

class PRNG:

    def __init__(self, seed=327680):

        self.seed = seed

        self.a = 4291010243

        self.c = 179203


    def random(self):

        self.seed = abs(self.a - self.seed * self.c) % 65536

        rnd = self.seed / 65536

        return rnd

Parola generată este secretă și rămâne doar pe ESP32. Pe laptop vom scrie un script în Python care încearcă să ghicească această parolă și va trimite parola către ESP32 pentru verificare. ESP32 va răspunde cu FALSE sau TRUE dacă parola a fost găsită sau nu.
