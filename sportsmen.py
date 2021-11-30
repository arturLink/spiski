#EXAMPLE
#Kmd=[] #tühi järjend
#Km=10 #esimene päev
#print("1. päeval pikkus oli ",Km)
#Kmd.append(Km)
#for p in range(2,8):
	#Km*=1.1 # > 10%
	#Kmd.append(round(Km,2))
#print(Kmd)
#print(Kmd[2])
#print(Kmd.index(16.11)+1)
#Kmd.remove(10) #pop(0)
#print(Kmd,"Elemdid mis võrdub 16.11",Kmd.count(16.11))
#print(len(Kmd),"oN JÄÄNUD LISTIS")

#Indeks po4tovii TASK2
from random import *
spisok=[]
N=int(input("N "))
for i in range(N):
	spisok.append(randint(1,100))
print(spisok)
###
max_=max(spisok)
print(max_)
max_2=max(spisok)/len(spisok)
print(max_2)
ind=spisok.index(max_)
spisok.pop(ind)
spisok.insert(ind,max_2)
print(spisok)
###

#for s in spisok:
	#print(s)
#len(spisok)%2==0

#spisok_c=spisok.copy()
#spisok_c.reverse()
#print(spisok_c)

#first=spisok[0]
#last=spisok[N-1]#-1
#spisok.pop(0)
#spisok.insert(0,last)
#or
#spisok.remove(last)
#spisok.append(first)


#TASK1
#Maakonnad=["Tallinn","Narva","Kohtla-Järve","Ida-Virumaa Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while 1:
	#try:
		#index=int(input("Index "))
		#if len(str(index))==5:
			#break
	#except ValueError:
		#print("Valesti sisestatud index!!!!!!!!!!!!")
#i_list=list(str(index))
#print(str(index))
#print(i_list)
#s1=int(i_list[0])#1 ->0, 2 ->1...
#print(Maakonnad[s1-1])
#if s1 in [1,2,3]:
	#print("Jätka kodus")
#else:
	#print("Kanna maski")