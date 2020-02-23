#εργασια 1
#Γράψτε ένα πρόγραμμα σε Python το οποίο βρίσκει τις πέντε μεγαλύτερες λέξεις ενός κειμένου το οποίο διαβάζει από αρχείο και τις εκτυπώνει ανάποδα, έχοντας αφαιρέσει τα φωνήεντα.

def fun(o):
    return len(o)

with open("testfile1.txt") as f:
    spy = f.read().replace('.','').replace(',','')
spy_2 = spy.split()
spy_2 = list(dict.fromkeys(spy_2))
spy_2.sort(key = fun)
katataksi = spy_2[::-1]
vowels = ('a','e','i','o','u','A','E','I','O','U')

 ena = katataksi[0]
 for i in ena:
    if i in vowels:
        ena = ena.replace (i,'')#εδω βγαζουμε το φωνηεν και το αντικαθιστουμε
 print (ena)#εμφανισε τη πρωτη καταταξη


dio = katataksi[1]
for i in dio:
    if i in vowels:
        dio = dio.replace (i,'')#εδω βγαζουμε το φωνηεν και το αντικαθιστουμε
print (dio)#εμφανισε την δευτερη καταταξη

tria = katataksi[2]
for i in tria:
    if i in vowels:
        tria= tria.replace (i,'')#εδω βγαζουμε το φωνηεν και το αντικαθιστουμε
print (tria)#εμφανισε την τριτη κατατξη

tessera = katataksi[3]
for i in tessera:
    if i in vowels:
        tessera = tessera.replace (i,'')#εδω βγαζουμε το φωνηεν και το αντικαθιστουμε
print (tessera)#εμφανισε την τεταρτη καταταξη

pente = katataksi[4]
for i in pente:
    if i in vowels:
        pente = pente.replace (i,'')#εδω βγαζουμε το φωνηεν και το αντικαθιστουμε
print (pente)
#εμφανισε την πεμπτη καταταξη
