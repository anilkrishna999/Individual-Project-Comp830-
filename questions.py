from constants import GameActions


class Question:
    def __init__(self, question):
        self.question = question
        self.yes = None
        self.no = None

    def add_yes(self, question):
        self.yes = question

    def get_yes(self, question):
        return self.yes

    def add_no(self, question):
        self.no = question

    def get_no(self, question):
        return self.no

    def get_question(self):
        return self.question


def build_questions() -> Question:
    q1 = Question(
        "Welcome to the game! Think of a design pattern and answer these following yes/no questions. Ready?")
    q2 = Question(
        "Does it provide the object creation mechanism that enhance the flexibilities of the existing code?")
    q3 = Question(
        "Does it ensure you have at most one instance of a class in your application?")
    q4 = Question("Is it Singleton pattern? ")
    q5 = Question("Is it Builder Pattern?")
    q6 = Question(
        "Is it responsible for how one class communicates with others?")
    q7 = Question(
        "Does it provide a mechanism to the context to change its behaviour?")
    q8 = Question("Is changing behaviour built into its scheme?")
    q9 = Question("Is it State Pattern?")
    q10 = Question("Is it Strategy Pattern?")
    q11 = Question(
        "Does it allow a group of objects to be notifies when some state changes?")
    q12 = Question("Is it Observer Pattern?")
    q13 = Question("Is it Command Pattern?")
    q14 = Question(
        "Does it explain how to assemble objects and classes into a larger structure and simplifies the structure by identifying the relationships?")
    q15 = Question(
        "Does it attach additional behaviour to an object dynamically at run-time?")
    q16 = Question("Is it Decorator Pattern?")
    q17 = Question("Is it Adapter Pattern?")
    q18 = Question("Woohoo! I guessed it! Try again?")
    q19 = Question("OOPs! Something went wrong! Try again?")

    # load q1 yes/no's
    q1.add_yes(q2)
    q1.add_no(GameActions.END_GAME)
    # load q2 yes/no's
    q2.add_yes(q3)
    q2.add_no(q6)
    # load q3 yes/no's
    q3.add_yes(q4)
    q3.add_no(q5)
    # load q4 yes/no's
    q4.add_yes(q18)
    q4.add_no(q19)
    # load q5 yes/no's
    q5.add_yes(q18)
    q5.add_no(q19)
    # load q6 yes/no's
    q6.add_yes(q7)
    q6.add_no(q14)
    # load q7 yes/no's
    q7.add_yes(q8)
    q7.add_no(q11)
    # load q8 yes/no's
    q8.add_yes(q9)
    q8.add_no(q10)
    # load q9 yes/no's
    q9.add_yes(q18)
    q9.add_no(q19)
    # load q10 yes/no's
    q10.add_yes(q18)
    q10.add_no(q19)
    # load q11 yes/no's
    q11.add_yes(q12)
    q11.add_no(q13)
    # load q12 yes/no's
    q12.add_yes(q18)
    q12.add_no(q19)
    # load q13 yes/no's
    q13.add_yes(q18)
    q13.add_no(q19)
    # load q14 yes/no's
    q14.add_yes(q15)
    q14.add_no(q19)
    # load q15 yes/no's
    q15.add_yes(q16)
    q15.add_no(q17)
    # load q16 yes/no's
    q16.add_yes(q18)
    q16.add_no(q19)
    # load q17 yes/no's
    q17.add_yes(q18)
    q17.add_no(q19)
    # load q18 yes/no's
    q18.add_yes(GameActions.START_OVER)
    q18.add_no(GameActions.END_GAME)
    # load q19 yes/no's
    q19.add_yes(GameActions.START_OVER)
    q19.add_no(GameActions.END_GAME)

    return q1


def question_input_error():
    raise Exception("Wrongly added questions")
