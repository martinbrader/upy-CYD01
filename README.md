# upy-CYD01

Cheap Yellow Display examples using micropython

Many thanks to Brian Lough for getting all the basics prepared:
https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display

The majority of the examples are modified versions of demos from here:
https://github.com/rdagger/micropython-ili9341/tree/master

## Getting Started

### Thonny setup
I used the latest version of Thonny https://thonny.org/

Download the latest version of micropython from here https://micropython.org/download/ESP32_GENERIC/ and install it using Thonny.
Here are the options I used:

![alt text](documentation/thonny_options.png)
![alt text](documentation/thonny_options2.png)

In Thonny create a "lib" folder in your CYD and copy in files:

- ili9341.py (the drivers for CYD)
- cyd_colours.py (my colour definitions)
- cyd_utils (my set of CYD utilities)
- xglcd_font.py (font drivers)
- xpt2046.py (touch screen drivers for CYD)

### SD card set up

My demos assume you have an SD card installed in your CYD.  
Copy the sd folder containing fonts and images onto the SD card.

### Running the demos

I found the easiest way to run the demos was from the "this computer" window on Thonny.  
This avoids the need to download each one onto the CYD.

### Password Search demo set up

Copy the password_search directory to CYD  
Create a wifi credentials text file in the root directory called credentials.txt  
The format for credentials is:  
```
ssid_1,password1  
ssid_2,password2
```

### CYD folder structure

Your folder structure should look like this:

![alt text](documentation/thonny_folders.png)

## Implementation notes

### Touch screen

This is the original SPI for the touch screen:

`touch_spi = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))`

to get touch and display working at same time you need to use SPI(1, and SPI(2,...  
but this causes a conflict with SDcard using slot=2

I found that using SoftSPI for touch appears to resolve this problem!

`touch_spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(25), mosi=Pin(32), miso=Pin(39))`
`touch = Touch(touch_spi, cs=Pin(33), int_pin=Pin(36), int_handler=callback)`

### SD card

SD card must be formatted with a file system recognised by ESP32 (FAT)
