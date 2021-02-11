# ===============================================
# sample test, to test pytest run in Azure DevOps
# ===============================================

from pytest import fixture

# Let's have some function
def say_hello_to(name='World'):
    return f'Hello {name}!'


# We define here the fixture in the test file:
"""Some data for our tests."""
@fixture
def names():
    return 'Bob', '', None, 123, [], ()

# Now the test can run like this, to test many different formats at once (defined in the fixture function):
def test_say_hello_to(names):
    assert say_hello_to('Stefan') == 'Hello Stefan!'

    bob, empty, none, integer, li, tup = names

    assert say_hello_to(bob) == 'Hello Bob!'
    assert say_hello_to(empty) == 'Hello !'
    assert say_hello_to(none) == 'Hello None!'
    assert say_hello_to(integer) == 'Hello 123!'
    assert say_hello_to(li) == 'Hello []!'
    assert say_hello_to(tup) == 'Hello ()!'
