import connect4aboukarr

def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_input():
    inp = connect4aboukarr.player0_coord()
    assert inp == 6

if __name__ == "__main__":
    test_sum()
    test_input()
    print("Everything passed")


