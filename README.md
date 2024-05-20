# Raspberry Pi 5 Bluetooth Automatic Pairing (Without Pin Code Authentication)

This guide provides steps to set up automatic Bluetooth pairing on a Raspberry Pi 5 without using pin codes for authentication. After these settings, your RPI becomes a bluetooth device like headset/speaker, where you can connect automatically without using any UI.

## Requirements
Install these two **bluez** and **bluez-tools** packages from apt first.
```sh
sudo apt-get install bluez && sudo apt-get install bluez-tools
```

**NOTE**: After installation, you can test no-pin connection manually via this command:
```sh
sudo bt-agent -c NoInputNoOutput
```

## Steps
### Step 1. Create AutoStart Folder
Create an AutoStart folder in the Home directory.
```sh
mkdir ~/AutoStart
```

### Step 2. Create an Executable Script
Next, create an executable script named bluetooth-pair.sh inside /Home/AutoStart.
```sh
touch /Home/AutoStart/bluetooth-pair.sh && chmod +777 /Home/AutoStart/bluetooth-pair.sh
```
### Step 3. Script Content
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

### Step 4. Auto-Run Script on Boot
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




