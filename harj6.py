import tkinter as tk
import winsound
import time
import threading 
from matplotlib.colors import ListedColormap
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image



ikkuna=tk.Tk()
ikkuna.title("Exercise 6")
ikkuna.geometry("700x700")



monkey_img = Image.open("apina.png")
monkey_img= monkey_img.resize((40,40))
monkey_img = ImageTk.PhotoImage(monkey_img)

# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)





img2 = tk.PhotoImage()
saari2=tk.Label(ikkuna,background="blue",image=img2,width=700,height=700)
saari2.place(x=0,y=0)

img = tk.PhotoImage()
saari=tk.Label(ikkuna,background="yellow",image=img,width=400,height=400)
saari.place(x=200,y=200)



########################################### Allas

allas=np.zeros((20,60))
fig2,ax2=plt.subplots(figsize=(3,1))
fig2.subplots_adjust(0,0,1,1,0,0)

for j in range(20):
     for i in range(60):
          allas[j,i]=1

ax2.matshow(allas, cmap=ListedColormap(["blue", "gold"]),vmin=-2,vmax=3)
ax2.set_axis_off()
fig2.set_facecolor("none")
fig2.set_frameon("False")
erikois_kanvas2=FigureCanvasTkAgg(fig2,master=ikkuna)
erikois_kanvas2.get_tk_widget().place(x=250,y=400)
erikois_kanvas2.draw()

########################################### ernestin oja

ernestin_oja=np.zeros((100,1))

for j in range(100):
     for i in range(1):
         ernestin_oja[j,i]=1

fig1,ax1=plt.subplots(figsize=(0.02,2))
fig1.subplots_adjust(0,0,1,1,0,0)
ax1m = ax1.matshow(ernestin_oja,cmap=ListedColormap(["blue", "gold","yellow"]),vmin=-3,vmax=1)
ax1.set_axis_off()
fig1.set_facecolor("black")
erikois_kanvas=FigureCanvasTkAgg(fig1,master=ikkuna)
erikois_kanvas.get_tk_widget().place(x=250,y=200)

erikois_kanvas.draw()



########################################### kernestin oja
kernestin_oja=np.zeros((100,1))

for j in range(100):
     for i in range(1):
          kernestin_oja[j,i]=1

fig3,ax3=plt.subplots(figsize=(0.02,2))
fig3.subplots_adjust(0,0,1,1,0,0)
ax3m = ax3.matshow(kernestin_oja,cmap=ListedColormap(["blue", "gold","yellow"]),vmin=-3,vmax=1)
ax3.set_axis_off()
fig3.set_facecolor("black")
erikois_kanvas3=FigureCanvasTkAgg(fig3,master=ikkuna)
erikois_kanvas3.get_tk_widget().place(x=500,y=200)

erikois_kanvas3.draw()
#i_suppose_i_have_earned_so_much_points(1)
n=0
monkeypos=100
print(allas)

point_button=[]
for i in range(5):
    button_temp=tk.Button(ikkuna,text="Points: "+str(i+1),padx=40)
    button_temp.grid(row=0,column=i+1)
    point_button.append(button_temp)
def i_suppose_i_have_earned_so_much_points(amount_of_points):
    for i in range(5):
        point_button[i].configure(bg='gray')
    time.sleep(1)    
    for i in range(amount_of_points):
        point_button[i].configure(bg='green')
        winsound.Beep(440+i*100,500)


event = threading.Event()
##################################### ernesti

def ernesti_hae_apina():
 
    monkeypos_x=200
    monkeypos_y=400
    count=0
    monkey = tk.Label(ikkuna,image=monkey_img)
    fatigue=1
    oja_pos=99
    while monkeypos_y > 200:
        
        if event.is_set():
            break
        ernestin_oja[oja_pos,0] =ernestin_oja[oja_pos,0]-1

        winsound.Beep(800,60)
        time.sleep(fatigue)
        fatigue = fatigue*2
        ax1m.set_data(ernestin_oja)
        #ax1.matshow(ernestin_oja)
        fig1.canvas.draw()
        fig1.canvas.flush_events()
            
        monkeypos_y=monkeypos_y-2
        count = count +1
        monkey.place(x=monkeypos_x,y=monkeypos_y)
        oja_pos=oja_pos-1
            
        print("liikkuu<")
    monkey.destroy()    
    print(count)
    #i_suppose_i_have_earned_so_much_points(5)

    

def ernesti_hae_apina_thread():
    t=threading.Thread(target=ernesti_hae_apina)
    t.start()
    


def ernesti_sijoita_apina():

    oja_pos=random.randint(0,99)
    starting_pos=200+oja_pos*2
    switch=0
    startposswitch=0
    for i in range(10):
        

        monkeypos_y=200+oja_pos*2
        sijoitettu_apina_thread(monkeypos_y=monkeypos_y,oja_pos=oja_pos)
        if switch==0:
            if oja_pos < 93:
                oja_pos+=7
            else:
                switch=1
        if switch==1:
            if startposswitch==0:
                monkeypos_y=starting_pos
                startposswitch=1
            if oja_pos > 6:
                oja_pos-=7
            else:
                switch=0
        time.sleep(1)

     
        
def sijoitettu_apina(monkeypos_y,oja_pos):
    monkeypos_x=200
    monkey = tk.Label(ikkuna,image=monkey_img)
    monkeypos_y=monkeypos_y
    oja_pos=oja_pos

    fatigue=1
    checktime=0
    
    
    while monkeypos_y > 200:
        print("sijoitettu apina y ",monkeypos_y)
        print("ojapos ",oja_pos)
        if event.is_set():
            break
        ernestin_oja[oja_pos,0] =ernestin_oja[oja_pos,0]-1

        winsound.Beep(800,60)
        while checktime < fatigue:
            time.sleep(1)
            checktime+=1
            
        fatigue = fatigue*2
        ax1m.set_data(ernestin_oja)
        #ax1.matshow(ernestin_oja)
        fig1.canvas.draw()
        fig1.canvas.flush_events()
            
        monkeypos_y=monkeypos_y-2
        
        monkey.place(x=monkeypos_x,y=monkeypos_y)
        oja_pos=oja_pos-1
            
        
    monkey.destroy() 
    
    #i_suppose_i_have_earned_so_much_points(1)

def sijoitettu_apina_thread(monkeypos_y,oja_pos):
    t=threading.Thread(target=sijoitettu_apina,args=(monkeypos_y,oja_pos,))
    t.start()

def ernesti_sijoita_apina_thread():
    
    t=threading.Thread(target=ernesti_sijoita_apina)
    t.start()

#################################### kernesti

def kernesti_hae_apina():
    monkeypos_x=510
    monkeypos_y=400
    count=0
    monkey = tk.Label(ikkuna,image=monkey_img)
    fatigue=1
    checktime=0
    oja_pos=99

    while monkeypos_y > 200:
        if event.is_set():
            break
        kernestin_oja[oja_pos,0] =kernestin_oja[oja_pos,0]-1
        print(kernestin_oja[oja_pos,0])
        winsound.Beep(800,60)
        while checktime < fatigue:
            time.sleep(1)
            checktime+=1
            print(checktime)
        fatigue = fatigue*2
        ax3m.set_data(kernestin_oja)
        #ax1.matshow(ernestin_oja)
        fig3.canvas.draw()
        fig3.canvas.flush_events()
            
        monkeypos_y=monkeypos_y-2
        count = count +1
        monkey.place(x=monkeypos_x,y=monkeypos_y)
        oja_pos=oja_pos-1
            
        print("liikkuu<")
    print(count)
    monkey.destroy()
    

def kernesti_hae_apina_thread():
    
    t=threading.Thread(target=kernesti_hae_apina)
    t.start()


def ojan_taytto():
  
    event.set()
    for j in range(100):
        for i in range(1):
            ernestin_oja[j,i]=1
    for j in range(100):
        for i in range(1):
            kernestin_oja[j,i]=1
    print("täytetty")
    time.sleep(8)
    event.clear()

def oja_thread():
    
    t=threading.Thread(target=ojan_taytto)
    t.start()



     

#ernesti_hae_apina_thread() 
#kernesti_hae_apina_thread()
ernesti_sijoita_apina_thread()

ernesti_add_button = tk.Button(ikkuna, text ="ernesti lisää", command = ernesti_hae_apina_thread)
ernesti_add_button.place(x=50,y=50)

ernesti_place_button = tk.Button(ikkuna, text ="ernesti sijoita", command = ernesti_sijoita_apina_thread)
ernesti_place_button.place(x=50,y=140)

kernesti_add_button = tk.Button(ikkuna, text ="kernesti lisää", command = kernesti_hae_apina_thread)
kernesti_add_button.place(x=140,y=50)

ernesti_fill_button = tk.Button(ikkuna, text ="täytä ojat", command = oja_thread)
ernesti_fill_button.place(x=50,y=80)



    
ikkuna.mainloop()
