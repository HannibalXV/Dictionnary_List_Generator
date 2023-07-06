#Input
name = input("name")
pr = input("prenom")
year = input("year")
phone = input("phone")
gy=input("graduation year")
club = input("club")
pet= input ("pet")
nameaftercap =name.capitalize()
#all choices with name and family 
res =name+pr
res1=nameaftercap+pr
res2=name+pr+"123"
res3=name+pr+"1234"
res4=name+pr+"0000"
res5=name+pr+phone
res6=nameaftercap+"_"+year
res7=nameaftercap+"_"+gy
res8=name+"_"+gy
res9=name+"_"+year
res10=name+name
res11=nameaftercap+pr+"123"
res12=nameaftercap+pr+"1234"
res13=nameaftercap+pr+"0000"
res133=nameaftercap+pr+"000"
res1335=nameaftercap+pr+"#"
res1334=nameaftercap+pr+"##"
res1333=nameaftercap+pr+"@@"
res1332=nameaftercap+pr+"@#@"
res14=nameaftercap+pr+phone
res15=nameaftercap+pr+"@"
res16=name+pr+"@"
res17=name+club
res18=club+name
res19=name+year
res20=nameaftercap+year
res12=name+pr+year
res13=nameaftercap+pr+year
reslist1=[]
reslist2=[]
reslist3=[]
reslist4=[]
for x in range(10):
    resfor=name+"190"+str(x)
    reslist1.append(resfor)
for ox in range(10,99):
    resfor2=name+"19"+str(ox)
    reslist2.append(resfor2)
for oxx in range(10):
    resfor3=name+"200"+str(oxx)
    reslist3.append(resfor3)
for oxxx in range(10,100):
    resfor4=name+"20"+str(oxxx)
    reslist4.append(resfor4)
reslist11=[]
reslist22=[]
reslist33=[]
reslist44=[]
for a in range(10):
    resfor=name+"_"+"190"+str(a)
    reslist11.append(resfor)
for oa in range(10,99):
    resfor2=name+"_"+"19"+str(oa)
    reslist22.append(resfor2)
for oaa in range(10):
    resfor3=name+"_"+"200"+str(oaa)
    reslist33.append(resfor3)
for oaaa in range(10,100):
    resfor4=name+"_"+"20"+str(oaaa)
    reslist44.append(resfor4)
# phone number
res21=(name[0].upper())+name[1]+phone
res211=(name[0].upper())+name[1]+phone+"@"
res212=(name[0].upper())+name[1]+phone+"@@"
res22=name+phone
res23=nameaftercap+phone
res233=nameaftercap+phone+"@"
res232=nameaftercap+phone+"@@"
res24=nameaftercap+"_"+phone
res25=name+"_"+phone
res26=phone+phone
res27=pr+phone
#regular repetetive
res28="password1234"
res29="password0000"
res30="12345678"
res31="00000000"
res32="azerty12345"
res33="azertyazerty123123"
res333="azertyazerty"
res34="azerty123"
res35="azertyazerty1234"
res36="P@ssword"
res37="Password1234"
res38="Password"
res39="Password0000"
res40="qwerty1234"
res41="Qwerty1234"
res42="qwerty12"
res43="qwerty123"
res44="qwerty12345"
res45="qwerty12346"
res46="qwertyqwerty"
res47="qwerty0000"
res48="qwerty1234"
res49=name+"0000"
res50=name+"1234"
res51=nameaftercap+"0000"
res52=nameaftercap+"1234"
res53="admin"
res54="Admin"
res55=["abc123"
,"letmein"
,"enter","admin","pass","access","secret","Welcome","welcome123","monkey"
,"monkey123","password1","welcome1","password","password123","Welcome123","qwerty"
,"passw0rd","p@ssword","login","PASSWORD","Password123","123456","111111","shadow"
,"maste","trezaq"]
#Club
res56=name+club
res57=name+club+"0000"
res58=name+pr+club
res59=name+name
res60=name+name+"123"
res61=name+name+"1234"
res62=name+name+"12345"
res63=name+name+"123456"
res64=name+name+"0000"
res65=name+club+"0000"
res66=nameaftercap+club
res67=nameaftercap+name
res68=name+nameaftercap
res69=phone+phone
res70=phone+phone+phone
res71=(name[0].upper())+name[1]+"@"+"12345678"
res72=(name[0].upper())+name[1]+"@"+"1234567"
res73=(name[0].upper())+name[1]+"@"+"123456"
res74=(name[0].upper())+name[1]+"@"+"12345"
res75=(name[0].upper())+name[1]+"@"+"1234"
res76=(name[0].upper())+name[1]+"@"+"123"
ot = pet+pet
ot1 = pet+name
ot2= name + pet
ot3=name + pet +"123"
ot4=name + pet + "123456"
ot5=name + pet + "1234"
ot6=name + pet + year
ot7=pet +phone
ot8=name.capitalize()+pet
ot8=pet+pr
ot9=pet+name+"0000"
ot10=pet+name+"123"
ot11=pet+name+"1234"
ot12=pet + name +"12345"
ot13=pet + name +"123456"
ot14 =pet+pet+pet
ot15=name+pet+name
ot16=pet+"azerty"
ot17=name+pet+pet
ot18=pet+pr
ot19=pet[0].upper()+pet[1]+phone
ot20 = pet
ot21=phone
ot22=phone+phone+phone
ot23=phone+phone
ot24=phone+"@"
ot25=phone+"@@"
ot26=name+name+name
ot27=name+name
ot28=nameaftercap+pr
ot29=pet+year+name
ot30=nameaftercap+name
ot31=name+nameaftercap
ot32=name+"!"
ot33=nameaftercap+"!"
ot34=name+"!!"
ot35=name+"!!!"
ot36=nameaftercap+"!!"
ot37=name+"1243"
ot38=nameaftercap+"1243"
ot39="Passw00d"
ot40=phone+name
ot41=phone+nameaftercap
ot42=nameaftercap+"123"+"@"
ot43=name+"123"+"@@"
ot44=nameaftercap+"123"+"@@"
ot45=name+"123"+"#"
ot46=nameaftercap+"123"+"#"
ot47=name+"69"
ot48=nameaftercap+"69"
ot49=name+"@"+"12345"
ot50=nameaftercap+"@"+"12345"
ot51=nameaftercap+"@"+"0000"
ot52=nameaftercap+"@"+"00000"
ot53=nameaftercap+"@"+"123"
ot54=nameaftercap+"@"+"123456"
ot55=nameaftercap+"@"+"12"
ot56=name+"@"+"12345"
ot57=name+"@"+"0000"
ot58=name+"@"+"00000"
ot59=name+"@"+"123"
ot60=name+"@"+"123456"
ot61=name+"@"+"12345!"
ot62=pr+"@"+"12345!"
ot63=pr.capitalize()+"@"+"12345!"
ot64=pr+"@"+"1234"
ot65=pr+"@"+"12345"
ot66= pet+"@"
ot67=pet+"@@"
ot68=pet.capitalize()+"@"
ot69=pet.capitalize()+"@@"
ot70=nameaftercap+"azerty"
ot71=nameaftercap+"azerty"
ot72="azerty"+name
ot73=ot72+"@"
ot74="azerty"+nameaftercap+"@"
ot75=name+"123456@@"
ot76=nameaftercap+"123456@@"
#01
res77=nameaftercap+"01"
res78=nameaftercap+"02"
res79=nameaftercap+"03"
res80=nameaftercap+"04"
res81=nameaftercap+"05"
res82=nameaftercap+"06"
res83=nameaftercap+"07"
res84=name+"01"
res85=name+"02"
res86=name+"03"
res87=name+"04"
res88=name+"05"
res89=name+"06"
res90=name+"07"
res91=name+"08"
res92=name+"09"
res93=name+"00"
res94=name+pr+"00"
res95=name+pr+"01"
res96=name+pr+"02"
res97=name+pr+"03"
res98=name+pr+"04"
res99=name+pr+"05"
res100=name+pr+"06"
res101=name+pr+"07"
res102=name+pr+"08"
res103=name+pr+"09"

#PET
petres=[]
petres2=[]
petres3=[]
petres4=[]
for p in range(10):
    petresa=pet+"_"+"200"+str(p)
    petres.append(petresa)

for pp in range(10,100):
    petresa1=pet+"_"+"20"+str(pp)
    petres2.append(petresa1)

for ppp in range(10):
    petresa3=pet+"_"+"190"+str(ppp)
    petres3.append(petresa3)

for pppp in range(10,99):
    petresaa4=pet+"_"+"19"+str(pppp)
    petres4.append(petresaa4)

file = open("Wordlost.txt", "w")
file.write(res +"\n" +res1+"\n"+res2+"\n"+res3+"\n"+res4+"\n"+res5+"\n"+res6+"\n"+res7+"\n"+res8+"\n"+res9
+"\n"+res10+"\n"+res11+"\n"+res12+"\n"+res13+"\n"+res14+"\n"+res15+"\n"+res16+"\n"+res17+"\n"+res18
+"\n"+res19+"\n"+res20+"\n"+res21+"\n"+res22+"\n"+res23+"\n"+res24+"\n"+res25+"\n"+res26+"\n"+res27+"\n"+res28+"\n"+res29+"\n"+res30
+"\n"+res31+"\n"+res32+"\n"+res33+"\n"+res34+"\n"+res34+"\n"+res35+"\n"+res36+"\n"+res37+"\n"+res38+"\n"+res39+"\n"+res40+"\n"+res41+"\n"
+res42+"\n"+res43+"\n"+res44+"\n"+res45+"\n"+res46+"\n"+res47+"\n"+res47+"\n"+res48+"\n"+res48+"\n"+res49+"\n"+res50+"\n"+res51+"\n"+res52+"\n"
+res53+"\n"+res54+"\n"+res56+"\n"+res57+"\n"+res58+"\n"+res59+"\n"+res60+"\n"+res61+"\n"+res62+"\n"+res63+"\n"+res64+"\n"+res65+"\n"
+res67+"\n"+res68+"\n"+res69+"\n"+res70+"\n"+res333+"\n"+res233+"\n"+res232+"\n"+res133+"\n"+res212+"\n"+res211+"\n"+res71+"\n"+res72+"\n"+res73+"\n"+res74+"\n"+res75+"\n"+res76+"\n"+res1332+"\n"+res1333+"\n"+res1334+"\n"+res1335+"\n"+ot+"\n"+ot1+"\n"+ot2+"\n"+ot3+"\n"+ot4+"\n"+ot5+"\n"+ot6+"\n"+ot7+"\n"+ot8+"\n"+ot9+"\n"+ot10+"\n"+ot11+"\n"+ot12+"\n"+ot13+"\n"+ot14+"\n"+ot15+"\n"+ot16+"\n"+ot17+"\n"+ot18+"\n"+ot19+"\n"+ot20+"\n"+ot21+"\n"+ot22+"\n"+ot23+"\n"+ot24+"\n"+ot25+"\n"+ot26+"\n"+ot27+"\n"+ot28+"\n"+ot30+"\n"+ot31+"\n"+ot29+"\n"+"\n"+ot29+"\n"+"\n"+ot29+"\n"+"\n"+ot30+"\n"+"\n"+ot31+"\n"
+"\n"+ot32+"\n"+ot33+"\n")
file.write(ot34+"\n"+ot35+"\n"+ot36+"\n"+ot37+"\n"+ot38+"\n"+ot39+"\n"+ot40+"\n"+ot41+"\n"+ot42+"\n"+ot43+"\n"+ot44+"\n"+ot45+"\n"+ot46+"\n"+ot47+"\n"+ot48+"\n"+ot49+"\n"+ot50
+"\n"+ot51+"\n"+ot52+"\n"+ot53+"\n"+ot54+"\n"+ot55+"\n"+ot56+"\n"+ot57+"\n"+ot58+"\n"+ot59+"\n"+ot60+"\n"+ot61+"\n"+ot62+"\n"+ot63+"\n"+ot64+"\n"+ot65+"\n"+name+"\n"+nameaftercap+"\n"+pet+"\n"+club+"\n"+ot66+"\n"+ot67+"\n"+ot68
+"\n"+ot69+"\n"+"\n"+ot70+"\n"+"\n"+ot71+"\n"+"\n"+ot72+"\n"+"\n"+ot73+"\n"+"\n"+ot74+"\n"+"\n"+ot75+"\n"+"\n"+ot76+"\n"+res77+"\n"+res78+"\n"+res79+"\n"+res80+"\n"+res81+"\n"+res82+"\n"+res83+"\n"+res84+"\n"+res85+"\n"+res86
+"\n"+res87+"\n"+res88+"\n"+res89+"\n"+res90+"\n"+res91+"\n"+res92+"\n"+res93+"\n"+res94+"\n"+res95+"\n"+res96+"\n"+res97+"\n"+res98+"\n"+res99+"\n"+res100+"\n"+res101+"\n"+res102+"\n"+res103+"\n")
file.write('\n'.join(reslist1))
file.write('\n')
file.write('\n'.join(reslist2))
file.write('\n')
file.write('\n'.join(reslist3))
file.write('\n')
file.write('\n'.join(reslist4))
file.write('\n')
file.write('\n'.join(reslist11))
file.write('\n')
file.write('\n'.join(reslist22))
file.write('\n')
file.write('\n'.join(reslist33))
file.write('\n')
file.write('\n'.join(reslist44))
file.write('\n')
file.write('\n'.join(petres))
file.write('\n')
file.write('\n'.join(petres2))
file.write('\n')
file.write('\n'.join(petres3))
file.write('\n')
file.write('\n'.join(petres4))
file.write('\n')
file.write('\n'.join(res55))
file.close
print('Done')
