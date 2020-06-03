"""Contains command for !minesweeper."""
from discord.ext import commands

from minesweeper import Map


bot = commands.Bot(command_prefix='!')


@bot.command(aliases=["mines", "💣"])
async def minesweeper(ctx, size: int, diff: int):
    mines = Map(size, diff)

    for message in mines.create_mines():
        await ctx.send(message)


if __name__ == '__main__':
    bot.run("to.k.en")
