import json

def update_Punkte(Name, Punkte_neu):
    with open("Punkte.json", "r") as file:
        Punkte_Auflistung = json.load(file)

    Punkte_Auflistung[Name] = Punkte_neu

    with open("Punkte.json", "w") as file:
        json.dump(Punkte_Auflistung, file)

def get_Punkte(Name):
    with open("Punkte.json", "r") as file:
        Punkte_Auflistung_str = file.read()
        Punkte_Auflistung = json.loads(Punkte_Auflistung_str)
        return Punkte_Auflistung[Name]



