#pressing button or in case applying high voltage to any of this outputs can run its function
#this is a sound player that gives you ability to play, next, previus, stop, pause, unpause the sound.
#Only .wav files can be handeled
# we are supposed to use it to give surgery instructions.
import pygame.mixer
from time import sleep
import RPi.GPIO as GPIO
from sys import exit
import glob
import os
GPIO.setmode(GPIO.BCM)
#previous button
GPIO.setup(23, GPIO.IN)
#play button
GPIO.setup(24, GPIO.IN)
#next button
GPIO.setup(25, GPIO.IN)
#pause button
GPIO.setup(13, GPIO.IN)
#Unpause button
GPIO.setup(19, GPIO.IN)
#stop button
GPIO.setup(16, GPIO.IN)
#buzzer button
GPIO.setup(12, GPIO.IN)

pygame.mixer.init(48000, -16, 1, 1024)


soundChannelA = pygame.mixer.Channel(1)
soundChannelBuzzer = pygame.mixer.Channel(2)

dirname="/home/pi/Documents/sound_sample/"
print("Sampler Ready.")
pattern = '*.wav'
files = glob.glob(os.path.join(dirname, pattern))  
files = sorted(files) # sort in alphabetical order
print(files)
count=0
#btnPlay = Button("Play", 23, __onPlayButtonChanged) # GPIO header pin 22
#btnPrevious = Button("Previous", 24, __onPreviousButtonChanged) # GPIO header pin 16
#btnNext = Button("Next", 25, __onNextButtonChanged) # GPIO header pin 18

input_pin = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def my_function_play(channel):
    global count
    if GPIO.input(24)==GPIO.HIGH:
        print("I was called Play!")
        
        print("count",count)
        if count>0 and count <len(files):
         print("index",count)
         soundChannelA.play(pygame.mixer.Sound(files[count]))
        else:
          count=0
          print("index",count)
          soundChannelA.play(pygame.mixer.Sound(files[count]))

input_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def my_function_previous(channel):
    global count
    if GPIO.input(23)==GPIO.HIGH:
        global count
        print("I was called Previous!")
        print("count",count)
        if count>0:
                  count=count-1
        else:
                  count=0
        print("index",count)
        soundChannelA.play(pygame.mixer.Sound(files[count]))


input_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def my_function_Next(channel):
    global count
    if GPIO.input(25)==GPIO.HIGH:
        
        print("I was called Next!")
        print("count",count)
        if count<len(files):
              count=count+1
              
        else:
              count=0
        print("index",count)
        soundChannelA.play(pygame.mixer.Sound(files[count]))

def paused(channel):
    if GPIO.input(13)==GPIO.HIGH:
        ############
        print("I was called pause!")
        pygame.mixer.pause()
        #############
def unpause(channel):
    if GPIO.input(19)==GPIO.HIGH:
        global pause
        print("I was called unpause!")
        #################
        pygame.mixer.unpause()
        #################
        #pause = False
def stoped(channel):
    if GPIO.input(16)==GPIO.HIGH:
        print("I was called stop!")
        global pause
        #################
        pygame.mixer.stop()
    #################
    #pause = False
GPIO.setup(21,GPIO.OUT)
def buzzer_play(channel):
        if GPIO.input(12)==GPIO.HIGH:
            print("I was called buzzer!")
            soundChannelBuzzer.play(pygame.mixer.Sound("/home/pi/Documents/sound_sample/Buzzer-Sound.wav"))
            GPIO.output(21,GPIO.HIGH)
        else:
            GPIO.output(21,GPIO.LOW)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#while True:
##    #GPIO.add_event_detect(12, GPIO.RISING, callback=lambda x:buzzer_play(count), bouncetime=2)
#GPIO.add_event_detect(23, GPIO.FALLING, callback=lambda x: my_function_previous(count), bouncetime=200)
#GPIO.add_event_detect(24, GPIO.FALLING, callback=lambda x:my_function_play(count), bouncetime=20)
#GPIO.add_event_detect(25, GPIO.FALLING, callback=lambda x:my_function_Next(count), bouncetime=200)
#GPIO.add_event_detect(13, GPIO.FALLING, callback=lambda x:paused(count), bouncetime=200)
#GPIO.add_event_detect(19, GPIO.FALLING, callback=lambda x:unpause(count), bouncetime=200)
#GPIO.add_event_detect(16, GPIO.FALLING, callback=lambda x:stoped(count), bouncetime=200)
##GPIO.add_event_detect(12, GPIO.FALLING, callback=lambda x:buzzer_play(count), bouncetime=200)
#GPIO.add_event_detect(12, GPIO.FALLING, callback=lambda x:buzzer_play(count), bouncetime=2)
#    if GPIO.input(23)==GPIO.HIGH:
GPIO.add_event_detect(23, GPIO.RISING, callback=lambda x: my_function_previous(count), bouncetime=200)


#        my_function_previous(count)



#    if GPIO.input(24)==GPIO.HIGH:
GPIO.add_event_detect(24, GPIO.RISING, callback=lambda x:my_function_play(count), bouncetime=20)




#    if GPIO.input(25)==GPIO.HIGH:
#        my_function_Next(count)
GPIO.add_event_detect(25, GPIO.RISING, callback=lambda x:my_function_Next(count), bouncetime=200)





#    if GPIO.input(13)==GPIO.HIGH:
GPIO.add_event_detect(13, GPIO.RISING, callback=lambda x:paused(count), bouncetime=200)


    

#    if GPIO.input(19)==GPIO.HIGH:
GPIO.add_event_detect(19, GPIO.RISING, callback=lambda x:unpause(count), bouncetime=200)




#    if GPIO.input(16)==GPIO.HIGH:
GPIO.add_event_detect(16, GPIO.RISING, callback=lambda x:stoped(count), bouncetime=200)
        
    

while True:
    
#    GPIO.add_event_detect(12, GPIO.FALLING, callback=lambda x:buzzer_play(count), bouncetime=2)
    if GPIO.input(12)==GPIO.HIGH:
        buzzer_play(12)
    else:
            GPIO.output(21,GPIO.LOW)
        

print("done")
    #while True:
#        
#
#        #GPIO.cleanup()
##drill sound clip
##https://www.soundsnap.com/tags/drill
#
#
