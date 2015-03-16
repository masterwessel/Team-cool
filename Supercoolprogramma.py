def main():
    naamBestand = "sequence"
    leesBestand (naamBestand)
    
def leesBestand(bestand):
    lees = open (bestand, "r")
    startLezen = False
    gbSequentie = ""
    atcgSequentie = ""
    counter = 0
    for regel in bestand:
        if "ORIGIN" in regel:
            startLezen = True

        if startLezen == True:
            counter += 1

        if counter > 1:
            gbSequentie = gbSequentie + regel

    for letter in sequence:
        if letter in "atcg":
            atcgSequentie += letter
        
 #retourneert de sequentie uit het bestand
 #jacco
def bepaalGCpercentage (sequentie):
 #retourneert het GC percentage
 #joris
def schrijfHTMLrapport (gcPercentage, sequentie, bestandsnaam):
 #schrijft het HTML rapport met de naam bestandsnaam_rapport.html
 #wessel
main()
