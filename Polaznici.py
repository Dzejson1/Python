
from SkolaStranihJezika import Osoblje
from SkolaStranihJezika import Ponuda

def loadPolaznici():
    for line in open('polaznici.txt', 'r').readlines():
        if len(line) > 1:
            polaznik = strToPolaznik(line)
            polaznici.append(polaznik)

def strToPolaznik(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifra, ime, prezime, email, brTel, sifraPonude, uplata, brojBodova = line.split("|")
    polaznik= {
        'sifra': sifra,
        'ime': ime,
        'prezime': prezime,
        'email': email,
        'brTel': brTel,
        'sifraPonude': sifraPonude,
        'uplata': uplata,
        'brojBodova': brojBodova
    }
    return polaznik

def polaznikToStr(polaznik):
   
    return '|'.join([str(polaznik['sifra']), polaznik['ime'], polaznik['prezime'], polaznik['email'], polaznik['brTel'],
                     polaznik['sifraPonude'], polaznik['uplata'], polaznik['brojBodova']])

def formatHeader():
    return \
        "ID br.    |Ime         |Prezime     |Email             |Broj telefona  |Sif/Jezik/Nivo|Predavac       |Uplata   |Broj Bodova\n" \
        "----------+------------+------------+------------------+---------------+--------------+---------------+---------+------------"

def formatPolaznik(polaznik):
    try:
        pon=Ponuda.pronadjiPonudu('sifraPonude',polaznik['sifraPonude'])   
        prof=Osoblje.pronadjiOsobu(pon["sifraProfesora"])
    except:
        print("Nema podataka !")
        return    
    return "{0:10}|{1:12}|{2:12}|{3:18}|{4:15}|{5:14}|{6:15}|{7:9}|{8:13}".format(
        polaznik['sifra'],
        polaznik['ime'],
        polaznik['prezime'],
        polaznik['email'],
        polaznik['brTel'],
        pon['sifraPonude']+"/"+pon['jezik']+"/"+pon['nivo'],
        prof["ime"]+" "+prof["prezime"],
        polaznik['uplata'],
        polaznik['brojBodova']
    )

def formatPolaznici(polaznikList):    
        rezultat = ""
        for polaznik in polaznikList:
            rezultat += formatPolaznik(polaznik) + '\n'
        return rezultat

def formatSvePolaznike():
        return formatPolaznici(polaznici)

def napraviRedniBroj():    
    maxRbrPolaznik=max(polaznici, key=lambda x:int(x['sifra']))
    rbr=str(int(maxRbrPolaznik["sifra"])+1)    
    return rbr

def sortirajPolaznike(key,reverseValue=False):
    polaznici.sort(key= lambda x : x[key],reverse=reverseValue)

def sortirajPolaznikeInt(key,reverseValue=False):
    polaznici.sort(key= lambda x : int(x[key]),reverse=reverseValue)


def pronadjiPolaznika(field,value): 
    for polaznik in polaznici:
        if polaznik[field] == value:
            return polaznik
    return None

def pretraziPolaznike(field, value):    
    rezultat = []
    for polaznik in polaznici:
        if polaznik[field].upper() == value.upper():
            rezultat.append(polaznik)
    return rezultat


def upisBodova(polaznik,brojBodova):
    polaznik['brojBodova'] =brojBodova

def unosUplate(polaznik,uplata):
    polaznik['uplata'] =str(float(polaznik['uplata'])+float(uplata))

def savePolaznici():
    file = open('polaznici.txt', 'w')
    for polaznik in polaznici:
        file.write(polaznikToStr(polaznik))
        file.write('\n')
    file.close()
        
def addPolaznik(polaznik):
    polaznici.append(polaznik)
    
def delPolaznik(polaznik):
    polaznici.remove(polaznik)    


polaznici = []
loadPolaznici()

