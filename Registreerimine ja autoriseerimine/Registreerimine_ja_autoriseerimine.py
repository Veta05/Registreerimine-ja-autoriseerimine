import random
log_list=["Murik","Lili"]
pas_list=["123457","123456"]
def login(n: str,l:list):
    """Sisestatud kasutajanimi otsing

    Tagastab olemasolek järjendis bool formaadis
    :param str n: otsitav nimi
    :param list l:järjend
    :rtype: bool
    """
    if n in l:
        t=True
    else:
        t=False
    return t

def avtor(l:list,p:list):
    """Autoriseerib kasutaja

    Tagastab olemasolek logini ja parooli bool formaadis

    :param t:otsitavad andmed
    :rtype: bool
    """
    n=input("Sisesta oma kasutajanimi autoriseerimiseks: ")
    t=login(n,l)
    while t!=True:
        n=input("Sisesta veel kord oma nimi: ")
        t=login(n,l)
    pas=input("Sisesta salasõna: ")
    t=login(pas,p)
    if t==True and l.index(n)==p.index(pas):
        t=True
    else:
        t=False
    return t

def reg(v: str, l: list,p:list):
    """Inimese registreerimine

    Tagastab login ja salasõnade listid

    :param str v: kasutaja parooli loomise viis
    :rtype: list,list
    """
    t=login(input("Sisesta oma kasutaja nimi: "),l)
    while t==True:
        t=login(input("Sisesta veel kord oma kasutajanimi, andmebaasis on selline nimi"),l)
    if v=="a":
        pas=auto_reg(l,p)
    else:
        ise_reg(t,l,p)
    return l,p

def auto_reg(l:list,p:list):
    """Salasõna genireerimine

    Tagastab salasõna str formaadis

    :param str p: salasõna genereerimine
    :rtype: str
    """
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3)
    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    pas = ''.join([random.choice(ls) for x in range(12)]) # Извлекаем из списка 12 произвольных значений
    p.append(pas)
    print("Teie parool:", pas)
    print("Registreeritud")
    return pas


def ise_reg(t:str,l:list,p:list):
    """Parooli loomine

    Tagastab salasõna list formaadis

    :parap list u: kasutaja parool
    :rtype:list
    """
    log_list.append(t)
    pas=input("Sisesta parool: ")
    pas_list.append(pas)
    print("Registreeritud!")
    return l,p

while True:
    print("(r)Registreerimine,(a)autoriseerimine või (v)välja")
    v=input("Sinu valik: ")
    if v=="r":
        t=reg(input("(a)Auto või (i)ise?"),log_list,pas_list)
    elif v=="a":
        t=avtor(log_list,pas_list) #True, False
        if t:
            print("Tere tulemast!")
        else:
            print("Vale parool")
    else:
       v=input("Kas tahad registreerida? ")
       if v=="jah":
           print("Registreerimine")
           reg(input("(a)Auto või ise?"),log_list,pas_list)
       else:
           pass