from sense_emu import SenseHat, ACTION_RELEASED, ACTION_PRESSED, ACTION_HELD

sense = SenseHat()

pressed = ACTION_PRESSED
released = ACTION_RELEASED

count = 0

selection = False

while True:
    events = sense.stick.get_events()
    if events:
        for e in events:
            if e.action != released:
                try:
                    if e.direction == 'up':
                        count += 1
                        sense.show_letter(str(count))
                    elif e.direction == 'down':
                        count -= 1
                        sense.show_letter(str(count))
                except:
                    print("Entries only allowed up to 9")



