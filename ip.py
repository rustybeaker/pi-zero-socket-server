import socket
import lcd
from threading import Timer

usual_ip = "192.168.0.132"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("some-public-domain.com",80))
cur_ip = (s.getsockname()[0])
s.close()

lcd.lcd_init()
lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)

if ( usual_ip != cur_ip ):
  lcd.lcd_string("IP "+cur_ip)
else:
  lcd.lcd_string("checking ip",2)
  
  def print_ip():
      lcd.lcd_string("IP "+usual_ip,2)
  
  Timer(1.0, print_ip).start()
