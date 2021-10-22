# main.py -- put your code here!
#get your device's EUI
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))

#70B3D5499B0E6767
