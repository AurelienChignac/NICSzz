# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:38:18 2021

@author: Aurélien
"""
########################################################################

from tkinter import Tk
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import NW
from tkinter import TOP
from tkinter import LEFT
from tkinter import RIGHT
from tkinter import Button
from tkinter import StringVar
from tkinter import Entry
from tkinter import Spinbox
from tkinter import Checkbutton
from tkinter import IntVar

from PIL import Image

import os
import sys

from tkinter.filedialog import askopenfilename
#######################################################################
#Fonction d'execution du programme

def execution():
	chemin=filename.get()
	#nombreDeTrans=int(Trans.get())
	print(chemin)
	#print(nombre_transitions)
	#glum(chemin,nombreDeTrans)
	#plan_normal()
	fonction(chemin)

	canvas_fond.create_text(10,245, anchor="w", text="Execution du programme...", fill="gray70")
	
##########################################################################

	liste1=chemin.split("/")
	nom_du_fichier="trash.txt"
	#nom_du_fichier="Generated_"+liste1[-1]
	#print(nom_du_fichier)
	fichier_com=open(chemin,"r")
	fichier_trash=open(nom_du_fichier,"w")

	nom_du_fichier_gen="Generated_"+liste1[-1]
	fichier_gen=open(nom_du_fichier_gen,"w")

	#fichier_gen.write("nbprocshare=8\n"+"%mem=8GB"+"% nmr=giao...................\n")
	

	liste=[]
	for ligne in fichier_com :
		#print(ligne)
		#lignes=fichier_com.readlines()
		liste.append(ligne)
		#print("LISTE :",liste)
	for element in liste:
		#print("element: ",element)
		fichier_gen.write(str(element))

	listeABCD=[]
	listeABCD.append(liste[int(atomeA.get())+5])
	listeABCD.append(liste[int(atomeB.get())+5])
	listeABCD.append(liste[int(atomeC.get())+5])
	listeABCD.append(liste[int(atomeD.get())+5])
	#print("Liste ABCD: ",listeABCD)
	
	listeABCD2=[]
	for j in range(len(listeABCD)):
		listeABCD2.append(listeABCD[j].split())
	print("listeABCD2:      ",listeABCD2)
	
	A=listeABCD2[0]
	B=listeABCD2[1]
	C=listeABCD2[2]
	D=listeABCD2[3]
	
	#origineBC= milieu de [BC]; coord.: xC-xB, yC-yB, zC-zB
	xorigine1=(float(C[1])+float(B[1]))/2
	yorigine1=(float(C[2])+float(B[2]))/2
	zorigine1=(float(C[3])+float(B[3]))/2
	print("origine 1 :",xorigine1,yorigine1,zorigine1)
	#origineAD
	xorigine2=(float(D[1])+float(A[1]))/2
	yorigine2=(float(D[2])+float(A[2]))/2
	zorigine2=(float(D[3])+float(A[3]))/2
	#origine totale = moyenne des deux
	xorigine=round(((xorigine1+xorigine2)/2),8)
	yorigine=round(((yorigine1+yorigine2)/2),8)
	zorigine=round(((zorigine1+zorigine2)/2),8)


	fichier_gen.write(" Bq                 "+("{:.8f}".format(xorigine))+"    "+("{:.8f}".format(yorigine))+"    "+("{:.8f}".format(zorigine))+"\n")

	#vecteur normal 1 : vecteur normal au plan ABC
	xvecteur1=((float(C[2])-float(A[2]))*(float(B[3])-float(A[3])))-((float(C[3])-float(A[3]))*(float(B[2])-float(A[2])))
	yvecteur1=((float(C[3])-float(A[3]))*(float(B[1])-float(A[1])))-((float(C[1])-float(A[1]))*(float(B[3])-float(A[3])))
	zvecteur1=((float(C[1])-float(A[1]))*(float(B[2])-float(A[2])))-((float(C[2])-float(A[2]))*(float(B[1])-float(A[1])))
	norme1=(xvecteur1**2+yvecteur1**2+zvecteur1**2)**(1/2)

	#vecteur normal 2 : vecteur normal au plan BCD
	xvecteur2=-((float(C[2])-float(B[2]))*(float(D[3])-float(B[3])))-((float(C[3])-float(B[3]))*(float(D[2])-float(B[2])))
	yvecteur2=-((float(C[3])-float(B[3]))*(float(D[1])-float(B[1])))-((float(C[1])-float(B[1]))*(float(D[3])-float(B[3])))
	zvecteur2=-((float(C[1])-float(B[1]))*(float(D[2])-float(B[2])))-((float(C[2])-float(B[2]))*(float(D[1])-float(B[1])))
	norme2=(xvecteur2**2+yvecteur2**2+zvecteur2**2)**(1/2)

	#Moyenne des vecteurs normalises
	xvecteurnormal=((xvecteur1/norme1)+(xvecteur2/norme2))/2
	yvecteurnormal=((yvecteur1/norme1)+(yvecteur2/norme2))/2
	zvecteurnormal=((zvecteur1/norme1)+(zvecteur2/norme2))/2
	norme=(xvecteurnormal**2+yvecteurnormal**2+zvecteurnormal**2)**(1/2)

	for i in range(80):
		xpoint1=round((xorigine+xvecteurnormal*i/norme/10),8)
		ypoint1=round((yorigine+yvecteurnormal*i/norme/10),8)
		zpoint1=round((zorigine+zvecteurnormal*i/norme/10),8)
		fichier_gen.write(" Bq                 "+("{:.8f}".format(xpoint1))+"    "+("{:.8f}".format(ypoint1))+"    "+("{:.8f}".format(zpoint1))+"\n")


	for j in range(80): 
		xpoint2=round((xorigine-xvecteurnormal*j/norme/10),8)
		ypoint2=round((yorigine-yvecteurnormal*j/norme/10),8)
		zpoint2=round((zorigine-zvecteurnormal*j/norme/10),8)
		fichier_gen.write(" Bq                 "+("{:.8f}".format(xpoint2))+"    "+("{:.8f}".format(ypoint2))+"    "+("{:.8f}".format(zpoint2))+"\n")


#	for k in range(80):
#		x1=round((xorigine+k*xvecteur1/norme1/10),8)
#		y1=round((yorigine+k*yvecteur1/norme1/10),8)
#		z1=round((zorigine+k*zvecteur1/norme1/10),8)
#		fichier_gen.write(" Bq                 "+("{:.8f}".format(x1))+"    "+("{:.8f}".format(y1))+"    "+("{:.8f}".format(z1))+"\n")
#
#	for l in range(80):
#		x1_2=round((xorigine-l*xvecteur1/norme1/10),8)
#		y1_2=round((yorigine-l*yvecteur1/norme1/10),8)
#		z1_2=round((zorigine-l*zvecteur1/norme1/10),8)
#		fichier_gen.write(" Bq                 "+("{:.8f}".format(x1_2))+"    "+("{:.8f}".format(y1_2))+"    "+("{:.8f}".format(z1_2))+"\n")
#
#	for m in range(80):
#		x2=round((xorigine+m*xvecteur2/norme2/10),8)
#		y2=round((yorigine+m*yvecteur2/norme2/10),8)
#		z2=round((zorigine+m*zvecteur2/norme2/10),8)
#		fichier_gen.write(" Bq                 "+("{:.8f}".format(x2))+"    "+("{:.8f}".format(y2))+"    "+("{:.8f}".format(z2))+"\n")
#
#	for n in range(80):
#		x2_2=round((xorigine-n*xvecteur2/norme2/10),8)
#		y2_2=round((yorigine-n*yvecteur2/norme2/10),8)
#		z2_2=round((zorigine-n*zvecteur2/norme2/10),8)
#		fichier_gen.write(" Bq                 "+("{:.8f}".format(x2_2))+"    "+("{:.8f}".format(y2_2))+"    "+("{:.8f}".format(z2_2))+"\n")

	
	fichier_com.close()
	fichier_trash.close()
	#os.remove("/trash.txt")

#######################################################################
# Fenetre graphique Tkinter du programme
fenetre=Tk()
fenetre.title("NICS ZZ")
fenetre.geometry("440x292+400+200")

canvas_fond=Canvas(width=440, height=292, bg="black")
canvas_fond.pack()

canvas_fond.create_text(210, 20, text="Selectionnez un fichier .gjf",font=('courier',12,'bold'), fill="gray70")

canvas_fond.create_text(50, 49, text="Fichier .gjf :", fill="gray70")

filename=StringVar()
entry=Entry(fenetre, textvariable=filename, fg='black',width=26)
canvas_fond.create_window(100, 40, anchor=NW, window=entry)
FILETYPES=[("gjf file", "*.gjf")]

#Permet d'ouvrir un fichier .gjf: place son chemin absolu dans le champ entry. Signale à l'utilisateur que le fichier
#a bien été ouvert : affiche "Ouverture du fichier" et le nom du fichier .gjf. Pour cela, le chemin absolu est séparé
#par "/" et le dernier élément de la liste obtenue est affiché
def set_filename():
	filename.set(askopenfilename(filetypes=FILETYPES))
	chaine=filename.get()
	chaine_coupee=chaine.split("/")
	#print(chaine_coupee)
	ouverture="Ouverture du fichier : "+chaine_coupee[-1]
	canvas_fond.create_text(10,225, anchor="w",text=ouverture, fill="gray70")

button=Button(fenetre, text="Parcourir", command=set_filename, bg="gray70", activebackground="gray70")
button.configure(width=10)
button.configure(height=1)
canvas_fond.create_window(324, 37, anchor=NW, window=button)

image_schema=PhotoImage(file="Picture.png")
wi=image_schema.width()

canvas_fond.create_image(300, 160, image=image_schema)

canvas_fond.create_text(50, 112, text="Atome A",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 140, text="Atome B",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 168, text="Atome C",font=('courier',12,'bold'), fill="gray70")
canvas_fond.create_text(50, 196, text="Atome D",font=('courier',12,'bold'), fill="gray70")

atomeA=StringVar()
entry_atomeA=Entry(fenetre, textvariable=atomeA, fg='black',width=5)
canvas_fond.create_window(100, 100, anchor=NW, window=entry_atomeA)

atomeB=StringVar()
entry_atomeB=Entry(fenetre, textvariable=atomeB, fg='black',width=5)
canvas_fond.create_window(100, 128, anchor=NW, window=entry_atomeB)

atomeC=StringVar()
entry_atomeC=Entry(fenetre, textvariable=atomeC, fg='black',width=5)
canvas_fond.create_window(100, 156, anchor=NW, window=entry_atomeC)

atomeD=StringVar()
entry_atomeD=Entry(fenetre, textvariable=atomeD, fg='black',width=5)
canvas_fond.create_window(100, 184, anchor=NW, window=entry_atomeD)

#Boutons permettant l'execution de la fonction execution et/ou la fermeture de la fenetre
bouton_exe=Button(fenetre, text ="Entrer", command=execution, bg="gray70")
bouton_exe.configure(width=10, activebackground="gray70")
bouton_exe_window=canvas_fond.create_window(400, 200, anchor=NW, window=bouton_exe)
bouton_quitter=Button(fenetre, text="Quitter", command=fenetre.quit, bg="gray70",activebackground="gray70")
bouton_quitter.configure(width=10)
bouton_quitter_window=canvas_fond.create_window(400, 200, anchor=NW, window=bouton_quitter)
canvas_fond.create_window(212, 254, anchor=NW, window=bouton_exe)
canvas_fond.create_window(325, 254, anchor=NW, window=bouton_quitter)


fenetre.mainloop()

