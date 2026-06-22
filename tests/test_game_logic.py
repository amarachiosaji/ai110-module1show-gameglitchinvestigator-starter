from logic_utils import check_guess, update_score


def test_winning_guess():
    # check_guess returns a TUPLE: (outcome, message). We unpack it.
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # Guess 60 vs secret 50 -> too high
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    # Your fix: "Too High" should now tell the player to go LOWER
    assert "LOWER" in message


def test_guess_too_low():
    # Guess 40 vs secret 50 -> too low
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    # Your fix: "Too Low" should now tell the player to go HIGHER
    assert "HIGHER" in message


def test_score_never_goes_negative():
    # Your fix: a wrong guess subtracts 5 but floors at 0
    # Starting at 0, a wrong guess should stay at 0 (not -5)
    assert update_score(0, "Too High", 1) == 0


def test_score_decreases_on_wrong_guess():
    # Starting at 100, a wrong guess drops to 95
    assert update_score(100, "Too Low", 1) == 95