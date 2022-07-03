import functools
import random
import pyrostep
from pyrogram import Client, filters
from pyrogram.types import Message

from example_handler import create_new_app, run_app

# Create Client
# Example: app = Client("pyrostep", api_id=0000000, api_hash="xxxxxxxxxxxxxxxx", bot_token="0000:xxxxxx")
app = create_new_app()

@app.on_message(filters.command("start"))
async def handle_1(c: Client, m: Message) -> None:
    num = random.randrange(1, 11)

    await pyrostep.ask(
        m, functools.partial(handle_2, num=num), "Send me a number from 1 to 10",
    )

@pyrostep.end_step()
async def handle_2(c: Client, m: Message, num: int = 0) -> None:
    if m.text == str(num):
        await c.send_message(m.from_user.id, "You win ...")
    
    else:
        await c.send_message(m.from_user.id, "You lose, number is %d." % num)

# set step listener after all
pyrostep.set_step_listener(app)


# Run Client
run_app(app)
