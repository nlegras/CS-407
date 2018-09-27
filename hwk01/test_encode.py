from encode import encode


def test_empty_string():
	assert encode("") == ""

def test_non_repeating_string():
	assert encode("a") == "a1"
	assert encode("zzz") == "z3"

def test_solution():
	assert encode("aabbbccccddddd") == "a2b3c4d5"
	assert encode("zzzzzyyyyxxxww") == "z5y4x3w2"
