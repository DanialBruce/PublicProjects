These are very simple UDP applications based on Socket module of Python.

visit  https://docs.python.org/3/library/socket.html for official documentation.

These programs were used to test communications with OLIMEX MOD-WIFI-ESP8266 module.

Remeber to change the values to you own costume desires and change them according to you network and application. Remember to use correct decoder(ASCII, UTC-8 etc).


NOTES!:

- in reciever program, you can listen for one IP or leave it as an empty string (or set it to 0.0.0.0) to listen to all packets using defined ports. 
If for whatever reason the receiver can't receive packets from a source, try the full sender/receiver app first and than try again with the standalone listener program right away. For whatever reason, this seems to fix the issue (atleast it did for me). Perhaps the problem has something to do with the nature of UDP packets.

- above suggestion could also fix issues with WinError: "The IP is not valid in the corrent context" error. If this error occures, it simpy means your PC (or on whatever device these programs will run) cannot find and reach the specified ip address.

- You can only have one receiver console open at all times. If tried otherwise, the new instace simpy crashes. Having the program running through a debugger (like the one in VS code) also counts as an instance so it also generates an error.



Hope these come in handy :)

Regards,
Danial


