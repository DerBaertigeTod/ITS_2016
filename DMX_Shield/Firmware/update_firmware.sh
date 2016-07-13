sudo avrdude -p m162   -C ~/avrdude_gpio.conf -c pi_1 -v  -U flash:w:Firmware_v5.ino.hex
sudo avrdude -p m162   -C ~/avrdude_gpio.conf -c pi_1 -v  -U lfuse:w:0xff:m -U hfuse:w:0xd8:m -U efuse:w:0xfb:m
