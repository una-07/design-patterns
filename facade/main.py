from tv import TV
from audio_system import AudioSystem
from dvd_player import DVDPlayer
from game_console import GameConsole
from home_theater import HomeTheaterFacade

tv = TV()
audio = AudioSystem()
dvd = DVDPlayer()
game = GameConsole()

home = HomeTheaterFacade(tv, audio, dvd, game)

home.watch_movie()
home.set_volume(10)
home.end_movie()

home.play_game("FIFA 25")
home.listen_music()
