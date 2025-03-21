# ovos-tools 

This repository has documentation, scripts and other files to install and work with the Open Voice Operating System (OVOS).

This README document describes how to build a *Personal Voice Assistant* from the ground up.

## The build

The environment used to develop the code and write this document is a RasPi 4B with 4 GB of memory, running Ubuntu Desktop 24.10 inside an *enclosure*.  Details on the hardware and CNC G-code to build a *smart boombox* are here: https://github.com/mike99mac/ovos-tools/tree/main/gcode

The Raspberry Pi OS (aka Raspbian) versions 10 (buster) and 11 (bullseye) were also tested. However, this code and these steps should be relatively portable to any hardware that can run any Linux. 

The overall steps to build an OVOS box are:

- Acquire the hardware 
- Flash Linux to a memory device
- Connect the hardware
- Install and configure Linux
- Install and use ovos-tools
- Test microphone and speakers
- Install and configure OVOS 
- Start Minimy and use it!

## Acquire the hardware
The recommended hardware is a Raspberry Pi (RasPi) 4B, or 400 with 4 or 8 GB of memory.  The RasPi 5 is now available and is more powerful and hopefully easier to procure than the 4 was.


For a microphone, a flat, disk type with a mute/unmute switch for visible privacy is recommended.  Don't use a cheap one.  It is best to move the microphone away from the speakers and closer to the center of the room.

You can start with just about any speaker(s) with a 3.5mm jack that will plug into the RasPi.  A *DAC HAT* plugged on top of the RasPi will greatly improve audio quality.

## Flash Linux to a memory device
The RasPi boots from a micro-SD card that plugs into its underside. A 32 GB card or larger is recommended. You need to *prime the pump* and copy a Linux distribution to it. 

The following Linux distributions have been tested
- ``Ubuntu Desktop 24.10``
- ``Raspi OS Lite Debian GNU/Linux 12 (bookworm)``

### Prepare on Linux

If you have a Linux box with an SD card port, you can use **``rpi-imager``** to copy the Linux image. To do so, perform the following tasks.
- Put a micro-SD card into an SD adapter.
- Plug the SD adapter into the card reader.
- If you don't have it already, install the tool.

```
sudo apt-get install -y rpi-imager
```

- Run the tool.

```
rpi-imager
```
    
- To flash a Linux image to the card, perform the following steps:
    - Select the type of *Raspberry Pi Device* you have - a 4 or a 5.
    - Select one from *Operating System*.
        - Raspberry Pi OS (other) => Raspberry Pi OS Lite (64-bit)
        - Other General Purpose OS => Ubuntu => Desktop 24.10 (64-bit)
    - Select the *Storage* device. You should see just one micro-SD card in the dropdown menu. If you don't see any entry, your SD card has not been recognized.
    - Click **Write**.
    - If you are challenged for credentials, enter the password of the current user.

You should see a progress indicator as the image is copied to the SD card. It can take quite a while, depending on OS size and throughput. 

### Prepare an SD card on Windows
If you only have access to a Windows system Install the *Win 32 disk imager* from https://sourceforge.net/projects/win32diskimager/

There is now a port of **``rpi-imager``** to Windows. See: https://downloads.raspberrypi.org/imager/imager_latest.exe

## Connect the hardware

For the initial setup, a keyboard, monitor and mouse are needed. You can access the Internet using either Wi-Fi or with an Ethernet cable.

To connect all the computer hardware, perform the following steps:

- Plug the micro-SD card into the back underside of the RasPi.
- If you have wired ethernet, plug it in to the RJ-45 connector on the RasPi.
- Connect the mouse and keyboard to the USB slots.
- Connect the monitor to the RasPi with an appropriate micro-HDMI cable.  The RasPi 4 two micro HDMI ports - only the left one sends output at boot time.
- If you have a USB drive with music files on it, plug it in to a USB slot.
- Now that all the other hardware is connected, plug the 5v power supply with a USB-C end into the RasPi 4. An official RasPi power supply is recommended to avoid *undervoltage* warnings.  If you have an inline switch, turn it on.

## Install and configure Linux

To install and configure Ubuntu Desktop Linux, perform the following sections.

- Boot the RasPi
- Initial Ubuntu Desktop configuration -or- Initial Raspbian Desktop configuration
- Install the SSH server
- Start a terminal or SSH session
- Update and upgrade your system

### Boot the RasPi

When you supply power to the RasPi, it should start booting.  On the top, back, left side of a RasPi 4 there are two LEDs:

- The LED to the left should glow solid red. This signifies it has 5V DC power.
- The LED to the right should flicker green. This signifies that there is communicaiton with the CPU. If there is a red light, but no green one, it's likely the micro-SD card does not have Linux properly installed.

The RasPi 5 has a single LED that blinks both red and green.

- For Ubuntu, you should see a rainbow colored splash screen on the monitor, then the Ubuntu desktop should initialize.
- For Raspberry Pi OS, you should see a red raspberries at the top of the screen.

### Initial Ubuntu Desktop configuration

If you are installing RasPi OS, skip to the next section.

A welcome screen should open on the monitor. Perform the following steps:

- On the *Welcome* window, choose your language and click **Continue**.
- On the *Keyboard layout* window, choose your layout and click **Continue**.
- On the *Wireless* window, if you are not using a hard-wired Ethernet, click **Connect** and configure a Wi-Fi network. You must know the network SSID and will probably be prompted for a password.
- On the *Where are you?* window, choose your time zone.
- On the *Who are you?* window, set the following values:
    - Set your name.
    - Set your computer’s name (host name).
    - For a user name and password ``pi`` is recommended as it is documented in the reminder of this document.
    - For the last option, **Log in automatically** is recommended.
    - Click **Continue**.
 - The install process will take a number of minutes configuring and will reboot the computer.
 - When the system finishes rebooting, an *Online Accounts* window should appear. Click **Skip**.
 - Click **Next** at the *Enable Ubuntu Pro* window.
 - Choose an option on the *Help Improve Ubuntu* window and click **Next**.
 - Click **Next** at the *Privacy* window.
 - Click **Done** at the *Ready to go* window.

- Right click on the desktop and select ``Open in terminal``.  A command prompt should open
- At the command prompt type ``ip a`` - check the IP address of ``wlan0``.
- Install the OpenSSH server:

```
sudo apt-get install -y openssh-server
```

- Enable SSH to start at boot time:

```
sudo systemctl enable ssh
```

- Reboot the new system

```
sudo reboot 
```

Ubuntu Desktop 24.10 should now be installed.
 
### Initial RasPi OS Lite configuration

To install and configure RasPi OS Lite, perform the following steps:

- At the *Configuring Keyboard* panel, choose your keyboard.
- At the *Enter a user name* panel - enter ``pi``. 
- Enter a password for ``pi`` twice.
- You will be prompted to login - enter the credentials for ``pi``.
- Type ``sudo raspi-config`` and perform the following configurations:
  - Select **5 Localisation Options**.
    - Select **L2 Timezone** and choose your time zone.
  - Select **1 System Options**.
    - Select **S1 Wireless LAN** and enter the SSID and password of your WiFi.
    - Select **S4 Hostname** and enter the host name you would like.
  - Tab to the bottom and select **Finish**
  - When prompted to reboot - type **No**
- At the command prompt type ``ip a`` - check the IP address of ``wlan0``.
- At the command prompt type ``sudo sytsemctl enable ssh`` - this will set ``sshd`` to start at boot time. 
- At the command prompt type ``sudo reboot`` - this will restart the Raspberry Pi.

RasPi OS Lite - Debian GNU/Linux 12 (bookworm) should now be installed.

### Start an SSH session
You should now be able to start an SSH session to the IP address or hostname of your new system.
- Login as ``pi``.
- Update and upgrade your system which installs the latest code for all installed packages.
    
```
sudo apt-get update
```
    
```
sudo apt-get upgrade -y
```

## Install and use ovos-tools

The **``ovos-tools``** repo has been developed to help with the installation, configuration, use and testing of the free and open personal voice assistants.

To install **``ovos-tools``** perform the following steps:
  
- Install **``git``** and **``vim``** as they are needed shortly.

```
sudo apt-get install -y git vim
```
    
- Make **``vim``** the default editor.

```
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 100
```
    
- Allow members of the ``sudo`` group to be able to run **``sudo``** commands without a password, by adding **``NOPASSWD:``** to the line near the bottom of the file.

```
sudo visudo
```

```
...
%sudo   ALL=(ALL:ALL) NOPASSWD: ALL
...
```

- Clone the **``ovos-tools``** package in the ``pi`` home directory with the following commands:

```
git clone https://github.com/mike99mac/ovos-tools.git
```
    
- Change to the newly installed directory and run the setup script. It will copy scripts to the directory ``/usr/local/sbin`` which is in the default ``PATH``.

```
cd ovos-tools
sudo ./setup.sh
```
    
The ``ovos-tools`` repo is now installed.
    
### Further customize 

The script ``install1`` configures your system to run OVOS. It runs many commands and thus saves typing, time and possible errors.

- Run ``install1``:
```
time install1
```

### Test the changes

- Test your environment with the newly installed **``lsenv``** script which reports on many aspects of your Linux system.

```
lsenv
```
    
The output should show:

- Neither Neon, OVOS, nor Minimy are installed 
- Neither ``pulseaudio`` nor ``mpd`` are running 
- Useful information such as IP address, CPU temperature, root file system, CPU and memory usage
- None of the file systems frequently written to are mounted as in-memory ``tmpfs`` file systems

Some of the changes made by **``install1``** will not be realized until boot time. To test this, perform the following steps:

- Reboot your system

```
sudo reboot
```
    
- Restart your SSH session when it comes back up.
- Run ``lsenv`` again to see how the environment has changed.
    
You should see these changes:

- **``pulseaudio``** and **``mpd``** are now running.
- The **``/var/log/``** directory is now an in-memory ``tmpfs`` file system.

## Test microphone and speakers

It is important to know your microphone and speakers are working. 
There are scripts in *ovos-tools* named **``testrecord``** and **``testplay``**. 
They are wrappers around the **``arecord``** and **``aplay``** commands designed to make it easier to test recording audio to a file and playing it back on the speaker(s).

- To test your microphone and speakers, issue the following command then speak for up to five seconds. 

```
testrecord
```
    
```
Testing your microphone for 5 seconds - SAY SOMETHING!
INFO: running command: arecord -r 44100  -f S24_LE -d 5 /tmp/test-mic.wav
Recording WAVE '/tmp/test-mic.wav' : Signed 24 bit Little Endian, Rate 44100 Hz, Mono
Calling testplay to play back the recording ...
Playing WAVE '/tmp/test-mic.wav' : Signed 24 bit Little Endian, Rate 44100 Hz, Mono
```
    
You should hear your words played back to you. If you do not, you must debug the issues - there's no sense in going forward without a microphone and speaker(s).

At this point your system should have a solid sound and microphone stack running, especially **``mpd``** and **``pulseaudio``**, and all software necessary to install one of the three personal voice assistants.

If you want to install OVOS, perform the steps in the next section. 
If you want to install Neon, perform the steps in section after that.
If you want to install Minimy, go to https://github.com/mike99mac/minimy-mike99mac

## Install and configure OVOS 

Use the *OVOS installer* to install it in a virtual environment.

```
sh -c "curl -s https://raw.githubusercontent.com/OpenVoiceOS/ovos-installer/main/installer.sh -o installer.sh && chmod +x installer.sh && sudo ./installer.sh"
```

Answer questions as they are asked.

- Reboot the system

```
sudo reboot
```

When the installer finishes, OVOS should be running. 

After a reboot, you should notice the prompt ``(ovos)`` showing that you are in a virtual environment.

## Run OVOS 
The scripts **``startovos``** and **``stopovos``** can be used to start and stop processes. 
Each skill and service run as process and use the message bus or file system to synchronize. 
Their output is written to the ``logs/`` directory under the main install directory. 

- Run **``lsenv``** again. You should see two changes:

    - OVOS is now running - the output showing user and system skill processes.
    - The file systems frequently written to are now mounted over in-memory ``tmpfs``'s.

## Install and configure Neon 
The scripts **``installneon``** was written to make it easy to install Neon.  To use it, perform the following steps.
 
- Clone the Neon core repository:

```
git clone https://github.com/NeonGeckoCom/NeonCore
```

- Run ``installneon``:

```
installneon
```

- If the user and group ``docker`` do not exist, they will be created, and the group will be added to the user you are running from. You will see the following messages and will need to start a new shell and run ``installneon`` again.

```
...
Adding docker as a group of pi ...
24-06-26-16-27-17 - Running: sudo gpasswd -a pi docker ...
Adding user pi to group docker
Please start a new shell and run /usr/local/sbin/installneon again ...
...
```

- Reboot the system

```
sudo reboot
```

## The buttons process

The smart boombox model with the RasPi on-board has three pushbuttons on the front panel to allow quick access to *previous track*, *pause/resume*, and *next track* operations. If you hold the middle button for more that two seconds, it does a *stop* function, which also clears the music queue.  A new **``buttons``** system skill traps button presses and sends corresponding messages to the bus.

If you want to add buttons to your enclosure, attach them to the following GPIO pins:

    +-----+--------+-------------------------------+
    | Pin | Label  | Description                   |
    |-----|--------|-------------------------------|
    | 9   | GND    | Ground common to all buttons  |
    | 11  | GPIO17 | Previous track                |
    | 13  | GPIO27 | Pause/resume                  |
    | 15  | GPIO22 | Next track                    |
    +-----+--------+-------------------------------+
    
Here is a source of purchasing pushbuttons: https://www.amazon.com/dp/B09C8C53DM  

**TODO:** On the other boombox model, the computer is a RasPi 400 which is *offboard*, and the GPIO pins are not easily accessible. That will need new code to use the arrow keys on the RasPi 400 for the same function.

# Debugging
Maybe everything will work perfectly the first time, and you won't have to debug (but we know how that goes :))

Following are some debugging resources.

- Many, many debug statements have been added to the code.  In most classes, every function has at least one log statement when in debug mode with the class, the function, and the parameters passed. 

- Log files are in ``$HOME/minimy/logs``.  
    - Show the log files.
   
        **``$ cd $HOME/minimy/logs``**
        
        **``$ ls``**
        
        ``intent.log  media_player.log  skills.log  stt.log  tts.log``
   
    - When Minimy is running, you can watch all the log files get populated in real time with the following command:

        **``tail -f *``**
        
- There is an HTML file with JavaScript code that displays the message bus in real time. If you do not have a Web server running, you must view it from the local host.
    - Start a browser on the box you're installing on and point it to ``file:///home/pi/minimy/display/sysmon.html``
    - You should see all messages written to the message bus and the associated data.
      
- The **``sortlogs``** script - merges and sorts all the log files by timestamp and saves them to ``/tmp``. The merged output is often easier to peruse than the individual files.

    ```
    $ cat sortlogs
    #!/bin/bash
    #
    # sortlogs - merge and sort all log files
    #
    tmpFile="all.logs"
    cd $HOME/minimy/logs
    if [ -f $tmpFile ]; then                   # old one exists
      rm $tmpFile
    fi
    for i in *.log; do                         # copy all log files
      cat $i >> $tmpFile
    done
    outFile="/tmp/logs-`date +\"%F-%T\"`"
    sort $tmpFile > $outFile                   # sort by timestamp
    echo "sorted logs saved to: $outFile"
    ```
	
- The **``stopminimy``** script calls **``sortlogs``** so every time you stop Minimy, there is a new log file copied to ``/tmp/`` which persists across the starting and stopping of Minimy, unlike ``$HOME/minimy/tmp/``.

    ```
	$ stopminimy
	...
    killing process: pi        952424       1 10 16:25 pts/3    00:00:11 python3 framework/services/input/buttons.py ...
    killing process: pi        952425       1  7 16:25 pts/3    00:00:08 python3 framework/services/input/mic.py ...
    sorted logs saved to: /tmp/logs-2023-07-01-16:27:34
    ```
- There's a ``RELEASE-NOTES.md`` and ``TODO.md`` that show a history of the project and a wish list of things to do.
- Google searches, of course ...
- You can email me at mike99mac at gmail.com - can't promise anything, but I will try.

# Reference
These reference sections follow:
- Vocabulary and examples
- Other Documentation

## Vocabulary and examples

In the samples that follow, (words) in parenthesis are the actual words spoken, while {words} in curly brackets become variables populated with the actual words spoken. When (multiple|words|) are separated by vertical bars, any of those can be spoken, and a trailing vertical bar means that word can be omitted.

### Connectivity skill

**TODO:** Finish writing this skill.

Following is the Connectivity skill vocabulary.
 
Following are examples of Connectivity skill requests:

 
### Email skill

Following is the Email skill vocabulary.

```
(compose|create|new|start) email
send email
```

Following are examples of Email skill requests:

- **``start email``**
- ... dialog continues ...
- **``send email``**
 
### Example1 skill

Following is the Example1 skill vocabulary.

``(run|test|execute) example one``
 
Following are examples of Example1 skill requests:
 
- **``run exmple one``**
 
### Help skill

**TODO:** Finish the code for this skill!

Following is the Help skill vocabulary.

Following are examples of Help skill requests:
 
### MPC skill

The MPC skill can:

- Play from your music library
- Play Internet radio stations
- Play Internet music
- Play NPR news
- Create, delete, manage and play playlists (**TODO:** finish this code)
- Perform basic player operations 

Following are the vocabularies for the MPC skill:

- Music library vocabulary:
    ```
    play (track|song|title|) {track} by (artist|band|) {artist}
    play (album|record) {album} by (artist|band) {artist}
    play (any|all|my|random|some|) music 
    play (playlist) {playlist}
    play (genre|johnra) {genre}    
    ```

- Internet radio vocabulary:

    ```
    play (the|) radio
    play music (on the|on my|) radio
    play genre {genre} (on the|on my|) radio
    play station {station} (on the|on my|) radio
    play (the|) (radio|) station {station}
    play (the|) radio (from|from country|from the country) {country}
    play (the|) radio (spoken|) (in|in language|in the language) {language}
    play (another|a different|next) (radio|) station
    (different|next) (radio|) station
    ```  
    
- Internet music vocabulary:

    ```
    play (track|artist|album|) {music} (from|on) (the|) internet
    ```
    
- NPR News vocabulary: 

    ```
    play (NPR|the|) news
    ```
    
- Playlist vocabulary:

    ```
    (create|make) playlist {playlist}
    (delete|remove) playlist {playlist}
    add (track|song|title) {track} to playlist {playlist}
    add (album|record) {album} to playlist {playlist}
    (remove|delete) (track|song|title) {track} from playlist {playlist}
    list (my|) playlists
    what playlists (do i have|are there)
    what are (my|the) playlists
    ```  
    
- Basic player commands vocabulary:

    ```
    previous (song|station|title|track|)
    next (song|station|title|track|)
    pause                               # stop music but maintain queue
    resume
    stop                                # stop music and clear queue
    
    increase volume
    decrease volume
    ```

Following are examples of MPC skill's requests:
- Play track one and only by artist adele.
- Play album abbey road
- Play genre blues on the radio
- Play language german on the radio
- Play track stressed out by artist twenty on pilots
- Play npr news
- Play artist the chainsmokers from the Internet

### Timedate skill

Following is the Timedate skill vocabulary:

```
what time (is it|)
what (is|) (today's|) date
what day (of the week|) (is it|)
```

Following are examples of  skill's requests:

- What time is it?
- What is today's date
- What day of the week is it
 
### Weather skill

Following is the Weather skill vocabulary:

```
(what's|what is) (the|) weather (forecast|)
```
 
Following are examples of Weather skill requests:

- What's the weather?

### Wiki skill

The Wiki skill is a fallback skill. As such it does not have a vocabulary

**TODO:** Add ``Ask wikipedia {question}``

## More documentation

There is more documentation, by the original author Ken Smith, here: https://github.com/ken-mycroft/minimy/tree/main/doc

# Installing and running faster-whisper

Trying to install ``faster-whisper`` on a Raspberry Pi 5.
 
Mike Gray's writeup on how to do this is here:  https://blog.graywind.org/posts/fasterwhisper-stt-server-script/

To prepare for the install:

- Reflashed RasPiOS onto a micro-SD card and installed Linux.
- Reinstalled ovos-tools from https://github.com/mike99mac/ovos-tools
- Ran ``install1`` from ovos-tools.

To install it, perform the following steps.

- Get Mike Gray's script:

```
cd 
wget https://gist.githubusercontent.com/mikejgray/a7067743a3c50ed74f05a401fa6bb9ce/raw/73f9b87082573017d8c486f42d43eecd8181982c/fasterwhisper-setup.sh
```

- Copy to ``/usr/local/sbin``:

```
sudo cp fasterwhisper-setup.sh  /usr/local/sbin
cd /usr/local/sbin
sudo chown pi.pi fasterwhisper-setup.sh
chmod +x fasterwhisper-setup.sh
```

- Run it and save output:

```
fasterwhisper-setup.sh | tee $HOME/fasterwhisper-setup.out
```

- Make it a service and set it to run at boot time:

```
sudo cp ~/ovos-stt-server.service /etc/systemd/system/ovos-stt-server.service
sudo systemctl daemon-reload
sudo systemctl enable ovos-stt-server.service
```

- Start the service:

```
sudo systemctl start ovos-stt-server.service
```

- Test playing a sample audio file in the ``ovos-tools`` directory. It is an 11 second excerpt from a speech by John F. Kennedy.

```
aplay /home/pi/ovos-tools/jfk.wav
```

- Send the sample audio file to the flask Web server using the IP address and port 8080:

```
curl -X POST -H "Content-Type: audio/wav" -i --data-binary -F data="/home/pi/ovos-tools/jfk.wav" http://192.168.1.102:8080/stt
$ curl -X POST -H "Content-Type: audio/wav" -i --data-binary -F data="/home/pi/ovos-tools/jfk.wav" http://192.168.1.102:8080/stt
curl: (3) URL using bad/illegal format or missing URL
HTTP/1.1 500 INTERNAL SERVER ERROR
Server: Werkzeug/3.0.3 Python/3.11.2
Date: Sun, 02 Jun 2024 17:55:16 GMT
Content-Type: text/html; charset=utf-8
Content-Length: 265
Connection: close

<!doctype html>
<html lang=en>
<title>500 Internal Server Error</title>
<h1>Internal Server Error</h1>
<p>The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.</p>
```

Here is the output from the ``flask`` Web server:

```
Traceback (most recent call last):
  File "/home/pi/STT_venv/lib/python3.11/site-packages/flask/app.py", line 1473, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/pi/STT_venv/lib/python3.11/site-packages/flask/app.py", line 882, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/pi/STT_venv/lib/python3.11/site-packages/flask/app.py", line 880, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/pi/STT_venv/lib/python3.11/site-packages/flask/app.py", line 865, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/pi/STT_venv/lib/python3.11/site-packages/ovos_stt_http_server/__init__.py", line 34, in get_stt
    with AudioFile(fp.name) as source:
  File "/home/pi/STT_venv/lib/python3.11/site-packages/speech_recognition/__init__.py", line 274, in __enter__
    raise ValueError("Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format")
ValueError: Audio file could not be read as PCM WAV, AIFF/AIFF-C, or Native FLAC; check if file is corrupted or in another format
192.168.1.102 - - [02/Jun/2024 13:55:16] "POST /stt HTTP/1.1" 500 -
```

- I tried installing flac, restarting flask and sending the request again - same result :((

```
sudo apt-get install flac
```

