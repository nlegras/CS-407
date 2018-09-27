from encode import encode


def test_empty_string():
	assert encode("") == ""

def test_non_repeating_string():
	# non-repeating strings will always return the input string 
	assert encode("a") == "a"
	assert encode("abc") == "abc"

def test_solution():
	assert encode("aabbbccccddddd") == "a2b3c4d5"
	assert encode("zzzzzyyyyxxxww") == "z5y4x3w2"

def test_case_of_chars():
	assert encode("aAaaaaa") == "a1A1a5"
