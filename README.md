# Pyrostep
A step handler library for pyrogram framework. \
Helps you to step handling ...

> I tried to provide the best speed ...

1. [Installing](#installing)
2. [Usage](#usage)
    - [set_step_listener method](#setsteplistener-method)
    - [use set_step_listener or first_step](#use-setsteplistener-or-firststep)
    - [why use set_step_listener after all decorators](#why-use-setsteplistener-after-all-decorators)
    - [StepHandler](#stephandler-class)
3. [TODO](#todo)
4. [Copyright & License](#license)

# Installing
Can use **pip**:
```bash
pip3 install -U pyrostep
```

Or, Can use **git** (not recommended):
```bash
git clone https://github.com/aWolver/pyrostep && cd pyrostep && python3 setup.py install
```

# Usage
Usage is very easy ... Follow me

> **before learn, You should know that this library only works as async.**

First import `pyrostep`:
```python
import pyrostep
```

`pyrostep` has a decorator named `first_step`, use this for handler which is first step, example:
```python
app = Client(...)
# ...

@app.on_message()
@pyrostep.first_step()
async def step1(cli: Client, msg: Message):
    await msg.reply_text("please send your name:")
    await pyrostep.register_next_step(msg.from_user.id, step2)

# create handler to get name:
async def step2(cli: Client, msg: Message):
    await msg.reply_text("Hello %s!" % msg.text)

    # unregister step2 in end step (don't forget it)
    await pyrostep.unregister_steps(msg.from_user.id)

# ...
```

you can use `ask` method instead of `register_next_step`:

```python
...
async def step1(cli: Client, msg: Message):
    pyrostep.ask(msg, step2, "please send your name:")
...
```

End of this code, you see `unregister_steps` method, you can use `end_step` decorator instead of it:
```python
...
@end_step()
async def step2(cli: Client, msg: Message):
    await msg.reply_text("Hello %s!" % msg.text)
...
```

### set_step_listener method
`first_step` decorator may broken your code, so i recommended use `set_step_listener` instead of `first_step`.

Example:
```python
app = Client(...)
# ...

@app.on_message(filters=filters.command("sayhello"))
async def step1(cli: Client, msg: Message):
    await msg.reply_text("please send your name:")
    await pyrostep.register_next_step(msg.from_user.id, step2)

# create handler to get name:
async def step2(cli: Client, msg: Message):
    await msg.reply_text("Hello %s!" % msg.text)

    # unregister step2 in end step (don't forget it)
    await pyrostep.unregister_steps(msg.from_user.id)

# after all decorators
pyrostep.set_step_listener(app)

# ...
```

**Note: Better you use set_step_listener after all of decorators.**

## Use set_step_listener or first_step?
to answer this, you should know how does `set_step_listener` and `first_step` works.

`first_step` decorator sets middleware on your handler/decorator. checks if this user in listening users or not, if true, call step functions, and if false, call default handler.

`set_step_listener` too. it sets a step listener handler without default decorator.

#### Why use `set_step_listener` after all decorators?
to check the pyrogram as the last method.

> If you want clear all steps for all users, use `clear` method.

### StepHandler *class*

You can use it to have a different steps handler:

```python
from pyrostep import StepHandler

h = StepHandler()
```

It has all of methods you want.

# TODO
- [x] Complete tests
- [x] Add examples
- [ ] Add helper methods

# License
Licensed under the terms of the **GNU Lesser General Public License v2**
