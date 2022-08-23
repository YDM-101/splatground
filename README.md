# splatground

### Desktop background automation synced with the Splatoon 2 API.

Make your desktop background stay fresh! Configure your desktop to show the stages currently in rotation.

This software will be updated when the Splatoon 3 API releases to work with that also.

## Installation
This software is still in development, so there are quite a lot of rough edges especially during installation, where you will have to configure settings (requires knowledge of how path names work). Questions are welcomed here in github or on my corresponding youtube video (link ???), especially if there is an error or if help is needed.

### Requirements
- Python 3.7+ (3.5, 3.6 may work too)
- [appscript 1.2.0](https://pypi.org/project/appscript/)
- (Only tested to work on my Mac, which runs MacOS Version 12.2)

A way to automatically install requirements is in planning, but has many blockers, so it's still a long way away.

For now, here are a few guides to install the requirements.

First, install Python:
https://docs.python-guide.org/starting/install3/osx/

Afterwards, with the Terminal still open, install appscript with `pip install appscript`

### Installation - Configuration
After downloading this repo, you will need to configure some details to help it work on your local machine. Warning: this is not an user-friendly step (I will try to fix some of the design in future versions).

Step 1: Go to line 3 of the file `splatground.sh` and replace the file path there (the stuff after `cd`) with the full path of this folder on your computer.
One way to get the full path of this folder is to go to the folder in Finder, right click the folder and then click 'Get Info', then right click the third line under 'General' of the window that pops up. Click 'Copy as Pathname'. This would be something like `/Users/YDM101/Documents`. Add the name of this folder (e.g. `/splatground` to the end of that, to get the full path (e.g. `/Users/YDM101/Documents/splatground`).

Step 2: Go to line 1 of the file `config.txt` and replace the first line with the full path of this folder (same full path as above, e.g. `/Users/YDM101/Documents/splatground`).

After Step 2, if you would like to use the software directly, you can open the Terminal, go inside this folder, and use the command `sh splatground.sh`.

Step 3: Configure the software to launch when the computer is turned on. Open System Preferences, go to Users & Groups, click Login Items, press the + (plus) button. Navigate to this folder, click the file `splatground.sh`, and click 'Add'. Next time you turn on your computer, the software will start running. (You can restart your computer to get it running immediately)

## What you can try
There are two major settings right now, both in the `config.txt` file: 
  1) Time between image switches: The software cycles through the images
  2) Mode: You can choose between 'turf war', 'ranked', and 'league'.

You can also add or remove images to the folders in the `sample_bg` folder. However, each folder in the `sample_bg` folder must have at least one image.

You can also use another folder with your own images, however, the folder must contain 23 folders with the full names of the stages (Ancho-V Games, Arowana Mall, etc), and each folder must contain at least one image. If you do so, replace line 2 of `config.txt` with the name of your folder.

## Limitations and Bugs
The terminal window will be open, so the software knows when to switch the backgrounds. Note that the software will not take up CPU when it is waiting, only when it is switching the desktop background. This may be annoying. I am trying to find a way to make it invisible involving Automator shell script flows.
Only for Mac. I welcome any contributors who would like to make Windows or Linux versions.
Also, running the software long term at a sub-second refresh rate will cause your computer to overheat (although running it at splattershot speed (0.1) or n-zap speed (0.0833) is fun to watch)

## Author's notes
I made this last month -- shortly after I got the game in June 2022. Originally it was intended to only be used by me, and to release a public version I had to streamline the installation and configuration process as much as possible, but there is still a lot to do in that aspect.

