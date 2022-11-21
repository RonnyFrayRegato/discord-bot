# discord-bot

![CI for Discord Bot](https://github.com/RonnyFrayRegato/discord-bot/actions/workflows/ci.yml/badge.svg)

This repository is the final project for the course CNT 4104: Software Project in Computer Networks.
The project creates a Discord bot that performs several types of functionalities.
The project uses MariaDB as the database. A continuous integration (CI) pipeline automatically builds and tests
the project on every commit to the repository utilizing GitHub Actions. The following are the current functionalities of
the Discord bot:

## Functionalities

- Basic Functions:
  - Hello Command: displays a greeting to the user
  - Ping Command: pings the user and displays server latency
  - 8-Ball Command: a fun, interactive game that provides a response based on user input
  - Shutdown Command: remotely shuts down the Discord bot
- Event Functions:
  - On member joining: Discord bot greets new user joining the server
  - On member leaving: Discord bot gives a farewell message to user leaving the server
- Web-Scraping:
  - Searches the internet and retrieves an image to display in the Discord server

### MariaDB Set Up

Generate a MariaDB Docker Container and Create the Database Instance for the Discord Bot:
 ```
 docker run -d -p 3306:3306 -e MYSQL_DATABASE=DB_NAME -e MYSQL_ROOT_PASSWORD=ROOT_PW --name mdb103 mariadb:10.3
 ```
 
## Demonstration

![discord-bot](https://user-images.githubusercontent.com/71354370/202879000-b2af02d8-916e-4ad3-9ad0-35fa4952ae29.gif)
