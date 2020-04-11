import pymem
import pymem.process
import re
import time
import argparse

#https://github.com/danielkrupinski/OneByteWallhack/blob/master/OneByteWallhack.py
#https://github.com/danielkrupinski/OneByteRadar/blob/master/OneByteRadar.py
#https://github.com/frk1/hazedumper/blob/master/csgo.hpp
dwEntityList = (0x4D42A34)
dwGlowObjectManager = (0x528A810)
m_iGlowIndex = (0xA428)
m_iTeamNum = (0xF4)
dwRadarBase = (0x51777A4)
def makeitready():
    global pm
    global client
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll")





def esp():
    print("ESP wall is on.")

    while True:
        glow_manager = pm.read_int(client.lpBaseOfDll + dwGlowObjectManager)
        #print(glow_manager)
        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client.lpBaseOfDll + dwEntityList + i * 0x10)
            #print(entity)
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)
               # print(entity_team_id)

                if entity_team_id == 2:  # Terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.5))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow

                elif entity_team_id == 3:  # Counter-terrorist
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))   # R
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))   # B
                    pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.5))  # Alpha
                    pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow
def radar():
    print("radar is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08', clientModule).start() + 6    
    while True:
        pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
        time.sleep(0.5)

def Money():
    print("money is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',clientModule).start()
    while True:
        pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)
        time.sleep(1)

def main():
    print("###############################")
    print("dont use cheat idiot :D")
    print("just use it when you have to")
    print("-----------------------------")
    print("-----------khashi_n----------")
    print("-----------------------------")
    print("###############################")

    print("1 = wall | 2 = radar | 3 = money show")
    cheat = int(input("Enter Number  :  "))

    if cheat == 1:
        makeitready()
        esp()
    elif cheat == 2:
        makeitready()
        radar()
    elif cheat == 3:
        makeitready()
        Money()
    else:
        print("bad input!!!")
        exit()

if __name__ == '__main__':
    main()

