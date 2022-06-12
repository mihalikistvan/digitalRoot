from main import *

def test():
    assert digital_root(16) == 7 
    assert digital_root(942) == 6 
    assert digital_root(132189) == 6 
    assert digital_root(493193) == 2 
    assert digital_root(195) == 6 
    assert digital_root(992) == 2 
    assert digital_root(999999999999) == 9 
    assert digital_root(167346) == 9 
    assert digital_root(10) == 1 
    assert digital_root(0) == 0 