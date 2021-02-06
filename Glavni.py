
from SkolaStranihJezika import Osoblje
from SkolaStranihJezika import Polaznici
from SkolaStranihJezika import Ponuda


print()
print("*****SkolaStranihJezika Script*****")
print()

def main():  
    if not login():          
        print()   
        print("\nNiste uneli dobro korisnicko ime i lozinku.")
        print()
        main()        
    else:     
        komanda = '0'                   
        if Osoblje.session["radnomesto"] == 'k':            
            while komanda != 'X':
                komanda = menuK()                
                if komanda == '1':
                    listaPonuda()
                elif komanda == '2':
                    pronadjiPolaznika()                   
                elif komanda == '3':
                    listaPolaznika()
                elif komanda == '4':
                    pretraziPolaznike()
                elif komanda == '5':
                    dodajPolaznika()
                elif komanda == '6':
                    brisiPolaznika()
                elif komanda == '7':
                    unosUplate()
                elif komanda == '8':
                    azurirajPolaznika()
                elif komanda == '9':
                    izdavanjeSertifikata()    
            print()        
            print("Hvala Vam sto koristite usluge nase skole. Prijatno!")
            print()            
        else:              
            while komanda != 'X':
                komanda = menuP()
                if komanda == '1':
                    polazniciPredavaca(Osoblje.session['sifra'])
                elif komanda == '2':
                    upisBodovaSaTesta()
            print()       
            print("Hvala Vam sto koristite usluge nase skole. Prijatno!")       
            print()   
       
def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return Osoblje.login(username, password)
    
def menuK():
    printMenuK()
    command = input(">> ")
    while command.upper() not in ('1', '2', '3', '4','5','6','7','8','9', 'X'):
        print()
        print( "\nUneli ste pogresnu komandu.\n")
        print()
        printMenuK()
        command = input(">> ")
    return command.upper()

def menuP():
    printMenuP()
    command = input(">> ")
    while command.upper() not in ('1', '2','X'):
        print()
        print( "\nUneli ste pogresnu komandu.\n")
        print()
        printMenuP()
        command = input(">> ")
    return command.upper()

def printMenuK():
    opis="Koordinator : "+Osoblje.session["ime"]+" "+Osoblje.session["prezime"]+" "+Osoblje.session["opis"]
    print()
    print ("Dobrodosli "+opis+" izaberite opciju")
    print()
    print ("1- Ponuda skole")
    print ("2- Pronalazenje polaznika")
    print ("3- Pregled svih polaznika")
    print ("4- Pretrazivanje polaznika")
    print ("5- Dodaj polaznika")
    print ("6- Brisi polaznika")
    print ("7- Unos uplate")
    print ("8- Izmena podataka polaznika")
    print ("9- Izdavanje sertifikata")
    print ("X- Za izlaz")

def printMenuP():
    opis="Predavac : "+Osoblje.session["ime"]+" "+Osoblje.session["prezime"]+" "+Osoblje.session["opis"]
    print()                        
    print ("Dobrodosli "+opis+" izaberite opciju")
    print()
    print ("1- Lista polaznika")
    print ("2- Unos bodova sa testiranja")
    print ("X- Za izlaz")
       

#  KOORDINATOR    
     
def listaPonuda():
    print()
    print("1- Ponuda skole")
    print()
    Ponuda.ponudaPrikaz()
    
def pronadjiPolaznika():
    print()
    print("2 - Pronalazenje polaznika")
    print()
    sifra = input("Unesite sifru polaznika: (<Enter> za kraj) >> ")
    polaznik = Polaznici.pronadjiPolaznika('sifra',sifra)
    if polaznik != None:
        print(Polaznici.formatHeader())
        print(Polaznici.formatPolaznik(polaznik))
    else:
        print()
        print("Nije pronadjen polaznik sa rednim brojem ", sifra)
        print()  

def listaPolaznika():
    print()
    print("3- Pregled svih polaznika")
    print()
    Polaznici.sortirajPolaznikeInt('sifra')
    print(Polaznici.formatHeader())
    print(Polaznici.formatSvePolaznike())
    print()          
    
def pretraziPolaznike():
    print()
    print("4- Pretrazivanje polaznika")
    print()
    prezime = input("Unesite prezime: (<Enter> za kraj) >>")
    polaznikList = Polaznici.pretraziPolaznike('prezime', prezime)
    if len(polaznikList) == 0:
        print()
        print("\nNema trazenih polaznika")
        print()
    else:
        print("\n")
        print(Polaznici.formatHeader())
        print(Polaznici.formatPolaznici(polaznikList))   
        print()
 
def dodajPolaznika():
    print()
    print ("5- Dodaj polaznika")
    print()
    Ponuda.ponudaPrikaz()
    polaznik = {}
    rbr=Polaznici.napraviRedniBroj()
    polaznik['sifra'] =rbr
    polaznik['ime'] = input("Unesite ime polaznika >> ")
    polaznik['prezime'] = input("Unesite prezime polaznika >> ")
    polaznik['email'] = input("Unesite email polaznika >> ")
    polaznik['brTel'] = input("Unesite telefon polaznika >> ")
    sifra = input("Unesite sifru kursa iz ponude (<Enter> za kraj) >> ")
    uplata = input("Unesite uplatu polaznika  (<Enter> za kraj) >> ")        
    while sifra != '' and uplata !='' :        
        pon=Ponuda.pronadjiPonudu('sifraPonude',sifra)        
        if pon==None :
            print()
            print("Uneli ste sifru ponude koja ne postoji")
            print()
            sifra = input("Unesite sifru kursa iz ponude (<Enter> za kraj)>> ")
            continue            
        else:          
                try:
                    uplata=float(uplata)
                    polaznik['sifraPonude'] = sifra
                    polaznik['uplata'] =   str(uplata)
                    polaznik['brojBodova'] = "0"
                    Polaznici.addPolaznik(polaznik)
                    print()
                    print( "Polaznik", polaznik['sifra']+" / "+polaznik['ime']+" "+polaznik['prezime'], "  je unet .")
                    print()
                    break
                except ValueError:
                    print()
                    print("Uplata mora biti broj ")
                    print()
                    uplata=input("Unesite uplatu polaznika (<Enter> za kraj)>> ")
                    continue       
    Polaznici.savePolaznici()

def brisiPolaznika():
    print()
    print ("6- Brisi polaznika")
    print()
    Polaznici.sortirajPolaznikeInt('sifra')
    print(Polaznici.formatHeader())
    print(Polaznici.formatSvePolaznike())
    print()
    sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
    polaznik = Polaznici.pronadjiPolaznika('sifra',sifra)
    while sifra != '':
        if polaznik == None:
            print()
            print("Ne postoji takva sifra")
            print()
        else:
            Polaznici.delPolaznik(polaznik);
            print()
            print( "Polaznik ", polaznik['sifra']+" / "+polaznik['ime']+" "+polaznik['prezime'], "  je obrisan !")
            print()            
        sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >>")
        polaznik = Polaznici.pronadjiPolaznika('sifra',sifra)                     
    Polaznici.savePolaznici()

def unosUplate():
    print()
    print ("7- Unos uplate")
    print()    
    Polaznici.sortirajPolaznikeInt('sifra')
    print()
    print(Polaznici.formatHeader())
    print(Polaznici.formatSvePolaznike())
    print()
    sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
    uplata = input("Unesite uplatu polaznika  (<Enter> za kraj) >> ")    
    while sifra != '' and uplata !='' :
        polaznik = Polaznici.pronadjiPolaznika('sifra',sifra)
        if polaznik == None :
            print()
            print( "Ne postoji polaznik sa unetom sifrom.")
            print()
            sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
            continue
        else:          
                try:
                    uplata=float(uplata)
                    Polaznici.unosUplate(polaznik, uplata)
                    print()
                    print( "Polazniku ", polaznik['sifra']+" / "+polaznik['ime']+" "+polaznik['prezime'], "  je uneta uplata.")
                    print()
                except ValueError:
                    print()
                    print("Uplata mora biti broj ")
                    print()
                    uplata = input("Unesite uplatu polaznika  (<Enter> za kraj) >> ")
                    continue               
        sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
        uplata = input("Unesite uplatu polaznika  (<Enter> za kraj) >> ")        
    Polaznici.savePolaznici()

def azurirajPolaznika():
    print()
    print ("8 - Izmena podataka polaznika")
    print()
    Polaznici.sortirajPolaznikeInt('sifra')
    print(Polaznici.formatHeader())
    print(Polaznici.formatSvePolaznike())
    print()
    sifra = input("Unesite sifru polaznika (<Enter> za kraj) >> ")
    polaznik=Polaznici.pronadjiPolaznika('sifra',sifra)
    if polaznik == None:
        print()
        print ("Ne postoji polaznik sa datom sifrom.")
        print()
    else:        
        polaznik['ime'] = input("Unesite ime polaznika >> ")
        polaznik['prezime'] = input("Unesite prezime polaznika >> ")
        polaznik['email'] = input("Unesite e-mail polaznika >> ")
        polaznik['telefon'] = input("Unesite telefon polaznika >> ")        
    Polaznici.savePolaznici()

def izdavanjeSertifikata():
    print()
    print ("9 - Izdavanje sertifikata")
    print()
    Polaznici.sortirajPolaznikeInt('sifra')
    print()
    print(Polaznici.formatHeader())
    print(Polaznici.formatSvePolaznike())
    print()
    sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
    polaznik= Polaznici.pronadjiPolaznika('sifra',sifra)    
    if polaznik == None :
        print()
        print( "Ne postoji polaznik sa unetom sifrom.")
        print()
        return    
    ponuda=Ponuda.pronadjiPonudu('sifraPonude',polaznik["sifraPonude"])    
    granicaBodova=50        
    if (float(ponuda["cena"])>float(polaznik["uplata"]) or float(polaznik["brojBodova"])<granicaBodova):
        print("**********")
        if float(ponuda["cena"])>float(polaznik["uplata"]):
            print()
            print("Polazniku ne moze biti izdat sertifikat jer nije uplatio ceo iznos ")
            print("**** Uplata : "+polaznik["uplata"]+" Cena : "+ponuda["cena"])
            print()                   
        if float(polaznik["brojBodova"])<granicaBodova:
            print()
            print("Polazniku ne moze biti izdat sertifikat jer nije dobio dovoljan broj bodova ")
            print("**** Bodovi : "+polaznik["brojBodova"]+" Granica : "+str(granicaBodova))
            print()            
    else:        
        print()
        print("Izdaje se sertifikat polazniku : "+polaznik["ime"]+" "+polaznik["prezime"]+" "+ponuda["jezik"]+" "+ponuda["nivo"])  
        print() 


#  PREDAVAC

def polazniciPredavaca(userId):
    print() 
    print("1- Lista polaznika")
    print()
    rezultat=Osoblje.pretraziPolaznikePredavaca(userId) 
    print()
    print("Predavac : "+Osoblje.session['sifra']+" / "+Osoblje.session['ime']+" "+Osoblje.session['prezime']+" "+Osoblje.session['opis']+" "+" Broj polaznika "+str(len(rezultat))) 
    print("\n")
    print(Polaznici.formatHeader())
    print(Polaznici.formatPolaznici(rezultat))
    print()
    return rezultat 

def upisBodovaSaTesta(): 
    print()   
    print( "2- Unos bodova sa testiranja")
    print()
    rezultat=polazniciPredavaca(Osoblje.session["sifra"])
    sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
    brojBodova = input("Unesite broj bodova polaznika  (<Enter> za kraj) >> ")    
    while sifra != '' and brojBodova !='' :
        polaznik = Polaznici.pronadjiPolaznika('sifra',sifra)
        if sifra not in [x["sifra"] for x in rezultat]:            
            print()
            print( "Ne postoji polaznik sa unetom sifrom.")
            print()
            sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
            continue
        else:
                try:                    
                    if not ( int(brojBodova)>=0 and int(brojBodova)<=100 ):
                        print()
                        print( "broj bodova mora biti [0-100].")
                        print()
                        brojBodova = input("Unesite broj bodova polaznika  (<Enter> za kraj) >> ")
                        continue                                      
                    Polaznici.upisBodova(polaznik,brojBodova)
                    print()
                    print( "Polazniku ", polaznik['sifra']+" / "+polaznik['ime']+" "+polaznik['prezime'], " su upisani bodovi.")
                    print()
                except ValueError:
                    print()
                    print("Broj bodova mora biti broj ")
                    print()
                    brojBodova = input("Unesite broj bodova polaznika  (<Enter> za kraj) >> ")
                    continue                
        sifra = input("Unesite sifru polaznika  (<Enter> za kraj) >> ")
        brojBodova = input("Unesite broj bodova polaznika  (<Enter> za kraj) >> ")
    Polaznici.savePolaznici()
      
if __name__ == '__main__':
    main()
