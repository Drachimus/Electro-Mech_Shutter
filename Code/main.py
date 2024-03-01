# Shutter control for electro-mech shutter
# Authored by Drachimus



from rotary_irq_rp2 import RotaryIRQ
import time
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 32, i2c)
SW=Pin(15,Pin.IN,Pin.PULL_UP)  # shutter fire button pulling to grnd when fired
ind_led = Pin(25, Pin.OUT)     # diagnostic indicator onboard led used pi pico
shut_relay = Pin(16, Pin.OUT)  # output pin conected to control relay for shutter
shut_relay.value(0)


#function to actuate the shutter mechanism

def shut_fire(shut_delay):
    
    if shut_delay == 1:
        if shut_relay.value()==1:
            shut_relay.value(0)
            ind_led.value(0)
            oled.init_display()
            oled.rotate(2)
            oled.text("Shutter", 0, 0, 32)
            oled.text("Closed", 0, 12, 32)
            oled.show()
            time.sleep(0.5)
            global update_display
            update_display = 1
        else:
            ind_led.value(1)
            shut_relay.value(1)
            oled.init_display()
            oled.rotate(2)
            oled.text("Shutter", 0, 0, 32)
            oled.invert(1)
            oled.text("OPEN", 16, 12, 32)
            oled.show()

        
    else:
        ind_led.value(1)
        shut_relay.value(1)
        time.sleep(shut_spd)
        shut_relay.value(0)
        ind_led.value(0)
        oled.text("Shutter Fired", 0, 24)
        oled.show()



# setting displayed time for shutter and setting shutter open delay
# speeds going from 1/60 to 30 seconds plus focus

def scrn_txt(delay_sel):
    
    global shut_txt_val
    global shut_spd
    if delay_sel == 1:
        shut_txt_val="Focus"
    elif delay_sel == 2:
        shut_relay.value(0)
        shut_spd = 0.016
        shut_txt_val="1/60 Second"
    elif delay_sel == 3:
        shut_relay.value(0)
        shut_spd = 0.033
        shut_txt_val="1/30 Second"
    elif delay_sel == 4:
        shut_spd = 0.067
        shut_txt_val="1/15 Second"
    elif delay_sel == 5:
        shut_spd = 0.125
        shut_txt_val="1/8 Second"
    elif delay_sel == 6:
        shut_spd = 0.25
        shut_txt_val="1/4 Second"
    elif delay_sel == 7:
        shut_spd = 0.5
        shut_txt_val="1/2 Second"
    elif delay_sel == 8:
        shut_spd = 1
        shut_txt_val="1 Second"
    elif delay_sel == 9:
        shut_spd = 2
        shut_txt_val="2 Seconds"
    elif delay_sel == 10:
        shut_spd = 3
        shut_txt_val="3 Seconds"
    elif delay_sel == 11:
        shut_spd = 4
        shut_txt_val="4 Seconds"
    elif delay_sel == 12:
        shut_spd = 5
        shut_txt_val="5 Seconds"
    elif delay_sel == 13:
        shut_spd = 6
        shut_txt_val="6 Seconds"
    elif delay_sel == 14:
        shut_spd = 7
        shut_txt_val="7 Seconds"
    elif delay_sel == 15:
        shut_spd = 8
        shut_txt_val="8 Seconds"
    elif delay_sel == 16:
        shut_spd = 9
        shut_txt_val="9 Seconds"
    elif delay_sel == 17:
        shut_spd = 10
        shut_txt_val="10 Seconds"
    elif delay_sel == 18:
        shut_spd = 11
        shut_txt_val="11 Seconds"
    elif delay_sel == 19:
        shut_spd = 12
        shut_txt_val="12 Seconds"
    elif delay_sel == 20:
        shut_spd = 13
        shut_txt_val="13 Seconds"
    elif delay_sel == 21:
        shut_spd = 14
        shut_txt_val="14 Seconds"
    elif delay_sel == 22:
        shut_spd = 15
        shut_txt_val="15 Seconds"
    elif delay_sel == 23:
        shut_spd = 16
        shut_txt_val="16 Seconds"
    elif delay_sel == 24:
        shut_spd = 17
        shut_txt_val="17 Seconds"
    elif delay_sel == 25:
        shut_spd = 18
        shut_txt_val="18 Seconds"
    elif delay_sel == 26:
        shut_spd = 19
        shut_txt_val="19 Seconds"
    elif delay_sel == 27:
        shut_spd = 20
        shut_txt_val="20 Seconds"
    elif delay_sel == 28:
        shut_spd = 21
        shut_txt_val="21 Seconds"
    elif delay_sel == 29:
        shut_spd = 22
        shut_txt_val="22 Seconds"
    elif delay_sel == 30:
        shut_spd = 23
        shut_txt_val="23 Seconds"
    elif delay_sel == 31:
        shut_spd = 24
        shut_txt_val="24 Seconds"
    elif delay_sel == 32:
        shut_spd = 25
        shut_txt_val="25 Seconds"
    elif delay_sel == 33:
        shut_spd = 26
        shut_txt_val="26 Seconds"
    elif delay_sel == 34:
        shut_spd = 27
        shut_txt_val="27 Seconds"
    elif delay_sel == 35:
        shut_spd = 28
        shut_txt_val="28 Seconds"
    elif delay_sel == 36:
        shut_spd = 29
        shut_txt_val="29 Seconds"
    elif delay_sel == 37:
        shut_relay.value(0)
        shut_spd = 30
        shut_txt_val="30 Seconds"
    else:
        print("error")


# setting up rotary encoder input

r = RotaryIRQ(pin_num_clk=13,
              pin_num_dt=14,
              min_val=1,
              max_val=37,
              reverse=True,
              range_mode=RotaryIRQ.RANGE_WRAP)

val_old = r.value()
update_display = 1

while True:
    
    val_new = r.value()
    ind_led.value(0)

    if val_old != val_new: # acumulating rotary encoder steps
        
        val_old = val_new
        print('result =', val_new)
        update_display = 1
        
    if SW.value()==0 and n==0:  # firing shutter when trigger button pressed center button on encoder used
        
        shut_fire(val_new)
        print("Button Pressed")  
        n=1
        while SW.value()==0:  
           continue
    n=0  

    if update_display == 1:  # updating display with selected shutter speed and setting new speed value once new speed selected by turning rotary encoder
        
        update_display = 0
        scrn_txt(val_new)
        oled.init_display()
        oled.rotate(2)
        oled.text("Shutter Speed", 16, 0)
        oled.text(shut_txt_val, 8, 12)
        oled.show()

    time.sleep_ms(5)
