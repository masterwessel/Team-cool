import re
import matplotlib.pyplot as pl
import numpy

def main():
    sequentie = readFile()
    aminoAcidSeq = makeCodons(sequentie)
    countCodons = coCodons(aminoAcidSeq)
    plot(countCodons)
    recP53(aminoAcidSeq)
    

def readFile():
    file = open("m_p53.gb", 'r')
    startReading = False
    sequence = ""
    sequentie = ""
    K = 0
    
    leesBestand = file.readlines()
    for regel in leesBestand:
        if "ORIGIN" in regel:
            startReading = True
            
        if startReading == True:
            K += 1
        
        if K > 1:
            sequence = sequence + regel
            
    for letter in sequence:
        if letter in "atcg":
            sequentie += letter

    return sequentie
                
def makeCodons(sequentie):
    codons = [sequentie[i:i+3] for i in range(0, len(sequentie),3)]
    print ("De codons zijn: ", codons)
    aminoAcidSeq = ""
    codonList = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
	'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
	'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
	'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
	'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
	'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
	'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
	'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
	'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
	'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
	'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
	'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
	'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
	'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
	'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
	'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}

    for codon in codons:
        aminoAcidSeq += codonList[codon]

    print (aminoAcidSeq)
    return aminoAcidSeq


def coCodons(aminoAcidSeq):
    count = {}
    for i in aminoAcidSeq:
        count[i]= count.get(i,0)+1
    print (count)
    return count

def plot(count):
    X = numpy.arange(len(count))
    pl.bar(X, list(count.values()), align='center', width =0.5)
    pl.xticks(X, list(count.keys()), rotation=60)
    ymax = max(list(count.values()))+1
    pl.ylim(0,ymax)

    pl.show()
    
def recP53(aminoAcidSeq):

    if re.search("MCNSSC(M|V)GGMNRR", aminoAcidSeq): 
        print ("Het eiwit p53 komt voor")
    else:
        print ("Het eiwit p53 komt niet voor")

main()
