from drivers import Lcd
from gpiozero import *
class LCD:
    def __init__(self):
        self.lcd = Lcd()
    def write(self, str: string, int: line):
        self.lcd.lcd_display_string(string, line)
    def clear(self):
        self.lcd.lcd_clear()
    def full_dislay(self, str: line1, str: line2):
        self.lcd.lcd_display_string(line1, 1)
        self.lcd.lcd_display_string(line2, 2)