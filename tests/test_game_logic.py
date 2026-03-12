from logic_utils import check_guess, parse_guess

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


# --- Submit logic chain tests (covers the Enter-to-submit fix) ---
# These simulate what happens inside `if submit:` in app.py:
# parse_guess() runs first, then check_guess() — the full path triggered on form submit.

def test_parse_guess_valid_integer():
    # A normal number string should parse successfully
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_empty_string():
    # Pressing Enter on an empty input box should return an error, not crash
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_none():
    # None input (no input submitted) should return an error gracefully
    ok, value, err = parse_guess(None)
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_non_numeric():
    # Typing letters should return an error, not crash
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err is not None

def test_parse_guess_decimal_truncates():
    # Decimal input should be truncated to int, not rejected
    ok, value, err = parse_guess("7.9")
    assert ok is True
    assert value == 7
    assert err is None

def test_submit_valid_guess_reaches_check_guess():
    # Simulates a valid form submission: parse succeeds, then check_guess runs
    ok, guess_int, _ = parse_guess("42")
    assert ok is True
    outcome, message = check_guess(guess_int, 50)
    assert outcome in ("Win", "Too High", "Too Low")
    assert message is not None

def test_submit_invalid_guess_never_reaches_check_guess():
    # Simulates submitting a non-number: parse fails, check_guess should NOT be called
    ok, guess_int, _ = parse_guess("abc")
    assert ok is False
    # check_guess is only called if ok is True — this confirms the gate works
    assert guess_int is None

def test_submit_empty_guess_never_reaches_check_guess():
    # Simulates pressing Enter on an empty form: parse fails, check_guess skipped
    ok, guess_int, _ = parse_guess("")
    assert ok is False
    assert guess_int is None
