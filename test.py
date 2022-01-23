import main
def test_add_three():
    assert main.add_three(1,2,3)==6
    assert main.add_three(2,3,4)==9
    assert main.add_three(3,4,5)==12
    assert main.add_three(4,5,6)==15