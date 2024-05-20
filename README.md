# Raspberry Pi 5 Bluetooth Automatic Pairing (Without Pin Code)

This guide provides steps to set up automatic Bluetooth pairing on a Raspberry Pi 5 without using pins.

## Steps

### 1. Create AutoStart Folder
First, create an AutoStart folder in the Home directory.
```sh
mkdir ~/AutoStart
```

### 2. Create an Executable Script
Next, create an executable script named bluetooth-pair.sh inside /Home/AutoStart.
```sh
touch /Home/AutoStart/bluetooth-pair.sh && chmod +777 /Home/AutoStart/bluetooth-pair.sh
```
### 3. Script Content
Add your Bluetooth pairing script content to bluetooth-pair.sh.

```sh
#!/bin/bash
sudo bluetoothctl << EOF
power on
discoverable on
pairable on
agent NoInputNoOutput
default-agent
scan on
EOF
sudo bt-agent -c NoInputNoOutput
```

### 4. Auto-Run Script on Boot
To ensure this script runs automatically at every power cycle, add the following command to the **/etc/rc.local** file just before the Exit 0 command:

To edit the rc.local file, use:
```sh
sudo nano /etc/rc.local
```
While inside rc.local file, add *sudo sh /home/pi/AutoStart/bluetooth-pair.sh*
:
```sh
...

sudo sh /home/pi/AutoStart/bluetooth-pair.sh

Exit 0
```

**NOTE:** You can also add all commands above directly to the rc.local file, but this is more loosely-coupled way. Also, this may wark on also RPI 4.

