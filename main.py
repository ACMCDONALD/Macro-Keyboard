#macro_keyboard v1.2
#when a 60% keyboard was a bad idea
#created by: andrew mcdonald
#date created: January 15, 2023
#date edited: February 2, 2023

import time
import board
import digitalio
import usb_hid
import rotaryio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

kbd = Keyboard(usb_hid.devices)
consumer = ConsumerControl(usb_hid.devices)

# define buttons

# button1 = GP
button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.DOWN

# button2 = GP
button2 = digitalio.DigitalInOut(board.GP2)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.DOWN

# button3 = GP
button3 = digitalio.DigitalInOut(board.GP3)
button3.direction = digitalio.Direction.INPUT
button3.pull = digitalio.Pull.DOWN

# button4 = GP
button4 = digitalio.DigitalInOut(board.GP4)
button4.direction = digitalio.Direction.INPUT
button4.pull = digitalio.Pull.DOWN

# button5 = GP
button5 = digitalio.DigitalInOut(board.GP5)
button5.direction = digitalio.Direction.INPUT
button5.pull = digitalio.Pull.DOWN

# button6 = GP
button6 = digitalio.DigitalInOut(board.GP6)
button6.direction = digitalio.Direction.INPUT
button6.pull = digitalio.Pull.DOWN

# button7 = GP
button7 = digitalio.DigitalInOut(board.GP7)
button7.direction = digitalio.Direction.INPUT
button7.pull = digitalio.Pull.DOWN

# no button8
#button8 = digitalio.DigitalInOut(board.GP8)
#button8.direction = digitalio.Direction.INPUT
#button8.pull = digitalio.Pull.DOWN

# button9 = GP
button9 = digitalio.DigitalInOut(board.GP9)
button9.direction = digitalio.Direction.INPUT
button9.pull = digitalio.Pull.DOWN

# button10 = GP
button10 = digitalio.DigitalInOut(board.GP10)
button10.direction = digitalio.Direction.INPUT
button10.pull = digitalio.Pull.DOWN

# button11 = GP
button11 = digitalio.DigitalInOut(board.GP11)
button11.direction = digitalio.Direction.INPUT
button11.pull = digitalio.Pull.DOWN

# button12 = GP
button12 = digitalio.DigitalInOut(board.GP12)
button12.direction = digitalio.Direction.INPUT
button12.pull = digitalio.Pull.DOWN

# rotary encoder
enc = rotaryio.IncrementalEncoder(board.GP13, board.GP14)
encSw = digitalio.DigitalInOut(board.GP15)
encSw.direction = digitalio.Direction.INPUT
encSw.pull = digitalio.Pull.UP
lastPosition = 0

while True:
    # poll encoder position
    position = enc.position
    if position != lastPosition:
        if lastPosition < position:
            consumer.send(ConsumerControlCode.VOLUME_INCREMENT)
        else:
            consumer.send(ConsumerControlCode.VOLUME_DECREMENT)
        lastPosition = position
           
    # poll encoder button
    if encSw.value == 0:
        consumer.send(ConsumerControlCode.MUTE)
        
    # keycodes
    
    # button1 = ~
    if button1.value:
        kbd.send(Keycode.POUND)
        
    # button2 = left arrow
    if button2.value:
        kbd.send(Keycode.A)
        
    # button3 = 
    if button3.value:
        kbd.send(Keycode.A)
        
    # button4 = 
    if button4.value:
       consumer.send(ConsumerControlCode.PLAY_PAUSE)
    
    # button5 = 
    if button5.value:
        kbd.send(Keycode.DELETE)
    
    # button6 = up arrow
    if button6.value:
        kbd.send(Keycode.UP_ARROW)
    
    # button7 = 
    if button7.value:
        kbd.send(Keycode.A)
    
    # no button8
    #elif button8.value:
    #    kbd.send(Keycode.RIGHT_ARROW)
    
    # button9 = left arrow
    if button9.value:
        kbd.send(Keycode.LEFTT_ARROW)
    
    # button10 = down arrow    
    if button10.value:
        kbd.send(Keycode.DOWN_ARROW)
    
    # button11 = right arrow
    if button11.value:
        kbd.send(Keycode.RIGHT_ARROW)
        
    # button12 =    
    if button12.value:
        kbd.send(Keycode.A)
    
    time.sleep(0.2)
