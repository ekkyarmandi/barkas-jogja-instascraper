from instaloader import Instaloader, Profile
from itertools import dropwhile, takewhile
from datetime import datetime, timedelta
from decouple import config

from crud import insert

L = Instaloader()
L.login(
    config("IG_USERNAME"),
    config("IG_PASSWORD")
)

targets = [
    "infobarkas_jogja",
    # "barkasjogja24jam",
    # "promobarkas",
]

today = datetime.today()
a_week_ago = today - timedelta(days=7)

### Iterate profile post for the last 7 days
for target in targets:
    barkas = Profile.from_username(L.context,target)
    for post in takewhile(lambda p: p.date > today, dropwhile(lambda p: p.date > a_week_ago, barkas.get_posts())):
        ### Insert post data into the database
        ### skip post video and empty caption for now
        pass