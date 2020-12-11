import src.main as main

def test_play_Y():
    wantToPlay = main.play("Y")
    assert wantToPlay

def test_play_N():
    wantToPlay = main.play("N")
    assert not wantToPlay

