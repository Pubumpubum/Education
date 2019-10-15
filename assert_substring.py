def test_substring(full_string, substring):
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"


full_string = 'five'
substring = 'eight'

print(test_substring(full_string, substring))
