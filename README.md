# Discord-Cog-Template 🔗

> `NOTE 📝:` This is a discord.py v2 cog template with a command and slash command


# Table of Contents
- [Features](#features)
- [Bot Usage](#bot-usage)
- [Commands](#commands)
  - [Dice Command](#dice-command)
  - [Dice Slash Command](#dice-slash-command)
- [Installation](#installation)
- [Configuration](#configuration)
- [Showcase](#showcase)


## Features

- **Dice command** a command / slash command to roll a 6 sided dice

## Bot Usage
To use this bot, follow these steps: 
+ set up a bot on https://discord.com/developers/applications
+ get your bot token and put the token in the token.txt
+ Invite the bot to your Discord server 
+ Run the bot by putting your token in the `"token.txt"`, no other characters



## Commands

### Dice Command

- **Description:** Roll a dice with 6 sides
- **Usage:** `.roll` 



### Dice Slash Command

- **Description:** Roll a cube with 6 sides
- **Usage:** `/roll`

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TrapstarJannik/Discord-Cog-Template
    ```
   ```sh
   cd Discord-Cog-Template
   ```
   ```sh
   pip install -r requirements.txt
   ```


2. Run the bot:
   ```sh
   python main.py
   ```
   
> [!IMPORTANT]
> You need to put your token in the `config.json` or you will get an error!

## Configuration

- The bot's prefix is set to `.` by default. You can change it in the `config.json` file.
- add your discord bot token in the `config.json` by replacing the first line.

## Showcase
+ **This is a example how to run every cog in a specific folder (extentions)**
```python
# cogs loading
async def main():
    async with bot:
        for filename in os.listdir('./extensions'): 
            if filename.endswith('.py'): 
                await bot.load_extension(f'extensions.{filename[:-3]}')
        await bot.start(TOKEN) 

# run main.py
if __name__ == '__main__':
    asyncio.run(main())
```


+ **In discord.py V2 you need to async def the setup function and await the bot.add_cog**
```python
# setup function
async def setup(bot):
    await bot.add_cog(Dice(bot))
```








