from instaloader import Instaloader, Profile, Post
from decouple import config

L = Instaloader()
L.login(
    config("IG_USERNAME"),
    config("IG_PASSWORD")
)