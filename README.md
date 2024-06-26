# Raspberry Pi 5 Bluetooth Automatic Pairing (Without Pin Code Authentication)

This guide provides steps to set up automatic Bluetooth pairing on a Raspberry Pi 5 without using pin codes for authentication. After these settings, your RPI becomes a bluetooth device like headset/speaker, where you can connect automatically without using any UI.

# Requirements
## 1) Install **bluez** and **bluez-tools** packages from apt first.
```sh
sudo apt-get install bluez && sudo apt-get install bluez-tools
```
**NOTE**: After installation, you can test no-pin connection manually via this command:
```sh
sudo bt-agent -c NoInputNoOutput
```

## 2) Change Bluetooth configurations.
- Open *dbus.org.bluez.service* file.
```sh
sudo nano /etc/systemd/system/dbus.org.bluez.service
```
- Edit *ExecStart* line and add *ExecStartPost* line to the file.
```sh
...
ExecStart=/usr/libexec/bluetooth/bluetoothd -C
ExecStartPost = /usr/bin/sdptool add SP
...
```

#

# Steps to Auto Start Bluetooth Connection
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
Add your Bluetooth pairing script content to bluetooth-pair.sh file.

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

sudo bt-agent -c NoInputNoOutput & sudo rfcomm watch hci0
```

### Step 4. Auto-Run Script on Boot
To ensure this script runs automatically at every power cycle, add the following command to the **/etc/rc.local** file just before the Exit 0 command:

To edit the rc.local file, use:
```sh
sudo nano /etc/rc.local
```
While inside rc.local file, add *sudo sh /home/pi/AutoStart/bluetooth-pair.sh* line before *Exit 0*:
```sh
...

sudo sh /home/pi/AutoStart/bluetooth-pair.sh

Exit 0
```

**NOTE:** You can also add all commands above directly to the rc.local file, but this is more loosely-coupled way. This may also work in RPI 4.

**NOTE:** Added *bt_writer.py* and *bt_reader.py* files for online testing via *Serial Bluetooth Terminal* application in Android phones.
