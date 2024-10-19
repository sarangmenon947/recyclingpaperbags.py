import pgzrun
import random

WIDTH = 800
HEIGHT = 600

centrex = WIDTH/2
centrey = HEIGHT/2
center = (centrex, centrey)

items = ["bag", "cardboard", "chipspacket", "plasticwaterbottle", "battery"]
emptylistitems = []
emptylistanimations = []
currentlevel = 1
finallevel = 6
gameover = False
gamecomplete = False
startspeed = 10

def draw():
    global gameover, gamecomplete, items
    screen.clear()
    screen.blit("background", (0,0))
    if gameover:
        screen.draw.text("Game Over", center = center, fontsize = 60, color = "red")
    elif gamecomplete:
        screen.draw.text("You Won The Game, Congratulations!", center = center, fontsize = 40, color = "red")
    else:
        for i in emptylistitems:
            i.draw()

def update():
    global emptylistitems
    if len(emptylistitems) == 0:
        emptylistitems = makeitems(currentlevel)

def createitems(itemstocreate):
    newitems = []
    for a in itemstocreate:
        object = Actor(a + "img")
        newitems.append(object)
    return newitems

def makeitems(extraitems):
    itemstocreate = getoptiontocreate(extraitems)
    newitems = createitems(itemstocreate)
    layoutitems(newitems)
    animateitems(newitems)
    return newitems

def getoptiontocreate(extraitems):
    itemstocreate = ["cardboard"]
    for i in range(0,extraitems):
        randomoption = random.choice(items)
        itemstocreate.append(randomoption)
    return itemstocreate

def layoutitems(itemstolayout):
    gaps = len(itemstolayout) + 1
    gapssize = WIDTH/gaps
    random.shuffle(itemstolayout)
    for index, item in enumerate(itemstolayout):
        newxpos = (index + 1) * gapssize
        item.x = newxpos

def animateitems(itemstoanimate):
    global emptylistanimations
    for i in itemstoanimate:
        duration = startspeed-currentlevel
        i.anchor = ("center", "bottom")
        animation = animate(i, duration = duration, on_finished = handle_gameover, y = HEIGHT)
        emptylistanimations.append(animation)

def handle_gameover():
    global gameover
    gameover = True

def on_mouse_down(pos):
    global emptylistitems, currentlevel
    for i in emptylistitems:
        if i.collidepoint(pos):
            if "cardboard" in i.image:
                handle_game_complete()
            else:
                handle_gameover()

def handle_game_complete():
    global currentlevel, emptylistitems, emptylistanimations, gamecomplete
    stopanimations(emptylistanimations)
    if currentlevel == finallevel:
        gamecomplete = True
    else:
        currentlevel += 1
        emptylistitems = []
        emptylistanimations = []

def stopanimations(animationstostop):
    for i in animationstostop:
        if i.running:
            i.stop()

pgzrun.go()



    
