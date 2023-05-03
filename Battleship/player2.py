# Player 2 Code

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

# BLYNK_AUTH = '5iI58SeUW5v5Ozlj5PqFwLJWccM1mmo3' # Katie's player 1
BLYNK_AUTH = '9AiTTwD3YOoyakAF-rRt4JSGxzVm2Wgg' # Katie's player 2
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
player1guess = "NA"
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
    global player1guess
    global player2guess
    global player1response
    global player2response
    blynk.virtual_write(1, player2response)
    blynk.virtual_write(2, player2guess)

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

label0 = M5Label(player1guess, x=119, y=105, color=0x000, font=FONT_MONT_14, parent=None)

# Call this function when player 1 has entered a respond to player 2's guess
def player1responseFunc():
  if player1response == 'hit':
       screen.clean_screen()
       screen.set_screen_bg_color(0x00ff00)
       screen.clean_screen()
       
  elif player1response == 'miss':
       screen.clean_screen()
       screen.set_screen_bg_color(0xff0000)
       screen.clean_screen()
       
  elif player1response == 'sink':
       global sinks1
       screen.clean_screen()
       screen.set_screen_bg_color(0x0000ff)
       screen.clean_screen()
       sinks1 = sinks1 + 1


# Function for continuing after player 2 has responded
def player2guessFunc():
  # Display row position buttons
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
   
   
     def one_pressed():
        screen.clean_screen()
        global player2guess
        player2guess = "A1"
     
     one.pressed(one_pressed)
  
     def two_pressed():
        screen.clean_screen()
        global player2guess
        player2guess = "A2"
       
     two.pressed(two_pressed)
     
     def three_pressed():
        screen.clean_screen()
        blynk.virtual_write(2, "A3")
        player1respFunc()
      
     three.pressed(three_pressed)

     def four_pressed():
        screen.clean_screen()
        blynk.virtual_write(2, "A4")
        player1respFunc()
      
     four.pressed(three_pressed)
     
     def five_pressed():
        screen.clean_screen()
        blynk.virtual_write(2, "A5")
        player1respFunc()
      
     five.pressed(three_pressed)
     
     def six_pressed():
        screen.clean_screen()
        blynk.virtual_write(2, "A6")
        player1respFunc()
      
     six.pressed(three_pressed)
     
  A.pressed(A_pressed)
  
  def B_pressed():
       
       screen.clean_screen()
       wait(2)
       one = M5Btn(text='1', x=18, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
       two = M5Btn(text='2', x=118, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
       three = M5Btn(text='3', x=220, y=15, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
       four = M5Btn(text='4', x=18, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
       five = M5Btn(text='5', x=118, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
       six = M5Btn(text='6', x=220, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
     
     
       def one_pressed():
          screen.clean_screen()
          blynk.virtual_write(2, "B1")
          player1respFunc()
       
       one.pressed(one_pressed)
    
       def two_pressed():
          screen.clean_screen()
          blynk.virtual_write(2, "B2")
          player1respFunc()
         
       two.pressed(two_pressed)
       
       def three_pressed():
          screen.clean_screen()
          blynk.virtual_write(2, "B3")
          player1respFunc()
        
       three.pressed(three_pressed)
  
       def four_pressed():
          screen.clean_screen()
          blynk.virtual_write(2, "B4")
          player1respFunc()
        
       four.pressed(three_pressed)
       
       def five_pressed():
          screen.clean_screen()
          blynk.virtual_write(2, "B5")
          player1respFunc()
        
       five.pressed(three_pressed)
       
       def six_pressed():
          screen.clean_screen()
          blynk.virtual_write(2, "B6")
          player1respFunc()
        
        
       six.pressed(three_pressed)
       
  B.pressed(B_pressed)
    
  


def player2respFunc():
    #get and display player1guess on top of screen and offer hit, miss, sink options
  screen.clean_screen()
  lcd.print(str(player1guess), lcd.CENTER, lcd.CENTER)
  hit = M5Btn(text='Hit', x=18, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
  miss = M5Btn(text='Miss', x=118, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
  sink = M5Btn(text='Sink', x=220, y=138, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
  
  # Update channel V1 when either hit, miss, or sink is pressed
  def hit_pressed():
    global player2response
    player2response = "hit"
  
  hit.pressed(hit_pressed)
  
  def miss_pressed():
    global player2response
    player2response = "miss"
  
  miss.pressed(miss_pressed)
  
  def sink_pressed():
    global player2response
    player2response = "sink"
    global sinks2
    sinks2 = sinks2+1
  
  sink.pressed(sink_pressed)
  

def readyFunc():
    screen.clean_screen()
    ready = M5Btn(text='ready', x=118, y=118, w=85, h=85, bg_c=0xFFFFFF, text_c=0x000000, font=FONT_MONT_14, parent=None)
    global rpress
    rpress = False
    def ready_pressed():
        global rpress
        rpress = True
    ready.pressed(ready_pressed)

while sinks1 != ships1 and sinks2 != ships2:
  readyFunc()
  while not rpress:
    wait(1)
    updateBlynk()
  player2response = "NA"
  player2respFunc()
  while player2response == "NA":
    wait(1)
    updateBlynk()
  blynk.virtual_write(1, player2response)
  player2guess = "NA"
  player2guessFunc()
  while player2guess == "NA":
    wait(1)
    updateBlynk()
  blynk.virtual_write(2, player2guess)
