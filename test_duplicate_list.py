import duplicate_list

def test_duplicate_list():
	assert duplicate_list.check_duplicate(['orange', 'mango', 'mango', 'pawpaw']) == 'mango'