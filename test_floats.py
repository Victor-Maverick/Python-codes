import floats
def test_floats():
	assert floats.only_floats(12.1, 1.3) == 2
	assert floats.only_floats(1, 1) == 0
	assert floats.only_floats(1.3, 3) == 1