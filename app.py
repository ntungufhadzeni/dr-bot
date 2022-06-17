from chatbot import chatbot

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)


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
