# test_auth.py
from app_fixed import create_user, login

TEST_USER = "pytest_user"
TEST_PASS = "PyTestPass!234"

def setup_module(module):
    try:
        create_user(TEST_USER, TEST_PASS)
    except Exception:
        pass

def test_login_valid():
    assert login(TEST_USER, TEST_PASS) is not None

def test_login_invalid_password():
    assert login(TEST_USER, "badpassword") is None

def test_sql_injection_attempt_username():
    payload = "' OR '1'='1"
    assert login(payload, "whatever") is None
