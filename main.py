import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.event
async def on_voice_state_update(member, before, after):
    # Define the voice channels
    channel_1_1 = bot.get_channel(
        1232224266116796487
    )  # Replace with the ID of the first voice channel 1
    channel_1_2 = bot.get_channel(
        1232227608482287627
    )  # Replace with the ID of the second voice channel 1
    channel_1_3 = bot.get_channel(
        1232227736995758080
    )  # Replace with the ID of the third voice channel 1
    channel_1_4 = bot.get_channel(
        1232227845158342727
    )  # Replace with the ID of the fourth voice channel 1
    channel_1_5 = bot.get_channel(
        1234567894
    )  # Replace with the ID of the fifth voice channel 1
    channel_2_1 = bot.get_channel(
        1230252315789885470
    )  # Replace with the ID of the first voice channel 2
    channel_2_2 = bot.get_channel(
        1230253246577381507
    )  # Replace with the ID of the second voice channel 2
    channel_2_3 = bot.get_channel(
        1230253628284076173
    )  # Replace with the ID of the third voice channel 2
    channel_2_4 = bot.get_channel(
        1230254248860586084
    )  # Replace with the ID of the fourth voice channel 2
    channel_2_5 = bot.get_channel(
        1234567899
    )  # Replace with the ID of the fifth voice channel 2
    text_channel = bot.get_channel(
        1231671571467210824
    )  # Replace with the ID of the text channel

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
