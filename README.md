# pi-zero-socket-server
Code for pi zero socket server, grabs ip and runs on cron job to update LCD display with current local ip for ssh

## Overview
This is a relatively simple code set to implement, most of it I did not write aside from the logic.

The two python modules to use here are lcd.py and ip.py. Make sure both of these are in /home/pi for the instructions here to work.

Note that the lcd.py is code from this website:
https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/lcd_16x2.py

### Drive the LCD and how to wire the Pi Zero to your 16x2 LCD
This is the youtube video that was most helpful to me:
https://www.youtube.com/watch?v=cVdSc8VYVBM

I also used this photo for the pinout of the Pi Zero
https://www.element14.com/community/servlet/JiveServlet/previewBody/80667-102-1-338789/GPIO.png

### Get local IP with python
The method to find the IP was from this stackoverflow post:
http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib

I used the answer posted by UnkwnTech that uses gmail.com to get the local ip. I changed it to ping my own server as I wasn't sure if gmail.com would appreciate getting pinged every 5 minutes.

### Modify ip.py to ping a specific domain
I mentioned the code I used to find the IP address with Python, the original example used gmail.com, I'm not saying that's wrong, I'm not sure if there will be unforseen consequences pinging gmail every 5 minutes. I used my own webserver that I rent. It's up to you to decide who to ping if you decide to use this route to get your ip.

### Add to crontab to update very X-minutes
I was surprised how straightforward it was to add the process to cron.

So at a terminal, assuming you've ssh'd into your pi

```
crontab -e
```
Scroll all the way down and add these two lines

```
*/5 * * * * python /home/pi/ip.py
@reboot python /home/pi/ip.py
```

### Thanks to Raspberry Pi Forum for the help
