from sense_emu import SenseHat, ACTION_RELEASED, ACTION_PRESSED, ACTION_HELD

sense = SenseHat()

pressed = ACTION_PRESSED
released = ACTION_RELEASED

selection = False

while True:
	events = sense.stick.get_events()
	if events:
		for e in events:
			if e.action == pressed:
				if selection == False:
					selection = True
					sense.show_letter("O")
                		else:
                    			selection = False
                    			sense.show_letter("S")



