import functools
import pyrostep
from pyrogram import Client, filters
from pyrogram.types import Message

from example_handler import create_new_app, run_app

# Create Client
# Example: app = Client("pyrostep", api_id=0000000, api_hash="xxxxxxxxxxxxxxxx", bot_token="0000:xxxxxx")
app = create_new_app()

# Example username and password
USERNAME = "aWolver"
PASSWORD = "AW12"

# Handle /start
@app.on_message(filters.command("start"))
async def handle_start(client: Client, message: Message) -> None:
    await client.send_message(message.from_user.id, "Hello, send /signin to signin account.")

# Handle /cancel
@app.on_message(filters.command("cancel"))
async def cancel_func(client: Client, message: Message) -> None:
    await pyrostep.unregister_steps(message.from_user.id)

# Handle /signin
@app.on_message(filters.command("signin"))
async def handle_1(client: Client, message: Message) -> None:
    await pyrostep.ask(message, handle_2, "send username ( /cancel for cancel ):")

# get username
async def handle_2(client: Client, message: Message) -> None:
    username = message.text
    await pyrostep.ask(message, functools.partial(handle_3, username=username), "send password ( /cancel for cancel ):")

# get password
async def handle_3(client: Client, message: Message, username="") -> None:
    password = message.text

    print(username, password)

    try:
        if username != USERNAME or password != PASSWORD:
            return await message.reply_text("invalid username or password.")
    
        return await message.reply_text("successfuly signin.")
    finally:
        await pyrostep.unregister_steps(message.from_user.id)

# set step listener after all
pyrostep.set_step_listener(app)


# Run Client
run_app(app)
