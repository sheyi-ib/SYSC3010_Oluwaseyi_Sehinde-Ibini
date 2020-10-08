import sense_hat, random, time

"""
  lab2-hardwarestep1.py
  
  toggling initials
  
"""

sense = sense_hat.SenseHat()


Y = (255, 255, 0)
G = (0, 255, 0)
B = (0, 0, 255)
X = (0, 0, 0)

####
# Initials Images
####

char_O = [
    X, X, G, G, G, G, X, X,
    X, G, X, X, X, X, G, X,
    X, G, X, X, X, X, G, X,
    X, G, X, X, X, X, G, X,
    X, G, X, X, X, X, G, X,
    X, G, X, X, X, X, G, X,
    X, G, X, X, X, X, G, X,
    X, X, G, G, G, G, X, X
]
char_S = [
    X, X, G, G, G, G, G, X,
    X, G, G, G, G, G, G, X,
    X, G, G, X, X, X, X, X,
    X, G, G, G, G, X, X, X,
    X, X, G, G, G, G, G, X,
    X, X, X, X, X, G, G, X,
    X, G, G, G, G, G, G, X,
    X, G, G, G, G, G, X, X,
  ]

def initial_1():
    return char_O

def initial_2():
    return char_S

sense.clear()

####
# Main Loop
####
images = [initial_1, initial_2]
sense.set_pixels(images[0]())
count = 1

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            #this is a hold or keyup; move on
            continue
        
        #if event.direction == 'left' | :
        sense.set_pixels(images[count % len(images)]())
        count += 1