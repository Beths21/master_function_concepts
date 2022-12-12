import random

#exo3
alphabet = "abcdefghijklmnopqrstuvwxyz"
n = 5

def mo_aleyatwa(alphabet,n):
    return "".join(random.sample(alphabet,n))

print("exo3")
mo = mo_aleyatwa( alphabet,n)
print(f"mo a se: {mo}\n")


#exo4
alpha_numerique = "abcdefghijklmnopqrstuvwxyz0123456789"
n = 5

def mo_aleyatwa_alfanimerik(alpha_numerique,n):
    return "".join(random.sample(alpha_numerique,n))

print("exo 4")
mo = mo_aleyatwa_alfanimerik(alpha_numerique,n)
print(f"kod la se: {mo}\n")


#exo5
phrase = "How !to move *to texas"
def slug(phrase):
    chaine_caractere_speciaux = "!#$%^*_`~"
    phrase_slug = phrase
    for char in chaine_caractere_speciaux:
        phrase_slug = phrase_slug.replace(char,"")
    phrase_slug = phrase_slug.replace(" ","-")
    phrase_slug = phrase_slug.replace("@","a")
    phrase_slug = phrase_slug.replace("&","e")
    return phrase_slug  

print("exo 5") 
slg = slug(phrase)
print(f"slug : {slg}\n")    

#exo6
mo = "Informatique"
def separation_lettre(mo):
    mo_1 = []
    for i in range(len(mo)):
        mo_1.append(mo[i])
    return ",".join(mo_1)
print("exo 6")    
sl = separation_lettre(mo)
print(f"separation avec virgule: {sl}\n")


#exo7
word = "ALO"
def cryptage(word):
    crypt_word = []
    for char in word.lower():
        crypt_word.append(str(ord(char)-97))
    crypt_word = "-".join(crypt_word)  
    return crypt_word 
print("exo 7")    
cw = cryptage(word)
print(f"code: {cw}\n")


#exo8
index_word = "0-11-14"
def decodage(index_word):
    index = index_word.split("-")
    char_value = []
    for i in index:
        char_value.append(chr(int(i)+97))
    char_value = "".join(char_value)    
    return char_value
print("exo 8")    
dcw = decodage(index_word)    
print(f"mo dekode: {dcw}\n") 


#exo9
n = 10
m = 20
def permutation(n, m):
    val_temporaire = n
    n = m
    m = val_temporaire
    return (n,m)
print("exo 9")
p =   permutation(n,m) 
print(f"permutation: {p}\n")   



#exo10
name = "Jean-Valdemar Bethsaida"
def pseudo_name(name):
    separation_name = name.split(" ")
    separation_name_without_hyphen = []
    initial_name = ""
    for name in separation_name:
        separation_name_without_hyphen += name.split("-")
    for name in separation_name_without_hyphen:
        initial_name += name[0]
    return initial_name 

print("exo 10")     
pseudo = pseudo_name(name)
print(f"pseudo nom an: {pseudo}\n")
  
