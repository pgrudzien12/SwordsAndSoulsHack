import keyboard
import mouse
import PIL.ImageGrab
import datetime
import colorsys
from time import sleep


top = 316
left = 400
bottom = 915
right = 1201

# Red Color
color1_rgb = (1.0, 0.0, 0.0)
# Convert from RGB to Lab Color Space
color1_lab = colorsys.rgb_to_hsv(*color1_rgb)


color3_rgb = (1.0, 1.0, 0.0)
# Convert from RGB to Lab Color Space
color3_lab = colorsys.rgb_to_hsv(*color3_rgb)

stop = False

def train_attack():
        global stop, color1_lab
        print('train_attack')
        while (stop == False):
                im = PIL.ImageGrab.grab((left,top,right,bottom))
                
                if (is_red(im, (234,435))):
                        keyboard.send('down')
                if (is_red(im, (290,435))):
                        keyboard.send('down')
                if (is_red(im, (320,435))):
                        keyboard.send('down')

                if (is_red(im, (300, 354))):
                        keyboard.send('right')
                if (is_red(im, (285, 354))):
                        keyboard.send('right')
                if (is_red(im, (230, 354))):
                        keyboard.send('right')

                if (is_red(im, (202, 283))):
                        keyboard.send('up')
                if (is_red(im, (234, 280))):
                        keyboard.send('up')
                if (is_red(im, (252, 270))):
                        keyboard.send('up')
                if (is_red(im, (293, 250))):
                        keyboard.send('up')
                if (is_red(im, (323, 232))):
                        keyboard.send('up')

                        
                if (is_yellow(im, (50, 275))):
                        keyboard.send('left')
                if (is_yellow(im, (50, 300))):
                        keyboard.send('left')
                if (is_yellow(im, (50, 375))):
                        keyboard.send('left')

                if (keyboard.is_pressed('esc')):
                    train_stop()

                #sleep(0.10)

        stop = False

def is_red(im, xy):
        color2_rgb = im.getpixel(xy)
        color2_lab = colorsys.rgb_to_hsv(*color2_rgb)
        delta_e = color1_lab[0] - color2_lab[0]
        return delta_e < -0.3

        
def is_yellow(im, xy):
        color2_rgb = im.getpixel(xy)
        color2_lab = colorsys.rgb_to_hsv(*color2_rgb)
        return 0.10 < color2_lab[0] < 0.15

def make_screenshot():
        print('train_attack')
        im = PIL.ImageGrab.grab((left,top,right,bottom))
        print(im.getpixel((10,10)))
        im.show()

def train_stop():
    global stop
    print('train_stop')
    stop = True

def train_defence():
    print('train_defence')

def train_crit():
    print('train_crit')

def train_range():
    print('train_range')

    
def set_top_left():
    global top, left
    top = mouse.get_position()[1]
    left = mouse.get_position()[0]
    print(mouse.get_position())

    
def set_bottom_right():
    global bottom, right
    bottom = mouse.get_position()[1]
    right = mouse.get_position()[0]
    print(mouse.get_position())

keyboard.add_hotkey('ctrl+shift+9', make_screenshot)
keyboard.add_hotkey('ctrl+shift+0', train_stop)
keyboard.add_hotkey('ctrl+shift+1', train_attack)
keyboard.add_hotkey('ctrl+shift+2', train_defence)
keyboard.add_hotkey('ctrl+shift+3', train_crit)
keyboard.add_hotkey('ctrl+shift+4', train_range)
keyboard.add_hotkey('ctrl+shift+[', set_top_left)
keyboard.add_hotkey('ctrl+shift+]', set_bottom_right)



keyboard.wait()