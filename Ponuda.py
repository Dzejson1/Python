
from SkolaStranihJezika import Osoblje

def pronadjiPonudu(field,sifra):
    for pon in ponuda:
        if pon[field] == sifra:
            return pon
    return None

def pretraziPonude(field, value):
    rezultat = []
    for pon in ponuda:
        if pon[field].upper() == value.upper():
            rezultat.append(pon)
    return rezultat
         
def ponudaPrikaz():    
    print("Br".center(2)+" "+"Jezik".center(10)+"Nivo".center(4)+"  "+"Predavac".center(15)+ "Cena".center(15))                                  
    print("---------------------------------------------------------")         
    for pon in ponuda:
        prof = Osoblje.pronadjiOsobu(pon["sifraProfesora"])
        if prof == None:
            profData="Nepoznat predavac !";            
        profData=prof["ime"]+" "+prof["prezime"]        
        s=pon["sifraPonude"].rjust(2)+" "+pon["jezik"].ljust(10)+pon["nivo"].center(4)+"  "+profData.ljust(15)+ " {0:>10.2f} din."                                                            
        print(s.format(float(pon["cena"])))        
    return ponuda

def loadPonuda():
    for line in open('ponuda.txt', 'r').readlines():
        if len(line) > 1:
            pon = strToPonuda(line)
            ponuda.append(pon) 
 
def strToPonuda(line):
    if line[-1] == '\n':
        line = line[:-1]
    sifraPonude, jezik, nivo, sifraProfesora, cena = line.split("|")
    pon= {
        'sifraPonude': sifraPonude,
        'jezik': jezik,
        'nivo': nivo,
        'sifraProfesora': sifraProfesora,
        'cena': cena
    }
    return pon      
                
ponuda = []
loadPonuda()   
