#!/bin/bash

DISCORD_TOKEN=${1}  # parameter is passed as an env through workflow file

# run the Discord bot
python discord-script.py ${DISCORD_TOKEN}

sleep 60

python discord-script.py exit()
