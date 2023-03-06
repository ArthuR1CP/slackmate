from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import os
import re
import logging
import socket
from modules import test

logging.basicConfig(level=logging.INFO)


slackmate_app = App(token=os.environ["SLACK_BOT_TOKEN"])


@slackmate_app.event("message")
def handle_message(payload, say):
    chat_message = payload["text"]
    thread_message = payload["ts"] # thread reply
    if re.match(r"\b(hello|hi|hey|salut) slackmate\b", chat_message, re.IGNORECASE):
        say(f"Hi <@{payload['user']}>", thread_ts=thread_message)
    elif re.match(r"\bhow are you\b", chat_message, re.IGNORECASE):
        say("I'm doing great, thanks for asking!",thread_ts=thread_message)
    if re.match(r"\b something other\b", chat_message, re.IGNORECASE):
        text = test.Test("test")
        say(test.test(), thread_ts=thread_message)


@slackmate_app.event("app_mention")
def handle_mention(payload, say):
    thread_message = payload["ts"]
    say(f"Hi <@{payload['user']}>", thread_ts=thread_message)


@slackmate_app.command("/ip")
def handle_ipcommand(ack, body, command):
    try:
        ip = command["text"]
        socket.inet_aton(ip)
        host = socket.gethostbyaddr(ip) 
        response = "IP: {}, Host: {}".format(ip,host[0])
        ack(response)
    except socket.error:
        ack("Invalid IP")


@slackmate_app.command("/host")
def handle_hostcommand(ack, body, command):
    try:
        host = command["text"]
        ip = socket.gethostbyname(host) 
        response = "Host: {}, IP: {}".format(host,ip)
        ack(response)
    except socket.error:
        ack("Invalid Hostname")

if __name__ == "__main__":
    handler = SocketModeHandler(app_token=os.environ["SLACK_APP_TOKEN"], app=slackmate_app)
    handler.start()