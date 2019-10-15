def test_substring(full_string, substring):
    assert if substring in full_string, \
        f"expected '{substring}' to be substring of '{full_string}'"


full_string = 'fulltext some_value'
substring = 'some_value'

print(test_substring(full_string, substring))