# pylint: disable=E0401
import sys

from __init__ import run_ladder_game

# Load bot
from bot import CompetitiveBot

from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer

bot = Bot(Race.Terran, CompetitiveBot())

# Start game
if __name__ == "__main__":
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        result, opponent_id = run_ladder_game(bot)
        print(result, " against opponent ", opponent_id)
    else:
        # Local game
        print("Starting local game...")
        run_game(
            "AbyssalReefLE",
            [bot, Computer(Race.Protoss, Difficulty.VeryHard)],
            realtime=True,
		)
