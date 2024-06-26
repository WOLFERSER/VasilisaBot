# Discord Voice Channel Management Bot

This is a Discord bot designed to manage voice channels. It moves users to designated channels when they join specific voice channels and sends notifications to a text channel.

## Features

- Automatically move users to specific voice channels when they join certain channels.
- Send a notification to a text channel when a user is moved.
- Notify specific roles when a user joins a voice channel and is moved.

## Prerequisites

- Python 3.8 or higher
- `nextcord` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/WOLFERSER/VasilisaBot.git
    cd yourrepository
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install nextcord
    ```

## Configuration

1. Replace the placeholders for voice channel IDs, text channel ID, and role IDs with your actual channel and role IDs in the code.
2. Replace `"TOKEN BOT"` with your actual bot token.

## Usage

1. Run the bot:

    ```sh
    python bot.py
    ```

2. The bot will print "Bot is ready!" when it is successfully connected to your Discord server.

## Code

Here is the complete code for the bot:

    ```python
    import nextcord
    from nextcord.ext import commands

    bot = commands.Bot(command_prefix="!")

    @bot.event
    async def on_ready():
        print("Bot is ready!")

    @bot.event
    async def on_voice_state_update(member, before, after):
        # Define the voice channels
        channel_1_1 = bot.get_channel(1232224266116796487)  # Replace with the ID of the first voice channel 1
        channel_1_2 = bot.get_channel(1232227608482287627)  # Replace with the ID of the second voice channel 1
        channel_1_3 = bot.get_channel(1232227736995758080)  # Replace with the ID of the third voice channel 1
        channel_1_4 = bot.get_channel(1232227845158342727)  # Replace with the ID of the fourth voice channel 1
        channel_1_5 = bot.get_channel(1234567894)  # Replace with the ID of the fifth voice channel 1
        channel_2_1 = bot.get_channel(1230252315789885470)  # Replace with the ID of the first voice channel 2
        channel_2_2 = bot.get_channel(1230253246577381507)  # Replace with the ID of the second voice channel 2
        channel_2_3 = bot.get_channel(1230253628284076173)  # Replace with the ID of the third voice channel 2
        channel_2_4 = bot.get_channel(1230254248860586084)  # Replace with the ID of the fourth voice channel 2
        channel_2_5 = bot.get_channel(1234567899)  # Replace with the ID of the fifth voice channel 2
        text_channel = bot.get_channel(1231671571467210824)  # Replace with the ID of the text channel

        # Check if the member joined any of the channel_1 channels
        if before.channel is None and after.channel is not None:
            if after.channel == channel_1_1:
                await member.move_to(channel_2_1)
                await text_channel.send(
                    f"<@&1230251912037798059>, {member.mention} созывает всех в {channel_2_1.mention}!"
                )
            elif after.channel == channel_1_2:
                await member.move_to(channel_2_2)
                await text_channel.send(
                    f"<@&1230253265225257123>, {member.mention} созывает всех в {channel_2_2.mention}!"
                )
            elif after.channel == channel_1_3:
                await member.move_to(channel_2_3)
                await text_channel.send(
                    f"<@&1230253601314574337>, {member.mention} созывает всех в {channel_2_3.mention}!"
                )
            elif after.channel == channel_1_4:
                await member.move_to(channel_2_4)
                await text_channel.send(
                    f"<@&1230254395178876949>, {member.mention} созывает всех в {channel_2_4.mention}!"
                )
            elif after.channel == channel_1_5:
                await member.move_to(channel_2_5)
                await text_channel.send(
                    f"{member.mention} joined {channel_1_5.mention} and was moved to {channel_2_5.mention}!"
                )

    bot.run("TOKEN BOT")
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Please feel free to submit issues and pull requests for any improvements or features you would like to see!

## Acknowledgments

- Thanks to the contributors of the `nextcord` library for making this project possible.
