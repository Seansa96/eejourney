Tags: [[linux]] 

This is a simple command primarily used to mount network drives on to the machine the command is run on.

## Example

```
sudo mount -t cifs //192.168.56.1/ssd1 /mnt -o username=SeanS,password=Sunsinsix6!
```

`-t` is the "target filesystem". This is cifs in this case, with is the Common Internet File System, used for, in this case, an SMB (Samba) server.

`//192.168.56.1/ssd1` Now we just take the actual URI of the network share and put it in. Simplest way is to just do the IP address and the name of the share itself.  You can use the host name as well, but it's a bit finicky with DNS and other stuff.  Best to just use IP.

After that, we use the `-o` flag, which needs a username and password as that is typical of SMB shares for access.

The final part is the name of the mounted drive. It's standard in linux to name this `mnt`, but it can be literally whatever you want.

# Common Issues

**Unable to connect**

Make sure the share is still at the IP address you believed it to be. Ping it first and make sure it's up.
