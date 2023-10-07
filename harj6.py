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



monkey_img = Image.open("apina2.png")
monkey_img= monkey_img.resize((40,40))
monkey_img = ImageTk.PhotoImage(monkey_img)

saari_img = Image.open("saari4.png")
#saari_img= saari_img.resize((750,750))
saari_img = ImageTk.PhotoImage(saari_img)

# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)





img2 = tk.PhotoImage()
saari2=tk.Label(ikkuna,background="blue",image=img2,width=700,height=700)
saari2.place(x=0,y=0)

img = tk.PhotoImage()
saari=tk.Label(ikkuna,background="yellow",image=saari_img,width=600,height=380)
saari.place(x=100,y=197)



########################################### Allas

allas=np.zeros((20,60))
fig2,ax2=plt.subplots(figsize=(3,1))
fig2.subplots_adjust(0,0,1,1,0,0)

for j in range(20):
     for i in range(60):
          allas[j,i]=1

ax2m=ax2.matshow(allas, cmap=ListedColormap(["blue", "gold"]),vmin=-1,vmax=1)
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
ax1m = ax1.matshow(ernestin_oja,cmap=ListedColormap(["blue", "gold","yellow"]),vmin=-17,vmax=10)
ax1.set_axis_off()
fig1.set_facecolor("yellow")
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
ax3m = ax3.matshow(kernestin_oja,cmap=ListedColormap(["blue", "gold","yellow"]),vmin=-17,vmax=10)
ax3.set_axis_off()
fig3.set_facecolor("yellow")
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
######################################################################## ernesti

def ernesti_hae_apina():
 
    monkeypos_x=200
    monkeypos_y=400
    count=0
    monkey = tk.Label(ikkuna,image=monkey_img)
    fatigue=1
    checktime=0
    oja_pos=99
    break_var=0
    while monkeypos_y > 200 and break_var==0:
        
        winsound.Beep(800,60)
        while checktime < fatigue and break_var==0:
            time.sleep(1)
            checktime+=1
            if event.is_set():
                break_var=1
                
        ernestin_oja[oja_pos,0] =ernestin_oja[oja_pos,0]-1
        fatigue = fatigue*2
        ax1m.set_data(ernestin_oja)
        fig1.canvas.draw()
        fig1.canvas.flush_events()
            
        monkeypos_y=monkeypos_y-2
        count = count +1
        monkey.place(x=monkeypos_x,y=monkeypos_y)
        oja_pos=oja_pos-1
            
    monkey.destroy()    
    #i_suppose_i_have_earned_so_much_points(5)

    

def ernesti_hae_apina_thread():
    t=threading.Thread(target=ernesti_hae_apina)
    t.start()
    

def ernesti_sijoita_apina():

    oja_pos=random.randint(0,99)
    
    
    starting_oja_pos=oja_pos
    starting_pos_y=200+oja_pos*2
    switch=0
    startposswitch=0
    for i in range(12):
        
        if switch==0:
            if oja_pos <= 99:
                oja_pos+=7

        if switch==1:
            if oja_pos > 0:
                oja_pos-=7
            if startposswitch==0:
                monkeypos_y=starting_pos_y
                oja_pos=starting_oja_pos
                startposswitch=1


        if oja_pos >= 99:
            oja_pos=99
            switch=1
        if oja_pos <= 0:
            oja_pos=0
            switch=0

        monkeypos_y=200+oja_pos*2
        ernesti_sijoitettu_apina_thread(monkeypos_y=monkeypos_y,oja_pos=oja_pos)
           
        time.sleep(1)

     
        
def ernesti_sijoitettu_apina(monkeypos_y,oja_pos):
    monkeypos_x=200
    monkey = tk.Label(ikkuna,image=monkey_img)
    monkeypos_y=monkeypos_y
    oja_pos=oja_pos

    fatigue=1
    checktime=0
    break_var=0

    monkey.place(x=monkeypos_x,y=monkeypos_y)
    
    while monkeypos_y > 198 and break_var==0:
       
        

        winsound.PlaySound("dig.wav",winsound.SND_ASYNC)
        while checktime < fatigue and break_var==0:
            if event.is_set():
                break_var=1
            time.sleep(1)
            checktime+=1

        ernestin_oja[oja_pos,0] =ernestin_oja[oja_pos,0]-1    
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

def ernesti_sijoitettu_apina_thread(monkeypos_y,oja_pos):
    t=threading.Thread(target=ernesti_sijoitettu_apina,args=(monkeypos_y,oja_pos,))
    t.start()

def ernesti_sijoita_apina_thread():
    
    t=threading.Thread(target=ernesti_sijoita_apina)
    t.start()

#################################################################### kernesti

def kernesti_hae_apina():
    monkeypos_x=510
    monkeypos_y=400
    count=0
    monkey = tk.Label(ikkuna,image=monkey_img)
    fatigue=1
    checktime=0
    oja_pos=99
    break_var=0
    while monkeypos_y > 200 and break_var==0:
        
        kernestin_oja[oja_pos,0] =kernestin_oja[oja_pos,0]-1
        print(kernestin_oja[oja_pos,0])
        winsound.Beep(800,60)
        while checktime < fatigue and break_var==0:
            if event.is_set():
                break_var=1
            time.sleep(1)
            checktime+=1
            
        fatigue = fatigue*2
        ax3m.set_data(kernestin_oja)
        fig3.canvas.draw()
        fig3.canvas.flush_events()
            
        monkeypos_y=monkeypos_y-2
        count = count +1
        monkey.place(x=monkeypos_x,y=monkeypos_y)
        oja_pos=oja_pos-1
            
    monkey.destroy()
    

def kernesti_hae_apina_thread():
    
    t=threading.Thread(target=kernesti_hae_apina)
    t.start()

def kernesti_sijoita_apina():

    oja_pos=random.randint(0,99)
    
    
    starting_oja_pos=oja_pos
    starting_pos_y=200+oja_pos*2
    switch=0
    startposswitch=0
    for i in range(12):
        
        if switch==0:
            if oja_pos <= 99:
                oja_pos+=7

        if switch==1:
            if oja_pos > 0:
                oja_pos-=7
            if startposswitch==0:
                monkeypos_y=starting_pos_y
                oja_pos=starting_oja_pos
                startposswitch=1


        if oja_pos >= 99:
            oja_pos=99
            switch=1
        if oja_pos <= 0:
            oja_pos=0
            switch=0

        monkeypos_y=200+oja_pos*2
        kernesti_sijoitettu_apina_thread(monkeypos_y=monkeypos_y,oja_pos=oja_pos)
           
        time.sleep(1)

     
        
def kernesti_sijoitettu_apina(monkeypos_y,oja_pos):
    monkeypos_x=510
    monkey = tk.Label(ikkuna,image=monkey_img)
    monkeypos_y=monkeypos_y
    oja_pos=oja_pos

    fatigue=1
    checktime=0
    break_var=0

    monkey.place(x=monkeypos_x,y=monkeypos_y)
    
    while monkeypos_y > 198 and break_var==0:
       
        

        winsound.PlaySound("dig.wav",winsound.SND_ASYNC)
        while checktime < fatigue and break_var==0:
            if event.is_set():
                break_var=1
            time.sleep(1)
            checktime+=1

        kernestin_oja[oja_pos,0] =kernestin_oja[oja_pos,0]-1    
        fatigue = fatigue*2
        ax3m.set_data(kernestin_oja)
        fig3.canvas.draw()
        fig3.canvas.flush_events()
            
        monkeypos_y=monkeypos_y-2
        
        monkey.place(x=monkeypos_x,y=monkeypos_y)
        oja_pos=oja_pos-1
            
        
    monkey.destroy() 
    
    #i_suppose_i_have_earned_so_much_points(1)

def kernesti_sijoitettu_apina_thread(monkeypos_y,oja_pos):
    t=threading.Thread(target=kernesti_sijoitettu_apina,args=(monkeypos_y,oja_pos,))
    t.start()

def kernesti_sijoita_apina_thread():
    
    t=threading.Thread(target=kernesti_sijoita_apina)
    t.start()

def ojan_taytto():
  
    event.set()
    for j in range(100):
        for i in range(1):
            ernestin_oja[j,i]=1
            kernestin_oja[j,i]=1
    for j in range(100):
        for i in range(1):
            kernestin_oja[j,i]=1
            kernestin_oja[j,i]=1
    print("täytetty")
    time.sleep(5)
    #event.clear()

def oja_thread():
    
    t=threading.Thread(target=ojan_taytto)
    t.start()

def ernesti_oja_check():
    global oja_full
    oja_full=0
    n=0
    i=0
    while n==0:
        if i < 100:
            if ernestin_oja[i,0] < 1:
                ernestin_oja[i,0]=-10
                i+=1
                print(i)
                winsound.PlaySound("water.wav",winsound.SND_ASYNC)
                ax1m.set_data(ernestin_oja)
                fig1.canvas.draw()
                fig1.canvas.flush_events()
                time.sleep(0.07)
            if i==99:
                winsound.PlaySound("water.wav",winsound.SND_ASYNC)
                winsound.Beep(2000,100)
                oja_full=1
                n=1
                event.set()

def kernesti_oja_check():
    global oja_full
    oja_full=0
    n=0
    i=0
    while n==0:
        if i < 100:
            if kernestin_oja[i,0] < 1:
                kernestin_oja[i,0]=-10
                i+=1
                print(i)
                winsound.PlaySound("water.wav",winsound.SND_ASYNC)
                ax1m.set_data(ernestin_oja)
                fig3.canvas.draw()
                fig3.canvas.flush_events()
                time.sleep(0.07)
            if i==99:
                winsound.PlaySound("water.wav",winsound.SND_ASYNC)
                winsound.Beep(2000,100)
                oja_full=1
                n=1
                event.set()


def allas_check():
    global oja_full
    n=0
    i=0
    
    while n==0:
        if oja_full ==1:
                for j in range(20):
                     for i in range(60):
                        allas[j,i]=-1
               
                        #winsound.PlaySound("water.wav",winsound.SND_ASYNC)
                        ax2m.set_data(allas)
                        fig2.canvas.draw()
                        fig2.canvas.flush_events()
                        time.sleep(0.005)
                        if j ==19:
                            if i==59:
                                winsound.PlaySound("water.wav",winsound.SND_ASYNC)
                                n=1


                

def ernesti_oja_check_thread():
    
    t=threading.Thread(target=ernesti_oja_check)
    t.start()

def kernesti_oja_check_thread():
    
    t=threading.Thread(target=kernesti_oja_check)
    t.start()
            
            
def allas_check_thread():
    
    t=threading.Thread(target=allas_check)
    t.start()


ernesti_add_button = tk.Button(ikkuna, text ="ernesti lisää", command = ernesti_hae_apina_thread)
ernesti_add_button.place(x=50,y=50)

ernesti_place_button = tk.Button(ikkuna, text ="ernesti sijoita", command = ernesti_sijoita_apina_thread)
ernesti_place_button.place(x=50,y=140)

kernesti_add_button = tk.Button(ikkuna, text ="kernesti lisää", command = kernesti_hae_apina_thread)
kernesti_add_button.place(x=140,y=50)

ernesti_place_button = tk.Button(ikkuna, text ="kernesti sijoita", command = kernesti_sijoita_apina_thread)
ernesti_place_button.place(x=140,y=140)

ernesti_fill_button = tk.Button(ikkuna, text ="täytä ojat", command = oja_thread)
ernesti_fill_button.place(x=50,y=80)

ernesti_oja_check_thread()
kernesti_oja_check_thread()
allas_check_thread()
    
ikkuna.mainloop()
