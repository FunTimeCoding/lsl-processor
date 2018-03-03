from pypeg2 import parse, comment_c

from lsl_processor.lsl_processor import LslProcessor, States, Events
from mccabe import main as mccabe_main


def test_return_code() -> None:
    application = LslProcessor([])
    assert application.run() == 0


def test_flake_command(capsys) -> None:
    mccabe_main()
    actual_output, actual_error = capsys.readouterr()
    expected_error = ''
    assert expected_error == actual_error
    empty_output = ''
    assert empty_output != actual_output


def test_read_file() -> None:
    file = open('tests/fixture/example.lsl')
    things = parse(file.read().strip(), States, comment=comment_c)
    print(things)


def test_a_state() -> None:
    text = 'default{}'
    things = parse(text, States, comment=comment_c)
    print(things)


def test_multiple_states() -> None:
    text = 'default{} other{}'
    things = parse(text, States, comment=comment_c)
    print(things)


def test_state_with_an_event() -> None:
    text = 'default{ state_entry(){} }'
    things = parse(text, States, comment=comment_c)
    print(things)


def test_state_with_an_event_with_multiple_instructions() -> None:
    text = 'default{ state_entry(){ do_this; do_that; } }'
    things = parse(text, States, comment=comment_c)
    print(things)


def test_a_function_and_state_with_an_event_with_multiple_instructions() \
        -> None:
    text = 'int f(int a, long b) { do_this; do_that; }' \
           ' default{ state_entry(){ do_this; do_that; } }'
    things = parse(text, States, comment=comment_c)
    print(things)


def test_event_with_multiple_instructions() -> None:
    text = 'state_entry(){ do_this; do_that; }'
    things = parse(text, Events, comment=comment_c)
    print(things)


def test_event_with_a_parameter_with_multiple_instructions() -> None:
    text = 'state_entry(int foo){ do_this; do_that; }'
    things = parse(text, Events, comment=comment_c)
    print(things)


def print_verbose_things(things) -> None:
    print(things)
    print(things.name)
    print(things.typing)

    for index, item in enumerate(things):
        print(index, item)
