class HomeTheaterFacade:
    def __init__(self, tv, audio, dvd, game_console):
        self.tv = tv
        self.audio = audio
        self.dvd = dvd
        self.game_console = game_console

    def watch_movie(self):
        print("\nФильм қарау режимі")
        self.tv.on()
        self.audio.on()
        self.audio.set_volume(15)
        self.dvd.play()

    def end_movie(self):
        print("\nФильм тоқтатылды")
        self.dvd.stop()
        self.audio.off()
        self.tv.off()

    def play_game(self, game):
        print("\nОйын режимі")
        self.tv.on()
        self.audio.on()
        self.game_console.on()
        self.game_console.start_game(game)

    def listen_music(self):
        print("\nМузыка режимі")
        self.tv.on()
        self.audio.on()
        self.audio.set_volume(20)

    def set_volume(self, volume):
        self.audio.set_volume(volume)
