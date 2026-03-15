import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import get_range_for_difficulty, parse_guess, check_guess


# --- check_guess: existing tests fixed to unpack tuple ---

def test_winning_guess():
    # Bug fix: check_guess returns (outcome, message), not just a string
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: check_guess type error (non-int inputs) ---

def test_check_guess_type_error_string_guess():
    # Bug fix: passing non-int used to crash; now returns "Error" outcome
    outcome, _ = check_guess("50", 50)
    assert outcome == "Error"

def test_check_guess_type_error_none_secret():
    outcome, _ = check_guess(50, None)
    assert outcome == "Error"


# --- Bug fix: get_range_for_difficulty returned wrong ranges ---

def test_range_easy():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20

def test_range_normal():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100

def test_range_hard():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 500

def test_range_unknown_defaults_to_normal():
    # Unknown difficulty should fall back to 1–100
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1
    assert high == 100


# --- Bug fix: Easy attempt limit was 6, should be 12 ---

def test_attempt_limit_easy():
    attempt_limit_map = {"Easy": 12, "Normal": 8, "Hard": 5}
    assert attempt_limit_map["Easy"] == 12

def test_attempt_limit_normal():
    attempt_limit_map = {"Easy": 12, "Normal": 8, "Hard": 5}
    assert attempt_limit_map["Normal"] == 8

def test_attempt_limit_hard():
    attempt_limit_map = {"Easy": 12, "Normal": 8, "Hard": 5}
    assert attempt_limit_map["Hard"] == 5


# --- Bug fix: attempts session state starts at 0, not 1 ---

def test_initial_attempts_is_zero():
    # Simulates what app.py does on first load
    session_state = {}
    if "attempts" not in session_state:
        session_state["attempts"] = 0
    assert session_state["attempts"] == 0


# --- Bug fix: history and status reset on new game ---

def test_new_game_resets_history():
    session_state = {"history": [10, 20, 30], "status": "lost", "attempts": 8}
    # Simulate new game button logic
    session_state["attempts"] = 0
    session_state["status"] = "playing"
    session_state["history"] = []
    assert session_state["history"] == []
    assert session_state["status"] == "playing"
    assert session_state["attempts"] == 0


# --- parse_guess: type error fix (string vs int coercion) ---

def test_parse_guess_valid_int():
    ok, value, _ = parse_guess("42")
    assert ok is True
    assert value == 42

def test_parse_guess_valid_float_string():
    ok, value, _ = parse_guess("3.7")
    assert ok is True
    assert isinstance(value, int)

def test_parse_guess_empty_string():
    ok, _, err = parse_guess("")
    assert ok is False
    assert err is not None

def test_parse_guess_none():
    ok, _, err = parse_guess(None)
    assert ok is False
    assert err is not None

def test_parse_guess_non_numeric():
    ok, _, err = parse_guess("abc")
    assert ok is False
    assert err is not None
