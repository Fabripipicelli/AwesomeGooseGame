from game import Game

def test_game_has_two_players():
    game = Game(player1="Nick", player2="Bob")
    assert game.get_player1_name() and game.get_player2_name()

def test_is_over():
    game = Game(player1="Nick", player2="Bob")
    assert game.is_over() == False

def test_rolling_dice_moves_players():
    game = Game(player1='Nack', player2 = "Bub")
    assert game.get_player1_space()==None
    assert game.get_player2_space()==None
    game.roll_dice()
    dice = game.get_last_dice_roll()
    assert game.get_player2_space() == None
    assert game.get_player1_space() == dice[0] + dice[1]

