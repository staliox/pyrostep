from pyrostep import steps, connection
from example_handler import get_client, run_client

from pyrogram import Client, filters, types

connection.session_max_retries(2)
connection.connection_max_retries(2)

app = get_client() # type: Client

# account username/password
USERNAME = "awolver"
PASSWORD = "p@ssw0rd"


@app.on_message(filters.command("start"))
async def starthandler(_, message: types.Message) -> None:
    await message.reply_text(
        "Welcome! Use keyboards:",
        reply_markup=types.InlineKeyboardMarkup([
            [types.InlineKeyboardButton("Sign In", "sign-in")]
        ])
    )

@app.on_callback_query()
async def CallbackHandler(_, query: types.CallbackQuery) -> None:

    if query.data == "sign-in":
        await query.edit_message_text(
            "Send Your Username?"
        )
        steps.register_next_step(query.from_user.id, handle_sign_in)

    await query.answer()

async def handle_sign_in(_, message: types.Message) -> None:
    
    user_username = message.text
    user_password: types.Message = await steps.ask_wait(
        app, message.chat.id, "Send Your Password?", user_id=message.from_user.id,
    )

    if (user_username != USERNAME) or (user_password.text != PASSWORD):
        await message.reply_text(
            "Username or password is invalid ..."
        )
    
    else:
        await message.reply_text(
            "Successfuly sign-in. Welcome."
        )

# run client ..
steps.listen(app)
run_client()
