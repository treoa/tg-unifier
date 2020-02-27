from pyrogram import Filters, Client
from configs import *
from typing import List

with Client("my app", api_hash=api_hash, api_id=api_id, phone_number=phone_number) as app:
    app.send_message("me", "Greetings from MEEEEEEE")


def dialogs_iteartion ():
    for dialog in app.iter_dialogs():
        if dialog.chat.type == 'channel':
            print(f"{dialog.chat.title}   ///   {dialog.chat.id}   ///   {dialog.chat.username}   ///   {dialog.chat.type}\n\n")


def chat_identifier ():
    pass


@app.on_message(Filters.channel)
def handling(client, message):
    dialogs_iteartion()
    if message is not None:
        app.forward_messages(chat_id="me", from_chat_id=message.chat.id, message_ids=message.message_id, as_copy=False)
    else:
        app.send_message("me", f"The message is not reachable by address {message.chat.username or message.chat.title}")


app.run()
