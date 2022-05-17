# python3

from constants import GameActions
from questions import Question, question_input_error


class Game:
    """ Yes/No question game. It presents a sequence of questions to a user. The sequence changes
    depending on the user's answers to the previous questions.
    """

    def __init__(self, firstQuestion: Question):
        self.firstQuestion = firstQuestion
        self.question = firstQuestion

    def show_question(self, question: str):
        """Displays the question to a user."""
        answer = input(question)
        if(answer == "yes"):
            self.answer_yes()
        elif(answer == "no"):
            self.answer_no()
        else:
            print("Unknown input " + answer)

    def start(self):
        """It's called when a user is ready to play the game.
        Handles the game setup, such as showing the initial question.
        """
        self.show_question(self.question.get_question())

    def end_game(self):
        """Exits the game."""
        print("Ending game...")
        pass

    def answer_yes(self):
        """It's called when a user answers YES to a question.
         Handles the transition to the next question or exits the game.
         """

        if isinstance(self.question.yes, Question):
            self.question = self.question.yes
            self.show_question(self.question.get_question())
        elif isinstance(self.question.yes, GameActions):
            if self.question.yes == GameActions.START_OVER:
                self.question = self.firstQuestion
                self.start()
            elif self.question.yes == GameActions.END_GAME:
                self.end_game()
            else:
                question_input_error()
        else:
            question_input_error()

    def answer_no(self):
        """It's called when a user answers NO to a question.
        Handles the transition to the next question or exits the game.
        """
        if isinstance(self.question.no, Question):
            self.question = self.question.no
            self.show_question(self.question.get_question())
        elif isinstance(self.question.no, GameActions):
            if self.question.no == GameActions.START_OVER:
                self.question = self.firstQuestion
                self.start()
            elif self.question.no == GameActions.END_GAME:
                self.end_game()
            else:
                question_input_error()
        else:
            question_input_error()
