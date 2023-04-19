# Player 1 Code

from m5stack import *
from m5stack_ui import *
from uiflow import *

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)

import M5BlynkLib
from BlynkTimer import BlynkTimer
import network
import machine

WIFI_SSID = 'ND-guest'
WIFI_PASS = ''

BLYNK_AUTH = '5iI58SeUW5v5Ozlj5PqFwLJWccM1mmo3' # Katie's player 1
# BLYNK_AUTH = '9AiTTwD3YOoyakAF-rRt4JSGxzVm2Wgg' # Katie's player 2
# BLYNK_AUTH = 'L1_427mM05GzJ-M4Hl_npXIT6iSJ59nT' # Brockmans
#BLYNK_AUTH = '8imWFTlYhi8uGW1QbrJbRvTf5kQ973MU' # Alvins


wifi = network.WLAN(network.STA_IF)
if not wifi.isconnected():
    lcd.println("Connecting to WiFi...")
    wifi.active(True)
    wifi.connect(WIFI_SSID, WIFI_PASS)
    while not wifi.isconnected():
        pass

lcd.print('IP:')
lcd.println(wifi.ifconfig()[0])

# define variables
uptime = 0
player1 = ''
player2 = ''
blynk = M5BlynkLib.Blynk(BLYNK_AUTH)
playing = True

# handling states
@blynk.on("connected")
def blynk_connected(ping):
    pass
 
@blynk.on("disconnected")
def blynk_disconnected():
    lcd.println('Blynk disconnected')


# Make sure blynk channels are all reset
blynk.virtual_write(0, "NA")
blynk.virtual_write(1, "NA")
blynk.virtual_write(2, "NA")
blynk.virtual_write(3, "NA")

# Initialize blynk channel variables
player1guess = "A2"
player2response = "NA"
player2guess = "NA"
player1response = "NA"

button_pressed = False


# Register virtual pin handlers
@blynk.on("V0")
def v0_read_handler():
    player1guess = blynk.virtual_read(0)
   
@blynk.on("V1")
def v1_read_handler():
    player2response = blynk.virtual_read(1)
   
@blynk.on("V2")
def v2_read_handler():
    player2guess = blynk.virtual_read(2)
   
@blynk.on("V3")
def v3_read_handler():
    player1response = blynk.virtual_read(3)
   

# Will update Blynk every 1 Second
def updateBlynk():
    global player1
    global player2

# Create BlynkTimer Instance
timer = BlynkTimer()
timer.set_interval(1, updateBlynk)

screen = M5Screen()
screen.clean_screen()
screen.set_screen_bg_color(0xFFFFFF)


# declare the number of ships
ships1 = 6
ships2 = 6
sinks1 = 0
sinks2 = 0

Player1Response = ''
Player1Guess = ''
Player2Response = ''
Player2Guess = ''

 
# Display buttons for Player 1 to make their first guess
A = M5Btn(text='A', x=18, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
B = M5Btn(text='B', x=118, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
C = M5Btn(text='C', x=220, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
D = M5Btn(text='D', x=18, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
E = M5Btn(text='E', x=118, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
F = M5Btn(text='F', x=220, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

def A_pressed():
   
   screen.clean_screen()
   wait(2)
   one = M5Btn(text='1', x=18, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
   two = M5Btn(text='2', x=118, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
   three = M5Btn(text='3', x=220, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
   four = M5Btn(text='4', x=18, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
   five = M5Btn(text='5', x=118, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
   six = M5Btn(text='6', x=220, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
 
  #send selected variable to blynk
  #display selected coordinate then wait while the screen below is shown on student B
   
   def one_pressed():
     screen.set_screen_bg_color(0xffffff)
     blynk.virtual_write(0,"A1")
   one.pressed(one_pressed)
   
   def two_pressed():
     screen.set_screen_bg_color(0xffffff)
     blynk.virtual_write(0,"A2")
     screen.clean_screen()
     wait(1)
   two.pressed(two_pressed)
   
   #three.pressed(one_pressed)
   #four.pressed(one_pressed)
   #two.pressed(one_pressed)
   #five.pressed(one_pressed)
   #six.pressed(one_pressed)
A.pressed(A_pressed)
wait(5)
blynk.virtual_write(0, 'NA')


# After all buttons displayed, and selection sent to player 2, display hit, miss sink reaction
# store variable

def player2responsefunc():
  if Player2Response == 'hit':
     screen.clean_screen()
     screen.set_screen_bg_color(0x00ff00)
     screen.clean_screen()
     
  elif Player2Response == 'miss':
     screen.clean_screen()
     screen.set_screen_bg_color(0xff0000)
     screen.clean_screen()
     
  elif Player2Response == 'sink':
     screen.clean_screen()
     screen.set_screen_bg_color(0x0000ff)
     screen.clean_screen()
     sinks2 = sinks2 + 1
   

wait(5)
#wait for player 2 to guess
# display player 2 guess on the screen
screen.clean_screen()
lcd.print(Player2Guess)

#display.println(Player2Guess)
#display.display()
hit = M5Btn(text='hit', x=18, y=118, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
miss = M5Btn(text='miss', x=118, y=118, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
sink = M5Btn(text='sink', x=220, y=118, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)

def hit_pressed():
   blynk.virtual_write(3,"hit")
hit.pressed(hit_pressed)
     
def sink_pressed():
    blynk.virtual_write(3,"sink")
    global sinks1
    sinks1 = sinks1 + 1
    #need sd card to display image
    # Open the image file
    #with open('/sd/my_image.jpg', 'rb') as f:
    #img_data = f.read()

   # Display the image on the screen
   #lcd.image(0, 0, img_data)
   #wait(7)
sink.pressed(sink_pressed)
     
def miss_pressed():
    blynk.virtual_write(3,"miss")
miss.pressed(miss_pressed)

wait(5)
blynk.virtual_write(3,"NA")

#while loop
while True:
    blynk.run()
    timer.run()
