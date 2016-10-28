from lsl_processor.lsl_processor import LslProcessor
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
