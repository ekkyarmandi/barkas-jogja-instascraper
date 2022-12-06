from instaloader import Instaloader, Profile
from itertools import dropwhile, takewhile
from datetime import datetime, timedelta
import django

import warnings
warnings.filterwarnings("ignore")

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from instabarkas.models import (
    Post,
    PostOwner,
    PostSideCard,
    ProfileAnalytic,
    ScrapingHistory
)

from func import load_cookies

L = Instaloader()
L.context._session.cookies.update(load_cookies("cookies.json"))

targets = [
    "infobarkas_jogja",
    "barkasjogja24jam",
    "promobarkas",
]

today = datetime.today()
a_week_ago = today - timedelta(days=7)

### Iterate profile post for the last 7 days
for target in targets:
    barkas = Profile.from_username(L.context,target)

    ### Get post owner
    try:
        owner = PostOwner.objects.get(username=target)
        owner.followers = barkas.followers
        owner.total_post = barkas.mediacount
        owner.save()
    except:
        owner = PostOwner.objects.create(
            username=target,
            followers=barkas.followers,
            total_post=barkas.mediacount,
        )

    ### Record ProfileAnalytic
    ProfileAnalytic.objects.create(
        profile=owner,
        followers=owner.followers,
        total_post=owner.total_post
    )

    for post in barkas.get_posts():
        if post.date >= a_week_ago and post.date <= today:

            ### Insert post data into the database
            if (post.caption and post.caption.strip() != "") or not post.is_pinned:
                post_url = f"https://www.instagram.com/p/{post.shortcode}/"
                try:
                    scraped_post = Post.objects.get(shortcode=post.shortcode)
                except:
                    scraped_post = Post.objects.create(
                        shortcode=post.shortcode,
                        url=post_url,
                        img_url=post.url,
                        caption=post.caption,
                        seller_username=",".join(post.caption_mentions),
                        post_date=post.date,
                        likes=post.likes,
                        comments=post.comments,
                        is_video=post.is_video,
                    )
                    if post.typename != "GraphImage":
                        scraped_post.is_single_product = False
                    else:
                        scraped_post.is_single_product = True
                    scraped_post.save()

                    ### Get the PostSideCard object
                    if post.typename == "GraphSidecar":
                        for sidecard in post.get_sidecar_nodes():
                            PostSideCard.objects.create(
                                post=scraped_post,
                                sidecard_len=post.mediacount,
                                display_url=sidecard.display_url,
                                is_video=sidecard.is_video,
                                video_url=sidecard.video_url
                            )

                    ### Records post scraping
                    ScrapingHistory.objects.create(
                        owner=owner,
                        post=scraped_post,
                    )

                print(post_url)
        
        else:
            break