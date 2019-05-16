#!/usr/bin/env python3

def commandpush(devicecmd):
    for coffeetime in devicecmd.keys():
        print("Handshaking. .. ... connecting with " + coffeetime)
        for mycmds in devicecmd[coffeetime]:
            print("Attempting to sending command --> " + mycmds)

def main():
    work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"]}
    print("welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(work2do)


main()

