# Discord Radio Effects Bot

This is simple script i made in python to add effects to discord channels for RP servers. Its not perfect you are more than welcome to contribute.

### Usage

`.join` - Joins the bot to the server
`.leave` - Makes the bot leave
- Setup hot keys to mute and unmute to activate sound effects
- Disable default Discord sound effects


### Features

- Customizable radio effects on mute and unmute
- join and un-join commands

### Requirements
Python 3

PIP

discord.py

discord.py[voice]

python-dotenv

ffmpeg.exe [LINK](https://ffmpeg.org/download.html#build-windows "LINK")

Radio Effects of your choice [(Link to the ones i used)](https://www.lcpdfr.com/downloads/gta5mods/audio/10897-motorola-mdc1200-mic-clicks/# "(Link to the ones i used)")

### Installation 
`pip install -U discord.py`

`pip install -U discord.py[voice]`

`pip install -U python-dotenv`

place FFMPEG.exe and the audio files into the root folder (if using different audio files update the script with correct names)

### Discord Integration
- Go to the developer portal and create a new applicaiton
https://discord.com/developers/applications

- Go to bots and add bot

- Create a username and click copy token

- Create .env file and add `DISCORD_TOKEN="YOURTOKEN"`

- Replace YOURTOKEN with token from dev portal and save .env file

- Go to OAuth2, select BOT scope and copy the link.

- Paste the link into your browser and invite the bot to your server.

### Starting the bot

`phython main.py`

