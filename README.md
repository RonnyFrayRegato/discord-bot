# discord-bot

![Continuous Integration](https://github.com/RonnyFrayRegato/discord-bot/actions/workflows/ci.yml/badge.svg)

This repository is the final project for the course CNT 4104: Software Project in Computer Networks.
The project creates a Discord bot that performs several types of functionalities.
The project uses MariaDB as the database. A continuous integration (CI) pipeline automatically builds and tests
the project on every commit to the repository utilizing GitHub Actions. The following are the current functionalities of
the Discord bot:

## Functionalities

- Basic Functions:
  - Hello Command: Displays a greeting to the user
  - Ping Command: Pings the user and displays server latency
  - 8-Ball Command: A fun, interactive game that provides a response based on user input
  - Shutdown Command: Remotely shuts down the Discord bot
  - Mycount Command: Replies to the user's message with the number of messages that the user has sent to the server since they joined.
- Event Functions:
  - On member joining: Discord bot greets new user joining the server
  - On member leaving: Discord bot gives a farewell message to user leaving the server
- Moderation Functions:
  - Kick Command: Kicks a user from the server by passing a user object as a parameter. Can optionally provide a reason for the kick. 
  - Ban Command: Bans a user from the server by passing a user object as a parameter. Can optionally provide a reason for the ban. 
  - Clear Command: Purges a chat channel of a number of messages based on an amount specified by the user. Defaults to 5 messages purged if no amount is specified. 
- Web-Scraping:
  - Image Command: Searches Google Images via a link, clicks on the first image result, and acquires the source image link to paste onto the Discord server.

## Getting Started

### Prerequisites
- [**Docker**](https://docs.docker.com/get-docker/): Used to create and configure MariaDB database container
- MariaDB database set up on either your local machine or a remote host
- Python Version 3.10
- [**Selenium**](https://www.selenium.dev/Selenium): Used for browser automation and web-scraping
- [**Google Chrome**](https://www.google.com/chrome/): The webdriver browser type chosen for web-scraping
  - Must use the latest version of Google Chrome to be compatible with the webdriver
- [**Pillow**](https://pypi.org/project/Pillow/): Support for opening, manipulating, and saving many different image file formats.

### MariaDB Set Up

Generate a MariaDB Docker container and create the database instance for the Discord bot:
 ```
 docker run -d -p 3306:3306 -e MYSQL_DATABASE=DB_NAME -e MYSQL_ROOT_PASSWORD=ROOT_PW --name mdb103 mariadb:10.3
 ```
 
 ### Starting the Bot
 - Clone the repository
 - Use the [**invitation link**](https://discord.com/oauth2/authorize?client_id=1029964028602241075&permissions=8&scope=bot%20applications.commands) to invite the Discord bot to your server of choice
- Acquire Discord token
  - Go to the [**Discord Developer Portal**](https://discord.com/developers/applications) and create a new application
  - Retrieve application token from settings
  - Pass the token securely as an argument to the `discord-bot.sh`
- Start `discord-bot.sh` script by running:
```
./discord-bot.sh
```
 
## Demonstration

![discord-bot](https://user-images.githubusercontent.com/71354370/202879000-b2af02d8-916e-4ad3-9ad0-35fa4952ae29.gif)
