
from SkolaStranihJezika import Ponuda
from SkolaStranihJezika import Polaznici


def login(username, password):
    for osoba in osoblje:
        if osoba['username'] == username and osoba['password'] == password:            
            session['sifra']=osoba["sifra"]
            session['ime']=osoba["ime"]
            session['prezime']=osoba["prezime"]
            session['radnomesto']=osoba["radnomesto"]
            session['username']=osoba["username"]
            session['password']=osoba["password"]
            session['opis']=osoba["opis"]
            return True       
    return False

def loadOsoblje():
    for line in open('osoblje.txt', 'r').readlines():
        if len(line) > 1:
            osoba = strToOsoba(line)
            osoblje.append(osoba)

def strToOsoba(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifra, ime, prezime, radnomesto, username, password, opis = line.split("|")
    osoba = {
        'sifra' : sifra,
        'ime': ime,
        'prezime': prezime,
        'radnomesto' : radnomesto,
        'username': username,
        'password': password,
        'opis': opis
    }
    return osoba
                        
def pronadjiOsobu(sifra):
    for osoba in osoblje:
        if osoba['sifra'] == sifra:
            return osoba
    return None           
 
def pretraziPolaznikePredavaca(userId):
    try:
        rezultat=Ponuda.pretraziPonude("sifraProfesora", userId)   
        rezultatPom=[x["sifraPonude"] for x in rezultat]
        return  list(filter(lambda x: (x["sifraPonude"] in rezultatPom),Polaznici.polaznici))
    except:
        print("Nema podataka !")
        return
    
session = {}      
osoblje = []  
loadOsoblje()     

