from encode import encode


def test_empty_string():
	assert encode("") == ""

def test_single_char_string():
	assert encode(input_string) == input_string
