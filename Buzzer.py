import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import mraa
import pyupm_i2clcd as lcd
import sys
import random


counter = 0

# Create the button object using GPIO pin 0
button = mraa.Gpio(2)

# Create the buzzer object using GPIO pin 5
buzzer = upmBuzzer.Buzzer(3)
button.dir(mraa.DIR_IN)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];

#Crete the lcd object 
lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)
lcdDisplay.setColor(0,0,0)


lcdDisplay.write(counter + '')

# Read the input and print, waiting one second between readings
while 1:
	if(button.read() != 0):
		counter = counter + 1
		lcdDisplay.write(counter + '')
		r = random.randint(0, 255)
		g = random.randint(0, 255)
		b = random.randint(0, 255)
		lcdDisplay.setColor(r,g,b)
		for chord_ind in range (0,1):
    			# play each note for one second
			print("Boton presionado")
    			buzzer.playSound(chords[chord_ind], 1000000)
    		time.sleep(0.1)
	
	

# Delete the buzzer object
del buzzer

# Delete the button object
del button
