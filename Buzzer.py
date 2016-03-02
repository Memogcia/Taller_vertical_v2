import time
import pyupm_buzzer as upmBuzzer
import pyupm_grove as grove
import mraa

# Create the button object using GPIO pin 0
button = mraa.Gpio(2)

# Create the buzzer object using GPIO pin 5
buzzer = upmBuzzer.Buzzer(3)
button.dir(mraa.DIR_IN)

chords = [upmBuzzer.DO, upmBuzzer.RE, upmBuzzer.MI, upmBuzzer.FA, 
          upmBuzzer.SOL, upmBuzzer.LA, upmBuzzer.SI, upmBuzzer.DO, 
          upmBuzzer.SI];



# Read the input and print, waiting one second between readings
while 1:
	if(button.read() != 0):
		for chord_ind in range (0,2):
    			# play each note for one second
			print("Boton presionado")
    			buzzer.playSound(chords[chord_ind], 1000000)
    		time.sleep(0.1)
	

# Delete the buzzer object
del buzzer

# Delete the button object
del button
