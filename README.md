# How to run the project?
1. Login to server
```
ssh username@hostname
```
2. Install Docker
```
snap install docker
```
3. Clone the repo 
```
clone https://github.com/ntungufhadzeni/dr-bot.git
```

4. Run Dockerfile
```
cd dr-bot
docker build -t dr-bot .
docker run -p 5050:50 dr-bot 
```

5. Open Twilio account and enter container url to Twilio 
"A Message Comes In" "Webhook"
```angular2html
http://ip-address:5050/sms
```

7. Text "Hi" to your Twilio number.

# Note ⚠️
- This repo is being under development

# LICENSE
- Feel free to use this, I have no objections.
