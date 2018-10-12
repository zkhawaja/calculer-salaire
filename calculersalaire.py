
def CalculerSalaire(metier, exp):
    if metier == "Architecte" and exp == 4:
        return "4000 euro"
    if metier == "médecin" and exp == 8:
        return "7000 euro"
    if metier == "consultant" and exp == 5:
        return "5000 euro"
    pass
print("salaire Architecte = ",CalculerSalaire("Architecte",4))
print("salaire médecin = ",CalculerSalaire("médecin",8))
print("salaire consultant = ",CalculerSalaire("consultant",5))
