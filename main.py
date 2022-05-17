# python3

from constants import GameActions
from game import Game
from questions import Question, build_questions


def main():
    firstQuestion = build_questions()
    game = Game(firstQuestion)
    game.start()
    game = None


if __name__ == "__main__":
    main()
