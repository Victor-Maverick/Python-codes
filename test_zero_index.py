import zero_index

def test_zero_index():
	assert zero_index.zero([1, 3, 4, 5, 6]) == [0, 3, 4, 5, 0]