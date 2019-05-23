#https://www.lesswrong.com/posts/iJDrAuhByc8jJiFCE/constraints-and-slackness-reasoning-exercises
import tkinter as tk
from random import *
root=tk.Tk()
c = tk.Canvas(root)
c.pack(fill=tk.BOTH,expand=1)
xsz=root.wm_maxsize()[0]//2
pics={text:tk.PhotoImage(file=text+".png") for text in ("attack","defend","draw","energy")}
genemya=lambda:choice([0,0,0,0,1,1,2,3,4,6])
gprops=lambda :[3,0,0,0,10,10,genemya()]#Mana, Attack, Defence, deck pos, health, enemy health,enemy attack
props=gprops()#Mana, Attack, Defence, deck pos, health, enemy health,enemy attack
txtstr="Mana = %s  Attack = %s  Defence = %s\nDeck = %s  Health = %s  Enemy Health = %s  Enemy Attack = %s"
manatxt=c.create_text(xsz-200,100,text=txtstr%tuple(props),font=("sans",20))
freeze=False
class Card:
    cid=0
    def __init__(self,t):
        self.t=t
        self.img=pics[t]
        self.cid=Card.cid
        Card.cid+=1
        self.d=[]
        self.vis=False
    def show(self,x,y,w,h):
        self.d=[c.create_image(x,y,image=self.img)]#[c.create_rectangle(x,y,w,h),
        c.tag_bind(self.d[0],"<Button-1>",self.use)
    def hide(self):
        for i in self.d:
            c.delete(i)
    def use(self,e=None):
        if freeze: return
        if props[0]==0:
            return #no more mana
        props[0]-=1
        if self.t=="attack":
            props[1]+=1
        
        #print(self.t,self.cid)
        
        elif self.t=="defend":
            props[2]+=2
        elif self.t=="energy":
            props[0]+=2
        elif self.t=="draw":
            newval=max(props[3]-2,0)
            
            for i in range(newval,props[3]):
                cards[i].vis=True
            props[3]=newval
        self.vis=False
        show()

            

    
cards=[]#
for i,j in (("attack",6),("defend",6),("draw",4),("energy",4)):
    for k in range(j):
        cards.append(Card(i))
#Card("attack"),Card("attack"),Card("attack"),Card("defend"),Card("defend"),Card("defend"),Card("draw"),Card("draw")]
#shuffle(cards)
#cards[-1].vis=cards[-2].vis=cards[-3].vis=True
#props[3]=len(cards)-len(#number of starting cards
visCards=lambda :[i for i in cards if i.vis]

def show():
    for i in cards:
        i.hide()
    visC=visCards()
    fpos=xsz-len(visC)*40
    for i,j in enumerate(visC):
        j.show(fpos+i*80,300,0,0)
    c.itemconfig(manatxt,text=txtstr%tuple(props))
    
    if len(visC)==0 or props[0]==0:
        global freeze
        freeze=True
        print("reseting")
        root.after(800,rejig)
def reset():
    shuffle(cards)
    for i in cards:
        i.vis=False
    for i in cards[-5:]:
        i.vis=True
    #cards[-1].vis=cards[-2].vis=cards[-3].vis=True
    props[3]=len(cards)-len(visCards())#number of starting cards
    show()
def rejig():
    global freeze
    freeze=False
    
    
    props[5]=props[5]-props[1]
    props[4]-=max(props[6]-props[2],0)
    props[6]=genemya()
    props[0:3]=[3,0,0]
    rep=None
    if props[4]<=0:
        rep=tk.messagebox.askyesno("You lose","You lose\nWant to play again?")
            
    
    if props[5]<=0:
        rep=tk.messagebox.askyesno("You win","You win\nWant to play again?")
  
    if rep is True:
        global props
        props=gprops()
        
    if rep is False:
        root.destroy()
        return
    reset()
reset()
tk.mainloop()
#show()

#card=Card("attack")
#card.show(100,100,2,2)
#c.create_image(200,450,image=pics["draw"])
