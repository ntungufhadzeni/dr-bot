from service import create_bot
from train import train_with_csv, train_with_corpus

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# create the bot
chatbot = create_bot()

# train
train_with_corpus(chatbot, 'chatterbot.corpus.english')
train_with_csv(chatbot, 'data/mental_health_faq.csv')


@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    user_text = request.form['Body']

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message

    resp.message(str(chatbot.get_response(user_text)))

    return str(resp)


if __name__ == "__main__":
    app.run()
