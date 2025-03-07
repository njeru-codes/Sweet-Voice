# Sweet-Voice
A red-teaming tool using IVR systems to exploit users into handing over  OTP codes


![Sweet-Voice_A red-teaming tool using IVR systems to exploit users into handing over OTP codes(1)](https://github.com/user-attachments/assets/e8e0b282-ff09-428e-a1e3-1728f44add36)

## deployment
- **Prerequisites**<br/>
Before deploying, ensure you have the following installed:
```
- Docker
- Docker-compose
- Python 3.x
- A valid telegram bot token
```
- **setting  environment variables**<br/>
Create a .env file in the root directory and add:
```
TELEGRAM_API_TOKEN="*********"
```

- **deploy using docker** <br/>
build docker image:
```
docker build -t telegram-bot .
```
run docker container:
```
docker run -d --name my_bot --env-file .env telegram-bot
```
the bot will now run in the background.


## usage
- open telegram and search for your bot