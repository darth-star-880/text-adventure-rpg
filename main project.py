import random
import time
import webbrowser
import subprocess
import math
#########################################################
def random_amount_of_money ():
    gold1=random.randint(50,200)
    #gold2=random.randint(100,500)
    #return gold2,gold1
    return gold1


def random_shop_prices(base):
    price1=random.uniform(1.15,2)
    price2=random.random()
    #adding texs
    taxs=(10/100)+1
    
    newprice=(base*(1+price2)*price1)
    after_taxtes=newprice*taxs

    return round(after_taxtes,2) 

def lottery_ticket():
    random_items=random.randint(5,20)
    raws1=(f'***** {random_items} *****') 
    #raws2=(f'***** {random_items} *****')
    #raws3=(f'***** {random_items} *****')
    #tootalraws=[raws1,raws2,raws3]
    tootalraws=[raws1]
    return tootalraws
#def random_thife():
def thife_chanse():
    thife_chanse_123=random.random()
    return thife_chanse_123

def stat_randomzier(xsdqs):
    stat_items_item_random=random.random()
    if stat_items_item_random < 0.1:
        print('you got lengdary item')
        finalstat=max(1.0, xsdqs - (random.uniform(12.5, 41.0)))
        return finalstat

    elif stat_items_item_random >0.1 and stat_items_item_random <0.3:
        print('you got uncomon item item')
        finalstat=max(1.0, xsdqs - (random.uniform(12.5, 41.0)))
        return finalstat

    elif stat_items_item_random >0.3 and stat_items_item_random<0.7:
        print('you got normal item item')
        finalstat=max(1.0, xsdqs - (random.uniform(12.5, 41.0)))
        return finalstat
    else:
        print('you got scamed body,your itmes is so bad that it just usless')
        finalstat = math.floor(math.sqrt(xsdqs) * random.uniform(1.5, 2.5)) + 1

        return finalstat
def dam_contorl(armor,damge):
    pass
    dam_rad=min(0.7,armor/1000)
    final_damg=damge*(1-dam_rad)
    return final_damg

###########
#gonna make like a loan instersting wher just add monney based on you time
#your invontory has magic where it give money for ever 
#it has limits what is it idk
###########

####
#def for items you get and stat and def for items you got and chanse you got a low tier one really bad or noraml or legndary
################################
user=input('what is your name:')



########################################################
#########################################################
hero={
    "name":user ,
    "health":100 ,
    "stamina":100 ,
    "mana":100 ,
    #######
    "dexterty":1 ,
    "stratgh": 1,
    "magic":1 ,
    "deffence":0,
    #######
    "gold":random_amount_of_money () ,
    #"gold":random_amount_of_money (gold1)

}




if user == "1500":
    hero['gold']+=1000000
if user=='-30':
    hero['gold']=-30
print(hero)

invontory=[]
###############################################################
##items
##############################################################
raw_materail=["iron","stell","ice crystal","pages"]
liquer=["water","beer","lava",'poisen']
items=["sword","bow","axe","picaxe","magic sword","power fist","goodluck"]
books=["harrypotter","seven sin","magic sleeper","dragon eater","goonig cave"]
store1=[raw_materail,liquer,items,books,]

prices={
##################
    "raw_materail":{

    "iron":random_shop_prices(10),
    "stell":random_shop_prices(30),
    "ice crystal":random_shop_prices(10),
    "pages":random_shop_prices(5)


    } ,
###############
    "liquer":{

    "water":random_shop_prices(2.5),
    "beer":random_shop_prices(3),
    "lava":random_shop_prices(10),
    "poisen":random_shop_prices(15)


    } ,
####################
    "items":{

    "sword":random_shop_prices(50),
    "bow":random_shop_prices(30),
    "axe":random_shop_prices(20),
    "picaxe":random_shop_prices(20),

    "magic sword":random_shop_prices(350),
    "power fist":random_shop_prices(500),
    "goodluck":random_shop_prices(1000),
   

    } ,
######################
    "books":{

    "harrypotter":random_shop_prices(30),
    "seven sin":random_shop_prices(20),
    "magic sleeper":random_shop_prices(19),
    "dragon eater":random_shop_prices(13),

    "goonig cave":random_shop_prices(10),
   }
}

qunitity={
    
##################
    "raw_materail":{

    "iron":15,
    "stell":10,
    "ice crystal":3,
    "pages":200


    } ,
###############
    "liquer":{

    "water":15.3,
    "beer":16.5,
    "lava":1.5,
    "poisen":16.3


    } ,
####################
    "items":{

    "sword":30,
    "bow":50,
    "axe":15,
    "picaxe":30,

    "magic sword":12,
    "power fist":3,
    "goodluck":5,
   

    } ,
######################
    "books":{

    "harrypotter":200,
    "seven sin":300,
    "magic sleeper":50,
    "dragon eater":12,

    "goonig cave":2,
   }

}
#####
#thife
####
if thife_chanse()<0.3:
    print('skytchy area bewaere')
    stelling_money=random.random()
    if stelling_money <= 0.3:
        print("you got mogged")
        print("🥷 ( ﾟ👅ﾟ) 👉 💰 (‾.‾ ) 🧑")
        steling=hero["gold"]-random_amount_of_money ()

        hero["gold"]-=steling
        print(f' the thife have stole all of your money lol: {steling} and he leaft you with a wallelt emmpyy §{hero["gold"]}')

    else:
        print('you catsh a thife trying to steall you ')
###########
#zone that change prices
#####
 
######################################################
##shop
######################################################
print('you are going inside the store and you see the minue')
print("")

print('___________thigs for sell___________________')
print("")
print ('items          //////            prices           ///    qunitity ')
print("we have from raw materail:  ")

print(f"we have {'iron'} //// and its price is {prices["raw_materail"]["iron"]}///our stock of this {"iron"} have reached {qunitity["raw_materail"]["iron"]}")
print(f"we have {'stell'} //// and its price is {prices["raw_materail"]["stell"]}///our stock of this {"stell"} have reached {qunitity["raw_materail"]["stell"]}")
print(f"we have {'ice crystal'} //// and its price is {prices["raw_materail"]["ice crystal"]}///our stock of this {"ice crystal"} have reached {qunitity["raw_materail"]["ice crystal"]}")
print(f"we have {'pages'} //// and its price is {prices["raw_materail"]["pages"]}///our stock of this {"pages"} have reached {qunitity["raw_materail"]["pages"]}")

print("we have from items:  ")

print(f"we have {'bow'} //// and its price is {prices["items"]["bow"]}///our stock of this {"bow"} have reached {qunitity["items"]["bow"]}")
print(f"we have {'sword'} //// and its price is {prices['items']['sword']}///our stock of this {"sword"} have reached {qunitity["items"]["sword"]}")
print(f"we have {'axe'} //// and its price is {prices["items"]["axe"]}///our stock of this {"axe"} have reached {qunitity["items"]["axe"]}")
print(f"we have {'picaxe'} //// and its price is {prices["items"]["picaxe"]}///our stock of this {"picaxe"} have reached {qunitity["items"]["picaxe"]}")
print(f"we have {'magic sword'} //// and its price is {prices["items"]["magic sword"]}///our stock of this {"magic sword"} have reached {qunitity["items"]["magic sword"]}")
print(f"we have {'power fist'} //// and its price is {prices["items"]["power fist"]}///our stock of this {"power fist"} have reached {qunitity["items"]["power fist"]}")
print(f"we have {'goodluck'} //// and its price is {prices["items"]["goodluck"]}///our stock of this {"goodluck"} have reached {qunitity["items"]["goodluck"]}")

print("we have from books:  ")
print(f"we have {'harrypotter'} //// and its price is {prices["books"]["harrypotter"]}///our stock of this {"harrypotter"} have reached {qunitity["books"]["harrypotter"]}")
print(f"we have {'seven sin'} //// and its price is {prices["books"]["seven sin"]}///our stock of this {"seven sin"} have reached {qunitity["books"]["seven sin"]}")
print(f"we have {'magic sleeper'} //// and its price is {prices["books"]["magic sleeper"]}///our stock of this {"magic sleeper"} have reached {qunitity["books"]["magic sleeper"]}")
print(f"we have {'dragon eater'} //// and its price is {prices["books"]["dragon eater"]}///our stock of this {"dragon eater"} have reached {qunitity["books"]["dragon eater"]}")
print(f"we have {'goonig cave'} //// and its price is {prices["books"]["goonig cave"]}///our stock of this {"goonig cave"} have reached {qunitity["books"]["goonig cave"]}")

print("we have liquer:  ")

print(f"we have {"water"} //// and its price is {prices["liquer"]["water"]}///our stock of this {"water"} have reached {qunitity["liquer"]["water"]}")
print(f"we have {"beer"} //// and its price is {prices["liquer"]["beer"]}///our stock of this {"beer"} have reached {qunitity["liquer"]["beer"]}")
print(f"we have {"lava"} //// and its price is {prices["liquer"]["lava"]}///our stock of this {"lava"} have reached {qunitity["liquer"]["lava"]}")
print(f"we have {'poisen'} //// and its price is {prices["liquer"]['poisen']}///our stock of this {"poisen"} have reached {qunitity["liquer"]["poisen"]}")

storegold=24000
print("welcom to our shop coustmer we going to meet you in min")
time.sleep(3)

while True:

    user_choose=input("(type q to exit) are going to buy or sell").lower().strip()
    
    if user_choose =='q':
        break        
    ###############################################################
    ##buying
    #gold_buyer=random_amount_of_money (gold2)
    ################################################
    if not hero["gold"]>0 :
        print( f'you dont have any more money so you skip the store')
        break
    elif not storegold>0:
        print(f'the store dont have any money' ) 
        break  

    elif  hero["gold"]>0 or storegold>0:
            
    

        if user_choose== "buy":
            user_chooseb=input ("what are you going to buy:").lower().strip()
            user_chooseb=user_chooseb.replace(" ","")
            
            if user_chooseb == "iron" or user_chooseb == "stell" or user_chooseb =="icecrystal" or user_chooseb == "pages":
                user_dectite_whatlist="raw_materail"
    
            elif user_chooseb =="bow"or user_chooseb == "sword" or user_chooseb =="axe" or user_chooseb =="picaxe" or user_chooseb == "magicsword":
                user_dectite_whatlist="items"
            elif user_chooseb =="harrypotter" or user_chooseb == "sevensin" or user_chooseb =="magicsleeper" or user_chooseb =="dragoneater" or user_chooseb == "goonigcave ":
                user_dectite_whatlist="books"
            elif user_chooseb == "water" or user_chooseb == "beer" or user_chooseb =="slava" or user_chooseb == "poisen":
                user_dectite_whatlist="liquer"
            if qunitity[user_dectite_whatlist][user_chooseb] <0:
                print(f'sorry,we dont have any more stock fro {user_chooseb} ')
                continue
            else:
                print("we dont have this items")



            user_quintit_buy=int(input("how manny u want to buy "))

            print(f'you got {user_chooseb}x{user_quintit_buy} from the list of {user_dectite_whatlist}')

            user_total_ammount=prices[user_dectite_whatlist][user_chooseb]*user_quintit_buy
            new_quntite=qunitity[user_dectite_whatlist][user_chooseb]-user_quintit_buy
            qunitity[user_dectite_whatlist][user_chooseb]=new_quntite
        
            storegold+=user_total_ammount
            the_tottalamoubt_money=hero["gold"]-user_total_ammount
            hero["gold"]=the_tottalamoubt_money
            print(f'the new stock fo the store for this items {user_chooseb} is {new_quntite}')
            print(f'{qunitity[user_dectite_whatlist][user_chooseb]}')
            print(f'{hero["gold"]}')
            print (f'hero gold is: {the_tottalamoubt_money} / you buy this item {user_chooseb} for {user_quintit_buy} == {user_total_ammount}/')
            print(f'{storegold} and hero gold is {hero["gold"]}')
            invontory.append(user_chooseb)
            print(f'(delte thse only for testing)how manny of this itmes have left')
            print(f'{qunitity[user_dectite_whatlist][user_chooseb]}')
    ###
    ###
    #selling
    
        elif user_choose== "sell":
            user_chooses=input ("what are you going to sell :  ").lower().strip()
            user_chooses=user_chooses.replace(" ","")
            if user_chooses == "iron" or user_chooses == "stell" or user_chooses ==" icecrystal" or user_chooses == "pages":
                user_dectite_whatlist="raw_materail"

            elif user_chooses =="bow"or user_chooses == "sword" or user_chooses =="axe" or user_chooses =="picaxe" or user_chooses == "magicsword":
                user_dectite_whatlist="items"
            elif user_chooses =="harrypotter" or user_chooses == "sevensin" or user_chooses =="magicsleeper" or user_chooses =="dragoneater" or user_chooses == "goonigcave ":
                user_dectite_whatlist="books"
            elif user_chooses == "water" or user_chooses == "beer" or user_chooses =="slava" or user_chooses == "poisen":
                user_dectite_whatlist="liquer"
            if qunitity[user_dectite_whatlist][user_chooses] >120: 
                print('sorry,we cant accespt any more from this itmes')
                continue

            user_quintit_sell=int(input("how manny u want to sell "))

            print(f'you got {user_chooses}x{user_quintit_sell} from the list of {user_dectite_whatlist}')

            user_total_ammount=prices[user_dectite_whatlist][user_chooses]*user_quintit_sell
            new_quntite=qunitity[user_dectite_whatlist][user_chooses]+user_quintit_sell
            qunitity[user_dectite_whatlist][user_chooses]=new_quntite
            print(new_quntite)
            storegold-=user_total_ammount
            the_tottalamoubt_money=hero["gold"]+user_total_ammount
            hero["gold"]+=user_total_ammount
            print(f'{storegold} and hero gold is {hero["gold"]}')
            print(f'the new stock fo the store for this items {user_chooses} is {new_quntite}')
            print(f'{qunitity[user_dectite_whatlist][user_chooses]}')
            print(f'{hero["gold"]}')
            print (f'store money left {storegold}'f' and the hero money is {hero["gold"]}' f'you sell it for this ammount{user_total_ammount}')
            print(f'(delte thse only for testing)how manny of this itmes have left')
            print(f'{qunitity[user_dectite_whatlist][user_chooses]}')



        
#   if user_choose==user_chooseb
#   print(f"{user_chooseb}")
#
#   elif user_choose==user_chooses
#   print(f"{user_chooses}")


############################################################
###armor
############################################################
print("the store has a lottery ticket if you win you will get a random armor that will help you servive or if get a rare lottery you will chose any armor if you want with discount")
armors=["leather","star chaser","iron plate",'stell plate',"dark moon"]
price_armor={
    "leather":100,
    "star chaser":250,
    "iron plate":300,
    'stell plate':500,
    "dark moon":1000

}
random_armor=random.choice(armors)
user5=input("you want to enter the lottery: yes/ no")

if user5 == "yes" :
    print ('welcom to our lottery we wish you the best time: ')

    if hero['gold']>5:
        lottery_tick=hero["gold"]-5
        hero["gold"]-=5
        random_items=random.randint(5,20)
        raws1=(f'***** {random_items} *****') 
        #raws2=(f'***** {random_items} *****')
        #raws3=(f'***** {random_items} *****')
        print('you buyed our ticket let see if you win')
        for ticksss in lottery_ticket() :
            print('the lottery tickes ///// your lottery tickes')
            print(f'{ticksss} //////// {raws1}')
            #print(f'{ticksss} //////// {raws2}')
            #print(f'{ticksss} //////// {raws3}')
            print()
            #totaltickkk1=ticksss*3
            #tootalraws1=raws1+raws2+raws3
            tootalraws1=raws1.replace("*****","")
            tootalraws1=int(tootalraws1)
            totaltickkk1=ticksss.replace("*****","")
            totaltickkk1=int(totaltickkk1)
            #tootalraws1=random_items
            #totaltickkk1=random_items
            if not totaltickkk1 ==tootalraws1:
                
                print('sorry you dint win')
                print(f'{totaltickkk1}=/={tootalraws1}')
            else:
                print('you have won : lets give random pice with discount')
                
                discount=price_armor[random_armor]*(1-0.2)
                print(f'you got this armor {random_armor} you buy it for {discount} with discount %{100*0.2}')
                invontory.append(random_armor)

else:
    print ("best luck next time")

#invontory.append()

#################################################
                    ##random thing to do for fun######
#######################################################
if hero["gold"]>1000:
    webbrowser.open("https://www.youtube.com/watch?v=Bgqk6t9Be1Q", autoraise=True)
if hero ["gold"]<0:
    webbrowser.open("https://youtu.be/PHm_B_idud8?si=x7ivVVj3bCDimV2m", autoraise=True)
    print('boke ass hell,you cant buy shit in here')

    #subprocess.Popen(['C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe', 'https://www.youtube.com/watch?v=Bgqk6t9Be1Q'])
######################################################
######################################################


#random_armor+



######################################################
#skills add up
#v
#v
#v
############################################
###########################
#items
######################

if "bow" in invontory:
    hero["stamina"]+= stat_randomzier(100)
    hero["health"]+=stat_randomzier(50)
    hero["stratgh"]+=stat_randomzier(10)
    hero["dexterty"]+=stat_randomzier(200)
    
    
if "sword" in invontory:
    hero["stamina"]+=stat_randomzier(300)
    hero["health"]+=stat_randomzier(500)
    hero["dexterty"]-=stat_randomzier(1)
    
    
if "axe" in invontory:
    hero["stamina"]+=stat_randomzier(100)
    hero["health"]-=stat_randomzier(150)
    hero["mana"]+=stat_randomzier(0)
    hero["magic"]+=stat_randomzier(0)
    hero["dexterty"]+=stat_randomzier(3)
    
    
if "picaxe" in invontory:
    hero["stamina"]+=stat_randomzier(50)
    hero["health"]+=stat_randomzier(50)
    hero["stratgh"]+=stat_randomzier(32)
    
    
if "magicsword" in invontory:
    hero["stamina"]+=stat_randomzier(50)
    hero["health"]-=stat_randomzier(50)
    hero["mana"]+=stat_randomzier(400)
    hero["magic"]+=stat_randomzier(10)
    hero["dexterty"]+=stat_randomzier(7)
    
    
if "powerfist" in invontory:
    hero["stamina"]+=stat_randomzier(700)
    hero["health"]-=stat_randomzier(600)
    hero["mana"]+=stat_randomzier(560)
    hero["magic"]+=stat_randomzier(50)
    hero["dexterty"]+=stat_randomzier(35)
    
    
if "goodluck" in invontory:
    hero["stamina"]+=stat_randomzier(100)
    hero["health"]-=stat_randomzier(1000)
    hero["mana"]+=stat_randomzier(235)
    hero["magic"]+=stat_randomzier(456)
    hero["dexterty"]+=stat_randomzier(54)
    
#invontory.append()

#######################################################
#armor
############################################

if "leather" in invontory: 
    hero["stamina"]+=stat_randomzier(54)
    hero["health"]+=stat_randomzier(56)
    hero["stratgh"]+=stat_randomzier(54)
    hero["deffence"]+=50
elif "star chaser" in invontory:
    hero["stamina"]+=stat_randomzier(456)
    hero["health"]+=stat_randomzier(54)
    hero["stratgh"]+=stat_randomzier(546)
    hero["dexterty"]+=stat_randomzier(456)
    hero["deffence"]+=150
elif "iron plate" in invontory:
    hero["stamina"]+=stat_randomzier(456)
    hero["health"]-=stat_randomzier(456)
    hero["dexterty"]+=stat_randomzier(564)
    hero["deffence"]+=250
elif "stell plate" in invontory:
    hero["stamina"]=stat_randomzier(45)
    hero["health"]=stat_randomzier(54)
    hero["mana"]+=stat_randomzier(456)
    hero["magic"]+=stat_randomzier(10)
    hero["deffence"]+=400
    hero["stratgh"]+=stat_randomzier(654)
    hero["dexterty"]+=stat_randomzier(54)
elif "dark moon"in invontory:
    hero["stamina"]+=stat_randomzier(45)
    hero["health"]+=stat_randomzier(54)
    hero["mana"]+=stat_randomzier(45)
    hero["stratgh"]+=stat_randomzier(456)
    hero["dexterty"]+=stat_randomzier(465)
    hero["magic"]+=stat_randomzier(10)
    hero["deffence"]+=1000


############################################################
#books
#########################################################
booksquotes=random.random()
if "harrypotter" in invontory :

    if booksquotes < 0.3:
        print('It is our choices, Harry, that show what we truly are, far more than our abilities.')
    else:
        print("Do not pity the dead, Harry. Pity the living, and, above all, those who live without love.")

if "sevensin" in invontory :
    if booksquotes < 0.3:
        print('The most dangerous trap in Luxuria is not a blade or a poison it is a warm bed and the promise that you never have to be lonely again')
    else:
        print('Do not look into the mirrors they do not show your reflection they show the beautiful lies that will bury you alive,')

if "magicsleeper" in invontory :

    if booksquotes < 0.3:
        print('He felt the heavy fog of sleep pulling him down but his willpower kept him standing')
    else:
        print("If you close your eyes in the domain of Sloth you might never open them again")

if "dragoneater" in invontory :
    if booksquotes < 0.3:
        print('To slay the beast you must become the one thing that a dragon fears more than death')
    else:
        print("The Dragon Eater does not hunt for meat it devours the very fire inside your soul")

if "goonigcave" in invontory :
    if booksquotes < 0.3:
        print('You can only leave the cavern if your hands are completely empty of stolen treasure')
    else:
        print("The Goonig Cave turns your own gold into a heavy cage that will trap you forever")

for x123,y123 in hero.items():
    print (f'{x123} /// {y123}' )


########################################
#crafting
#thses where the plyer can craft or upgrad they stuff before the fights
######################################

#for x,f;z in invontory

names_genrate=("Crystal Fury Shadow Fist Iron Slumber Aqua Wrath Void Spell Doom Axe Prism Bow Hell Fire""Phantom Edge Chaos Bringer Mystic Grimoire Solar Flare Abyssal Watcher Titan Grip, Spirit Walker Nebula Shield""Vortex Brand, Catalyst Spine, Mirage Core, Static Shard, Zephyr Edge, Chrono Lash, Null Sector, Primal Maw, Dread Forge, Torrent Crest, Horizon Dagger, Apex Veil, Glint Shaman, Umbra Grip, Radiant Shield, Rust Wand, Hollow Spire, Wild Bow, Kinetic Grasp, Shard Walker, Aeon Tome, Astral Phase, Pyro Strand, Sonic Vault, Basalt Cloak, Chasm Step, Obsidian Axe, Vertex Ring, Karma Mace, Nexus Shield, Plasma Weaver, Fracture Loom, Helix Point, Vector Matrix, Singularity Shift, Nomad Lash, Glitch Boot, Quantum Glove, Entropy Gear, Zero Wave, Dynamo Crown, Pulsar Helm, Overdrive Crest, Inertia Spike, Friction Reaper, Velocity Sight, Torque Point, Zenith Ward, Celestial Spine, Nether Grasp, Spirit Shard, Prismatic Edge, Mythic Lash, Cosmic Sector, Shadow Maw, Inferno Forge, Glacier Crest, Gale Dagger, Terra Veil, Death Shaman, Life Grip, Astral Shield, Doom Wand, Light Spire, Plague Bow, Frost Grasp, Magma Walker, Thunder Tome, Soul Phase, Rune Strand, Star Vault, Bone Cloak, Night Step, Sky Axe, Ash Ring, Dream Mace, Nova Shield")
names_genrate22=('Echo Vault, Cinder Spine, Mirage Edge, Twilight Grasp, Frost Veil, Venom Shaman, Pyre Walker, Static Fang, Oblivion Core, Warp Strand, Horizon Bow, Golem Shell, Quake Fist, Zenith Blade, Flux Tome, Rift Stalker, Tectonic Plate, Eclipse Ward, Aether Spire, Phase Shifter, Nebula Grip, Primal Crest, Dread Maw, Solar Flare, Abyssal Sight, Catalyst Wand, Whisper Page, Torrent Step, Magnetar Axe, Apex Predator, Glint Dagger, Umbra Cloak, Radiant Spike, Rust Reaper, Hollow Heart, Wild Spark, Kinetic Mace, Shard Weaver, Aeon Trigger, Astral Loom, Pyro Clastic, Sonic Boom, Basalt Guard, Chasm Dweller, Obsidian Veil, Vertex Shield, Karma Bond, Nexus Point, Plasma Conduit, Fracture Line, Helix Staff, Vector Point, Singularity Ring, Nomad Hood, Glitch Matrix, Quantum Shift, Entropy Lash, Zero Point, Dynamo Core, Pulsar Wave, Overdrive Gear, Inertia Boot, Friction Glove, Velocity Boots, Vector Bow, Torque Wrench, Zenith Crown, Vertex Helm')
names_genrate=names_genrate.split()
names_genrate22=names_genrate22.split()
names_genrate=random.choices(names_genrate)
names_genrate2=random.choices(names_genrate22)


if"sword" in invontory and "axe" in invontory :
    print(names_genrate+names_genrate2)

    hero["stamina"]+=stat_randomzier(456)
    hero["health"]+=stat_randomzier(45)
    hero["mana"]+=stat_randomzier(654)
    hero["stratgh"]+=stat_randomzier(46)
    hero["dexterty"]+=stat_randomzier(5)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("sword")
    invontory.remove("axe")
    invontory.append(names_genrate) 
    invontory.append(names_genrate2)


if"picaxe" in invontory and "beer"in invontory:
    print(names_genrate+names_genrate2)
    hero["stamina"]+=stat_randomzier(45)
    hero["health"]+=stat_randomzier(46)
    hero["mana"]+=stat_randomzier(46)
    hero["stratgh"]+=stat_randomzier(46)
    hero["dexterty"]+=stat_randomzier(46)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("picaxe")
    invontory.remove("beer")
    invontory.append(names_genrate) 
    invontory.append(names_genrate2)

if"magicsword" in invontory and 'poisen'in invontory:

    print(names_genrate+names_genrate2)
    hero["stamina"]+=stat_randomzier(4)
    hero["health"]+=stat_randomzier(456)
    hero["mana"]+=stat_randomzier(46)
    hero["stratgh"]+=stat_randomzier(46)
    hero["dexterty"]+=stat_randomzier(46)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("magicsword")
    invontory.remove("poisen")
    invontory.append(names_genrate) 
    invontory.append(names_genrate2)

if"powerfist" in invontory and "water"in invontory:
    print(names_genrate+names_genrate2)
    hero["stamina"]+=stat_randomzier(456)
    hero["health"]+=stat_randomzier(54)
    hero["mana"]+=stat_randomzier(64)
    hero["stratgh"]+=stat_randomzier(6)
    hero["dexterty"]+=stat_randomzier(6)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("powerfist")
    invontory.remove("water")
    invontory.append(names_genrate) 
    invontory.append(names_genrate2)

if"lava"in invontory and "goodluck" in invontory:
    print(names_genrate+names_genrate2)

    hero["stamina"]+=stat_randomzier(65)
    hero["health"]+=stat_randomzier(48)
    hero["mana"]+=stat_randomzier(48)
    hero["stratgh"]+=stat_randomzier(84)
    hero["dexterty"]+=stat_randomzier(64)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("goodluck")
    invontory.remove("lava")
    invontory.append(names_genrate) 
    invontory.append(names_genrate2)

if"iron"in invontory and "goonig cave"in invontory:
    print(names_genrate+names_genrate2)
    hero["stamina"]+=stat_randomzier(456)
    hero["health"]+=stat_randomzier(56)
    hero["mana"]+=stat_randomzier(56)
    hero["stratgh"]+=stat_randomzier(546)
    hero["dexterty"]+=stat_randomzier(456)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("goonig cave")
    invontory.remove("iron")
    invontory.append(names_genrate)
    invontory.append(names_genrate2)

if"stell" in invontory and "harrypotter"in invontory:
    print(names_genrate+names_genrate2)
    hero["stamina"]+=stat_randomzier(78)
    hero["health"]+=stat_randomzier(78)
    hero["mana"]+=stat_randomzier(89)
    hero["stratgh"]+=stat_randomzier(4)
    hero["dexterty"]+=stat_randomzier(65)
    hero["magic"]+=stat_randomzier(10)

    invontory.remove("stell")
    invontory.remove("harrypotter")
    invontory.append(names_genrate)
    invontory.append(names_genrate2)

if"ice crystal"in invontory and "dragon eater"in invontory :
    print(names_genrate+names_genrate2)
    hero["stamina"]+=stat_randomzier(654)
    hero["health"]+=stat_randomzier(45)
    hero["mana"]+=stat_randomzier(56)
    hero["stratgh"]+=stat_randomzier(45)
    hero["dexterty"]+=stat_randomzier(456)
    hero["magic"]+=stat_randomzier(12)
    invontory.remove("dragon eater")
    invontory.remove("ice crystal")
    invontory.append(names_genrate)
    invontory.append(names_genrate2)

if"pages"in invontory and "seven sin"in invontory:
    print(names_genrate+names_genrate2)
    removethise="".replace('')
    hero["stamina"]+=stat_randomzier(45)
    hero["health"]+=stat_randomzier(65)
    hero["mana"]+=stat_randomzier(65)
    hero["stratgh"]+=stat_randomzier(5)
    hero["dexterty"]+=stat_randomzier(4)
    hero["magic"]+=stat_randomzier(10)
    invontory.remove("seven sin")
    invontory.remove("pages")
    invontory.append(names_genrate)
    invontory.append(names_genrate2)

print(f'your invontory is {invontory}')

##########################
###########################
##########################
print("after done with the shop you got in your invontory this")
print(invontory)






########################################################################################################################################################################
########################################################################################################################################################################
#^----the top repsent the store and the hero intraction
#its the middle bewtin what hero did to be pearpeded to fight or die 
#v-----this repsent the final project were the hero jorny to saly everything and powerfull and defeat and save the princess
########################################################################################################################################################################
########################################################################################################################################################################

damge=0
#wapons+damg
if "bow" in invontory:
    damge+=10

if "sword" in invontory:
    damge+=10

if "axe" in invontory:
    damge+=5

if "picaxe" in invontory:
    damge+=5

if "magicsword" in invontory:
    damge+=50

if "powerfist" in invontory:
    damge+=60

if "goodluck" in invontory:
    damge+=100

if names_genrate in invontory and names_genrate22 in invontory:
    random_tier=random.random()
    damge_randomzier=random.uniform(1.1,3)
    damge+=300
    damge*=damge_randomzier
    if random_tier<0.3:
        damge*=1.1
        print('you got really good item')
    else:
        pass
damge=(damge+(hero["stratgh"]*1.5))*(1+hero["dexterty"]/100)*random.uniform(0.8,1.1)
##########
##aera and inside it is 
###########4
cave={
   "goblin":{
    "name":"goblin",
    "health":50,
    "stamina":80,
    "mana":10,
    "deffence":100,

},
   "dragon":{
    "name":"dragon",
    "health":5000,
    "stamina":100,
    "mana":20,
    "deffence":500,
},
}

#for x124,y124 in cave.items() :
 #   print(dir(f'{x124}///{y124}'))

#random_enemy=random.choice(x124,y124)
#print(random_enemy)
#comabt skelton

##################
##########
lowteris=[cave['goblin']]
highteris=[cave['dragon']]
random_enemy=random.choice(list(cave.keys()))
print(random_enemy)
#exmple pley get damg         hero["health"]-=dam_contorl(armor(hero),damge(enemy))
#exmple goblin get damg       random_enemy[health]-=dam_contorl(armor(random_enemy),damge(plyer))
while True:
    if not hero['health']>0 or not cave[random_enemy]["health"]>0:
        break
    while hero['health']>0 and not cave[random_enemy]["health"]<0:
        qqqqq=input('type enter to attack or q to exit')
        if qqqqq =="q":
            break
        #random_enemy attack
        #health+damg

        damgerandom_enemy=random.uniform(20,50)
        hero["health"]-=max(0,dam_contorl(hero["deffence"],damgerandom_enemy))
        print(f'you got damged from {random_enemy} and you health have drope to {hero["health"]} so you damged by{dam_contorl(hero["deffence"],damgerandom_enemy):.1f}')
        #plyer attack
        #health+damg
        cave[random_enemy]["health"]-=max(0,dam_contorl(cave[random_enemy]["deffence"],damge))
        print(f'you mange to hit him/her {random_enemy} delling damge {dam_contorl(cave[random_enemy]["deffence"],damge):.1f}')