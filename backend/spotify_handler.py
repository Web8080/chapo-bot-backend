import time

class SpotifyHandler:
    def __init__(self, player):
        self.player = player

    def try_play_song(self, song_name):
        print(f"🎵 Trying to play: {song_name}")
        success = self.player.play_song(song_name)
        retries = 0

        while not success and retries < 2:
            print("⚠️ No active device detected. Asking user to open Spotify...")
            print("🔄 Waiting 5 seconds before retrying...")
            time.sleep(5)
            success = self.player.play_song(song_name)
            retries += 1

        if not success:
            print("❌ Still no active device after retries.")
            return False
        
        print("✅ Successfully started playing!")
        return True

    def prompt_user_to_open_spotify(self):
        print("🔊 Chapo: I couldn't find an active device.")
        print("📱 Please open Spotify on your phone, laptop, or TV.")
        print("▶️ Start playing any song for a few seconds, then say 'try again'.")

    def safe_play_song(self, song_name):
        success = self.try_play_song(song_name)
        if not success:
            self.prompt_user_to_open_spotify()
            return "❌ Failed to play song. Please start a song on your device and try again."
        return f"🎶 Now playing: {song_name}!"
