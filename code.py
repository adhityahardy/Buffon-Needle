import turtle
import math
import random
import numpy as np

#menginput banyak jarum, panjang jarum, dan jarak antar garis
print("Banyak Jarum (N): ")
banyakjarum = int(input())
print("Panjang Jarum (l): ")
panjangjarum = int(input())
print("Jarak Garis (d): ")
jarakgaris = int(input())

#menetapkan garis dan speednya = 0
gambar = turtle.Turtle()
gambar.hideturtle()
gambar.speed(0)

smby = 180

#menggammbar garis
for i in range(0,10):
  gambar.penup()
  gambar.goto(-200,smby)
  gambar.pendown()
  gambar.goto(200,smby)
  smby-=jarakgaris

#memberi warna pada jarum
  gambar.color("black")
  hit = 0

#posisi jatuhnya jarum random
for needle in range(0,banyakjarum):
  x = random.randint(-180,180)
  y = random.randint(-180,180)
  
#sudut posisi jarum
  sudut = random.randint(0,360)
  if x <= panjangjarum * np.cos(sudut) or y <= panjangjarum * np.cos(sudut) :
            hit += 1
            
#menggambar jarum diatas kertas
  gambar.penup()
  gambar.goto(x,y)
  gambar.setheading(sudut)
  gambar.pendown()
  gambar.forward(panjangjarum)

#mencari nilai pi dari hasil percobaan
print ("Hasil :")
print("N = " + str(banyakjarum) + " (banyak jarum) ")
print("l = " + str(panjangjarum) + " (panjang jarum) " )
print("d = " + str(jarakgaris) + " (jarak antar garis) ")   
print("Q = " + str(hit) + " (banyaknya jarum yang menyentuh garis)")
pi = (2*panjangjarum*banyakjarum)/(jarakgaris*hit)
print("Pi percobaan yang didapat = "+ str(pi))
error = math.pi-pi
print("Error (pi percobaan - pi eksak) = " + str(error))
