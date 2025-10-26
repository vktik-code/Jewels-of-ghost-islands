import tkinter
import playsound
import pygame
import random
import win32gui, win32con, win32api

import threading
import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If running in development, use the current working directory
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

from PIL import Image, ImageTk
global pickkey2
global check,huse,huse1,huse2,huse3,huse4,huse5,huse6,Guideui,timeall,pick,gass,wheatb,beerb,Hpcontobt,ember,houseown,fact_id,pickupgrade,pickguid,overlay,Time,pickable4,pickable3,hp, hpmeter, maxhp, infslab1, infslab2, hppicknum, gm, text_id,dot,mmap,mappicknum,quest1redeem,gmbank,gmbank2,amm,ballance, padlo2, pickable1,dun1door,pickable2
pickable2=0
huse=0
check=False
huse1=0
huse2=0
huse3=0
huse4=0
huse5=0
huse6=0
Guideui=None
timeall=0
wheatb=None
gass=None
pick=None
beerb=None
Hpcontobt=None
houseown=0
fact_id=None
pickupgrade=0
pickguide=0
wtrsplash=None
pickkey2=0
pickable3=0
pickable4=0
dun1door=0
pickable1=0
ballance=0
amm=0
gmbank2=0
gmbank=0
quest1redeem=0
mappicknum=0
mmap=0
dot=0
text_id=0
maxhp = 100
hpmeter= 0
root = tkinter.Tk()
canvas = tkinter.Canvas(width="1024",height="768", bg="white")
Time = 4320
canvas.pack()
ember=None

hp=maxhp
gm = 0
gm_label = tkinter.Label(text=f"Ghosts Captured: {gm}", bg="blue", fg="white", font=("Arial", 16))
gm_label.pack()

hppicknum=0
overlay = None

# Textures
image = tkinter.PhotoImage(file=resource_path(r"karakter.png"))
image1 = tkinter.PhotoImage(file=resource_path(r"karakter bal.png"))
image2 = tkinter.PhotoImage(file=resource_path(r"karakter elo.png"))
image3 = tkinter.PhotoImage(file=resource_path(r"karakter hat.png"))
grass = tkinter.PhotoImage(file=resource_path(r"grass.png"))
tree = tkinter.PhotoImage(file=resource_path(r"tree.png"))
stone = tkinter.PhotoImage(file=resource_path(r"ko.png"))
house = tkinter.PhotoImage(file=resource_path(r"ház.png"))
ghost = tkinter.PhotoImage(file=resource_path(r"szellem.png"))
alap2 = tkinter.PhotoImage(file=resource_path(r"map2.png"))
infslab1 = tkinter.PhotoImage(file=resource_path(r"infslab.png"))
wall = tkinter.PhotoImage(file=resource_path(r"wall.png"))
enter = tkinter.PhotoImage(file=resource_path(r"cave enterance.png"))
cave_floor = tkinter.PhotoImage(file=resource_path(r"cave floor.png"))
equipment = tkinter.PhotoImage(file=resource_path(r"equipment.png"))
pickaxe = tkinter.PhotoImage(file=resource_path(r"pickaxe.png"))
broke = tkinter.PhotoImage(file=resource_path(r"brokenwall.png"))
key = tkinter.PhotoImage(file=resource_path(r"key.png"))
keyhole = tkinter.PhotoImage(file=resource_path(r"Keyhole.png"))
yellowgem = tkinter.PhotoImage(file=resource_path(r"Yellowgem.png"))
boss1 = tkinter.PhotoImage(file=resource_path(r"Boss.png"))
bosseye1 = tkinter.PhotoImage(file=resource_path(r"Bosseye.png"))
brickwall= tkinter.PhotoImage(file=resource_path(r"brickwall.png"))
door  = tkinter.PhotoImage(file=resource_path(r"door.png"))
roofb = tkinter.PhotoImage(file=resource_path(r"roofb.png"))
roofb2 = tkinter.PhotoImage(file=resource_path(r"roofb2.png"))
planks = tkinter.PhotoImage(file=resource_path(r"floor.png"))
Mmap = tkinter.PhotoImage(file=resource_path(r"Map.png"))
hpcont = tkinter.PhotoImage(file=resource_path(r"heart container.png"))
Mapscreen = tkinter.PhotoImage(file=resource_path(r"Mapscreen.png"))
Merchant = tkinter.PhotoImage(file=resource_path(r"Merchant.png"))
NPC = tkinter.PhotoImage(file=resource_path(r"NPC.png"))
door4k = tkinter.PhotoImage(file=resource_path(r"door4k.png"))
onswitch=tkinter.PhotoImage(file=resource_path(r"on switch.png"))
offswitch=tkinter.PhotoImage(file=resource_path(r"off switch.png"))
bulb1=tkinter.PhotoImage(file=resource_path(r"bulb1.png"))
healthbarfull=tkinter.PhotoImage(file=resource_path(r"healthbarfull.png"))
healthbarhalf=tkinter.PhotoImage(file=resource_path(r"healthbarhalf.png"))
healthbarlow=tkinter.PhotoImage(file=resource_path(r"healthbarlow.png"))
watersplash=tkinter.PhotoImage(file=resource_path(r"watrbosssplash.png"))
drop=tkinter.PhotoImage(file=resource_path(r"drop.png"))  
passport=tkinter.PhotoImage(file=resource_path(r"passport.png"))
beer=tkinter.PhotoImage(file=resource_path(r"beer.png"))
wheat=tkinter.PhotoImage(file=resource_path(r"wheat.png"))
guide=tkinter.PhotoImage(file=resource_path(r"guide.png"))
upgrade=tkinter.PhotoImage(file=resource_path(r"upgrade.png"))
gas=tkinter.PhotoImage(file=resource_path(r"gas.png"))
Loading=tkinter.PhotoImage(file=resource_path(r"loading.png"))
guideui=tkinter.PhotoImage(file=resource_path(r"guideui.png"))

loading1=canvas.create_image(512, 0, image=Loading,anchor="n")
root.update()
infslab2 = infslab1
pick_positions = []
pick_images = []

# variables
global x
global y
global ghost2, ghost3
global x2 ,x3
global y2 ,y3
global mapv
global a,b ,read ,ghost2_alive,textblob,wallbrokometer, keybrokometer, kh ,bosseye_alive,bosseyecap, eyestage, bosseyecap1, bosseye2_alive
global bosseye3_alive , bosseyecap2 ,pickkkey,gems, questpick1, hidfor, hppicknum2, switch1, switch2, switch3, switch4,stand,stand1,switch_id,switch_id1,lamp_id,lamp1,lamp2,lamp3,lamp4
global passport_hud_image,stand2,stand3,switch_id2,switch_id3,lamparr,xwtr,ywtr,watrbosshp, ghostbossw,wtrcounter,splcon,dropcon,dropcon2,droploc,pickkey3,bossinit,hppicknum3
global new1,new2,new3,new4,hppicknum6,pickkey4,passpamm,daveenter,dis_gh_cntr,bushlcntr,wheat_hud_image,webtype,weblev,wepquestfin,guide_images,upgrade_images,gas_hud_image,tankq,tankqred
tankqred=0
new1=0
new2=0
new3=0
new4=0
hppicknum6=0
pickkey4=0
tankq=0
gas_hud_image=None
wepquestfin=0
weptype=[]
weplev=2
wheat_hud_image=None
bushlcntr=0
beer_hud_image=None
dis_gh_cntr=0
daveenter=0
passpamm=0
hppicknum3=0
bossinit=0
pickkey3=0
droploc=0
dropcon2=0
dropcon=0
splcon=0
wtrcounter=0
upgrade_images = []
watersplash_images = []
ghostbossw = None
guide_images = []
healthfull_images = []
healthhalf_images = []
healthlow_images = []
watrbosshp=3
xwtr=512
ywtr=128
lamparr=[]
lamp1=0
lamp2=0
lamp3=0
lamp4=0
stand1=0
stand2=0
stand3=0
switch_id = None
switch_id1 = None
switch_id2 = None
switch_id3 = None
stand = 0
lamp_id = None
stand=0
switch1=1
switch2=1
switch3=1
switch4=1
hppicknum2=0
hidfor=""
questpick1=0
bulb1_images = []
Mpcontobt_images = []
Mpcontobt_positions = []
Door4k_positions = []
hpcontobt_images = []
hpcontobt_positions = []
mapobt_images = []
mapobt_positions = []
roofb_positions = []
roofb2_positions = []
brickwall_positions = []


gems = 0


bosseyecap2 = 1
bosseyecap1 = 1
eyestage=0
bosseyecap = 1
pickkey = 0
kh = None
wallbrokometer = 0
keybrokometer = 0
textblob = 0
x3 = 800
y3 = 200
ghost3 = 0
ghost2_alive = True
bosseye_alive = False
bosseye2_alive = True
bosseye3_alive = True
read=0
a=500
b=500
mapv=1
true =True
x2 = 300
y2 = 300

x=638
global ghost_alive, ghost4, ghost5, ghost6
ghost_alive = True
gm=0
y=432

ghost2 = 0
ghost4 = 0
ghost5 = 0
ghost6 = 0
tree_images = []
drop_images = []
stone_images = []
house_images = []
stone_positions = []
ghost_images = []
wall_positions = []
wall_images = []
yellowgem_positions = []
yellowgem_images = []
key_positions = []
key_images = []
eq_positions = []
eq_images = []
keyhole_positions = []
keyhole_images = []
bosseye_positions = []
bosseye_images = []
boss1_positions = []
boss1_images = []
pickaxe_equipped_image = None
equipment_logo_id = None
pickaxe_hud_image = None
key_hud_image = None
passport_hud_image=None
c=1
tree_positions=[]
Infslab_images = []
Infslab_positions = []
wallb_images = []
wallb_positions = []
hpe=100

tree_x = 100
tree_y = 100
global tool, pickable ,pickused, hppicknum1,hppicknum4,hppicknum5 
hppicknum4 = 0
hppicknum5 = 0
hppicknum1 = 0
pickable = 0
tool = 0
pickused=0
global xp,yp
xp=0
yp=0
global eqtool, Map3, Map4, Map5, Map6,Map7,Map8,gameover,padlo3
eqtool = ""
global x4,y4, x5, y5, x6, y6
x4=300
y4=200
x5=700
y5=400
x6=800
y6=200
def makeTransparent(img, colorToMakeTransparentInHexFormat):
    newPhotoImage = tkinter.PhotoImage(width=img.width(), height=img.height())
    for x in range(img.width()):
        for y in range(img.height()):
            rgb = '#%02x%02x%02x' % img.get(x, y)
            if rgb != colorToMakeTransparentInHexFormat:
                newPhotoImage.put(rgb, (x, y))
    return newPhotoImage
def makeTransparent_optimized(filename, colorToMakeTransparentInHexFormat):
    img = Image.open(filename).convert('RGBA')
    hex_color = colorToMakeTransparentInHexFormat.lstrip('#')
    transparent_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)
    transparent_pixel = transparent_color[:3] + (0,)

    data = img.getdata()
    new_data = []
    for item in data:
        if item[:3] == transparent_color[:3]:
            new_data.append(transparent_pixel)
        else:
            new_data.append(item)

    img.putdata(new_data)
    
    final_tk_image = ImageTk.PhotoImage(img)
    
    return final_tk_image
global newpickImage
newpickImage = makeTransparent(pickaxe, "#ffffff")
global newgasImage
newgasImage = makeTransparent(gas, "#ffffff")
global newkeyImage
newkeyImage = makeTransparent(key, "#ffffff")
Cherry=makeTransparent_optimized(resource_path(r"cherry.png"), "#ffffff")
Seven=makeTransparent_optimized(resource_path(r"seven.png"), "#ffffff")

watrboss_images = []
watrboss=tkinter.PhotoImage(file=resource_path(r"watrboss.png"))
newwatrbossImage = makeTransparent(watrboss, "#ffffff")
watrboss_images.append(newwatrbossImage) 
# text blobs

def load_text():
    # Global assignments are essential for thread communication
    global textblob48,textblob49,textblob50,textblob51,Title,textblob47,textblob46,textblob45,textblob44,textblob43,textblob42,textblob41, textblob40, textblob39, textblob1, textblob2, textblob3, textblob4, textblob5, textblob6, textblob7, textblob8, textblob9, textblob10, textblob11, textblob12, textblob13, textblob14, textblob15, textblob16, textblob17, textblob18, textblob19, textblob20, textblob21, textblob22, textblob23, textblob24, textblob25, textblob26, textblob27, textblob28, textblob29, textblob30, textblob31, textblob32, textblob33, textblob34, textblob35, textblob36, textblob37, textblob38, factint, factint1, factint2, factint3

    # All calls now use the fast, one-step function: makeTransparent_optimized(filename, color)
    textblob1 = makeTransparent_optimized(resource_path(r"textblob.png"), "#ffffff")
    print("The loading is ready for textblob1", flush=True)
    textblob2 = makeTransparent_optimized(resource_path(r"textblob1.png"), "#ffffff")
    print("The loading is ready for textblob2", flush=True)
    textblob3 = makeTransparent_optimized(resource_path(r"textblob2.png"), "#ffffff")
    print("The loading is ready for textblob3", flush=True)
    textblob4 = makeTransparent_optimized(resource_path(r"textblob3.png"), "#ff0000")
    print("The loading is ready for textblob4", flush=True)
    textblob5 = makeTransparent_optimized(resource_path(r"textblob4.png"), "#ff0000")
    print("The loading is ready for textblob5", flush=True)
    textblob6 = makeTransparent_optimized(resource_path(r"textblob5.png"), "#ff0000")
    print("The loading is ready for textblob6", flush=True)
    textblob7 = makeTransparent_optimized(resource_path(r"textblob6.png"), "#ff0000")
    print("The loading is ready for textblob7", flush=True)
    textblob8 = makeTransparent_optimized(resource_path(r"textblob7.png"), "#ff0000")
    print("The loading is ready for textblob8", flush=True)
    textblob9 = makeTransparent_optimized(resource_path(r"textblob8.png"), "#ff0000")
    print("The loading is ready for textblob9", flush=True)
    textblob10 = makeTransparent_optimized(resource_path(r"textblob9.png"), "#ff0000")
    print("The loading is ready for textblob10", flush=True)
    textblob11 = makeTransparent_optimized(resource_path(r"textblob10.png"), "#ff0000")
    print("The loading is ready for textblob11", flush=True)
    textblob12 = makeTransparent_optimized(resource_path(r"textblob11.png"), "#ffffff")
    print("The loading is ready for textblob12", flush=True)
    textblob13 = makeTransparent_optimized(resource_path(r"textblob12.png"), "#ff0000")
    print("The loading is ready for textblob13", flush=True)
    textblob14 = makeTransparent_optimized(resource_path(r"textblob13.png"), "#ff0000")
    print("The loading is ready for textblob14", flush=True)
    textblob15 = makeTransparent_optimized(resource_path(r"textblob14.png"), "#ff0000")
    print("The loading is ready for textblob15", flush=True)
    textblob16 = makeTransparent_optimized(resource_path(r"textblob15.png"), "#ff0000")
    print("The loading is ready for textblob16", flush=True)
    textblob17 = makeTransparent_optimized(resource_path(r"textblob16.png"), "#ff0000")
    print("The loading is ready for textblob17", flush=True)
    textblob18 = makeTransparent_optimized(resource_path(r"textblob17.png"), "#ffffff")
    print("The loading is ready for textblob18", flush=True)
    textblob19 = makeTransparent_optimized(resource_path(r"textblob18.png"), "#ff0000")
    print("The loading is ready for textblob19", flush=True)
    textblob20 = makeTransparent_optimized(resource_path(r"textblob19.png"), "#ff0000")
    print("The loading is ready for textblob20", flush=True)
    textblob21 = makeTransparent_optimized(resource_path(r"textblob20.png"), "#ff0000")
    print("The loading is ready for textblob21", flush=True)
    textblob22 = makeTransparent_optimized(resource_path(r"textblob21.png"), "#ff0000")
    print("The loading is ready for textblob22", flush=True)
    textblob23 = makeTransparent_optimized(resource_path(r"textblob22.png"), "#ff0000")
    print("The loading is ready for textblob23", flush=True)
    textblob24 = makeTransparent_optimized(resource_path(r"textblob23.png"), "#ff0000")
    print("The loading is ready for textblob24", flush=True)
    textblob25 = makeTransparent_optimized(resource_path(r"textblob24.png"), "#ff0000")
    print("The loading is ready for textblob25", flush=True)
    textblob26 = makeTransparent_optimized(resource_path(r"textblob25.png"), "#ff0000")
    print("The loading is ready for textblob26", flush=True)
    textblob27 = makeTransparent_optimized(resource_path(r"textblob26.png"), "#ff0000")
    print("The loading is ready for textblob27", flush=True)
    textblob28 = makeTransparent_optimized(resource_path(r"textblob27.png"), "#ff0000")
    print("The loading is ready for textblob28", flush=True)
    textblob29 = makeTransparent_optimized(resource_path(r"textblob28.png"), "#ff0000")
    print("The loading is ready for textblob29", flush=True)
    textblob30 = makeTransparent_optimized(resource_path(r"textblob29.png"), "#ff0000")
    print("The loading is ready for textblob30", flush=True)
    textblob31 = makeTransparent_optimized(resource_path(r"textblob30.png"), "#ff0000")
    print("The loading is ready for textblob31", flush=True)

    textblob32 = tkinter.PhotoImage(file=resource_path(r"textblob31.png"))
    print("The loading is ready for textblob32", flush=True)
    textblob33 = tkinter.PhotoImage(file=resource_path(r"textblob32.png"))
    print("The loading is ready for textblob33", flush=True)
    textblob34 = tkinter.PhotoImage(file=resource_path(r"textblob33.png"))
    print("The loading is ready for textblob34", flush=True)
    textblob35 = tkinter.PhotoImage(file=resource_path(r"textblob34.png"))
    print("The loading is ready for textblob35", flush=True)
    
    textblob36 = makeTransparent_optimized(resource_path(r"textblob35.png"), "#ff0000")
    print("The loading is ready for textblob36", flush=True)
    textblob37 = makeTransparent_optimized(resource_path(r"textblob36.png"), "#ff0000")
    print("The loading is ready for textblob37", flush=True)
    textblob38 = makeTransparent_optimized(resource_path(r"textblob37.png"), "#ff0000")
    print("The loading is ready for textblob38", flush=True)
    textblob39 = tkinter.PhotoImage(file=resource_path(r"slots.png"))
    print("The loading is ready for textblob39", flush=True)
    textblob40 = makeTransparent_optimized(resource_path(r"textblob38.png"), "#ff0000")
    print("The loading is ready for textblob40", flush=True)
    textblob41 = makeTransparent_optimized(resource_path(r"textblob39.png"), "#ff0000")
    print("The loading is ready for textblob41", flush=True)
    textblob42 = tkinter.PhotoImage(file=resource_path(r"textblob40.png"))
    print("The loading is ready for textblob42", flush=True)
    textblob43 = tkinter.PhotoImage(file=resource_path(r"textblob41.png"))
    print("The loading is ready for textblob43", flush=True)
    textblob44 = tkinter.PhotoImage(file=resource_path(r"textblob42.png"))
    print("The loading is ready for textblob44", flush=True)
    textblob45 = tkinter.PhotoImage(file=resource_path(r"textblob43.png"))
    print("The loading is ready for textblob45", flush=True)
    textblob46 = makeTransparent_optimized(resource_path(r"textblob44.png"), "#ff0000")
    print("The loading is ready for textblob46", flush=True)
    textblob47 = makeTransparent_optimized(resource_path(r"textblob45.png"), "#ff0000")
    print("The loading is ready for textblob47", flush=True)
    Title = tkinter.PhotoImage(file=resource_path(r"tittle.png"))
    print("The loading is ready for Title", flush=True)
    textblob48 = makeTransparent_optimized(resource_path(r"textblob46.png"), "#ff0000")
    print("The loading is ready for textblob48", flush=True)
    textblob49 = makeTransparent_optimized(resource_path(r"textblob47.png"), "#ff0000")
    print("The loading is ready for textblob49", flush=True)
    textblob50 = makeTransparent_optimized(resource_path(r"textblob48.png"), "#ff0000")
    print("The loading is ready for textblob50", flush=True)
    textblob51 = makeTransparent_optimized(resource_path(r"credits.png"), "#ff0000")
    print("The loading is ready for textblob51", flush=True)

    factint = makeTransparent_optimized(resource_path(r"factint.png"), "#ff0000")
    print("The loading is ready for factint", flush=True)
    factint1 = makeTransparent_optimized(resource_path(r"factint1.png"), "#ff0000")
    print("The loading is ready for factint1", flush=True)
    factint2 = makeTransparent_optimized(resource_path(r"factint2.png"), "#ff0000")
    print("The loading is ready for factint2", flush=True)
    factint3 = makeTransparent_optimized(resource_path(r"factint3.png"), "#ff0000")
    print("The loading is ready for factint3", flush=True)
    return

# obstacles
def load_maps():
    global padlo12,Map22,Map23,Map24,Map21, Map3, Map4, Map5, Map6, Map7, Map8, Map9, Map10, Map11, Map13, Map14, Map15, Map16, Map17, Map18, Map19, Map20, padlo2, padlo3, padlo4, padlo5, padlo6, padlo7, padlo8, padlo9, padlo10, padlo11, barlang, factory, gameover
    Map3 = tkinter.PhotoImage(file=resource_path(r"map3.png"))
    print("The loading is ready for Map3", flush=True)
    Map4 = tkinter.PhotoImage(file=resource_path(r"map4.png"))
    print("The loading is ready for Map4", flush=True)
    Map5 = tkinter.PhotoImage(file=resource_path(r"map5.png"))
    print("The loading is ready for Map5", flush=True)
    Map6 = tkinter.PhotoImage(file=resource_path(r"map6.png"))
    print("The loading is ready for Map6", flush=True)
    Map7 = tkinter.PhotoImage(file=resource_path(r"map7.png"))
    print("The loading is ready for Map7", flush=True)
    Map8 = tkinter.PhotoImage(file=resource_path(r"map8.png"))
    print("The loading is ready for Map8", flush=True)
    Map9 = tkinter.PhotoImage(file=resource_path(r"map9.png"))
    print("The loading is ready for Map9", flush=True)
    Map10 = tkinter.PhotoImage(file=resource_path(r"map10.png"))
    print("The loading is ready for Map10", flush=True)
    Map11 = tkinter.PhotoImage(file=resource_path(r"map11.png"))
    print("The loading is ready for Map11", flush=True)
    Map13 = tkinter.PhotoImage(file=resource_path(r"map13.png"))
    print("The loading is ready for Map13", flush=True)
    Map14 = tkinter.PhotoImage(file=resource_path(r"map14.png"))
    print("The loading is ready for Map14", flush=True)
    Map15 = tkinter.PhotoImage(file=resource_path(r"map15.png"))
    print("The loading is ready for Map15", flush=True)
    Map16 = tkinter.PhotoImage(file=resource_path(r"map16.png"))
    print("The loading is ready for Map16", flush=True)
    Map17 = tkinter.PhotoImage(file=resource_path(r"map17.png"))
    print("The loading is ready for Map17", flush=True)
    Map18 = tkinter.PhotoImage(file=resource_path(r"map18.png"))
    print("The loading is ready for Map18", flush=True)
    Map19 = tkinter.PhotoImage(file=resource_path(r"map19.png"))
    print("The loading is ready for Map19", flush=True)
    Map20 = tkinter.PhotoImage(file=resource_path(r"map20.png"))
    print("The loading is ready for Map20", flush=True)
    padlo2=tkinter.PhotoImage(file=resource_path(r"floor2.png"))
    print("The loading is ready for padlo2", flush=True)
    padlo3=tkinter.PhotoImage(file=resource_path(r"floor3.png"))
    print("The loading is ready for padlo3", flush=True)
    padlo4=tkinter.PhotoImage(file=resource_path(r"floor4.png"))
    print("The loading is ready for padlo4", flush=True)
    padlo5=tkinter.PhotoImage(file=resource_path(r"floor5.png"))
    print("The loading is ready for padlo5", flush=True)
    padlo6=tkinter.PhotoImage(file=resource_path(r"floor6.png"))
    print("The loading is ready for padlo6", flush=True)
    padlo7=tkinter.PhotoImage(file=resource_path(r"floor7.png"))
    print("The loading is ready for padlo7", flush=True)
    padlo8=tkinter.PhotoImage(file=resource_path(r"floor8.png"))
    print("The loading is ready for padlo8", flush=True)
    padlo9=tkinter.PhotoImage(file=resource_path(r"floor9.png"))
    print("The loading is ready for padlo9", flush=True)
    padlo10=tkinter.PhotoImage(file=resource_path(r"floor10.png"))
    print("The loading is ready for padlo10", flush=True)
    padlo11=tkinter.PhotoImage(file=resource_path(r"floor11.png"))
    print("The loading is ready for padlo11", flush=True)
    padlo12=tkinter.PhotoImage(file=resource_path(r"floor12.png"))
    print("The loading is ready for padlo12", flush=True)
    barlang=tkinter.PhotoImage(file=resource_path(r"cave floor1.png"))
    print("The loading is ready for barlang", flush=True)
    factory = tkinter.PhotoImage(file=resource_path(r"factory.png"))
    print("The loading is ready for factory", flush=True)
    gameover=tkinter.PhotoImage(file=resource_path(r"game over.png"))
    print("The loading is ready for gameover", flush=True)
    Map21=tkinter.PhotoImage(file=resource_path(r"map21.png"))
    print("The loading is ready for Map21", flush=True)
    Map22=tkinter.PhotoImage(file=resource_path(r"map22.png"))
    print("The loading is ready for Map22", flush=True)
    Map23=tkinter.PhotoImage(file=resource_path(r"map23.png"))
    print("The loading is ready for Map23", flush=True)
    Map24=tkinter.PhotoImage(file=resource_path(r"map24.png"))
    print("The loading is ready for Map24", flush=True)
    return


def fa(x1,y1):
    global x, y, tree
    newTreeImage = makeTransparent(tree, "#ffffff")
    tree_images.append(newTreeImage)
    tree_positions.append((x1, y1))
    fa=canvas.create_image(x1, y1, image=newTreeImage, tag="map",anchor="n")
def ko(x1, y1):
    global x, y, stone
    newStoneImage = makeTransparent(stone, "#ffffff")
    stone_images.append(newStoneImage)
    stone_positions.append((x1, y1))
    ko=canvas.create_image(x1, y1, image=newStoneImage, tag="map", anchor="n")
def cave(x1, y1):
    global x, y, enter
    canvas.create_image(x1,y1, image=enter,anchor="n",tag="map")
def Keyhole(xk, yk):
    global x, y, keyhole,xkk,ykk ,kh
    xkk = xk
    ykk = yk
    newkeyholeImage = makeTransparent(keyhole, "#ffffff")
    keyhole_images.append(newkeyholeImage)
    keyhole_positions.append((xk, yk))
    kh=canvas.create_image(xk, yk, image=newkeyholeImage, anchor="n",tag="map")
def infslab(a,b):
    global infslab1 ,x,y, Merchant,mapv, infslab2
    
    if mapv in (9,10,15,50,54,58):
        infslab1 = Merchant
    if mapv in (12,14,34,42,46,47,48,51,52,57,59,62,63,65,67,71):
        infslab1=NPC
    if mapv in (2,3,7,30,49):
        infslab1 = infslab2
    newInfslabImage = makeTransparent(infslab1, "#ffffff")
    Infslab_images.append(newInfslabImage)
    Infslab_positions.append((x1, y1))
    slab=canvas.create_image(a, b, image=newInfslabImage, anchor="n",tag="map")
def fal(x1,y1):
    global x, y, wall
    newWallImage = makeTransparent(wall, "#ffffff")
    wall_images.append(newWallImage)
    wall_positions.append((x1, y1))
    fal=canvas.create_image(x1, y1, image=newWallImage, tag="map", anchor="n")
def inf(event):
    global gems,tankq,tankqred,tankq,houseown,hppicknum4,x1,y1, a, b,text_id,read,textblob ,mapv, tool, questpick1, gm, quest1redeem,gmbank, ballance, dis_gh_cntr,bushlcntr,tool,x,y,fact_id,wepquestfin,weptype
    if mapv == 77 or mapv == 73 or mapv == 71 or mapv == 2 or mapv == 3 or mapv == 7 or mapv == 10 or mapv == 9 or mapv == 12 or mapv == 14 or mapv == 15 or mapv == 30 or mapv == 34 or mapv == 42 or mapv == 46 or mapv == 47 or mapv == 48 or mapv == 49 or mapv ==50 or mapv == 51 or mapv == 52 or mapv == 54 or mapv == 57 or mapv == 58 or mapv == 59 or mapv == 62 or mapv == 63 or mapv == 65 or mapv == 67 or mapv == 70:
        if mapv == 3:
            textblob = textblob2
            a=800
            b=300
        if mapv == 2:
            textblob = textblob1
            a=500
            b=500
        if mapv == 7:
            textblob = textblob3
            a=850
            b=393
        if mapv == 10:
            textblob = textblob4
            a=850
            b=200
        if mapv == 9:
            textblob = textblob5
            a=96
            b=256
        if mapv == 12 and questpick1 == 0:
            textblob = textblob6
            a = 512
            b = 384
        if mapv == 12 and questpick1 == 1:
            textblob = textblob7
            a = 512
            b = 384
        if mapv == 14 :
            textblob = textblob8
            a = 512
            b = 384
        if mapv == 15 :
            textblob = textblob9
            a = 512
            b = 384
        if mapv == 30 :
            textblob = textblob12
            a = 256
            b = 384
        if mapv == 34 :
            textblob = textblob13
            a = 400
            b = 384
        if mapv == 42 :
            textblob = textblob14
            a = 475
            b = 270
        if mapv == 46 :
            textblob = textblob15
            a = 600
            b = 300
        if mapv == 47 :
            textblob = textblob16
            a = 512
            b = 384
        if mapv == 48 :
            textblob = textblob17
            a = 512
            b = 384
        if mapv == 49 :
            textblob = textblob18
            a = 320
            b = 384
        if mapv == 50 :
            textblob = textblob8
            a = 512
            b = 384
        if mapv == 51 :
            textblob = textblob19
            a = 512
            b = 200
        if mapv == 52 and dis_gh_cntr < 2:
            textblob = textblob20
            a = 606
            b = 110
        if mapv == 52 and dis_gh_cntr == 2:
            textblob = textblob21
            a = 606
            b = 110
        if mapv == 54 and bushlcntr == 0:
            textblob = textblob22
            a = 512
            b = 384
        if mapv == 54 and bushlcntr == 1:
            textblob = textblob23
            tool=0
            equipment_logo(992,0)
            a = 512
            b = 384
        if mapv == 57 :
            textblob = textblob24
            a = 652
            b = 452
        if mapv == 57  and 90<x<290 and 155<y<355 and wepquestfin == 0:
            textblob = factint
            a = 190
            b = 255
        if mapv == 57 and wepquestfin == 1 and weptype.count(0) == 0:
            textblob = textblob26
            a = 652
            b = 452
            if hppicknum4==0:
                hpcontobt(512,384)
        if mapv == 57 and wepquestfin == 1 and weptype.count(0) > 0:
            textblob = textblob25
            a = 652
            b = 452
        if mapv == 58 :
            textblob = textblob27
            a = 770
            b = 257
        if mapv == 59 and houseown == 0 :
            textblob = textblob28
            a = 770
            b = 257
        if mapv == 59 and houseown == 1 :
            textblob = textblob29
            a = 770
            b = 257
        if mapv == 62 :
            textblob = textblob30
            a = 512
            b = 384
        if mapv == 63  and tankq==0:
            textblob = textblob31
            a = 340
            b = 512
        if mapv == 62  and tankq==1:
            textblob = textblob26
            a = 512
            b = 384
        if mapv == 65 :
            textblob = textblob36
            a = 400
            b = 455
        if mapv == 67 :
            textblob = textblob38
            a = 400
            b = 455
        if mapv == 70  and 237<x<437 and 167<y<367:
            textblob = textblob39
            a = 339
            b = 265
        if mapv == 70  and 565<x<765 and 217<y<417:
            textblob = textblob40
            a = 665
            b = 317
        if mapv == 71:
            textblob = textblob41
            a = 512
            b = 384
        if mapv == 73:
            textblob = textblob46
            a = 381
            b = 277
        if mapv == 77 and 312<x<712 and 300<y<600:
            textblob = textblob48
            a = 512
            b = 400
        if read==0:
            if a-100<x<a+100 and b-100<y<b+100:
                canvas.unbind_all("w")
                canvas.unbind_all("s")
                canvas.unbind_all("a")
                canvas.unbind_all("d")
                 
                if mapv in (2,3,7,30,49,70) :
                    
                    if mapv == 70  and 565<x<765 and 217<y<417:
                        text_id = canvas.create_image(0, 468, image=textblob, anchor="nw")
                        fact_id=None
                    elif mapv == 70 and gm >= 3:
                        canvas.bind('<Button-1>',slot)
                    else:
                        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
                        fact_id=None
                         
                if mapv in (9,10,12,14,15,34,42,46,47,48,50,51,52,54,57,58,59,62,63,65,67,71,73,77):
                    if mapv == 65 and textblob in (textblob32,textblob33,textblob34,textblob35):
                        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
                        fact_id=None
                    elif mapv == 57 and 90<x<290 and 155<y<355 and wepquestfin == 0:
                        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
                        fact_id = canvas.create_image(205, 110, image=factint1, anchor="nw",tag="back")
                        canvas.create_rectangle(260,192,476,247,outline="white",width="5",tag="fact")
                        canvas.bind('<Button-1>',wepquest)
                    else:
                        text_id = canvas.create_image(0, 468, image=textblob, anchor="nw")
                        fact_id=None
                    if mapv ==9 and questpick1==0:
                        if tool == 0:
                            canvas.bind_all("i",accept)
                        canvas.bind_all("o",esc)
                    if mapv == 12 and questpick1==1 and quest1redeem==0:
                        tool=0
                        equipment_logo(992,0)
                        gm=gm+30
                        gm_label.config(text=f"Ghosts Captured: {gm}")
                        quest1redeem=1
                    if mapv == 62 and tankq==1 and tankqred==0:
                        gm=gm+30
                        gm_label.config(text=f"Ghosts Captured: {gm}")
                        tankqred=1
                    if mapv==14 or mapv == 50:
                        ballance=canvas.create_text(600,580,text=gmbank, font=("Impact",20), fill="White")
                        canvas.bind_all("<Up>",increase)
                        canvas.bind_all("<Down>",decrease)
                        canvas.bind_all("i",deposit)
                        canvas.bind_all("o",tkout)
                    if mapv == 15:
                        canvas.bind_all("i",doctor)
                    if mapv==42:
                        canvas.bind_all("i",acceptpass)
                    if mapv==46:
                        canvas.bind_all("i",acceptguard)
                    if mapv ==51:
                        canvas.bind_all("i",pray)
                    if mapv ==52:
                        canvas.bind_all("i",buybeer)
                    if mapv ==59 and houseown == 0 :
                        canvas.bind_all("i",buyhouse)
                    if mapv == 63 and tool == 0:
                        canvas.bind_all("i",buygas)
                    if mapv == 65:
                        canvas.bind_all("i",nextpag)
                        canvas.bind_all("n",nextpag)
                    if mapv == 71 and gm >= 5:
                        canvas.bind_all("i",buynews)
                    if mapv == 73 and gems == 4:
                        canvas.bind_all("i",finisl)
                    if mapv == 77:
                        canvas.bind_all("o",finalI)
                        canvas.bind_all("i",finalO)
                read=1
                read_sound.play()
def finalI(event):
    global text_id, textblob
    canvas.unbind_all("<Escape>")
    canvas.delete("all")
    canvas.unbind_all("i")

    textblob = textblob49
    text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")

    check_keys()
def finalO(event):
    global text_id, textblob
    canvas.unbind_all("<Escape>")
    canvas.delete("all")
    canvas.unbind_all("o")

    textblob = textblob50
    text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")

    check_keys()

def check_keys():
    global text_id, textblob, check
    
    if win32api.GetAsyncKeyState(ord('N')) & 0x8000:
        canvas.delete(text_id)
        textblob = textblob51
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
        check=True

    if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) & 0x8000 and check==True:
        on_close()
        return

    canvas.after(50, check_keys)
def finisl(event):
    global x,y,after_id
    if after_id:
                canvas.after_cancel(after_id)
                after_id = None
    canvas.unbind_all("i")
    tree_positions.clear()
    stone_positions.clear()
    wall_positions.clear()
    wallb_positions.clear()
    keyhole_positions.clear()
    boss1_positions.clear()
    brickwall_positions.clear()
    roofb_positions.clear()
    roofb2_positions.clear()
    Door4k_positions.clear()
    canvas.delete("all")
    map36()
    equipment_logo(992,0)
    x=721
    y=447
    canvas.bind_all("d",mozog_jobb)
    canvas.bind_all("a",mozog_bal)
    canvas.bind_all("w",mozog_elo)
    canvas.bind_all("s",mozog_hat)
def buynews(event):
    global gm, gems, wepquestfin, textblob, new1,new2,new3,new4, text_id
    canvas.unbind_all("i")
    gm = gm-5
    gm_label.config(text=f"Ghosts Captured: {gm}")
    canvas.delete(text_id)
    if gems >= 1 and new1 == 0:
        new1=1
        textblob=textblob42
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif gems >= 2 and new2 == 0:
        new2=1
        textblob=textblob43
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif gems >= 3 and new3 == 0:
        new3=1
        textblob=textblob44
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif gems >= 4 and new4 == 0:
        new4=1
        textblob=textblob45
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    else:
        gm = gm+5
        gm_label.config(text=f"Ghosts Captured: {gm}")
def slot(koor):
    global gm
    if gm >= 3:
        sslot=[]
        gm = gm-3
        gm_label.config(text=f"Ghosts Captured: {gm}")
        xsl=koor.x
        ysl=koor.y
        if 852<xsl<907 and 203<ysl<258:
            slot1=random.randrange(1,9)
            slot2=random.randrange(1,9)
            slot3=random.randrange(1,9)
            sslot.append(slot1)
            sslot.append(slot2)
            sslot.append(slot3)
            canvas.delete("Cherry")
            canvas.delete("yyelowgem")
            canvas.delete("Seven")
            canvas.delete("Hpcontobt")
            canvas.delete("wheatb")
            canvas.delete("beerb")
            canvas.delete("gass")
            canvas.delete("pick")
            if slot1 == 1:
                canvas.create_image(340,246, image=Cherry, anchor="n", tag= "Cherry")
            if slot2 == 1:
                canvas.create_image(506,246, image=Cherry, anchor="n", tag= "Cherry")
            if slot3 == 1:
                canvas.create_image(668,246, image=Cherry, anchor="n", tag= "Cherry")
            if slot1 == 2:
                Wheat(340,246)
            if slot2 == 2:
                Wheat(506,246)
            if slot3 == 2:
                Wheat(668,246)
            if slot1 == 3:
                Beer(340,246)
            if slot2 == 3:
                Beer(506,246)
            if slot3 == 3:
                Beer(668,246)
            if slot1 == 4:
                Yellowgem(340,246)
            if slot2 == 4:
                Yellowgem(506,246)
            if slot3 == 4:
                Yellowgem(668,246)
            if slot1 == 5:
                pickax(340,246)
            if slot2 == 5:
                pickax(506,246)
            if slot3 == 5:
                pickax(668,246)
            if slot1 == 6:
                hpcontobt(340,246)
            if slot2 == 6:
                hpcontobt(506,246)
            if slot3 == 6:
                hpcontobt(668,246)
            if slot1 == 7:
                Gas(340,246)
            if slot2 == 7:
                Gas(506,246)
            if slot3 == 7:
                Gas(668,246)
            if slot1 == 8:
                canvas.create_image(340,246, image=Seven, anchor="n", tag ="Seven")
            if slot2 == 8:
                canvas.create_image(506,246, image=Seven, anchor="n",tag ="Seven")
            if slot3 == 8:
                canvas.create_image(668,246, image=Seven, anchor="n",tag ="Seven")
            
            if sslot.count(1)==2:
                gm = gm+10
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(1)==3:
                gm = gm+50
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(2)==2:
                gm = gm+3
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(2)==3:
                gm = gm+10
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(3)==2:
                gm = gm+3
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(3)==3:
                gm = gm+10
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(4)==2:
                gm = gm+5
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(4)==3:
                gm = gm+10
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(5)==2:
                gm = gm+6
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(5)==3:
                gm = gm+20
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(6)==2:
                gm = gm+8
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(6)==3:
                gm = gm+30
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(7)==2:
                gm = gm+10
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(7)==3:
                gm = gm+40
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(8)==2:
                gm = gm+15
                gm_label.config(text=f"Ghosts Captured: {gm}")
            if sslot.count(8)==3:
                gm = gm+50
                gm_label.config(text=f"Ghosts Captured: {gm}")
        
        
            
def nextpag(event):
    global text_id,textblob
    if mapv == 65 and textblob == textblob36:
        canvas.delete(text_id)
        textblob=textblob32
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif mapv == 65 and textblob == textblob32:
        canvas.delete(text_id)
        textblob=textblob33
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif mapv == 65 and textblob == textblob33:
        canvas.delete(text_id)
        textblob=textblob34
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif mapv == 65 and textblob == textblob34:
        canvas.delete(text_id)
        textblob=textblob35
        text_id = canvas.create_image(0, 0, image=textblob, anchor="nw")
    elif mapv == 65 and textblob == textblob35:
        canvas.delete(text_id)
        textblob=textblob37
        text_id = canvas.create_image(0, 468, image=textblob, anchor="nw")
    elif mapv == 65 and textblob == textblob37:
        canvas.unbind("n")
        canvas.unbind("i")
def buyhouse(event):
    global houseown,gm
    if gm>=150:
        gm=gm-150
        gm_label.config(text=f"Ghosts Captured: {gm}")
        houseown=1
def wepquest(koor):
    global weptype,wepquestfin
    global weplev,fact_id,text_id,read
    wepx=koor.x
    wepy=koor.y
    
    if 450<wepx<500 and 566<wepy<610:
        canvas.delete("fact")
        if weplev < 2:
            weplev=weplev+1
            print(weplev)
        if weplev==0:
            canvas.create_rectangle(259,325,476,380,outline="white",width="5",tag="fact")
        if weplev==1:
            canvas.create_rectangle(259,255,476,313,outline="white",width="5",tag="fact")
        if weplev==2:
            canvas.create_rectangle(260,192,476,247,outline="white",width="5",tag="fact")
    if 450<wepx<500 and 654<wepy<700:
        canvas.delete("fact")
        if weplev  > 0:
            weplev=weplev-1
            print(weplev)
        if weplev==0:
            canvas.create_rectangle(259,325,476,380,outline="white",width="5",tag="fact")
        if weplev==1:
            canvas.create_rectangle(259,255,476,313,outline="white",width="5",tag="fact")
        if weplev==2:
            canvas.create_rectangle(260,192,476,247,outline="white",width="5",tag="fact")
    if 597<wepx<647 and 607<wepy<650:
        canvas.delete("fact")
        canvas.delete(fact_id)
        weptype.append(weplev)
        if len(weptype)==1:
            fact_id = canvas.create_image(205, 110, image=factint2, anchor="nw")
        if len(weptype)==2:
            fact_id = canvas.create_image(205, 110, image=factint3, anchor="nw")
        if len(weptype)==3:
            canvas.delete(amm)
            canvas.delete("game")
            canvas.delete(ballance)
            canvas.delete(text_id)
            canvas.delete(mmap)
            canvas.delete(dot)
            canvas.delete("fact")
            canvas.delete("back")
            canvas.delete(fact_id)
            canvas.unbind_all("i")
            canvas.unbind_all("o")
            canvas.unbind_all("<Up>")
            canvas.unbind_all("<Down>")
            canvas.bind_all("d",mozog_jobb)
            canvas.bind_all("a",mozog_bal)
            canvas.bind_all("w",mozog_elo)
            canvas.bind_all("s",mozog_hat)
            read=0
            wepquestfin=1
def buygas(event):
    global tool,eqtool,tankq
    canvas.unbind_all("i")
    canvas.unbind_all("o")
    if tool == 0 and eqtool=="gas"and tankq == 0 :
        tool=6
        equipment_logo(992,0)
def doctor(event):
    global hp, maxhp, hpmeter,gm
    if gm>=5:
        gm=gm-5
        gm_label.config(text=f"Ghosts Captured: {gm}")
        hp=maxhp
        canvas.delete(hpmeter)
        hpmeter = canvas.create_text(900,750, text="health:"+str(hp), font="Impact 20", fill ="red")
    else:
        return
def pray(event):
    global hp,hpmeter,maxhp
    if hp+50<=maxhp:
        hp=hp+50
        canvas.delete(hpmeter)
        hpmeter = canvas.create_text(900,750, text="health:"+str(hp), font="Impact 20", fill ="red")
def buybeer(event):
    global gm, tool, dis_gh_cntr
    canvas.unbind_all("i")
    canvas.unbind_all("o")
    if gm >= 5 and tool == 0 and dis_gh_cntr == 2:
        gm=gm-5
        gm_label.config(text=f"Ghosts Captured: {gm}")
        tool=4
        equipment_logo(992,0)
    else:
        return
def deposit(event):
    global gm,gmbank,gmbank2,amm,ballance
    if gmbank2>gm:
        gmbank2=gm
    gmbank=gmbank+gmbank2
    gm=gm-gmbank2
    gm_label.config(text=f"Ghosts Captured: {gm}")
    gmbank2=0
    canvas.delete(amm)
    canvas.delete(ballance)
    ballance=canvas.create_text(600,580,text=gmbank, font=("Impact",20), fill="White")
    amm=canvas.create_text(600,648,text=gmbank2, font=("Impact",20), fill="White")
def tkout(event):
    global gm,gmbank,gmbank2,amm,ballance
    if gmbank2>gmbank:
        gmbank2=gmbank
    gmbank=gmbank-gmbank2
    gm=gm+gmbank2
    gm_label.config(text=f"Ghosts Captured: {gm}")
    canvas.delete(amm)
    canvas.delete(ballance)
    ballance=canvas.create_text(600,580,text=gmbank, font=("Impact",20), fill="White")
    amm=canvas.create_text(600,648,text=gmbank2, font=("Impact",20), fill="White")
def increase(event):
    global gmbank2,amm
    gmbank2=gmbank2+1
    canvas.delete(amm)
    amm=canvas.create_text(600,648,text=gmbank2, font=("Impact",20), fill="White")
def decrease(event):
    global gmbank2,amm
    gmbank2=gmbank2-1
    if gmbank2<0:
        gmbank2=gmbank2+1
    canvas.delete(amm)
    amm=canvas.create_text(600,648,text=gmbank2, font=("Impact",20), fill="White")
def esc(event):
    global text_id, read,mmap,dot, ballance,amm,mapv,fact_id
    global weptype
    global weplev
    if mapv==28:
        tree_positions.clear()
        stone_positions.clear()
        wall_positions.clear()
        wallb_positions.clear()
        keyhole_positions.clear()
        boss1_positions.clear()
        brickwall_positions.clear()
        roofb_positions.clear()
        roofb2_positions.clear()
        Door4k_positions.clear()
        canvas.delete("all")
        dun2()
        equipment_logo(992,0)
        x=1024
        y=350
    weptype=[]
    weplev=2
    canvas.delete(amm)
    canvas.delete("game")
    canvas.delete(ballance)
    canvas.delete(text_id)
    canvas.delete(mmap)
    canvas.delete(dot)
    canvas.delete(Guideui)
    canvas.delete("fact")
    canvas.delete(fact_id)
    canvas.delete("timelin")
    if mapv not in (70,8,34,38,65,67):
        canvas.delete("y")
    if mapv not in (68,58,57,41,25,21,10):
        canvas.delete("hp")
    canvas.delete("Cherry")
    canvas.delete("yyelowgem")
    canvas.delete("Seven")
    canvas.delete("Hpcontobt")
    canvas.delete("wheatb")
    canvas.delete("beerb")
    canvas.delete("gass")
    canvas.delete("pick")
    canvas.unbind_all("i")
    canvas.unbind_all("o")
    canvas.unbind_all("<Up>")
    canvas.unbind_all("<Down>")
    canvas.bind_all("d",mozog_jobb)
    canvas.bind_all("a",mozog_bal)
    canvas.bind_all("w",mozog_elo)
    canvas.bind_all("s",mozog_hat)
    equipment_logo(992, 0)
    read=0
def fal2(xb,yb):
    global x, y, broke,xxb,yyb,falb
    xxb=xb
    yyb=yb
    newWallbImage = makeTransparent(broke, "#ffffff")
    wallb_images.append(newWallbImage)
    wallb_positions.append((xb, yb))
    falb=canvas.create_image(xb, yb, image=newWallbImage, tag="map", anchor="n")    
def Boss1(xbo, ybo):
    global x, y, boss1 ,xxbo, yybo, bboss1
    xxbo=xbo
    yybo=ybo
    newboss1Image = makeTransparent(boss1, "#ffffff")
    boss1_images.append(newboss1Image)
    boss1_positions.append((xxbo, yybo))
    bboss1=canvas.create_image(xbo, ybo, image=newboss1Image, tag="map", anchor="n")
def Yellowgem(xg, yg):
    global x, y, yellowgem ,xxg,yyg, yyellowgem, mapv
    xxg = xg
    yyg = yg
    newyellowgemImage = makeTransparent(yellowgem, "#ffffff")
    yellowgem_images.append(newyellowgemImage)
    yellowgem_positions.append((xg, yg))
    if mapv != 70:
        yyellowgem=canvas.create_image(xg, yg, image=newyellowgemImage, tag="y",anchor="n")
    elif mapv == 70:
        yyellowgem=canvas.create_image(xg, yg, image=newyellowgemImage, tag="yyelowgem",anchor="n")
def Brickwall(x1, y1):
    global x,y,brickwall
    bricks=canvas.create_image(x1, y1, image=brickwall, tag="map",anchor="n")
    brickwall_positions.append((x1, y1))
def Brickwall1(x1, y1):
    global x,y,brickwall,bricks1
    bricks1=canvas.create_image(x1, y1, image=brickwall, tag="map",anchor="n")
    brickwall_positions.append((x1, y1))
def Brickwall2(x1, y1):
    global x,y,brickwall,bricks2
    bricks2=canvas.create_image(x1, y1, image=brickwall, tag="map",anchor="n")
    brickwall_positions.append((x1, y1))
    
def Roofb(x1,y1):
    global x,y,roofb
    roofbs = canvas.create_image(x1, y1, image=roofb, tag="map",anchor="n")
    roofb_positions.append((x1, y1))
def Roofb2(x1,y1):
    global x,y,roofb2
    roofb2s = canvas.create_image(x1, y1, image=roofb2, tag="map",anchor="n")
    roofb2_positions.append((x1, y1))
def Door(xd,yd):
    global door
    doors = canvas.create_image(xd, yd, image=door, tag="map",anchor="n")
def mapobt(xm,ym):
    global Map, xxm, yym, Mapobt
    xxm = xm
    yym = ym
    newmapobtImage = makeTransparent(Map, "#ffffff")
    mapobt_images.append(newmapobtImage)
    mapobt_positions.append((xm, ym))
    Mapobt=canvas.create_image(xm, ym, image=newmapobtImage, tag="map", anchor="n")
def hpcontobt(xhp,yhp):
    global hpcont, xxhp, yyhp, Hpcontobt, mapv
    xxhp = xhp
    yyhp = yhp
    newhpcontobtImage = makeTransparent(hpcont, "#ffffff")
    hpcontobt_images.append(newhpcontobtImage)
    hpcontobt_positions.append((xhp, yhp))
    if mapv != 70:
        Hpcontobt=canvas.create_image(xhp, yhp, image=newhpcontobtImage, tag="hp", anchor="n")
    elif mapv == 70:
        Hpcontobt=canvas.create_image(xhp, yhp, image=newhpcontobtImage, tag="Hpcontobt", anchor="n")
def Guide(xgd,ygd):
    global  xxgd, yygd, GGuide, guide
    xxgd = xgd
    yygd = ygd
    newguideImage = makeTransparent(guide, "#ffffff")
    guide_images.append(newguideImage)
    GGuide=canvas.create_image(xgd, ygd, image=newguideImage, tag="guide", anchor="n")
def Upgrade(xup,yup):
    global  xxup, yyup, upgrade, UUpgrade
    xxup = xup
    yyup = yup
    newupgradeImage = makeTransparent(upgrade, "#ffffff")
    upgrade_images.append(newupgradeImage)
    UUpgrade=canvas.create_image(xup, yup, image=newupgradeImage, tag="guide", anchor="n")
def MMAP(xmp,ymp):
    global Mmap, xxmp, yymp, Mpcontobt
    xxmp = xmp
    yymp = ymp
    newMpcontobtImage = makeTransparent(Mmap, "#ffffff")
    Mpcontobt_images.append(newMpcontobtImage)
    Mpcontobt_positions.append((xmp, ymp))
    Mpcontobt=canvas.create_image(xmp, ymp, image=newMpcontobtImage, tag="map", anchor="n")
def Door4k(xd,yd):
    global door4k,xxdp,yydp,doors4k
    xxdp = xd
    yydp = yd
    Door4k_positions.append((xd, yd))
    doors4k = canvas.create_image(xd, yd, image=door4k, tag="map",anchor="n")
def Bulb1(x1,y1):
    global bulb1,Bulb
    newbulb1Image = makeTransparent(bulb1, "#ffffff")
    bulb1_images.append(newbulb1Image)
    
    Bulb=canvas.create_image(x1, y1, image=newbulb1Image, tag="bulb", anchor="n")
def Bulb2(x1,y1):
    global bulb1,Bulbone
    newbulb1Image = makeTransparent(bulb1, "#ffffff")
    bulb1_images.append(newbulb1Image)
    
    Bulbone=canvas.create_image(x1, y1, image=newbulb1Image, tag="bulb", anchor="n")
def Bulb3(x1,y1):
    global bulb1,Bulbtwo
    newbulb1Image = makeTransparent(bulb1, "#ffffff")
    bulb1_images.append(newbulb1Image)
    
    Bulbtwo=canvas.create_image(x1, y1, image=newbulb1Image, tag="bulb", anchor="n")
def Bulb4(x1,y1):
    global bulb1,Bulbthree
    newbulb1Image = makeTransparent(bulb1, "#ffffff")
    bulb1_images.append(newbulb1Image)
    
    Bulbthree=canvas.create_image(x1, y1, image=newbulb1Image, tag="bulb", anchor="n")
def Healthbarfull(x1,y1):
    global healthbarfull,barfull
    newhealthbarfullImage = makeTransparent(healthbarfull, "#ffffff")
    healthfull_images.append(newhealthbarfullImage)
    
    barfull=canvas.create_image(x1, y1, image=newhealthbarfullImage, anchor="n",tag="barfull")
def Healthbarhalf(x1,y1):
    global healthbarhalf,barhalf
    newhealthbarhalfImage = makeTransparent(healthbarhalf, "#ffffff")
    healthhalf_images.append(newhealthbarhalfImage)
    
    barhalf=canvas.create_image(x1, y1, image=newhealthbarhalfImage, anchor="n",tag="barhalf")
def Healthbarlow(x1,y1):
    global healthbarlow,barlow
    newhealthbarlowImage = makeTransparent(healthbarlow, "#ffffff")
    healthlow_images.append(newhealthbarlowImage)
    
    barlow=canvas.create_image(x1, y1, image=newhealthbarlowImage, anchor="n",tag="barlow")
def Watersplash(x1,y1):
    global watersplash,wtrsplash
    newwatersplashImage = makeTransparent(watersplash, "#ffffff")
    watersplash_images.append(newwatersplashImage)
    
    wtrsplash=canvas.create_image(x1, y1, image=newwatersplashImage, anchor="n")        
def Drop(x1,y1):
    global drop,xdp,ydp,drp
    xdp=x1
    ydp=y1
    newdropImage = makeTransparent(drop, "#ffffff")
    drop_images.append(newdropImage)
    drp=canvas.create_image(x1, y1, image=newdropImage, anchor="n")
# sounds
pygame.init()
pygame.mixer.init()
walking_sound = pygame.mixer.Sound(resource_path("walkinggr.wav"))
walkingcave_sound = pygame.mixer.Sound(resource_path("walkingca.wav"))
pickup_sound = pygame.mixer.Sound(resource_path("Pickup.wav"))
read_sound = pygame.mixer.Sound(resource_path("Read.wav"))
pickaxe_sound = pygame.mixer.Sound(resource_path("Random3.wav"))
walkingwood_sound = pygame.mixer.Sound(resource_path("Woodwal.wav"))

# inventory
def equipment_logo(x1, y1):
    global tool, pickaxe_hud_image, key_hud_image,questpick1,passport_hud_image,beer_hud_image,wheat_hud_image,gas_hud_image

    neweqImage = equipment  
    canvas.create_image(x1, y1, image=neweqImage, tag="hud", anchor="n")
        
    

    
    if tool == 1:
        if pickaxe_hud_image is None:
            pickaxe_hud_image = makeTransparent(pickaxe, "#ffffff")
        canvas.create_image(x1 + 40, y1 + 40, image=pickaxe_hud_image, tag="hud", anchor="nw")
        show_pickaxe_in_inventory()
    if tool == 2:
        if key_hud_image is None:
            key_hud_image = makeTransparent(key, "#ffffff")
        canvas.create_image(x1 + 40, y1 + 40, image=key_hud_image, tag="hud", anchor="nw")
        show_key_in_inventory()
    if tool == 3:
        if passport_hud_image is None:
            passport_hud_image = makeTransparent(passport, "#ffffff")
        canvas.create_image(x1 + 40, y1 + 40, image=passport_hud_image, tag="hud", anchor="nw")
        show_passport_in_inventory()
    if tool == 4:
        if beer_hud_image is None:
            beer_hud_image = makeTransparent(beer, "#ffffff")
        canvas.create_image(x1 + 40, y1 + 40, image=beer_hud_image, tag="hud", anchor="nw")
        show_beer_in_inventory()
    if tool == 5:
        if wheat_hud_image is None:
            wheat_hud_image = makeTransparent(wheat, "#ffffff")
        canvas.create_image(x1 + 40, y1 + 40, image=wheat_hud_image, tag="hud", anchor="nw")
        show_wheat_in_inventory()
    if tool == 6:
        if gas_hud_image is None:
            gas_hud_image = makeTransparent(gas, "#ffffff")
        canvas.create_image(x1 + 40, y1 + 40, image=gas_hud_image, tag="hud", anchor="nw")
        show_gas_in_inventory()

def pickax(xp, yp):
    global pickaxe_image, pick, mapv
    pickaxe_image = makeTransparent(pickaxe, "#ffffff")
    if mapv != 70:
        pick = canvas.create_image(xp, yp, image=pickaxe_image, tag="item", anchor="n")
    elif mapv == 70:
        pick = canvas.create_image(xp, yp, image=pickaxe_image, tag="pick", anchor="n")
def Gas(x1, y1):
    global gas_image, gass, mapv
    gas_image = makeTransparent(gas, "#ffffff")
    if mapv != 70:
        gass = canvas.create_image(x1, y1, image=gas_image, anchor="n")
    elif mapv == 70:
        gass = canvas.create_image(x1, y1, image=gas_image, tag="gass", anchor="n")
def Passport(x1,y1):
    global passp,passport_image
    passport_image = makeTransparent(passport, "#ffffff")
    passp = canvas.create_image(x1, y1, image=passport_image, tag="item", anchor="n")
def Beer(x1,y1):
    global beer, beer_image, mapv
    beer_image = makeTransparent(beer, "#ffffff")
    if mapv != 70:
        beerb = canvas.create_image(x1, y1, image=beer_image, tag="item", anchor="n")
    elif mapv == 70:
        beerb = canvas.create_image(x1, y1, image=beer_image, tag="beerb", anchor="n")
def Wheat(x1,y1):
    global wheat, wheat_image, mapv
    wheat_image = makeTransparent(wheat, "#ffffff")
    if mapv != 70:
        wheatb = canvas.create_image(x1, y1, image=wheat_image, tag="item", anchor="n")
    elif mapv == 70:
        wheatb = canvas.create_image(x1, y1, image=wheat_image, tag="wheatb", anchor="n")
def show_passport_in_inventory():
    global passport_equipped_image,passport_image
    passport_image = makeTransparent(passport, "#ffffff")
    passport_equipped_image = canvas.create_image(992, 0, image=passport_image, anchor="n")
def show_beer_in_inventory():
    global beer_equipped_image,beer_image
    beer_image = makeTransparent(beer, "#ffffff")
    beer_equipped_image = canvas.create_image(992, 0, image=beer_image, anchor="n")
def show_wheat_in_inventory():
    global wheat_equipped_image,wheat_image
    wheat_image = makeTransparent(wheat, "#ffffff")
    wheat_equipped_image = canvas.create_image(992, 0, image=wheat_image, anchor="n")
def show_pickaxe_in_inventory():
    global pickaxe_equipped_image,newpickImage
    pickaxe_equipped_image = canvas.create_image(992, 0, image=newpickImage, anchor="n")
def show_gas_in_inventory():
    global gas_equipped_image,newgasImage
    gas_equipped_image = canvas.create_image(992, 0, image=newgasImage, anchor="n") 
def use(event):
    global tankq,gm,beer_equipped_image,tool,xxb,yyb,falb,x,y, pickaxe_equipped_image, wallbrokometer ,keybrokometer ,xkk, ykk, key_equipped_image, kh,xxdp,yydp,keybrokometer1,dun1door,doors4k,x,y
    if tool == 1:
        if xxb - 100 < x < xxb + 100 and yyb - 100 < y < yyb + 100:
            wallb_positions.clear()
            canvas.delete(falb)
            canvas.delete(pickaxe_equipped_image)
            pickup_sound.play()
            tool=0
            wallbrokometer = 1
            
    if tool == 2:
        if mapv == 5:
            if xkk - 100 < x < xkk + 100 and ykk - 100 < y < ykk + 100:
                keyhole_positions.clear()
                canvas.delete(kh)
                canvas.delete(key_equipped_image)
                pickup_sound.play()
                tool=0
                keybrokometer = 1
        if mapv == 27:
            if xxdp - 100 < x < xxdp + 100 and yydp - 100 < y < yydp + 100:
                canvas.delete(key_equipped_image)
                pickup_sound.play()
                tool=0
                keybrokometer1 = 1
                dun1door=dun1door+1
                if dun1door==4:
                    canvas.delete(doors4k)
                    Door4k_positions.clear()
    if tool == 4:
        if mapv == 48 and 412<x<612 and 284<x<484:
            canvas.delete(beer_equipped_image)
            pickup_sound.play()
            tool=0
            gm=gm+10
            gm_label.config(text=f"Ghosts Captured: {gm}")
        else:
            canvas.delete(beer_equipped_image)
            pickup_sound.play()
            tool=0
            canvas.unbind_all("w")
            canvas.unbind_all("s")
            canvas.unbind_all("a")
            canvas.unbind_all("d")
            canvas.bind_all("a",mozog_jobb)
            canvas.bind_all("d",mozog_bal)
            canvas.bind_all("s",mozog_elo)
            canvas.bind_all("w",mozog_hat)
    if tool == 6:
        if mapv==61 and tankq == 0 and eqtool == "gas" and tool == 6 and 32 < x < 232 and 407 < y <  607:
            tool = 0
            pickaxe_sound.play()
            tankq = 1
            equipment_logo(992, 0)
            
            
def kkey(xp, yp):
    global key_image, key2
    key_image = makeTransparent(key, "#ffffff")
    key2 = canvas.create_image(xp, yp, image=key_image, tag="item", anchor="n")


def show_key_in_inventory():
    global key_equipped_image,newkeyImage
    key_equipped_image = canvas.create_image(992, 0, image=newkeyImage, anchor="n")    
def Map(event):
    global Time,Mapscreen,mmap,mapv,read,dot,pickguide,Guideui, mappicknum,gems,yel1,yel2,yel3,yel4,hppicknum,hppicknum1,hppicknum2,hppicknum3,hppicknum4,hppicknum5,hppicknum6
    if mapv not in (70,8,34,38,65,67,68,58,57,41,25,21,10):
        if read==0:
            canvas.unbind_all("w")
            canvas.unbind_all("s")
            canvas.unbind_all("a")
            canvas.unbind_all("d")
            read=1
            
            
            if mappicknum  == 1:
                mmap=canvas.create_image(0,0,image=Mapscreen, anchor="nw")
                if mapv == 1:
                    dot=canvas.create_oval(121,731,131,741,fill="red")
                if mapv == 2:
                    dot=canvas.create_oval(37,731,47,741,fill="red")
                if mapv == 3:
                    dot=canvas.create_oval(37,667,47,677,fill="red")
                if mapv in (4,5,6,7,8):
                    dot=canvas.create_oval(121,667,131,677,fill="red")
                if mapv in (9,10,11,12):
                    dot=canvas.create_oval(121,603,131,613,fill="red")
                if mapv in (13,14,15,16):
                    dot=canvas.create_oval(37,603,47,613,fill="red")
                if mapv == 17:
                    dot=canvas.create_oval(121,539,131,549,fill="red")
                if mapv == 18:
                    dot=canvas.create_oval(37,539,47,549,fill="red")
                if mapv == 19:
                    dot=canvas.create_oval(205,603,215,613,fill="red")
                if mapv == 20:
                    dot=canvas.create_oval(205,539,215,549,fill="red")
                if mapv == 21:
                    dot=canvas.create_oval(37,475,47,485,fill="red")
                if mapv in (22,23):
                    dot=canvas.create_oval(121,475,131,485,fill="red")
                if mapv == 24:
                    dot=canvas.create_oval(289,539,299,549,fill="red")
                if mapv == 25:
                    dot=canvas.create_oval(205,475,215,485,fill="red")
                if mapv in (26,27,28,29,30,31,32,33,34):
                    dot=canvas.create_oval(289,475,299,485,fill="red")
                if mapv in (35,38):
                    dot=canvas.create_oval(289,603,299,613,fill="red")
                if mapv == 36:
                    dot=canvas.create_oval(205,667,215,677,fill="red")
                if mapv == 37:
                    dot=canvas.create_oval(289,667,299,677,fill="red")
                if mapv == 39:
                    dot=canvas.create_oval(373,667,383,677,fill="red")
                if mapv == 40:
                    dot=canvas.create_oval(373,603,383,613,fill="red")
                if mapv == 41:
                    dot=canvas.create_oval(373,539,383,549,fill="red")
                if mapv == 42:
                    dot=canvas.create_oval(373,475,383,485,fill="red")
                if mapv == 43:
                    dot=canvas.create_oval(373,411,383,421,fill="red")
                if mapv == 44:
                    dot=canvas.create_oval(373,347,383,357,fill="red")
                if mapv == 45:
                    dot=canvas.create_oval(457,347,467,357,fill="red")
                if mapv in (46,47,48):
                    dot=canvas.create_oval(541,347,551,357,fill="red")
                if mapv in (49,50,51,52,53,54):
                    dot=canvas.create_oval(625,347,635,357,fill="red")
                if mapv == 55:
                    dot=canvas.create_oval(625,283,635,293,fill="red")
                if mapv in (56,57,58,59,60):
                    dot=canvas.create_oval(541,283,551,293,fill="red")
                if mapv in (61,62,63):
                    dot=canvas.create_oval(625,411,635,421,fill="red")
                if mapv in (64,65):
                    dot=canvas.create_oval(541,411,551,421,fill="red")
                if mapv in (66,67,68):
                    dot=canvas.create_oval(625,219,635,229,fill="red")
                if mapv in (69,70,71):
                    dot=canvas.create_oval(541,219,551,229,fill="red")
                if mapv == 72 :
                    dot=canvas.create_oval(625,155,635,165,fill="red")
                if mapv == 73 :
                    dot=canvas.create_oval(541,155,551,165,fill="red")
            if pickguide==1:
                Guideui=canvas.create_image(700,0,image=guideui, anchor="nw")
                if gems >= 1:
                    Yellowgem(864, 190)
                if gems >= 2:
                    Yellowgem(864, 253)
                if gems >= 3:
                    Yellowgem(864, 315)
                if gems >= 4:
                    Yellowgem(864, 378)
                if hppicknum == 1:
                    hpcontobt(828,534)
                if hppicknum1 == 1:
                    hpcontobt(909,535)
                if hppicknum2 == 1:
                    hpcontobt(787,611)
                if hppicknum3 == 1:
                    hpcontobt(867,611)
                if hppicknum4 == 1:
                    hpcontobt(952,611)
                if hppicknum5 == 1:
                    hpcontobt(829,683)
                if hppicknum6 == 1:
                    hpcontobt(914,683)
                if 0<=Time<360 :
                    canvas.create_line(861,121,861,76,width="5",tag="timelin")
                if 360<=Time<720 or 4680<=Time<5040:
                    canvas.create_line(861,121,883,83,width="5",tag="timelin")
                if 720<=Time<1080 or 5040<=Time<5400:
                    canvas.create_line(861,121,899,98,width="5",tag="timelin")
                if 1080<=Time<1440 or 5400<=Time<5760:
                    canvas.create_line(861,121,905,121,width="5",tag="timelin")
                if 1440<=Time<1800 or 5760<=Time<6120:
                    canvas.create_line(861,121,899,143,width="5",tag="timelin")
                if 1800<=Time<2160 or 6120<=Time<6480:
                    canvas.create_line(861,121,881,159,width="5",tag="timelin")
                if 2160<=Time<2520 or 6480<=Time<6840:
                    canvas.create_line(861,121,861,165,width="5",tag="timelin")
                if 2520<=Time<2880 or 6840<=Time<7200:
                    canvas.create_line(861,121,839,159,width="5",tag="timelin")
                if 2880<=Time<3240 or 7200<=Time<7560:
                    canvas.create_line(861,121,823,143,width="5",tag="timelin")
                if 3240<=Time<3600 or 7560<=Time<7920:
                    canvas.create_line(861,121,816,121,width="5",tag="timelin")
                if 3600<=Time<3960 or 7920<=Time<8280:
                    canvas.create_line(861,121,823,98,width="5",tag="timelin")
                if 4320<=Time<4680 or 8280<=Time<8640:
                    canvas.create_line(861,121,839,82,width="5",tag="timelin")
def accept(event):
    global gm, tool, questpick1
    canvas.unbind_all("i")
    canvas.unbind_all("o")
    if questpick1 == 0 and gm >= 10:
        gm=gm-10
        gm_label.config(text=f"Ghosts Captured: {gm}")
        tool=1
        equipment_logo(992,0)
        questpick1=1
    else:
        return
def acceptpass(event):
    global gems, mapv, tool, passpamm
    canvas.unbind_all("i")
    if mapv == 42 and gems == 3 and passpamm == 0:
        tool = 3
        equipment_logo(992,0)
        passpamm = 1
    else :
        return
def acceptguard(event):
    global gm, tool,daveenter,passpamm
    canvas.unbind_all("i")
    if tool==3 and passpamm==1:
        tool=0
        equipment_logo(992,0)
        daveenter=1
    else:
        return
def make_clickthrough(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    ex_style |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)    
    
def time():
    global Time,overlay, timeall
    Time=Time+1
    timeall=timeall+1
    if Time == 8640:
        Time=0
    if (Time > 6480 or Time < 2160) and overlay == None:
        overlay = tkinter.Toplevel()
        overlay.title("OverlayWindow")
        overlay.attributes("-topmost", True)         
        overlay.attributes("-alpha", 0.3)            
        overlay.configure(bg="black")
        overlay.overrideredirect(True)
        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        overlay.geometry(f"{w}x{h}+{x}+{y}")
        overlay.attributes("-transparentcolor", "pink")
        overlay.update_idletasks()
        overlay.lift(root) 
        hwnd = win32gui.FindWindow(None, "OverlayWindow")
        make_clickthrough(hwnd)
        
    elif overlay != None and 2160<Time<6480:
        overlay.destroy()
        overlay = None
    
# map code
def map1():
    
    alap=canvas.create_image(0,0,image=grass,tag="map",anchor="nw")
    global x1,a
    global y1,b
    global x ,mapv ,ghost_alive, ghost2_alive, eqtool,hp,gameover,wtrsplash
    eqtool= ""
    canvas.delete("ghostbossw")
    canvas.delete("barlow")
    canvas.delete(wtrsplash)
    mapv=1
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=30
    y1=0
    for h in range(3):
        for i in range(16):
            fa(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=30
    x1=30
    for i in range(16):
        fa(x1,670)
        x1=x1+64
    x1=992
    y1=192
    for i in range (8):
        ko(x1,y1)
        y1=y1+60
    newHouseImage = makeTransparent(house, "#ffffff")
    house_images.append(newHouseImage)
    canvas.create_image(700, 400, image=newHouseImage, tag="map", anchor="n")
    if hp <= 0:
        canvas.unbind_all("w")
        canvas.unbind_all("s")
        canvas.unbind_all("a")
        canvas.unbind_all("d")
        canvas.create_image(0,0,image=gameover,tag="game",anchor="nw")
def map1ch():
    global houseown,daveenter,bossinit,watrbosshp,hp,bricks1,bricks2,secwall,secwall2,x, mapv, after_id ,y, hidfor, textblob11, text_id,switch1,switch2,switch3,switch4,stand,stand1,stand2,stand3,switch_id,switch_id1,lamparr,switch_id2,switch_id3,lamp_id,lamp1,lamp2,lamp3,lamp4,Bulb,Bulbone,Bulbtwo,Bulbthree
    if mapv == 1:
        if x < 0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wallb_positions.clear()
            wall_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map2()
            equipment_logo(992,0)
            x = 1024
        else:
            canvas.after(100, map1ch)
    elif mapv == 2:
        if x > 1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map1()
            equipment_logo(992,0)
            x = 0
            
        else:
            canvas.after(100, map1ch)
        if x<340:
            x=x+10
        if y<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map3()
            equipment_logo(992,0)
            y = 768
    elif mapv == 3:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map2()
            equipment_logo(992,0)
            y = 0
            x=600
        else:
            canvas.after(100, map1ch)
        if x<340:
            x=x+10
        if y<64:
            y=y+10
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map4()
            equipment_logo(992,0)
            x=0
    elif mapv == 4:
        if x < 0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map3()
            equipment_logo(992,0)
            x = 1024
            y = 300
        else:
            canvas.after(100, map1ch)
            
        if 632<x<696 and 334<y<398:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave1()
            equipment_logo(992,0)
            x = 512
            y = 704
        if y < 0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            y = 768
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map17()
            equipment_logo(992,0)
            x=0
            y=350
    elif mapv == 5:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            map4()
            equipment_logo(992,0)
            x = 664
            y = 400
        else:
            canvas.after(100, map1ch)
        if x < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave2()
            equipment_logo(992,0)
            x = 1024
            y = 384
        if x > 1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave3()
            equipment_logo(992,0)
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave4()
            equipment_logo(992,0)
    elif mapv == 6:
        if x > 1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave1()
            equipment_logo(992,0)
            x = 0
            y = 352
        else:
            canvas.after(100, map1ch)
    elif mapv == 7:
        if x < 0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave1()
            equipment_logo(992,0)
            x = 1024
            y = 352
        else:
            canvas.after(100, map1ch)
    elif mapv == 8:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            canvas.delete("all")
            cave1()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
    elif mapv == 9:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map4()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
        if 192<y<256 and 288<x<352:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room1()
            equipment_logo(992,0)
            x=512
            y=768
        if 448<y<512 and 288<x<352:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room2()
            equipment_logo(992,0)
            x=512
            y=768
        if 192<y<256 and 672<x<736:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room3()
            equipment_logo(992,0)
            x=512
            y=768
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map6()
            equipment_logo(992,0)
            x=1024
            y=384
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map7()
            equipment_logo(992,0)
            x=512
            y=768
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map9()
            equipment_logo(992,0)
            x=0
            y=368
    elif mapv == 10:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            x=320
            y=256
        else:
            canvas.after(100, map1ch)
    elif mapv == 11:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            x=320
            y=512
        else:
            canvas.after(100, map1ch)
    elif mapv == 12:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            x=704
            y=256
        else:
            canvas.after(100, map1ch)
    elif mapv == 13:
        if x > 1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            x=0
            y=384
        else:
            canvas.after(100, map1ch)
        if x<340:
            x=x+10
        if 192<y<256 and 500<x<564:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room4()
            equipment_logo(992,0)
            x=512
            y=768
        if 192<y<256 and 820<x<884:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room5()
            equipment_logo(992,0)
            x=512
            y=768
        if 576<y<640 and 500<x<564:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room6()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 14:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map6()
            equipment_logo(992,0)
            x=532
            y=256
        else:
            canvas.after(100, map1ch)
    elif mapv == 15:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map6()
            equipment_logo(992,0)
            x=852
            y=256
        else:
            canvas.after(100, map1ch)
    elif mapv == 16:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map6()
            equipment_logo(992,0)
            x=532
            y=640
        else:
            canvas.after(100, map1ch)
    elif mapv == 17:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
        if x < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map8()
            equipment_logo(992,0)
            x=1024
            y=368
        if x > 1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map10()
            equipment_logo(992,0)
            x=0
            y=368
    elif mapv == 18:
        if x > 1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map7()
            equipment_logo(992,0)
            x=0
            y=368
        else:
            canvas.after(100, map1ch)
        if x<340:
            x=x+10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map11()
            equipment_logo(992,0)
            x=450
            y=768
    elif mapv == 19:
        if x < 0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map5()
            equipment_logo(992,0)
            x=1024
            y=368
        else:
            canvas.after(100, map1ch)
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map16()
            equipment_logo(992,0)
            x=0
            y=100
        if y>768:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map17()
            equipment_logo(992,0)
            x=512
            y=0 
    elif mapv == 20:
        if x < 0:
            if after_id:
                    canvas.after_cancel(after_id)
                    after_id = None
            if hidfor =="LLLL":
                tree_positions.clear()
                stone_positions.clear()
                wall_positions.clear()
                wallb_positions.clear()
                keyhole_positions.clear()
                boss1_positions.clear()
                brickwall_positions.clear()
                roofb_positions.clear()
                roofb2_positions.clear()
                canvas.delete("all")
                map7()
                equipment_logo(992,0)
                x=1024
                y=368
                hidfor=""
            else:
                if len(hidfor)==4:
                    hidfor=""
                tree_positions.clear()
                stone_positions.clear()
                wall_positions.clear()
                wallb_positions.clear()
                keyhole_positions.clear()
                boss1_positions.clear()
                brickwall_positions.clear()
                roofb_positions.clear()
                roofb2_positions.clear()
                canvas.delete("all")
                map10()
                equipment_logo(992,0)
                x=512
                y=368
                hidfor=hidfor+"L"
                
        else:
            canvas.after(100, map1ch)
        if x>1024:
            if hidfor =="RRRR":
                    tree_positions.clear()
                    stone_positions.clear()
                    wall_positions.clear()
                    wallb_positions.clear()
                    keyhole_positions.clear()
                    boss1_positions.clear()
                    brickwall_positions.clear()
                    roofb_positions.clear()
                    roofb2_positions.clear()
                    canvas.delete("all")
                    map13()
                    equipment_logo(992,0)
                    x=0
                    y=512
                    hidfor=""
            else:
                    if len(hidfor)==4:
                        hidfor=""
                    tree_positions.clear()
                    stone_positions.clear()
                    wall_positions.clear()
                    wallb_positions.clear()
                    keyhole_positions.clear()
                    boss1_positions.clear()
                    brickwall_positions.clear()
                    roofb_positions.clear()
                    roofb2_positions.clear()
                    canvas.delete("all")
                    map10()
                    equipment_logo(992,0)
                    x=512
                    y=368
                    hidfor=hidfor+"R"
                
        if y>768:
            if hidfor =="LRLD":
                    tree_positions.clear()
                    stone_positions.clear()
                    wall_positions.clear()
                    wallb_positions.clear()
                    keyhole_positions.clear()
                    boss1_positions.clear()
                    brickwall_positions.clear()
                    roofb_positions.clear()
                    roofb2_positions.clear()
                    canvas.delete("all")
                    map14()
                    equipment_logo(992,0)
                    x=512
                    y=384
                    hidfor=""
            else:
                    if len(hidfor)==4:
                        hidfor=""
                    tree_positions.clear()
                    stone_positions.clear()
                    wall_positions.clear()
                    wallb_positions.clear()
                    keyhole_positions.clear()
                    boss1_positions.clear()
                    brickwall_positions.clear()
                    roofb_positions.clear()
                    roofb2_positions.clear()
                    canvas.delete("all")
                    map10()
                    equipment_logo(992,0)
                    x=512
                    y=368
                    hidfor=hidfor+"D"
        if y<0:
             if hidfor =="RRDU":
                    tree_positions.clear()
                    stone_positions.clear()
                    wall_positions.clear()
                    wallb_positions.clear()
                    keyhole_positions.clear()
                    boss1_positions.clear()
                    brickwall_positions.clear()
                    roofb_positions.clear()
                    roofb2_positions.clear()
                    canvas.delete("all")
                    map15()
                    equipment_logo(992,0)
                    x=512
                    y=384
                    hidfor=""
             else:
                    if len(hidfor)==4:
                        hidfor=""
                    tree_positions.clear()
                    stone_positions.clear()
                    wall_positions.clear()
                    wallb_positions.clear()
                    keyhole_positions.clear()
                    boss1_positions.clear()
                    brickwall_positions.clear()
                    roofb_positions.clear()
                    roofb2_positions.clear()
                    canvas.delete("all")
                    map10()
                    equipment_logo(992,0)
                    x=512
                    y=368
                    hidfor=hidfor+"U"
                
    elif mapv == 21:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map8()
            equipment_logo(992,0)
            x=450
            y=0
        else:
            canvas.after(100, map1ch)
        if x<340:
            x=x+10
        if y<130:
            y=y+10
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map12()
            equipment_logo(992,0)
            x=0
            y=210
    elif mapv == 22:
        if x < 0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map11()
            equipment_logo(992,0)
            x=1024
            y=210
        else:
            canvas.after(100, map1ch)
        if y<140:
            y=y+10
        if 496<x<560 and 500<y<564:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            room7()
            equipment_logo(992,0)
            x=480
            y=704
    elif mapv == 23:
        if y > 768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map12()
            equipment_logo(992,0)
            x=544
            y=564
        else:
            canvas.after(100, map1ch)
        if x>1024:
            canvas.unbind_all("w")
            canvas.unbind_all("s")
            canvas.unbind_all("a")
            canvas.unbind_all("d")
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map12()
            equipment_logo(992,0)
            text_id = canvas.create_image(0, 468, image=textblob11, anchor="nw")
            x=544
            y=564
    elif mapv == 24:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map10()
            equipment_logo(992,0)
            x=1024
            y=368
        else:
            canvas.after(100, map1ch)
        if y>768:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map16()
            equipment_logo(992,0)
            x=512
            y=0
    elif mapv == 25:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map10()
            equipment_logo(992,0)
            x=1024
            y=368
        else:
            canvas.after(100, map1ch)
        if y<140:
            y=y+10
    elif mapv == 26:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            map10()
            equipment_logo(992,0)
            x=1024
            y=368
        else:
            canvas.after(100, map1ch)
        if y<140:
            y=y+10
        if 400<x<464 and 396<y<460:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            dun1()
            equipment_logo(992,0)
            x=512
            y=704
    elif mapv == 27:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map15()
            equipment_logo(992,0)
            x=470
            y=400
        else:
            canvas.after(100, map1ch)
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun2()
            equipment_logo(992,0)
            x=1024
            y=350
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            
            dun5()
            equipment_logo(992,0)
            x=0
            y=350
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun8()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 28:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun1()
            equipment_logo(992,0)
            x=0
            y=350
        else:
            canvas.after(100, map1ch)
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun3()
            equipment_logo(992,0)
            x=1024
            y=350
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun4()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 29:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun1()
            equipment_logo(992,0)
            x=0
            y=350
        else:
            canvas.after(100, map1ch)
    elif mapv == 30:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun1()
            equipment_logo(992,0)
            x=0
            y=350
        else:
            canvas.after(100, map1ch)
    elif mapv == 31:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            
            dun1()
            equipment_logo(992,0)
            x=1024
            y=350
        else:
            canvas.after(100, map1ch)
        if not (326 < x < 390 and 366 < y < 430):
            stand = 0
        elif stand == 0 and (326 < x < 390 and 366 < y < 430):
            stand = 1
            switch1 = 2 if switch1 == 1 else 1
            if switch_id is not None:
                canvas.delete(switch_id)
                switch_id = None
            if switch1 % 2 == 0:
                switch_id = canvas.create_image(358, 366, image=onswitch, anchor="n")
                if lamp1==0:
                    lamp1=1
                    Bulb1(357,304)
                    lamparr.append(lamp1)
                elif lamp1==1:
                    lamp1=0
                    canvas.delete(Bulb)
                    lamparr.pop(lamp1)
                if lamp2==0:
                    lamp2=1
                    Bulb2(482,304)
                    lamparr.append(lamp2)
                elif lamp2==1:
                    lamp2=0
                    canvas.delete(Bulbone)
                    lamparr.pop(lamp2)
            else:
                
                switch_id = canvas.create_image(358, 366, image=offswitch, anchor="n")
                if lamp1==0:
                    lamp1=1
                    Bulb1(357,304)
                    lamparr.append(lamp1)
                elif lamp1==1:
                    lamp1=0
                    canvas.delete(Bulb)
                    lamparr.pop(lamp1)
                if lamp2==0:
                    lamp2=1
                    Bulb2(482,304)
                    lamparr.append(lamp2)
                elif lamp2==1:
                    lamp2=0
                    canvas.delete(Bulbone)
                    lamparr.pop(lamp2)
        if not (452 < x < 516 and 366 < y < 430):
            stand1 = 0
        elif stand1 == 0 and (452 < x < 516 and 366 < y < 430):
            stand1 = 1
            switch2 = 2 if switch2 == 1 else 1
            if switch_id1 is not None:
                canvas.delete(switch_id1)
                switch_id1 = None
            if switch2 % 2 == 0:
                switch_id1 = canvas.create_image(484, 366, image=onswitch, anchor="n")
                if lamp3==0:
                    lamp3=1
                    Bulb3(611,304)
                    lamparr.append(lamp3)
                elif lamp3==1:
                    lamp3=0
                    canvas.delete(Bulbtwo)
                    lamparr.pop(lamp3)
                if lamp2==0:
                    lamp2=1
                    Bulb2(482,304)
                    lamparr.append(lamp2)
                elif lamp2==1:
                    lamp2=0
                    canvas.delete(Bulbone)
                    lamparr.pop(lamp2)
            else:
                
                switch_id1 = canvas.create_image(484, 366, image=offswitch, anchor="n")
                if lamp3==0:
                    lamp3=1
                    Bulb3(611,304)
                    lamparr.append(lamp3)
                elif lamp3==1:
                    lamp3=0
                    canvas.delete(Bulbtwo)
                    lamparr.pop(lamp3)
                if lamp2==0:
                    lamp2=1
                    Bulb2(482,304)
                    lamparr.append(lamp2)
                elif lamp2==1:
                    lamp2=0
                    canvas.delete(Bulbone)
                    lamparr.pop(lamp2)
        if not (582 < x < 648 and 366 < y < 430):
            stand2 = 0
        elif stand2 == 0 and (582 < x < 648 and 366 < y < 430):
            stand2 = 1
            switch3 = 2 if switch3 == 1 else 1
            if switch_id2 is not None:
                canvas.delete(switch_id2)
                switch_id2 = None
            if switch3 % 2 == 0:
                switch_id2 = canvas.create_image(613, 366, image=onswitch, anchor="n")
                if lamp3==0:
                    lamp3=1
                    Bulb3(611,304)
                    lamparr.append(lamp3)
                elif lamp3==1:
                    lamp3=0
                    canvas.delete(Bulbtwo)
                    lamparr.pop(lamp3)
                if lamp4==0:
                    lamp4=1
                    Bulb4(740,309)
                    lamparr.append(lamp4)
                elif lamp4==1:
                    lamp4=0
                    canvas.delete(Bulbthree)
                    lamparr.pop(lamp4)
            else:
                
                switch_id2 = canvas.create_image(613, 366, image=offswitch, anchor="n")
                if lamp3==0:
                    lamp3=1
                    Bulb3(611,304)
                    lamparr.append(lamp3)
                elif lamp3==1:
                    lamp3=0
                    canvas.delete(Bulbtwo)
                    lamparr.pop(lamp3)
                if lamp4==0:
                    lamp4=1
                    Bulb4(740,309)
                    lamparr.append(lamp4)
                elif lamp4==1:
                    lamp4=0
                    canvas.delete(Bulbthree)
                    lamparr.pop(lamp4)
        if not (708 < x < 772 and 366 < y < 430):
            stand3 = 0
        elif stand3 == 0 and (708 < x < 772 and 366 < y < 430):
            stand3 = 1
            switch4 = 2 if switch4 == 1 else 1
            if switch_id3 is not None:
                canvas.delete(switch_id3)
                switch_id3 = None
            if switch4 % 2 == 0:
                switch_id3 = canvas.create_image(740, 366, image=onswitch, anchor="n")
                if lamp1==0:
                    lamp1=1
                    Bulb1(357,304)
                    lamparr.append(lamp1)
                elif lamp1==1:
                    lamp1=0
                    canvas.delete(Bulb)
                    lamparr.pop(lamp1)
                
            else:
                
                switch_id3 = canvas.create_image(740, 366, image=offswitch, anchor="n")
                if lamp1==0:
                    lamp1=1
                    Bulb1(357,304)
                    lamparr.append(lamp1)
                elif lamp1==1:
                    lamp1=0
                    canvas.delete(Bulb)
                    lamparr.pop(lamp1)
        if len(lamparr)==4:
            canvas.delete(bricks1)
            brickwall_positions.clear()
        if len(lamparr)==3:
            canvas.delete(bricks2)
            brickwall_positions.clear()
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun6()
            equipment_logo(992,0)
            x=512
            y=768
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun7()
            equipment_logo(992,0)
            x=0
            y=350
    elif mapv == 32:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            
            dun5()
            equipment_logo(992,0)
            x=512
            y=500
        else:
            canvas.after(100, map1ch)
    elif mapv == 33:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            
            dun5()
            equipment_logo(992,0)
            x=512
            y=500
        else:
            canvas.after(100, map1ch)
    elif mapv == 34:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun1()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
    elif mapv == 35:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map9()
            equipment_logo(992,0)
            x=1024
            y=100
        else:
            canvas.after(100, map1ch)
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map13()
            equipment_logo(992,0)
            x=512
            y=768
        if y>768 and 220<x<284:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map18()
            equipment_logo(992,0)
            x=250
            y=0
        if y>768 and not 220<x<284:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map18()
            equipment_logo(992,0)
            x=700
            y=0
        if 400<y<500 and 220<x<284 and watrbosshp==3:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            dun9()
            equipment_logo(992,0)
            x=512
            y=680
        
    elif mapv == 36:
        if y<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map9()
            equipment_logo(992,0)
            x=512
            y=768
        else:
            canvas.after(100, map1ch)
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map4()
            equipment_logo(992,0)
            x=1024
            y=368
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map18()
            equipment_logo(992,0)
            x=0
            y=668
    elif mapv == 37:
        if y<0 and 220<x<282:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map16()
            equipment_logo(992,0)
            x=247
            y=768
        else:
            canvas.after(100, map1ch)
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map17()
            equipment_logo(992,0)
            x=1024
            y=668
        if y<0 and not 220<x<282:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map16()
            equipment_logo(992,0)
            x=700
            y=768
        if x >1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map19()
            equipment_logo(992,0)
            x=0
            y=668
    elif mapv == 38:  
        if y<0 :
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map16()
            equipment_logo(992,0)
            x=700
            y=768
        else:
            canvas.after(100, map1ch)
        if y<300 :
            hp = hp-10
        if hp <= 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            canvas.create_image(0,0,image=gameover,tag="game",anchor="nw")
            map1()
            equipment_logo(992,0)
            hp = maxhp
            gm = 0
            gm_label.config(text=f"Ghosts Captured: {gm}")
    elif mapv == 39:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map18()
            equipment_logo(992,0)
            x=1024
            y=668
        else:
            canvas.after(100, map1ch)
        if x >680:
            x=x-10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map20()
            equipment_logo(992,0)
            x=100
            y=768
    elif mapv == 40:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map19()
            equipment_logo(992,0)
            x=100
            y=0
        else:
            canvas.after(100, map1ch)
        if x >680:
            x=x-10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map21()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 41:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map20()
            equipment_logo(992,0)
            x=100
            y=0
        else:
            canvas.after(100, map1ch)
        if x > 1024:
            x=x-10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map22()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 42:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map21()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
        if x > 683:
            x=x-10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map23()
            equipment_logo(992,0)
            x=302
            y=768
    elif mapv == 43:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map22()
            equipment_logo(992,0)
            x=302
            y=0
        else:
            canvas.after(100, map1ch)
        if x < 266:
            x=x+10
        if x > 332:
            x=x-10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map24()
            equipment_logo(992,0)
            x=302
            y=768
    elif mapv == 44:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map23()
            equipment_logo(992,0)
            x=302
            y=0
        else:
            canvas.after(100, map1ch)
        if x < 266:
            x=x+10
        if y<314:
            y=y+10
        if x > 1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map25()
            equipment_logo(992,0)
            x=0
            y=346
    elif mapv == 45:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map24()
            equipment_logo(992,0)
            x=1024
            y=0
        else:
            canvas.after(100, map1ch)
        if y < 314:
            y=y+10
        if y > 378:
            y=y-10
        if x > 1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map26()
            equipment_logo(992,0)
            x=400
            y=384
    elif mapv == 46:
        if x<338:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map25()
            equipment_logo(992,0)
            x=1024
            y=0
        else:
            canvas.after(100, map1ch)
        if daveenter == 0 and x > 668 :
            x=x-10
        if 832<x<896 and 64<y<128:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room8()
            equipment_logo(992,0)
            x=512
            y=768
        if y > 768 and x < 668:
            y=y-10
        if 832<x<896 and 564<y<628:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room9()
            equipment_logo(992,0)
            x=512
            y=768
        if x>1024:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map28()
            equipment_logo(992,0)
            x=0
            y=384
        if y < 0 and x < 668 :
            y=y+10
    elif mapv == 47:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map26()
            equipment_logo(992,0)
            x=864
            y=128
        else:
            canvas.after(100, map1ch)
    elif mapv == 48:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map26()
            equipment_logo(992,0)
            x=864
            y=628
        else:
            canvas.after(100, map1ch)
    elif mapv == 49:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map26()
            equipment_logo(992,0)
            x=1024
            y=384
        else:
            canvas.after(100, map1ch)
        if 64<x<128 and 192<y<256:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room10()
            equipment_logo(992,0)
            x=512
            y=768
        if 490<x<554 and 192<y<256:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room11()
            equipment_logo(992,0)
            x=512
            y=768
        if 64<x<128 and 564<y<628:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room12()
            equipment_logo(992,0)
            x=512
            y=768
        if 490<x<554 and 564<y<628:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room13()
            equipment_logo(992,0)
            x=512
            y=768
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map28()
            equipment_logo(992,0)
            x=512
            y=768
        if y>768:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map30()
            equipment_logo(992,0)
            x=512
            y=0
    elif mapv == 50:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map27()
            equipment_logo(992,0)
            x=96
            y=256
        else:
            canvas.after(100, map1ch)
    elif mapv == 51:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map27()
            equipment_logo(992,0)
            x=522
            y=256
        else:
            canvas.after(100, map1ch)
    elif mapv == 52:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map27()
            equipment_logo(992,0)
            x=96
            y=628
        else:
            canvas.after(100, map1ch)
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            cave5()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 53:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room12()
            equipment_logo(992,0)
            x=96
            y=64
        else:
            canvas.after(100, map1ch)
    elif mapv == 54:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map27()
            equipment_logo(992,0)
            x=522
            y=628
        else:
            canvas.after(100, map1ch)
    elif mapv == 55:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map27()
            equipment_logo(992,0)
            x=300
            y=0
        else:
            canvas.after(100, map1ch)
        if x > 684:
            x=x-10
        if x < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map29()
            equipment_logo(992,0)
            x=1024
            y=384
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map32()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 56:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map28()
            equipment_logo(992,0)
            x=0
            y=384
        else:
            canvas.after(100, map1ch)
        if 620<x<700 and 232<y<308:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room14()
            equipment_logo(992,0)
            x=512
            y=768
        if 832<x<996 and 240<y<304:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room15()
            equipment_logo(992,0)
            x=512
            y=768
        if 522<x<586 and 569<y<633:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room16()
            equipment_logo(992,0)
            x=512
            y=768
        if 832<x<996 and 569<y<633 and houseown==1:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room17()
            equipment_logo(992,0)
            x=512
            y=768
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map33()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 57:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map29()
            equipment_logo(992,0)
            x=650
            y=320
        else:
            canvas.after(100, map1ch)
    elif mapv == 58:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map29()
            equipment_logo(992,0)
            x=864
            y=304
        else:
            canvas.after(100, map1ch)
    elif mapv == 59:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map29()
            equipment_logo(992,0)
            x=554
            y=633
        else:
            canvas.after(100, map1ch)
    elif mapv == 60:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map29()
            equipment_logo(992,0)
            x=864
            y=633
        else:
            canvas.after(100, map1ch)
    elif mapv == 61:
        if y<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map27()
            equipment_logo(992,0)
            x=512
            y=768
        else:
            canvas.after(100, map1ch)
        if x > 684:
            x=x-10
        if 67<x<131 and 127<y<200:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room18()
            equipment_logo(992,0)
            x=512
            y=768
        if 449<x<513 and 127<y<200:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room19()
            equipment_logo(992,0)
            x=512
            y=768
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map31()
            equipment_logo(992,0)
            x=1024
            y=384
    elif mapv == 62:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map30()
            equipment_logo(992,0)
            x=93
            y=223
        else:
            canvas.after(100, map1ch)
    elif mapv == 63:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map30()
            equipment_logo(992,0)
            x=480
            y=223
        else:
            canvas.after(100, map1ch)
        if y<384:
            y=y+10
    elif mapv == 64:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map30()
            equipment_logo(992,0)
            x=0
            y=384
        else:
            canvas.after(100, map1ch)
        if x<332:
            x=x+10
        if y>526:
            y=y-10
        if 607<x<659 and 349<y<442:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room20()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 65:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map31()
            equipment_logo(992,0)
            x=632
            y=460
        else:
            canvas.after(100, map1ch)
        if y < 0:
            y=y+10
        if x < 414 and y < 208:
            x=x+10
        if x > 667 and y < 208:
            x=x-10
    elif mapv == 66:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map28()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
        if x > 680:
            x=x-10
        if 285<x<349 and 245<y<346:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room21()
            equipment_logo(992,0)
            x=512
            y=768
        if 483<x<547 and 91<y<156:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            cave6()
            equipment_logo(992,0)
            x=512
            y=768
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map33()
            equipment_logo(992,0)
            x=1024
            y=384
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map34()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 67:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map32()
            equipment_logo(992,0)
            x=317
            y=346
        else:
            canvas.after(100, map1ch)
        if y < 229:
            y=y+10
        if x > 780:
            x=x-10
        if x < 200:
            x=x+10
        
    elif mapv == 68:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map32()
            equipment_logo(992,0)
            x=552
            y=186
        else:
            canvas.after(100, map1ch)
    elif mapv == 69:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map32()
            equipment_logo(992,0)
            x=0
            y=384
        else:
            canvas.after(100, map1ch)
        if y>768:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map29()
            equipment_logo(992,0)
            x=512
            y=0
        if x < 407:
            x=x+10
        if 596<x<660 and 164<y<228:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room22()
            equipment_logo(992,0)
            x=512
            y=768
        if 532<x<596 and 554<y<618:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room23()
            equipment_logo(992,0)
            x=512
            y=768
        if y<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map35()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 70:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map33()
            equipment_logo(992,0)
            x=628
            y=228
        else:
            canvas.after(100, map1ch)
    elif mapv == 71:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map33()
            equipment_logo(992,0)
            x=564
            y=618
        else:
            canvas.after(100, map1ch)
    elif mapv == 72:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map32()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
        if x<0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map35()
            equipment_logo(992,0)
            x=1024
            y=384
    elif mapv == 73:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map34()
            equipment_logo(992,0)
            x=0
            y=384
        else:
            canvas.after(100, map1ch)
        if x < 340:
            x=x+10
        if y > 768:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map33()
            equipment_logo(992,0)
            x=512
            y=0
    elif mapv == 74:
        if x<0:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map37()
            equipment_logo(992,0)
            x=1024
            y=384
        else:
            canvas.after(100, map1ch)
        if y>484:
            y=y-10
        if x>1024:
            x=x-10
        if y<359:
            y=y+10
    elif mapv == 75:
        if x>1024:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map36()
            equipment_logo(992,0)
            x=0
            y=384
        else:
            canvas.after(100, map1ch)
        if y>545:
            y=y-10
        if x<178:
            x=x+10
        if y < 335 and x < 454:
            y=y+10
        if y < 350 and x > 627:
            y=y+10
        if y < 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map38()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 76:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map37()
            equipment_logo(992,0)
            x=512
            y=0
        else:
            canvas.after(100, map1ch)
        if x<468:
            x=x+10
        if x > 594:
            x=x-10
        if y<516:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            room24()
            equipment_logo(992,0)
            x=512
            y=768
    elif mapv == 77:
        if y>768:
            if after_id:
                canvas.after_cancel(after_id)
                after_id = None
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            Door4k_positions.clear()
            canvas.delete("all")
            map38()
            equipment_logo(992,0)
            x=512
            y=584
        else:
            canvas.after(100, map1ch)
        
        
        
        
            
        
        
        
                
            
def map2():
    
    canvas.create_image(0,0,image=alap2,anchor="nw",tag="map")
    global x1,x,x2
    global y1,y,y2 ,mapv ,ghost_alive ,ghost2_alive, textblob1_raw, textblob1, eqtool
    eqtool= ""
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=1024
    mapv = 2
    x1=352
    y1=670
    
    for i in range(11):
        fa(x1,y1)
        x1=x1+64
    y1=0
    x1=880
    for i in range(3):
        fa(x1,y1)
        x1=x1+64
    x1=944
    y1=64
    for i in range(2):
        fa(x1,y1)
        x1=x1+64
    x1=1008
    y1=128
    fa(x1,y1)
    x1=520
    y=300
    for i in range(2):
        for k in range(2):
            ko(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=520
    x1=720
    y=600
    for i in range(2):
        for k in range(3):
            ko(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=720
        a=500
        b=500
    
    infslab(a,b)
    equipment_logo(992, 0)
def map3():
    canvas.create_image(0,0,image=alap2,anchor="nw",tag="map")
    global x1,x,x2
    global y1,y,y2 ,mapv ,ghost_alive,ghost2_alive ,a,b, textblob1_raw, textblob1, eqtool
    eqtool= ""
    ghost_alive = True
    ghost_alive2 = True
    bosseye_alive = False
    bosseye3_alive = False
    bosseye2_alive = False
    y=1024
    mapv = 3
    y1=0
    x1=416
    
    for i in range(10):
        fal(x1,y1)
        x1=x1+64
    x1=352
    fa(x1,y1)
    x1=880
    y1=576
    for i in range(3):
        for i in range(3):
            fa(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=880
    x1 = 736
    y1 = 236
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
        
    x1=736
    y1=y1+64
    fal(x1,y1)
    x1=x1+128
    fal(x1,y1)
    
    x1=736
    y1=y1+64
    fal(x1,y1)
    x1=x1+128
    fal(x1,y1)
    
    a=800
    b=300
    
    infslab(a,b)
    equipment_logo(992, 0)
def map4():
    alap=canvas.create_image(0,0,image=grass,tag="map",anchor="nw")
    global x1,a
    global y1,b
    global x ,mapv ,ghost_alive, ghost2_alive, eqtool
    eqtool= ""
    mapv=4
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=0
    y1=576
    fa(x1,y1)
    for i in range(3):
        for i in range(17):
            fa(x1,y1)
            x1=x1+64
        x1=0
        y1=y1+64
    x1=600
    y1=300
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
    x1=600
    y1=y1+64
    fal(x1,y1)
    x1=x1+128
    fal(x1,y1)
    x1=664
    cave(x1,y1)
    equipment_logo(992, 0)
def cave1():
    cavef=canvas.create_image(0,0,image=cave_floor,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    eqtool= ""
    
    mapv = 5
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    x=512
    y=704
    x1=0
    y1=704
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    if wallbrokometer == 0:
        fal2(992,320)
    if keybrokometer == 0:
        Keyhole(512,0)
    x1=992
    y1=704
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    x1=0
    y1=0
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    ko(550,432)
    ko(745,259)
    ko(400,340)
    equipment_logo(992, 0)
def cave2():
    cavef=canvas.create_image(0,0,image=cave_floor,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, pickused
    eqtool = "pickaxe"
    mapv = 6
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = True
    x = 1024
    y = 384
    x1=32
    y1=704
    
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    fal(32,y1-64)
    if pickused==0:
        yp=y1-64
        pickax(96,yp)
        
    x1=32
    y1=y1-128
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    for i in range(17):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=y1-64
    equipment_logo(992, 0)
def cave3():
    cavef=canvas.create_image(0,0,image=cave_floor,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool
    eqtool = "key"
    mapv = 7
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x = 0
    y = 384
    
    equipment_logo(992, 0)
    x1=32
    y1=0
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(6):
        fal(x1,y1)
        y1=y1+64
    y1=y1+64
    for i in range(6):
        fal(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=990
    y1=704
    for i in range(16):
        fal(x1,y1)
        y1=y1-64
    if pickable==0:
        kkey(786,393)
        xp=786
        yp=393
    ko(823, 247)
    ko(256,596)
    ko(579,356)
    infslab(850,393)
def cave4():
    cavef=canvas.create_image(0,0,image=cave_floor,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey
    eqtool = "gem"
    mapv = 8
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = True
    bosseye2_alive = True
    bosseye3_alive = True
    x = 512
    y = 768
    x1=32
    y1=0
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=768
    for i in range(16):
        fal(x1,y1)
        y1=y1-64
    x1=992
    y1=0
    for i in range(16):
        fal(x1,y1)
        y1=y1+64
    x1=1024
    y1=704
    for i in range(8):
        fal(x1,y1)
        x1=x1-64
    x1=x1-64
    for i in range(8):
        fal(x1,y1)
        x1=x1-64
    x1=448
    y1=336
    fal(x1,y1)
    x1=x1+128
    fal(x1,y1)
    x1=448
    y1=272
    fal(x1,y1)
    x1=x1+128
    fal(x1,y1)
    x1=448
    y1=208
    fal(x1,y1)
    x1=x1+64
    fal(x1,y1)
    x1=x1+64
    fal(x1,y1)
    Boss1(512,336)
    if pickkey == 0:
        Yellowgem(512,272)
def map5():
    alap=canvas.create_image(0,0,image=grass,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey
    eqtool = ""
    mapv = 9
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    y=768
    x1=32
    y1=0
    for i in range(5):
        fal(x1,y1)
        y1=y1+64
    y1=y1+128
    for i in range(6):
        fal(x1,y1)
        y1=y1+64
    x1=256
    y1=128
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=256
    y1=192
    Roofb(x1,y1)
    x1=x1+128
    Roofb(x1,y1)
    xd=x1-64
    yd=y1
    Door(xd,yd)
    
    x1=640
    y1=128
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=640
    y1=192
    Roofb(x1,y1)
    x1=x1+128
    Roofb(x1,y1)
    xd=x1-64
    yd=y1
    Door(xd,yd)
    
    x1=256
    y1=384
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=256
    y1=448
    Roofb(x1,y1)
    x1=x1+128
    Roofb(x1,y1)
    xd=x1-64
    yd=y1
    Door(xd,yd)
    
    x1=640
    y1=384
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=640
    y1=448
    Roofb(x1,y1)
    x1=x1+128
    Roofb(x1,y1)
    xd=x1-64
    yd=y1
    Roofb(xd,yd)
    Door(xd,yd)
    a=96
    b=256
    infslab(a,b)
def room1():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum
    eqtool = ""
    mapv = 10
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    infslab(850,200)
    if hppicknum ==0:
        xhp=300
        yhp=264
        hpcontobt(xhp,yhp)
    if mappicknum ==0:
        xmp=500
        ymp=264
        MMAP(xmp,ymp)
def room2():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum
    eqtool = ""
    mapv = 11
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def room3():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum
    eqtool = ""
    mapv = 12
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64   
    
def map6():
    
    canvas.create_image(0,0,image=alap2,anchor="nw",tag="map")
    global x1,x,x2
    global y1,y,y2 ,mapv ,ghost_alive ,ghost2_alive, textblob1_raw, textblob1, eqtool
    eqtool= ""
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=1024
    y=384
    mapv = 13    
    x1=340
    y1=704
    for i in range(14):
        fal(x1,y1)
        x1=x1+54
    x1=340
    y1=0
    for i in range(14):
        fal(x1,y1)
        x1=x1+54
    x1=992
    y1=0
    for i in range(5):
        fal(x1,y1)
        y1=y1+64
    y1=y1+128
    for i in range(6):
        fal(x1,y1)
        y1=y1+64
    x1=404
    y1=128
    for i in range(5):
        Roofb2(x1,y1)
        x1=x1+64
    x1=404
    y1=192
    Roofb(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    xd=x1+64
    yd=y1
    Door(xd,yd)
    x1=x1+128
    Roofb(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
    x1=788
    y1=128
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=788
    y1=192
    Roofb(x1,y1)
    x1=x1+128
    Roofb(x1,y1)
    xd=x1-64
    yd=y1
    Door(xd,yd)
    
    x1=404
    y1=448
    for i in range(5):
        Roofb2(x1,y1)
        x1=x1+64
    x1=404
    y1=512
    for i in range(5):
        Roofb2(x1,y1)
        x1=x1+64
    x1=404
    y1=576
    Roofb(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    xd=x1+64
    yd=y1
    Door(xd,yd)
    x1=x1+128
    Roofb(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
def room4():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum
    eqtool = ""
    mapv = 14
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def room5():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum
    eqtool = ""
    mapv = 15
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def room6():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum
    eqtool = ""
    mapv = 16
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
def map7():
    alap=canvas.create_image(0,0,image=grass,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey
    eqtool = ""
    mapv = 17
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=200
    y1=400
    for i in range(2):
        fa(x1,y1)
        x1=x1+64
    x1=200
    y1=y1+64
    for i in range(2):
        fa(x1,y1)
        x1=x1+64
    x1=800
    y1=200
    for i in range(2):
        fa(x1,y1)
        x1=x1+64
    x1=800
    y1=y1+64
    for i in range(2):
        fa(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(18):
        fa(x1,y1)
        x1=x1+64
    x1=32
    y1=y1+64
    for i in range(18):
        fa(x1,y1)
        x1=x1+64
def map8():
    canvas.create_image(0,0,image=alap2,anchor="nw",tag="map")
    global x1,x,x2
    global y1,y,y2 ,mapv ,ghost_alive ,ghost2_alive, textblob1_raw, textblob1, eqtool
    eqtool= ""
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=1024
    y=384
    mapv = 18
    x1=340
    y1=704
    for i in range(14):
        fal(x1,y1)
        x1=x1+54
    x1=596
    y1=0
    for i in range(14):
        fa(x1,y1)
        x1=x1+54
    x1=596
    y1=64
    for i in range(14):
        fa(x1,y1)
        x1=x1+54
    x1=784
    y1=256
    for i in range(2):
        ko(x1,y1)
        x1=x1+64
    x1=784
    y1=320
    for i in range(2):
        ko(x1,y1)
        x1=x1+64
    x1=450
    y1=456
    for i in range(2):
        ko(x1,y1)
        x1=x1+64
    x1=450
    y1=520
    for i in range(2):
        ko(x1,y1)
        x1=x1+64
def map9():
    global x1,x,x2
    global y1,y,y2 ,mapv ,ghost_alive ,ghost2_alive, textblob1_raw, textblob1, eqtool, Map3
    eqtool= ""
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=0
    y=384
    mapv=19
    x1=715
    y1=704
    for i in range(8):
        fal(x1,y1)
        y1=y1-64
    for i in range(5):
        fal(x1,y1)
        x1=x1+64
    canvas.create_image(0,0,image=Map3,anchor="nw",tag="map")
    x1=32
    y1=0
    for i in range(18):
        fa(x1,y1)
        x1=x1+64
    x1=220
    y1=64
    for i in range(10):
        fa(x1,y1)
        y1=y1+64
def map10():
    alap=canvas.create_image(0,0,image=grass,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey
    eqtool = ""
    mapv = 20
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(6):
        for i in range(9):
            fa(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=32
    x1=636
    y1=0
    for i in range(6):
        for i in range(9):
            fa(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=636
    x1=32
    y1=448
    for i in range(6):
        for i in range(9):
            fa(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=32
    x1=636
    y1=448
    for i in range(6):
        for i in range(9):
            fa(x1,y1)
            x1=x1+64
        y1=y1+64
        x1=636
def map11():
    global Map4
    canvas.create_image(0,0,image=Map4,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum1
    eqtool = ""
    mapv = 21
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=450
    y=768
    x1=522
    y1=768
    for i in range(4):
        for i in range(9):
            fa(x1,y1)
            y1=y1-64
        y1=768
        x1=x1+64
    for i in range(7):
        fa(x1,y1)
        y1=y1-64
    x1=x1+64
    y1=768
    for i in range(5):
        fa(x1,y1)
        y1=y1-64
    fa(x1,256)
    x1=x1+64
    y1=768
    for i in range(3):
        for i in range(9):
            fa(x1,y1)
            y1=y1-64
        y1=768
        x1=x1+64
    if hppicknum1 ==0:
        xhp=842
        yhp=448
        hpcontobt(xhp,yhp)
def map12():
    global Map5
    canvas.create_image(0,0,image=Map5,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum1
    eqtool = ""
    mapv = 22
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=0
    y=210
    x1=32
    y1=256
    for i in range(9):
        fa(x1,y1)
        y1=y1+64
    y1=y1-128
    for i in range(16):
        fa(x1,y1)
        x1=x1+64
    x1=x1-64
    for i in range(10):
        fa(x1,y1)
        y1=y1-64
    Brickwall(400,500)
    Brickwall(464,500)
    Door(528,500)
    Brickwall(592,500)
    Brickwall(656,500)
    x1=400
    y1=436
    for i in range(4):
        Roofb(x1,y1)
        x1=x1+64
    Roofb2(x1,y1)
    x1=400
    y1=y1-64
    for i in range(4):
        Roofb2(x1,y1)
        x1=x1+64
def room7():
    global padlo2
    canvas.create_image(0,0,image=padlo2,tag="map",anchor="nw")
    canvas.unbind_all("w")
    canvas.unbind_all("s")
    canvas.unbind_all("a")
    canvas.unbind_all("d")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum, textblob10, text_id
    eqtool = ""
    mapv = 23
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1+64
    y1=y1+64
    for i in range(7):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    Brickwall(480,64)
    Brickwall(928,128)
    Brickwall(870,640)
    Brickwall(544,640)
    Brickwall(544,576)
    Brickwall(608,64)
    Brickwall(794,64)
    Brickwall(344,128)
    Brickwall(410,254)
    Brickwall(410,318)
    Brickwall(344,446)
    Brickwall(96,382)
    Brickwall(512,832)
    text_id = canvas.create_image(0, 468, image=textblob10, anchor="nw")
def map13():
    alap=canvas.create_image(0,0,image=grass,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey
    eqtool = ""
    mapv = 24
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        fa(x1,y1)
        x1=x1+64
    x1=160
    y1=256
    for i in range(10):
        fa(x1,y1)
        x1=x1+64
    x1=992
    y1=0
    for i in range(16):
        fa(x1,y1)
        y1=y1+64
    x1=288
    y1=512
    for i in range(3):
        ko(x1,y1)
        x1=x1+64
    x1=288
    y1=y1+64
    for i in range(3):
        ko(x1,y1)
        x1=x1+64
def map14():
    global Map5
    canvas.create_image(0,0,image=Map5,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 25
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=128
    for i in range(12):
        fa(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(6):
        fa(x1,y1)
        y1=y1+64
    for i in range(7):
        fa(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        fa(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        fa(x1,y1)
        x1=x1+64
    if hppicknum2==0:
        xhp=512
        yhp=448
        hpcontobt(xhp,yhp)
def map15():
    global x1,a
    global y1,b ,y ,xp, yp
    x1=340
    y1=396
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    y1=y1-64
    x1=340
    for i in range(5):
        fal(x1,y1)
        x1=x1+64
    y1=y1-64
    x1=340
    for i in range(5):
        fal(x1,y1)
        x1=x1+64
    y1=y1-64
    x1=404
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    
    global Map6
    canvas.create_image(0,0,image=Map6,tag="map",anchor="nw")
    
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 26
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=128
    for i in range(12):
        fa(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(6):
        fa(x1,y1)
        y1=y1+64
    for i in range(7):
        fa(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        fa(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        fa(x1,y1)
        x1=x1+64
def dun1():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    eqtool= ""
    
    mapv = 27
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=512
    y=704
    x1=0
    y1=704
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=992
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=0
    y1=0
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    if pickable1 == 0 or pickable2 == 0 or pickable3 == 0 or pickable4==0:
        Door4k(x1,y1)
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    
def dun2():
    global padlo2
    canvas.create_image(0,0,image=padlo2,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    eqtool= ""
    
    mapv = 28
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=1024
    y=350
    x1=0
    y1=704
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=992
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=0
    y1=0
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    Brickwall(928,128)
    Brickwall(864,640)
    Brickwall(448,576)
    Brickwall(320,640)
    Brickwall(320,64)
    Brickwall(224,320)
    Brickwall(160,256)
    Brickwall(96,256)
def dun3():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer, pickable1,xp,yp
    eqtool= "key"
    
    mapv = 29
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=1024
    y=350
    x1=0
    y1=704
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(13):
        Brickwall(x1,y1)
        y1=y1-64
    x1=992
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=0
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    if pickable1==0:
        xp=512
        yp=386
        kkey(xp,yp)
def dun4():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum, pickable2
    eqtool = "key"
    mapv = 30
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=256
    b=384
    infslab(a,b)
    if pickable2==0:
        xp=512
        yp=386
        kkey(xp,yp)
def dun5():
    global padlo3
    canvas.create_image(0,0,image=padlo3,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer,secwall,secwall2
    eqtool= ""
    
    mapv = 31
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=0
    y=350
    x1=0
    y1=704
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=992
    y1=704
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    Brickwall1(x1,y1)
    y1=y1-64
    for i in range(6):
        Brickwall(x1,y1)
        y1=y1-64
    x1=0
    y1=0
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    Brickwall2(x1,y1)
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
def dun6():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum, pickable2
    eqtool = "key"
    mapv = 32
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    if pickable3==0:
        xp=512
        yp=386
        kkey(xp,yp)
def dun7():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum, pickable4
    eqtool = "key"
    mapv = 33
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(5):
        Brickwall(x1,y1)
        y1=y1+64
    y1=y1+64
    for i in range(8):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    
    if pickable4==0:
        xp=512
        yp=386
        kkey(xp,yp)
def dun8():
    padlo=canvas.create_image(0,0,image=planks,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum, pickable4,pickkey2
    eqtool = "gem"
    mapv = 34
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    if pickkey2==0:
        xg=512
        yg=384
        Yellowgem(xg,yg)
    a=400
    b=384
    infslab(a,b)
def map16():
    global x1,a
    global y1,b ,y ,xp, yp
    x1=32
    y1=218
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    x1=453
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=324
    y1=500
    for i in range(8):
        fal(x1,y1)
        y1=y1+64
    x1=180
    y1=500
    for i in range(8):
        fal(x1,y1)
        y1=y1+64
    
    global Map7
    canvas.create_image(0,0,image=Map7,tag="map",anchor="nw")
    
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 35
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    Roofb(188,436)
    Door(252,436)
    Roofb(316,436)
    Roofb2(188,372)
    Roofb2(252,372)
    Roofb2(316,372)
    x1=992
    y1=0
    for i in range(16):
        fa(x1,y1)
        y1=y1+64
def map17():
    global x1,a
    global y1,b ,y ,xp, yp
    x1=714
    y1=0
    for i in range(10):
        fal(x1,y1)
        y1=y1+64
    y1=y1-64
    x1=x1+64
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    
    global Map8
    canvas.create_image(0,0,image=Map8,tag="map",anchor="nw")
    
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 36
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    fa(350,480)
    fa(621,240)
    fa(178,985)
    fa(489,564)
    x1=32
    y1=704
    for i in range(16):
        fa(x1,y1)
        x1=x1+64
def map18():
    global x1,a
    global y1,b ,y ,xp, yp
    x1=32
    y1=486
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
    x1=x1+96
    for i in range(4):
        fal(x1,y1)
        x1=x1+64
    y1=y1-64
    for i in range(8):
        fal(x1,y1)
        y1=y1-64
    x1=188
    y1=490
    for i in range(9):
        fal(x1,y1)
        y1=y1-64
    x1=316
    y1=490
    for i in range(9):
        fal(x1,y1)
        y1=y1-64
    
    global Map8
    canvas.create_image(0,0,image=Map9,tag="map",anchor="nw")
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 37
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    
    x1=32
    y1=704
    for i in range(16):
        fa(x1,y1)
        x1=x1+64
def dun9():
    padlo=canvas.create_image(0,0,image=padlo4,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y ,xp, yp
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum, mappicknum, pickable4,pickkey2,waterboss_alive,bossinit
    eqtool = "gem"
    mapv = 38
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    waterboss_alive = True
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    bosswater()
def map19():
    global x1,a
    global y1,b ,y ,xp, yp
    global Map10
    canvas.create_image(0,0,image=Map10,tag="map",anchor="nw")
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 39
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    
    x1=32
    y1=0
    for i in range(9):
        fa(x1,y1)
        y1=y1+64
    x1=253
    y1=273
    for i in range(3):
        fa(x1,y1)
        x1=x1+64
    x1=253
    y1=y1+64
    for i in range(3):
        fa(x1,y1)
        x1=x1+64
    x1=278
    y1=0
    for i in range(7):
        fa(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(11):
        fa(x1,y1)
        x1=x1+64
def map20():
    global x1,a
    global y1,b ,y ,xp, yp
    global Map10
    canvas.create_image(0,0,image=Map10,tag="map",anchor="nw")
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 40
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    
    x1=32
    y1=0
    for i in range(16):
        fa(x1,y1)
        y1=y1+64
    x1=253
    y1=273
    for i in range(3):
        fa(x1,y1)
        x1=x1+64
    x1=393
    y1=y1+64
    for i in range(3):
        fa(x1,y1)
        y1=y1+64
    x1=253
    for i in range(3):
        fa(x1,y1)
        x1=x1+64
    x1=279
    y1=704
    for i in range(7):
        fa(x1,y1)
        x1=x1+64
def map21():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    x1=722
    y1=0
    for i in range(5):
        fal(x1,y1)
        y1=y1+64
    y1=y1-64
    x1=x1+64
    for i in range(4):
        fal(x1,y1)
        x1=x1+64
    y1=y1+128
    yhp=y1-64
    xhp=x1-64
    x1=786
    for i in range(4):
        fal(x1,y1)
        x1=x1+64
    x1=722
    for i in range(10):
        fal(x1,y1)
        y1=y1+64
    global Map10
    canvas.create_image(0,0,image=Map10,tag="map",anchor="nw")
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 41
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    
    x1=32
    y1=0
    for i in range(16):
        fa(x1,y1)
        y1=y1+64
    x1=253
    y1=273
    for i in range(3):
        fa(x1,y1)
        x1=x1+64
    x1=386
    y1=564
    for i in range(2):
        ko(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=386
    for i in range(2):
        ko(x1,y1)
        x1=x1+64
    if hppicknum3==0:
        hpcontobt(xhp,yhp)
def map22():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    x1=32
    y1=96
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
    for i in range(4):
        fal(x1,y1)
        y1=y1-64
    y1=96
    x1=364
    for i in range(10):
        fal(x1,y1)
        x1=x1+64
    x1=364
    y1=96
    for i in range(4):
        fal(x1,y1)
        y1=y1-64
    global Map11
    canvas.create_image(0,0,image=Map11,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 42
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    
    x1=32
    y1=0
    for i in range(16):
        fa(x1,y1)
        y1=y1+64
    a=475
    b=270
    infslab(a,b)
def map23():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global Map13
    canvas.create_image(0,0,image=Map13,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 43
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
def map24():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    x1=364
    y1=704
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    y1=380
    x1=364
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    global Map14
    canvas.create_image(0,0,image=Map14,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 44
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
def map25():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global Map15
    canvas.create_image(0,0,image=Map15,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 45
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
def map26():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global alap2
    canvas.create_image(0,0,image=alap2,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 46
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    y1=315
    x1=32
    for i in range(6):
        Roofb2(x1,y1)
        x1=x1+64
    x1=668
    y1=0
    for i in range(5):
        fal(x1,y1)
        y1=y1+64
    y1=y1+128
    for i in range(6):
        fal(x1,y1)
        y1=y1+64
    a=600
    b=300
    infslab(a,b)
    x1=928
    y1=0
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1-64
    x1=928
    y1=64
    Roofb(x1,y1)
    x1=x1-64
    Door(x1,y1)
    x1=x1-64
    Roofb(x1,y1)
    x1=928
    y1=500
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1-64
    x1=928
    y1=564
    Roofb(x1,y1)
    x1=x1-64
    Door(x1,y1)
    x1=x1-64
    Roofb(x1,y1)
def room8():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 47
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def room9():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 48
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def map27():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global alap2
    canvas.create_image(0,0,image=Map10,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 49
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=650
    y1=0
    for i in range(20):
        fal(x1,y1)
        y1=y1+64
    x1=32
    y1=64
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=32
    y1=128
    for i in range(3):
        Roofb(x1,y1)
        x1=x1+64
    x1=32
    y1=192
    Brickwall(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Brickwall(x1,y1)
    
    
    x1=458
    y1=0
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=458
    y1=64
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=458
    y1=128
    for i in range(3):
        Roofb(x1,y1)
        x1=x1+64
    x1=458
    y1=192
    Brickwall(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Brickwall(x1,y1)
    
    x1=32
    y1=500
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=32
    y1=564
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
    x1=458
    y1=500
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    x1=458
    y1=564
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    a=320
    b=384
    infslab(a,b)
def room10():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 50
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def room11():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    canvas.create_image(0,0,image=padlo5,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 51
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=200
    infslab(a,b)
def room12():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    x1=588
    y1=170
    for i in range(10):
        Brickwall(x1,y1)
        x1=x1+64
    x1=588
    y1=234
    for i in range(10):
        Brickwall(x1,y1)
        x1=x1+64
    canvas.create_image(0,0,image=padlo6,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = "beer"
    mapv = 52
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=160
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    
    a=606
    b=110
    infslab(a,b)
def cave5():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,dis_gh_cntr
    global planks
    x1=217
    y1=120
    Brickwall(x1,y1)
    y1=y1+64
    Brickwall(x1,y1)
    x1=762
    y1=120
    Brickwall(x1,y1)
    y1=y1+64
    Brickwall(x1,y1)
    x1=410
    y1=280
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=720
    y1=360
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    canvas.create_image(0,0,image=barlang,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 53
    if dis_gh_cntr<1:
        ghost_alive = True
    if dis_gh_cntr<2:
        ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
def room13():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 54
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def map28():
    padlo=canvas.create_image(0,0,image=Map16,tag="map",anchor="nw")
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    eqtool= "wheat"
    
    mapv = 55
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x=512
    y=704
    x1=0
    y1=704
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    x1=x+128
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    y1=y1-128
    for i in range(6):
        fal(x1,y1)
        y1=y1-64
    x1=0
    y1=0
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    x1=x1+128
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
def map29():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    x1=500
    y1=270
    for i in range(2):
        fal(x1,y1)
        x1=x1+32
    x1=500
    y1=206
    for i in range(4):
        fal(x1,y1)
        x1=x1+64
    padlo=canvas.create_image(0,0,image=Map17,tag="map",anchor="nw")
    eqtool= ""
    
    mapv = 56
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=372
    y1=0
    for i in range(16):
        fal(x1,y1)
        y1=y1+64
    x1=372
    y1=704
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=800
    y1=176
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=800
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
    x1=490
    y1=505
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=490
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
    x1=800
    y1=505
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=800
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
def room14():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3
    global planks
    x1=96
    y1=654
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=212
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=325
    y1=345
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
    x1=807
    y1=450
    fal(x1,y1)
    x1=885
    y1=520
    fal(x1,y1)
    canvas.create_image(0,0,image=factory,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2
    eqtool = ""
    mapv = 57
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        fal(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    a=652
    b=452
    infslab(a,b)
def room15():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global planks
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2,pickupgrade,pickguide
    eqtool = ""
    mapv = 58
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=770
    b=257
    infslab(a,b)
    if pickupgrade==0:
        Upgrade(612,384)
    if pickguide==0:
        Guide(356,384)
    if hppicknum5==0:
        hpcontobt(500,384)
def room16():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global planks
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2,pickupgrade,pickguide
    eqtool = ""
    mapv = 59
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=770
    b=257
    infslab(a,b)
def room17():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo7
    canvas.create_image(0,0,image=padlo7,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2,pickupgrade,pickguide
    eqtool = ""
    mapv = 60
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
def map30():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    x1=41
    y1=60
    for i in range(3):
        Brickwall(x1,y1)
        x1=x1+64
    x1=41
    y1=y1+64
    for i in range(3):
        Brickwall(x1,y1)
        x1=x1+64
    x1=155
    y1=164
    for i in range(2):
        Brickwall(x1,y1)
    Brickwall(203,256)
    x1=433
    y1=60
    for i in range(3):
        Brickwall(x1,y1)
        x1=x1+64
    x1=433
    y1=y1+64
    for i in range(3):
        Brickwall(x1,y1)
        x1=x1+64
    x1=155
    y1=y1+64
    for i in range(2):
        Brickwall(x1,y1)
    x1=505
    y1=400
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=505
    y1=y1+64
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=704
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    padlo=canvas.create_image(0,0,image=Map18,tag="map",anchor="nw")
    eqtool= "gas"
    
    mapv = 61
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
def room18():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo7
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2,pickupgrade,pickguide
    eqtool = ""
    mapv = 62
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def room19():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo7
    canvas.create_image(0,0,image=padlo8,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum2,pickupgrade,pickguide
    eqtool = "gas"
    mapv = 63
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=340
    b=512
    infslab(a,b)
def map31():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    x1=577
    y1=352
    Brickwall(x1,y1)
    x1=577
    y1=y1+64
    Brickwall(x1,y1)
    x1=687
    y1=352
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    x1=687
    y1=y1+64
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    x1=577
    y1=288
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    x1=577
    y1=y1-64
    for i in range(2):
        fal(x1,y1)
        x1=x1+64
    padlo=canvas.create_image(0,0,image=Map19,tag="map",anchor="nw")
    eqtool= ""
    
    mapv = 64
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    y1=0
    x1=350
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
def room20():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo9
    x1=82
    y1=210
    for i in range(5):
        Brickwall(x1,y1)
        x1=x1+64
    x1=700
    y1=210
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=202
    y1=395
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=202
    y1=395
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=560
    y1=390
    for i in range(5):
        Brickwall(x1,y1)
        x1=x1+64
    
    canvas.create_image(0,0,image=padlo9,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey4, hppicknum2,pickupgrade,pickguide
    eqtool = "gem"
    mapv = 65
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    a=400
    b=455
    infslab(a,b)
    if pickkey4==0:
        xg=540
        yg=33
        Yellowgem(xg,yg)
def map32():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    x1=171
    y1=300
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=171
    y1=234
    for i in range(5):
        Brickwall(x1,y1)
        x1=x1+64
    x1=388
    y1=300
    for i in range(2):
        Brickwall(x1,y1)
        x1=x1+64
    x1=314
    y1=70
    Brickwall(x1,y1)
    padlo=canvas.create_image(0,0,image=Map20,tag="map",anchor="nw")
    eqtool= ""
    
    mapv = 66
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    y1=0
    x1=32
    for i in range(5):
        fal(x1,y1)
        y1=y1+64
    y1=y1+128
    for i in range(8):
        fal(x1,y1)
        y1=y1+64
def room21():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo10
    
    canvas.create_image(0,0,image=padlo10,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey4, hppicknum2,pickupgrade,pickguide
    eqtool = "gem"
    mapv = 67
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    a=400
    b=455
    infslab(a,b)

def cave6():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,dis_gh_cntr
    global cave_floor
    canvas.create_image(0,0,image=cave_floor,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum6
    eqtool = ""
    mapv = 68
    ghost_alive = True
    ghost2_alive = True
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        fal(x1,y1)
        x1=x1+64
    cave(x1,y1)
    x1=x1+64
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    if hppicknum6==0:
        xhp=512
        yhp=384
        hpcontobt(xhp,yhp)
def map33():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    padlo=canvas.create_image(0,0,image=alap2,tag="map",anchor="nw")
    eqtool= ""
    
    mapv = 69
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    y1=0
    x1=375
    for i in range(16):
        fal(x1,y1)
        y1=y1+64
    x1=500
    y1=100
    for i in range(5):
        Roofb2(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=500
    Roofb(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
    x1=500
    y1=480
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=500
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
    
    x1=750
    y1=480
    for i in range(3):
        Roofb2(x1,y1)
        x1=x1+64
    y1=y1+64
    x1=750
    Roofb(x1,y1)
    x1=x1+64
    Door(x1,y1)
    x1=x1+64
    Roofb(x1,y1)
def room22():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo10
    
    canvas.create_image(0,0,image=padlo11,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey4, hppicknum2,pickupgrade,pickguide
    eqtool = ""
    mapv = 70
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
def room23():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,hppicknum5 
    global padlo10
    
    canvas.create_image(0,0,image=planks,tag="map",anchor="nw") 
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey4, hppicknum2,pickupgrade,pickguide
    eqtool = ""
    mapv = 71
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=32
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        Brickwall(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        Brickwall(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        Brickwall(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(16):
        Brickwall(x1,y1)
        x1=x1+64
    a=512
    b=384
    infslab(a,b)
def map34():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    padlo=canvas.create_image(0,0,image=Map10,tag="map",anchor="nw")
    eqtool= ""
    
    mapv = 72
    ghost_alive = True
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=650
    y1=0
    for i in range(16):
        fal(x1,y1)
        y1=y1+64
    x1=32
    y1=0
    for i in range(10):
        fal(x1,y1)
        x1=x1+64
    x1=256
    y1=256
    for i in range(3):
        for i in range(6):
            fa(x1,y1)
            y1=y1+64
        x1=x1+64
        y1=256
def map35():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    x1=380
    y1=111
    for i in range(3):
        fal(x1,y1)
        x1=x1+64
    x1=485
    y1=310
    for i in range(4):
        fal(x1,y1)
        y1=y1-64
    padlo=canvas.create_image(0,0,image=Map21,tag="map",anchor="nw")
    eqtool= ""
    
    
    mapv = 73
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    x1=372
    y1=0
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=645
    y1=372
    for i in range(2):
        for i in range(4):
            fa(x1,y1)
            x1=x1+64
        x1=645
        y1=y1+64
def map36():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    
    padlo=canvas.create_image(0,0,image=Map22,tag="map",anchor="nw")
    eqtool= ""
    
    
    mapv = 74
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
def map37():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    
    padlo=canvas.create_image(0,0,image=Map23,tag="map",anchor="nw")
    eqtool= ""
    
    
    mapv = 75
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
def map38():
    
    global x1,a
    global y1,b ,y
    global x ,mapv ,ghost_alive, ghost2_alive, wallbrokometer, eqtool, xk, xk, keybrokometer
    
    padlo=canvas.create_image(0,0,image=Map24,tag="map",anchor="nw")
    eqtool= ""
    
    
    mapv = 76
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False 
def room24():
    global x1,a
    global y1,b ,y ,xp, yp,hppicknum3,dis_gh_cntr
    global cave_floor, textblob, text_id
    canvas.unbind_all("w")
    canvas.unbind_all("s")
    canvas.unbind_all("a")
    canvas.unbind_all("d")
    textblob=textblob47
    global x ,mapv ,ghost_alive, ghost2_alive ,pickable, eqtool, tool, bosseye_alive , pickkey, hppicknum6
    x1=32
    y1=0
    for i in range(16):
        fal(x1,y1)
        x1=x1+64
    x1=32
    y1=0
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=992
    y1=0
    for i in range(12):
        fal(x1,y1)
        y1=y1+64
    x1=32
    y1=704
    for i in range(7):
        fal(x1,y1)
        x1=x1+64
    x1=x1+64
    for i in range(8):
        fal(x1,y1)
        x1=x1+64
    canvas.create_image(0,0,image=padlo12,tag="map",anchor="nw")
    eqtool = ""
    mapv = 77
    ghost_alive = False
    ghost2_alive = False
    bosseye_alive = False
    bosseye2_alive = False
    bosseye3_alive = False
    text_id = canvas.create_image(0, 468, image=textblob, anchor="nw")   
def map_loop():
    global after_id
    map1ch()
    after_id = canvas.after(100, map_loop)
def time_loop():
    time()
    time_id = canvas.after(10, time_loop)








# Movement for the character
def mozog_jobb(event):
    global new_x, new_y, hp, hpmeter
    global huse,huse1,huse2,huse3,huse4,huse5,huse6,mapv, bosseyecap, bosseyecap1, bosseye2_alive, bosseyecap2, hppicknum
    if mapv in (1, 2, 3, 4, 9, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 35, 36, 37, 39, 40, 41, 42, 46, 49, 55, 56, 61, 64, 66, 69, 72, 73, 75, 76):
        walking_sound.play()
    elif mapv in (5, 6, 7, 8, 53, 57, 63, 65, 68, 74, 77):
        walkingcave_sound.play()
    elif mapv in (10,11,12,14,15,16,23,27,28,29,30,31,32,33,34,38,43,44,45,47,48,50,51,52,54,58,59,60,62,67,70,71):
        walkingwood_sound.play()
    
    enemy()
    
    if mapv in (3, 7, 11 ,18, 26, 27, 29, 53, 68):
        enemy2()
    if mapv == 8 and bosseyecap == 1:
        enemyboss1()
    if mapv == 8 and bosseyecap1==1:
        enemyboss2()
    if mapv == 8 and bosseyecap2==1:
        enemyboss3()
    global newPhotoImage
    newPhotoImage = makeTransparent(image,"#ffffff")
    global ember
    canvas.delete(ember)
    global x
    global y
    new_x = x + 10
    ember=canvas.create_image(x,y,image=newPhotoImage,tag="1")
    if mapv in (28,23):
        for i in range(32):
            if not check_collision(new_x, y):
                x=new_x
                new_x=x+32
    if mapv not in (28,23):        
        if not check_collision(new_x, y):
            x = new_x
    
    
    if hppicknum == 1 and huse == 0:
        hp = maxhp
        huse=1
    if hppicknum1 == 1 and huse1==0:
        hp = maxhp
        huse1=1
    if hppicknum2 == 1 and huse2==0:
        hp = maxhp
        huse2=1
    if hppicknum3 == 1 and huse3==0:
        hp = maxhp
        huse3=1
    if hppicknum4 == 1 and huse4==0:
        hp = maxhp
        huse4=1
    if hppicknum5 == 1 and huse5==0:
        hp = maxhp
        huse5=1
    if hppicknum6 == 1 and huse6==0:
        hp = maxhp
        huse6=1
    canvas.delete(hpmeter)
    hpmeter = canvas.create_text(900,750, text="health:"+str(hp), font="Impact 20", fill ="red")
    
def mozog_bal(event):
    global new_x, new_y, hp, hpmeter
    global huse,huse1,huse2,huse3,huse4,huse5,huse6,mapv, bosseyecap , bosseyecap1, bosseye2_alive, bosseyecap2, hppicknum
    if mapv in (1, 2, 3, 4, 9, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 35, 36, 37, 39, 40, 41, 42, 46, 49, 55, 56, 61, 64, 66, 69, 72, 73, 75, 76):
        walking_sound.play()
    elif mapv in (5, 6, 7, 8, 53, 57, 63, 65, 68, 74, 77):
        walkingcave_sound.play()
    elif mapv in (10,11,12,14,15,16,23,27,28,29,30,31,32,33,34,38,43,44,45,47,48,50,51,52,54,58,59,60,62,67,70,71):
        walkingwood_sound.play()

    enemy()
    
    
    if mapv in (3, 7,11, 18, 26, 27, 29, 53, 68):
        enemy2()
    if mapv == 8 and bosseyecap == 1:
        enemyboss1()
    if mapv == 8 and bosseyecap1==1:
        enemyboss2()
    if mapv == 8 and bosseyecap2==1:
        enemyboss3()
    global newPhotoImage
    newPhotoImage = makeTransparent(image1,"#ffffff")
    global ember
    canvas.delete(ember)
    global x
    global y
    new_x = x - 10
    ember=canvas.create_image(x,y,image=newPhotoImage,tag="1")
    if mapv in (28,23):
        for i in range(32):
            if not check_collision(new_x, y):
                x=new_x
                new_x=x-32
    if mapv not in (28,23):        
        if not check_collision(new_x, y):
            x = new_x
    
    
    if hppicknum == 1 and huse == 0:
        hp = maxhp
        huse=1
    if hppicknum1 == 1 and huse1==0:
        hp = maxhp
        huse1=1
    if hppicknum2 == 1 and huse2==0:
        hp = maxhp
        huse2=1
    if hppicknum3 == 1 and huse3==0:
        hp = maxhp
        huse3=1
    if hppicknum4 == 1 and huse4==0:
        hp = maxhp
        huse4=1
    if hppicknum5 == 1 and huse5==0:
        hp = maxhp
        huse5=1
    if hppicknum6 == 1 and huse6==0:
        hp = maxhp
        huse6=1
    canvas.delete(hpmeter)
    hpmeter = canvas.create_text(900,750, text="health:"+str(hp), font="Impact 20" ,fill ="red")
    
def mozog_elo(event):
    global new_x, new_y, hp, hpmeter
    global huse,huse1,huse2,huse3,huse4,huse5,huse6,mapv, bosseyecap, bosseyecap1, bosseye2_alive ,bosseyecap2, hppicknum
    if mapv in (1, 2, 3, 4, 9, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 35, 36, 37, 39, 40, 41, 42, 46, 49, 55, 56, 61, 64, 66, 69, 72, 73, 75, 76):
        walking_sound.play()
    elif mapv in (5, 6, 7, 8, 53, 57, 63, 65, 68, 74, 77):
        walkingcave_sound.play()
    elif mapv in (10,11,12,14,15,16,23,27,28,29,30,31,32,33,34,38,43,44,45,47,48,50,51,52,54,58,59,60,62,67,70,71):
        walkingwood_sound.play()

    enemy()
    
    if mapv in (3, 7,11, 18, 26, 27, 29, 53, 68):
        enemy2()
    if mapv == 8 and bosseyecap == 1:
        enemyboss1()
    if mapv == 8 and bosseyecap1==1:
        enemyboss2()
    if mapv == 8 and bosseyecap2==1:
        enemyboss3()
    global newPhotoImage
    newPhotoImage = makeTransparent(image2,"#ffffff")
    global ember
    canvas.delete(ember)
    global x
    global y
    new_y = y - 10
    ember=canvas.create_image(x,y,image=newPhotoImage,tag="1")
    if mapv in (28,23):
        for i in range(32):
            if not check_collision(x, new_y):
                y=new_y
                new_y=y-32
    if mapv not in (28,23):        
        if not check_collision(x, new_y):
            y = new_y
    
    if hppicknum == 1 and huse == 0:
        hp = maxhp
        huse=1
    if hppicknum1 == 1 and huse1==0:
        hp = maxhp
        huse1=1
    if hppicknum2 == 1 and huse2==0:
        hp = maxhp
        huse2=1
    if hppicknum3 == 1 and huse3==0:
        hp = maxhp
        huse3=1
    if hppicknum4 == 1 and huse4==0:
        hp = maxhp
        huse4=1
    if hppicknum5 == 1 and huse5==0:
        hp = maxhp
        huse5=1
    if hppicknum6 == 1 and huse6==0:
        hp = maxhp
        huse6=1
    canvas.delete(hpmeter)
    hpmeter = canvas.create_text(900,750, text="health:"+str(hp), font="Impact 20", fill ="red")
    
def mozog_hat(event):
    global new_x, new_y, hp ,hpmeter
    global huse,huse1,huse2,huse3,huse4,huse5,huse6,mapv, bosseyecap ,bosseyecap1, bosseye2_alive, bosseyecap2, hppicknum
    if mapv in (1, 2, 3, 4, 9, 13, 17, 18, 19, 20, 21, 22, 24, 25, 26, 35, 36, 37, 39, 40, 41, 42, 46, 49, 55, 56, 61, 64, 66, 69, 72, 73, 75, 76):
        walking_sound.play()
    elif mapv in (5, 6, 7, 8, 53, 57, 63, 65, 68, 74, 77):
        walkingcave_sound.play()
    elif mapv in (10,11,12,14,15,16,23,27,28,29,30,31,32,33,34,38,43,44,45,47,48,50,51,52,54,58,59,60,62,67,70,71):
        walkingwood_sound.play()

    enemy()
    
    if mapv in (3, 7,11, 18, 26, 27, 29, 53, 68):
        enemy2()
    if mapv == 8 and bosseyecap == 1:
        enemyboss1()
    if mapv == 8 and bosseyecap1==1:
        enemyboss2()
    if mapv == 8 and bosseyecap2==1:
        enemyboss3()
    global newPhotoImage
    newPhotoImage = makeTransparent(image3,"#ffffff")
    global ember
    canvas.delete(ember)
    global x
    global y
    new_y = y + 10
    ember=canvas.create_image(x,y,image=newPhotoImage,tag="1")
    if mapv in (28,23):
        for i in range(32):
            if not check_collision(x, new_y):
                y=new_y
                new_y=y+32
    if mapv not in (28,23):        
        if not check_collision(x, new_y):
            y = new_y
    
    
    if hppicknum == 1 and huse == 0:
        hp = maxhp
        huse=1
    if hppicknum1 == 1 and huse1==0:
        hp = maxhp
        huse1=1
    if hppicknum2 == 1 and huse2==0:
        hp = maxhp
        huse2=1
    if hppicknum3 == 1 and huse3==0:
        hp = maxhp
        huse3=1
    if hppicknum4 == 1 and huse4==0:
        hp = maxhp
        huse4=1
    if hppicknum5 == 1 and huse5==0:
        hp = maxhp
        huse5=1
    if hppicknum6 == 1 and huse6==0:
        hp = maxhp
        huse6=1
    canvas.delete(hpmeter)
    hpmeter = canvas.create_text(900,750, text="health:"+str(hp), font="Impact 20", fill ="red")


def check_collision(new_x, new_y):
    half_size = 16 
    char_left = new_x - half_size
    char_right = new_x + half_size
    char_top = new_y - half_size
    char_bottom = new_y + half_size

    for (tx, ty) in tree_positions:
        
        offset = 16
        tree_left = tx - half_size
        tree_right = tx + half_size
        tree_top = ty + offset - half_size
        tree_bottom = ty + offset + half_size

        if not (char_right <= tree_left or char_left >= tree_right or
                char_bottom <= tree_top or char_top >= tree_bottom):
            return True
    for (sx, sy) in stone_positions:
        offset = 16
        stone_left = sx - half_size
        stone_right = sx + half_size
        stone_top = sy + offset - half_size
        stone_bottom = sy + offset + half_size

        if not (char_right <= stone_left or char_left >= stone_right or
                char_bottom <= stone_top or char_top >= stone_bottom):
            return True
    for (wx, wy) in wall_positions:
        offset = 16
        wall_left = wx - half_size
        wall_right = wx + half_size
        wall_top = wy + offset - half_size
        wall_bottom = wy + offset + half_size

        if not (char_right <= wall_left or char_left >= wall_right or
                char_bottom <= wall_top or char_top >= wall_bottom):
            return True
    for (bx, wb) in wallb_positions:
        offset = 16
        wallb_left = bx - half_size
        wallb_right = bx + half_size
        wallb_top = wb + offset - half_size
        wallb_bottom = wb + offset + half_size

        if not (char_right <= wallb_left or char_left >= wallb_right or
                char_bottom <= wallb_top or char_top >= wallb_bottom):
            return True
    for (xw, yw) in keyhole_positions:
        offset = 16
        keyhole_left = xw - half_size
        keyhole_right = xw + half_size
        keyhole_top = yw + offset - half_size
        keyhole_bottom = yw + offset + half_size

        if not (char_right <= keyhole_left or char_left >= keyhole_right or
                char_bottom <= keyhole_top or char_top >= keyhole_bottom):
            return True
    for (box, bow) in boss1_positions:
        offset = 16
        boss1_left = box - half_size
        boss1_right = box + half_size
        boss1_top = bow + offset - half_size
        boss1_bottom = bow + offset + half_size

        if not (char_right <= boss1_left or char_left >= boss1_right or
                char_bottom <= boss1_top or char_top >= boss1_bottom):
            return True
    for (brx, brw) in brickwall_positions:
        offset = 16
        brickwall_left = brx - offset -  half_size
        brickwall_right = brx + offset + half_size
        brickwall_top = brw + offset - half_size
        brickwall_bottom = brw + offset + half_size

        if not (char_right <= brickwall_left or char_left >= brickwall_right or
                char_bottom <= brickwall_top or char_top >= brickwall_bottom):
            return True
    for (rfx, rfw) in roofb_positions:
        offset = 16
        roofb_left = rfx - half_size
        roofb_right = rfx + half_size
        roofb_top = rfw + offset - half_size
        roofb_bottom = rfw + offset + half_size

        if not (char_right <= roofb_left or char_left >= roofb_right or
                char_bottom <= roofb_top or char_top >= roofb_bottom):
            return True
    for (rf2x, rf2w) in roofb2_positions:
        offset = 16
        roofb2_left = rf2x - half_size
        roofb2_right = rf2x + half_size
        roofb2_top = rf2w + offset - half_size
        roofb2_bottom = rf2w + offset + half_size

        if not (char_right <= roofb2_left or char_left >= roofb2_right or
                char_bottom <= roofb2_top or char_top >= roofb2_bottom):
            return True
    for (xdpx, xdpw) in Door4k_positions:
        offset = 16
        Door4k_left = xdpx - offset -  half_size
        Door4k_right =xdpx + offset + half_size
        Door4k_top = xdpw + offset - half_size
        Door4k_bottom = xdpw + offset + half_size

        if not (char_right <= Door4k_left or char_left >= Door4k_right or
                char_bottom <= Door4k_top or char_top >= Door4k_bottom):
            return True
    return False
# enemies
def enemy():
    global ghost2
    global ember, x, y, y2, x2, hp, ghost_alive, maxhp, mapv, gameover

    speed = 5  
    if not ghost_alive:
        return x2, y2 
    dx = x2 - x
    dy = y2 - y

    
    if abs(dy) < 1e-6:
        d = 0
    else:
        d = dx / dy

    canvas.delete(ghost2)
    newGhostImage = makeTransparent(ghost, "#ffffff")
    ghost_images.append(newGhostImage)
    ghost2 = canvas.create_image(x2, y2, image=newGhostImage, tag="6", )
    
    if abs(d) > 0:
        x2 += speed * (d / abs(d))  
    if abs(dy) > 0:
        y2 -= speed * (dy / abs(dy))
    if x2-32<x<x2+32 and y2-32<y<y2+32 :
        hp = hp-1
    if mapv > 10:
        if x2-32<x<x2+32 and y2-32<y<y2+32 :
            hp = hp-1
    if mapv > 20:
        if x2-32<x<x2+32 and y2-32<y<y2+32 :
            hp = hp-1
    if hp <= 0:
        tree_positions.clear()
        stone_positions.clear()
        wall_positions.clear()
        wallb_positions.clear()
        keyhole_positions.clear()
        boss1_positions.clear()
        brickwall_positions.clear()
        roofb_positions.clear()
        roofb2_positions.clear()
        canvas.delete("all")
        canvas.create_image(0,0,image=gameover,tag="game",anchor="nw")
        map1()
            
        equipment_logo(992,0)
        hp = maxhp
        gm = 0
        gm_label.config(text=f"Ghosts Captured: {gm}")
    return x2, y2

def enemy2():
    global ghost3, x, y, x3, y3, ghost2_alive, hp, maxhp, mapv,gameover

    speed = 5
    if not ghost2_alive:
        return x3, y3

    dx = x3 - x
    dy = y3 - y

    if abs(dy) < 1e-6:
        d = 0
    else:
        d = dx / dy

    canvas.delete(ghost3)
    newGhostImage = makeTransparent(ghost, "#ffffff")
    ghost_images.append(newGhostImage)
    ghost3 = canvas.create_image(x3, y3, image=newGhostImage, tag="7")

    if abs(d) > 0:
        x3 += speed * (d / abs(d))
    if abs(dy) > 0:
        y3 -= speed * (dy / abs(dy))
    if x3-32<x<x3+32 and y3-32<y<y3+32 :
        hp = hp-1
    if mapv > 10:
        if x3-32<x<x3+32 and y3-32<y<y3+32 :
            hp = hp-1
    if mapv > 20:
        if x3-32<x<x3+32 and y3-32<y<y3+32 :
            hp = hp-1
    if hp <= 0:
        tree_positions.clear()
        stone_positions.clear()
        wall_positions.clear()
        wallb_positions.clear()
        keyhole_positions.clear()
        boss1_positions.clear()
        brickwall_positions.clear()
        roofb_positions.clear()
        roofb2_positions.clear()
            
        canvas.delete("all")
            
        map1()
            
        equipment_logo(992,0)
        hp = maxhp
        gm = 0
        gm_label.config(text=f"Ghosts Captured: {gm}")
    return x3, y3
def enemyboss1():
    global ghost4
    global ember, x, y, y4, x4, hp, bosseye_alive, bosseye1, hp, maxhp,gameover

    speed = 5  
    if not bosseye_alive:
        return x4, y4 
    dx = x4 - x
    dy = y4 - y

    
    if abs(dy) < 1e-6:
        d = 0
    else:
        d = dx / dy

    canvas.delete(ghost4)
    newbosseyeImage = makeTransparent(bosseye1, "#ffffff")
    bosseye_images.append(newbosseyeImage)
    ghost4 = canvas.create_image(x4, y4, image=newbosseyeImage, tag="6", )
    
    if abs(d) > 0:
        x4 += speed * (d / abs(d))  
    if abs(dy) > 0:
        y4 -= speed * (dy / abs(dy))
    if x4-32<x<x4+32 and y4-32<y<y4+32 :
        hp = hp-1
        if hp <= 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            
            map1()
            
            equipment_logo(992,0)
            hp = maxhp
            gm = 0
            gm_label.config(text=f"Ghosts Captured: {gm}")
    return x4, y4
def enemyboss2():
    global ghost5, bosseye2_alive, x5, y5, hp, maxhp,gameover
    if not bosseye2_alive:
        return x5,y5
    speed = 5
    dx, dy = x5 - x, y5 - y
    
    canvas.delete("boss2")  
    new_img = makeTransparent(bosseye1, "#ffffff")
    ghost5 = canvas.create_image(x5, y5, image=new_img, tag="boss2")
    bosseye_images.append(new_img)
    
    
    if abs(dx) > 0:
        x5 -= speed * dx/abs(dx)
    if abs(dy) > 0:
        y5 -= speed * dy/abs(dy)
    if x5-32<x<x5+32 and y5-32<y<y5+32 :
        hp = hp-1
        if hp <= 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            canvas.create_image(0,0,image=gameover,tag="game",anchor="nw")
            map1()
            equipment_logo(992,0)
            hp = maxhp
            gm = 0
            gm_label.config(text=f"Ghosts Captured: {gm}")
    return x5, y5
def enemyboss3():
    global ghost6, bosseye3_alive, x6, y6, hp, maxhp,gameover
    if not bosseye3_alive:
        return x6,y6
    speed = 5
    dx, dy = x6 - x, y6 - y
    
    canvas.delete("boss3")  
    new_img = makeTransparent(bosseye1, "#ffffff")
    ghost6 = canvas.create_image(x6, y6, image=new_img, tag="boss3")
    bosseye_images.append(new_img)
    
    if abs(dx) > 0:
        x6 -= speed * dx/abs(dx)
    if abs(dy) > 0:
        y6 -= speed * dy/abs(dy)
    if x6-32<x<x6+32 and y6-32<y<y6+32 :
        hp = hp-1
        if hp <= 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            canvas.create_image(0,0,image=gameover,tag="game",anchor="nw")
            map1()
            equipment_logo(992,0)
            hp = maxhp
            gm = 0
            gm_label.config(text=f"Ghosts Captured: {gm}")
    return x6, y6

def bosswater():
    global newwatrbossImage, xwtr, ywtr, x, y, watrbosshp
    global barfull, barhalf, barlow, ghostbossw, wtrcounter, wtrsplash, splcon,waterboss_alive
    global hp, dropcon, dropcon2, droploc, watrboss_alive

    
    if not waterboss_alive:
        return

    wtrcounter += 1

    
    canvas.delete("ghostbossw")
    ghostbossw = canvas.create_image(xwtr, ywtr, image=newwatrbossImage,tag="ghostbossw")
    xwtr = x

    
    if watrbosshp == 3:
        Healthbarfull(512, 0)
    elif watrbosshp == 2:
        canvas.delete("barfull")
        Healthbarhalf(512, 0)
    elif watrbosshp == 1:
        canvas.delete("barhalf")
        Healthbarlow(512, 0)
    elif watrbosshp <= 0:
        canvas.delete("barlow")
        try:
            canvas.delete("barfull")
            canvas.delete("barhalf")
            canvas.delete("barlow")
        except:
            pass
        canvas.delete("ghostbossw")
        watrboss_alive = False   
        return
    if wtrcounter == 30 and splcon == 0:
        Watersplash(xwtr, ywtr + 100)
        wtrcounter = 0
        splcon = 1
        if xwtr - 32 < x < xwtr + 32 and ywtr + 100 < y < ywtr + 610:
            hp -= 5
        if hp <= 0:
            tree_positions.clear()
            stone_positions.clear()
            wall_positions.clear()
            wallb_positions.clear()
            keyhole_positions.clear()
            boss1_positions.clear()
            brickwall_positions.clear()
            roofb_positions.clear()
            roofb2_positions.clear()
            canvas.delete("all")
            canvas.create_image(0, 0, image=gameover, tag="game", anchor="nw")
            map1()
            wtrcounter = 0
            watrbosshp = 3
            equipment_logo(992, 0)
            hp = maxhp
            gm = 0
            gm_label.config(text=f"Ghosts Captured: {gm}")
            canvas.delete("ghostbossw")
            canvas.delete("barlow")
            canvas.delete(wtrsplash)
    if wtrcounter == 10 and splcon == 1:
        canvas.delete(wtrsplash)
        splcon = 0

    if dropcon == 0:
        droploc = random.randint(1, 3)
        dropcon = 1
    if dropcon == 1 and dropcon2 == 0:
        if droploc == 3:
            Drop(240, 456)
        elif droploc == 2:
            Drop(500, 346)
        elif droploc == 1:
            Drop(800, 446)
        dropcon2 = 1
    if mapv == 38:
        canvas.after(50, bosswater)
        
    
        
    
        
    
    
    
    
def gh_cap(event):
    global ghost2, x2, y2, ghost3, x3, y3, y, x, gm, ghost_alive, ghost2_alive, xp, yp, pickable, tool, eqtool ,pickused, mapv, bboss1, xbo, ybo
    global x4,y4,bosseye_alive, ghost4, bosseyecap, eyestage, x5,y5,bosseyecap1, ghost5, bosseye2_alive, bosseye3_alive, x6 ,y6,  ghost6, bosseyecap2
    global hppicknum6,pickkey4,tankq,hppicknum5,pickguide,pickupgrade,xxgd,yydg,xxup,yyup,hppicknum4,bushlcntr,dis_gh_cntr,hppicknum3,pickkey3,wtrsplash,dropcon2,dropcon,watrbosshp,drp,xdp,ydp,pickkey,pickkey2, xxg,yyg, yyellowgem, gems, xxhp,yyhp, Hpcontobt, maxhp, hppicknum,pickable3,pickable4, xxmp, yymp, mappicknum, Mpcontobt, hppicknum1, hppicknum2, pickable1, pickable2
    if ghost_alive and x2 - 100 < x < x2 + 100 and y2 - 100 < y < y2 + 100:
        if mapv == 53:
            dis_gh_cntr=dis_gh_cntr+1
        pickup_sound.play()
        canvas.delete(ghost2)
        ghost_alive = False
        gm += 1
        if pickupgrade==1:
            gm+=2
        gm_label.config(text=f"Ghosts Captured: {gm}")
    if bosseye_alive and x4 - 100 < x < x4 + 100 and y4 - 100 < y < y4 + 100:
        pickup_sound.play()
        canvas.delete(ghost4)
        bosseye_alive = False
        gm += 1
        if pickupgrade==1:
            gm+=2
        gm_label.config(text=f"Ghosts Captured: {gm}")
        eyestage=eyestage+1
        bosseyecap = 0
    if bosseye2_alive and x5 - 100 < x < x5 + 100 and y5 - 100 < y < y5 + 100:
        pickup_sound.play()
        canvas.delete(ghost5)
        bosseye2_alive = False
        gm += 1
        gm_label.config(text=f"Ghosts Captured: {gm}")
        eyestage=eyestage+1
        bosseyecap1 = 1
    if bosseye3_alive and x6 - 100 < x < x6 + 100 and y6 - 100 < y < y6 + 100:
        pickup_sound.play()
        canvas.delete(ghost6)
        bosseye3_alive = False
        gm += 1
        gm_label.config(text=f"Ghosts Captured: {gm}")
        eyestage=eyestage+1
        bosseyecap2 = 0
    if ghost2_alive and x3 - 100 < x < x3 + 100 and y3 - 100 < y < y3 + 100:
        if mapv == 53:
            dis_gh_cntr=dis_gh_cntr+1
        pickup_sound.play()
        canvas.delete(ghost3)
        ghost2_alive = False
        gm += 1
        gm_label.config(text=f"Ghosts Captured: {gm}")
    if pickused == 0 and eqtool == "pickaxe" and tool == 0 and  xp - 100 < x < xp + 100 and yp - 100 < y < yp + 100 :
        tool = 1
        canvas.delete(pick)
        pickaxe_sound.play()
        pickused = 1
        equipment_logo(992, 0)
        show_pickaxe_in_inventory()
    if mapv == 7 and pickable == 0 and eqtool == "key" and tool == 0 and xp - 100 < x < xp + 100 and yp - 100 < y < yp + 100 :
        tool = 2
        canvas.delete(key2)
        pickaxe_sound.play()
        pickable = 1
        equipment_logo(992, 0)
        show_key_in_inventory()
    if mapv==29 and pickable1 == 0 and eqtool == "key" and tool == 0 and xp - 100 < x < xp + 100 and yp - 100 < y < yp + 100 :
        tool = 2
        canvas.delete(key2)
        pickaxe_sound.play()
        pickable1 = 1
        equipment_logo(992, 0)
        show_key_in_inventory()
    if mapv==55 and bushlcntr == 0 and eqtool == "wheat" and tool == 0 and 120 < x < 320 and 540 < y < 740 :
        tool = 5
        pickaxe_sound.play()
        bushlcntr = 1
        equipment_logo(992, 0)
        show_wheat_in_inventory()
    if mapv==38 and xdp - 100 < x < xdp + 100 and ydp - 100 < y < ydp + 100 :
        pickup_sound.play()
        xdp=0
        ydp=0
        dropcon=0
        dropcon2=0
        watrbosshp=watrbosshp-1
        canvas.delete(drp)
        gm += 1
        gm_label.config(text=f"Ghosts Captured: {gm}")
        if watrbosshp==0:
            canvas.delete("ghostbossw")
            canvas.delete("barlow")
            canvas.delete(wtrsplash)
            Yellowgem(512,600)
    if mapv==30 and pickable2 == 0 and eqtool == "key" and tool == 0 and xp - 100 < x < xp + 100 and yp - 100 < y < yp + 100 :
        tool = 2
        canvas.delete(key2)
        pickaxe_sound.play()
        pickable2 = 1
        equipment_logo(992, 0)
        show_key_in_inventory()
    if mapv==32 and pickable3 == 0 and eqtool == "key" and tool == 0 and xp - 100 < x < xp + 100 and yp - 100 < y < yp + 100 :
        tool = 2
        canvas.delete(key2)
        pickaxe_sound.play()
        pickable3 = 1
        equipment_logo(992, 0)
        show_key_in_inventory()
    if mapv==33 and pickable4 == 0 and eqtool == "key" and tool == 0 and xp - 100 < x < xp + 100 and yp - 100 < y < yp + 100 :
        tool = 2
        canvas.delete(key2)
        pickaxe_sound.play()
        pickable4 = 1
        equipment_logo(992, 0)
        show_key_in_inventory()
    if mapv==8 and pickkey == 0 and eqtool == "gem" and xxg - 100 < x < xxg + 100 and yyg - 100 < y < yyg + 100 :
        canvas.delete(yyellowgem)
        pickaxe_sound.play()
        pickkey = 1
        gems=gems+1
    if mapv==38 and pickkey3 == 0 and eqtool == "gem" and xxg - 100 < x < xxg + 100 and yyg - 100 < y < yyg + 100 :
        canvas.delete(yyellowgem)
        pickaxe_sound.play()
        pickkey3 = 1
        gems=gems+1
        tree_positions.clear()
        stone_positions.clear()
        wall_positions.clear()
        wallb_positions.clear()
        keyhole_positions.clear()
        boss1_positions.clear()
        brickwall_positions.clear()
        roofb_positions.clear()
        roofb2_positions.clear()
        Door4k_positions.clear()
        canvas.after_cancel(bosswater)
        canvas.delete("all")
        map16()
        equipment_logo(992,0)
        x=250
        y=555
    if mapv==65 and pickkey4 == 0 and eqtool == "gem" and xxg - 100 < x < xxg + 100 and yyg - 100 < y < yyg + 100 :
        canvas.delete(yyellowgem)
        pickaxe_sound.play()
        pickkey4 = 1
        gems=gems+1
    if mapv==34 and pickkey2 == 0 and eqtool == "gem" and xxg - 100 < x < xxg + 100 and yyg - 100 < y < yyg + 100 :
        canvas.delete(yyellowgem)
        pickaxe_sound.play()
        pickkey2 = 1
        gems=gems+1
    if mapv == 8 and eyestage==3 and xxbo - 100 < x < xxbo + 100 and yybo - 100 < y < yybo + 100 :
        canvas.delete(bboss1)
        pickup_sound.play()
        gm += 1
        gm_label.config(text=f"Ghosts Captured: {gm}")
        boss1_positions.clear()
        eyestage = 4
    if mapv == 10 and hppicknum==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 and gm >= 20:
        canvas.delete(Hpcontobt)
        read_sound.play()
        gm=gm-20
        maxhp = maxhp+50
        gm_label.config(text=f"Ghosts Captured: {gm}")
        hppicknum=1
    if mapv == 58 and pickguide==0 and xxgd - 100 < x < xxgd + 100 and yygd - 100 < y < yygd + 100 and gm >= 15:
        canvas.delete(GGuide)
        read_sound.play()
        gm=gm-15
        gm_label.config(text=f"Ghosts Captured: {gm}")
        pickguide=1
        canvas.bind_all("m",Map)
    if mapv == 58 and pickupgrade==0 and xxup - 100 < x < xxup + 100 and yyup - 100 < y < yyup + 100 and gm >= 20:
        canvas.delete(UUpgrade)
        read_sound.play()
        gm=gm-20
        gm_label.config(text=f"Ghosts Captured: {gm}")
        pickupgrade=1
    if mapv == 21 and hppicknum1==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 :
        canvas.delete(Hpcontobt)
        read_sound.play()
        maxhp = maxhp+50
        hppicknum1=1
    if mapv == 25 and hppicknum2==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 :
        canvas.delete(Hpcontobt)
        read_sound.play()
        maxhp = maxhp+50
        hppicknum2=1
    if mapv == 41 and hppicknum3==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 :
        canvas.delete(Hpcontobt)
        read_sound.play()
        maxhp = maxhp+50
        hppicknum3=1
    if mapv == 57 and hppicknum4==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 :
        canvas.delete(Hpcontobt)
        read_sound.play()
        maxhp = maxhp+50
        hppicknum4=1
    if mapv == 58 and hppicknum5==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 and gm >= 10:
        canvas.delete(Hpcontobt)
        read_sound.play()
        maxhp = maxhp+50
        gm=gm-10
        gm_label.config(text=f"Ghosts Captured: {gm}")
        hppicknum5=1
    if mapv == 68 and hppicknum6==0 and xxhp - 100 < x < xxhp + 100 and yyhp - 100 < y < yyhp + 100 :
        canvas.delete(Hpcontobt)
        read_sound.play()
        maxhp = maxhp+50
        hppicknum6=1
    if mapv == 10 and mappicknum==0 and xxmp - 100 < x < xxmp + 100 and yymp - 100 < y < yymp + 100 and gm >= 10:
        canvas.delete(Mpcontobt)
        read_sound.play()
        gm=gm-10
        gm_label.config(text=f"Ghosts Captured: {gm}")
        mappicknum=1
        canvas.bind_all("m",Map)
def on_close():
    global after_id
    if after_id:
        canvas.after_cancel(after_id)
    root.destroy()

root.wm_title("Jewels of the Ghost Islands")
root.iconbitmap(resource_path(r"gem.ico"))
def check_loading_status():
    global loading1, Title
    VK_SPACE = 0x20
    if t.is_alive():

        root.after(100, check_loading_status)
    else:

        if loading1 is not None:
            canvas.delete(loading1)
        canvas.create_image(0,0,image=Title,anchor="nw",tag="title")
        
        if win32api.GetAsyncKeyState(win32con.VK_SPACE) < 0:
            canvas.delete("title")
            equipment_logo(992,0)
            canvas.delete(loading1)
            map1()
            equipment_logo(992,0)
            canvas.after(100, map_loop)
            canvas.after(100,time_loop)
            canvas.bind_all("d",mozog_jobb)
            canvas.bind_all("a",mozog_bal)
            canvas.bind_all("w",mozog_elo)
            canvas.bind_all("s",mozog_hat)
            canvas.bind_all("c",gh_cap)
            canvas.bind_all("r",inf)
            canvas.bind_all("<Escape>",esc)
            canvas.bind_all("q",use)
        else:
            root.after(100, check_loading_status)
 
def load():
    load_text()
    load_maps()
t=threading.Thread(target=load)
t.start()

root.after(100, check_loading_status)    
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()



