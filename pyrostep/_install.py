from . import steps
from pyrogram.client import Client

def _register_next_step(_, id, _next, store = None):
    steps.register_next_step(id, _next, store)

def _unregister_next_step(_, id, store = None):
    steps.unregister_steps(id, store)

async def _wait_for(_, id, timeout = None, store = None):
    return await steps.wait_for(id, timeout, store)

def install(
    register_next_step=True, unregister_next_step=True, wait_for=True, listen=True
):
    """
    install adds new functions on pyrogram client.

    Example::

        import pyrostep
        pyrostep.install()

        from pyrogram import Client, idle

        cli = Client()
        cli.listen()
    
    Which functions can be install?
    - register_next_step ( -> pyrogram.Client.register_next_step )
    - unregister_next_step ( -> pyrogram.Client.unregister_next_step )
    - wait_for ( -> pyrogram.Client.wait_for )
    - listen ( -> pyrogram.Client.listen )
    """
    funcs = {
        "register_next_step": (register_next_step, _register_next_step),
        "unregister_next_step": (unregister_next_step, _unregister_next_step),
        "wait_for": (wait_for, _wait_for),
        "listen": (listen, steps.listen),
    }

    for k, v in filter(lambda k: k[1][0] is True, funcs.items()):
        setattr(Client, k, v[1])
    