import pymem
import pymem.process
import re
import time
import argparse


dwEntityList = (0x4DA2F24)
dwGlowObjectManager = (0x52EB520)
m_iGlowIndex = (0xA438)
m_iTeamNum = (0xF4)
dwRadarBase = (0x51D7C9C)
dwClientState = (0x58EFE4)
def makeitready():
    global pm
    global client
    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll")





def esp():
    print("ESP wall is on.")

    while True:
        glow_manager = pm.read_int(client.lpBaseOfDll + dwGlowObjectManager)
        print(glow_manager)
        for i in range(1, 32):  # Entities 1-32 are reserved for players.
            entity = pm.read_int(client.lpBaseOfDll + dwEntityList + i * 0x10)
            clientst = pm.read_int(client.lpBaseOfDll + dwClientState + i * 0x10)
            print (clientst)
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_glow = pm.read_int(entity + m_iGlowIndex)

                print(entity_glow)


                pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))   # R
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # G
                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # B
                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0.5))  # Alpha
                pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)           # Enable glow

               # Enable glow


def wall():
    print("wall secound is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x83\xF8.\x8B\x45\x08\x0F',clientModule).start() + 2


    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)

def radar():
    print("radar is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08', clientModule).start() + 6

    pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)


def Money():
    print("radar is on.")
    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',clientModule).start()

    pm.write_uchar(address, 0xEB if pm.read_uchar(address) == 0x75 else 0x75)

def main():
    print("         _             _            _       _    _                    _             _        ")
    print("        /\ \     _    /\ \         / /\    / /\ / /\                /\ \           /\_\      ")
    print("       /  \ \   /\_\ /  \ \       / / /   / / // /  \              /  \ \         / / /  _   ")
    print("      / /\ \ \_/ / // /\ \ \     / /_/   / / // / /\ \            / /\ \ \       / / /  /\_\ ")
    print("     / / /\ \___/ // / /\ \ \   / /\ \__/ / // / /\ \ \          / / /\ \ \     / / /__/ / / ")
    print("    / / /  \/____// / /  \ \_\ / /\ \___\/ // / /  \ \ \        / / /  \ \_\   / /\_____/ /  ")
    print("   / / /    / / // / /   / / // / /\/___/ // / /___/ /\ \      / / /    \/_/  / /\_______/   ")
    print("  / / /    / / // / /   / / // / /   / / // / /_____/ /\ \    / / /          / / /\ \ \      ")
    print(" / / /    / / // / /___/ / // / /   / / // /_________/\ \ \  / / /________  / / /  \ \ \     ")
    print("/ / /    / / // / /____\/ // / /   / / // / /_       __\ \_\/ / /_________\/ / /    \ \ \    ")
    print("\/_/     \/_/ \/_________/ \/_/    \/_/ \_\___\     /____/_/\/____________/\/_/      \_\_\   ")
    print("")
    print("Created By:")
    print("   __     __               __    _            ")
    print("  / /__  / /  ___ _  ___  / /   (_)       ___ ")
    print(" /  '_/ / _ \/ _ `/ (_-< / _ \ / /       / _ \ ")
    print("/_/\_\ /_//_/\_,_/ /___//_//_//_/   ____/_//_/")
    print("                                   /___/      ")
    print("")
    print("USAGE:")
    print("1: Wall Hack (Recomended) \n2: radar hack \n3: show enemy money \n4: Another Wall Hack\n5: Turn Off\n6: Exit")

    while True:
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
        elif cheat == 4:
            makeitready()
            wall()
        elif cheat == 5:
            pm.close_process()
            print("Its Off Now")
        elif cheat == 6:
            pm.close_process()
            print("See U Soon")
            time.sleep(1)
            exit()
        else:
            print("beyne gozine ha entekhab kon!!!")

if __name__ == '__main__':
    main()

#https://github.com/danielkrupinski/OneByteWallhack/blob/master/OneByteWallhack.py
#https://github.com/danielkrupinski/OneByteRadar/blob/master/OneByteRadar.py
#https://github.com/frk1/hazedumper/blob/master/csgo.hpp
#https://github.com/naaax123/Python-CSGO-Cheat
