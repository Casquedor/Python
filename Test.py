# a=10
# b=5
# c=a
# print('a='+str(a)+" b="+str(b)+" c="+str(c))
# print('a='+str(id(a))+" b="+str(id(b))+"  c="+str(id(c)))
# a=a+2
# print('a='+str(a)+" b="+str(b)+" c="+str(c))
# print('a='+str(id(a))+" b="+str(id(b))+"  c="+str(id(c)))
# Affectation paralléle
# print('Affectation paralléle')
# a,b=b,a
# print('a='+str(a)+" b="+str(b)+" c="+str(c))
#print('a='+str(id(a))+" b="+str(id(b))+"  c="+str(id(c)))
# Input
texte=input('Quel est votre âge ?')
if texte.isdecimal():
    print('Vous êtes né en ' + str(int(2022-float(texte))))
else:
    print("Erreur de saise")
#for i in range(10):
#    print(str(i).zfill(4))