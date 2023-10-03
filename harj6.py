import tkinter as tk
import winsound
import time
import threading
from matplotlib.colors import ListedColormap
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ikkuna=tk.Tk()
ikkuna.title("Exercise 5")
ikkuna.geometry("700x700")

# add five buttons to the top line of the window
koristetta=tk.Label(ikkuna,text="").grid(row=0,column=0)



img2 = tk.PhotoImage()
saari2=tk.Label(ikkuna,background="blue",image=img2,width=700,height=700)
saari2.place(x=0,y=0)

img = tk.PhotoImage()
saari=tk.Label(ikkuna,background="yellow",image=img,width=400,height=400)
saari.place(x=200,y=200)



allas=np.zeros((20,60))
fig2,ax2=plt.subplots(figsize=(3,1))
fig2.subplots_adjust(0,0,1,1,0,0)
#ax2.plot(allas,color="white")
for j in range(20):
     for i in range(60):
          allas[j,i]=1

ax2.matshow(allas, cmap=ListedColormap(["gold", "blue"]),vmin=-2,vmax=3)
ax2.set_axis_off()
fig2.set_facecolor("none")
fig2.set_frameon("False")
erikois_kanvas2=FigureCanvasTkAgg(fig2,master=ikkuna)
erikois_kanvas2.get_tk_widget().place(x=250,y=400)
erikois_kanvas2.draw()


oja=np.zeros((100,1))

for j in range(100):
     for i in range(1):
          oja[j,i]=0

fig1,ax1=plt.subplots(figsize=(0.2,2))
fig1.subplots_adjust(0,0,1,10,0,0)
ax1.matshow(oja,cmap=ListedColormap(["gold", "blue"]),vmin=-2,vmax=3)
ax1.set_axis_off()
fig1.set_facecolor("black")
erikois_kanvas=FigureCanvasTkAgg(fig1,master=ikkuna)
erikois_kanvas.get_tk_widget().place(x=250,y=200)

erikois_kanvas.draw()



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


def ernesti_laheta():
    
        
        monkey = tk.Label(ikkuna,text="")
        monkeypos=200
        monkey.place(x=monkeypos,y=150)
     
    
        while monkeypos < 500:
            time.sleep(0.001)
            
            monkey.place(x=monkeypos,y=150)
            monkeypos=monkeypos+3
            winsound.Beep(500,5)
        
        if monkeypos >= 500 and monkeypos < 550:
            winsound.Beep(2000,20)
            
            
            
            

def ernesti_laheta_thread():
    
    t=threading.Thread(target=ernesti_laheta)
    t.setDaemon = True
    t.start()

ernesti_laheta()
i_suppose_i_have_earned_so_much_points(3)
ikkuna.mainloop()
