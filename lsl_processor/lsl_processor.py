from sys import argv as argument_vector, exit as system_exit

from pypeg2 import Keyword, Enum, attr, K, blank, name, Namespace, word, endl
from pypeg2 import optional, maybe_some, indent, csl, List


class Type(Keyword):
    grammar = Enum(K('int'), K('long'))


class Parameter:
    grammar = attr('typing', Type), blank, name()


class Parameters(Namespace):
    grammar = optional(csl(Parameter))


class Instruction(str):
    def heading(self, parser):
        """
        Method may not be static.
        """
        return '/* on level ' + str(parser.indention_level) + ' */', endl

    grammar = heading, word, ';', endl


block = '{', endl, maybe_some(indent(Instruction)), '}', endl


class Function(List):
    grammar = attr('typing', Type), blank, name(), '(', Parameters, ')', endl, block


class Event(List):
    grammar = name(), '(', Parameters, ')', endl, block


class Events(Namespace):
    grammar = optional(csl(Event))


class State(List):
    grammar = name(), '{', Events, '}', endl


class States(Namespace):
    grammar = maybe_some(State)


class Script():
    grammar = maybe_some(States)


class LslProcessor:
    def __init__(self, arguments: list) -> None:
        pass

    @staticmethod
    def main():
        application = LslProcessor(argument_vector[1:])
        exit_code = application.run()
        system_exit(exit_code)

    @staticmethod
    def run() -> int:
        exit_code = 0
        return exit_code
