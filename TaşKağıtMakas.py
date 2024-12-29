# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 14:56:31 2023

@author: YASEMİN
"""

#TAŞ-KAĞIT-MAKAS-OYUNU
import random
liste=["Taş","Makas","Kağıt"]
pc=random.choice(liste)
kullanıcı=input('Bir karakter giriniz').capitalize()


print("Bilgisayar ",pc,"seçti")
print("Siz",kullanıcı,"seçtiniz.")

if pc==kullanıcı:
    print("berabere")
if pc=="Taş" and kullanıcı== "Kağıt":
    print("kazandınız")
if pc =="Kağıt" and kullanıcı=="Makas":
    print("kazandınız")
if pc=="Makas" and kullanıcı=="Taş":
    print("kazandınız")

if pc=="Taş" and kullanıcı== "Makas":
    print("kaybettiniz")
if pc =="Kağıt" and kullanıcı=="Taş":
    print("kaybettiniz")
if pc=="Makas" and kullanıcı=="Kağıt":
    print("kaybettiniz")
    