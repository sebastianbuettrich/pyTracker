###############################################################################
# LoRaWAN Configuration
###############################################################################

# May be either 'otaa', 'abp', or 'off'
LORA_MODE         = 'otaa'

LORA_OTAA_EUI     = '70B3D57ED001825F'
LORA_OTAA_KEY     = '66622B11DCFE3853380083B1F41D4895'     # See README.md for instrufrctions!

# Interval between measures transmitted to TTN.
# Measured airtime of transmission is 56.6 ms, fair use policy limits us to
# 30 seconds per day (= roughly 500 messages). We default to a 180 second
# interval (=480 messages / day).

LORA_SEND_RATE    = 60 # (! not a rate - this is in seconds!
MIN_MOVE_DISTANCE = 0 #setting this to zero for now - i want it all"
