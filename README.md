# Electro-Mechanical Shutter Controller
This is a controller intended to control solonoid operated electromechanical shutters typically used fro large format photography.
It uses a Raspberry PI Pico as the main control and can operate off batteries as included with the current files. (18650x4 in my case)
The power supply can be adpted to tool batteries or AC adapters as is apropriate for your shutter.
One limitation is my design is that the control is designed to operate with a MOSFET controlling up to 24 volts DC and will not work as is for an AC operated shutter as can be found in some packard shutters.

## Wiring and construction:
  
  This will be covered in detail in a Youtube video found here;
  ![Youtube Link](https://youtu.be/-WX2WRZfZw8)
  
But assembly of the core system can also be accomplished by following the wiring diagram included in the code folder.

![Wiring diagram](https://github.com/Drachimus/Electro-Mech_Shutter/assets/136056199/be9e471f-25f2-4fde-a4b2-98fd325e6dce)

## Code:

  The code is written entirely in Python. To load the firmware to your Pico;
  - hold the boot button down on the pico while plugging it into your computer
  - when the Pico conects to your computer, it will show as a flash drive. Drag the circuit python UF2 downloaded from [Here](https://circuitpython.org/board/raspberry_pi_pico/) into that drive and it will reboot automatically
  - Once rebooted, hold the boot button again while unplugging and replugging the pico from the computer if it doesn't automatically come back up as a drive.
  - drag the file main.py and the folder modules onto the pico
  - reboot the pico by cycling power and you should be good to go.


