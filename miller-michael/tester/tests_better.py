# The test function which looks for the functions globally defined as test_

def run_tests():
	results = {"pass": 0, "fail": 0, "error": 0}
	for (name, test) in globals().items():
		if not names.startswith("test_"):
			continue
		try:
			test()
			results["pass"] += 1
		except AssertionError:
			results["fail"] += 1
		except Exception:
			results["error"] += 1
	print(f"pass {results['pass']}")
	print(f"fail {results['fail']}")
	print(f"error {results['error']}")

# This is our sign function

def sign(value):
	if value < 0:
		return -1
	else:
		return 1

# The various needed tests

def test_sign_negative():
	assert sign(-3) == -1


def test_sign_postive():
	assert sign(19) == 1

def test_sign_zero():
	assert sign(0) == 0

def test_sign_error(): # Intentional Typo
	assert sgn(1) == 1

# Run the tests

run_tests()