from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_hint_says_lower_when_guess_too_high():
    # Bug: hint said "Go HIGHER!" when guess was above secret (should be "Go LOWER!")
    outcome, hint = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in hint, f"Expected hint to say LOWER, got: {hint}"

def test_hint_says_higher_when_guess_too_low():
    # Bug: hint said "Go LOWER!" when guess was below secret (should be "Go HIGHER!")
    outcome, hint = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in hint, f"Expected hint to say HIGHER, got: {hint}"
