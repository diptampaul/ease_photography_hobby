from instagrapi import Client
# https://subzeroid.github.io/instagrapi/usage-guide/media.html
# https://www.youtube.com/watch?v=cW7kMeOUr20

client = Client()
client.login("diptam.paul", "FyyR1234@#4321")

client.photo_upload("maxim-hopman-fiXLQXAhCfk-unsplash.jpg", "Test Upload")