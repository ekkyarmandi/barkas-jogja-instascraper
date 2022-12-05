from django.db import models

class PostOwner(models.Model):
    owner_username = models.CharField(max_length=256)
    owner_followers = models.IntegerField()
    owner_total_posts = models.IntegerField()

    def __str__(self):
        return f"{self.owner_username} (followers: {self.owner_followers}, total_post: {self.owner_followers})"

class Post(models.Model):
    post_url = models.CharField(max_length=256)
    shortcode = models.CharField(max_length=256)
    thumbnail_url = models.CharField(max_length=700)
    caption = models.CharField(max_length=1200)
    product_name = models.CharField(max_length=256, blank=True, null=True)
    product_label = models.CharField(max_length=256, blank=True, null=True)
    product_category = models.CharField(max_length=256, blank=True, null=True)
    seller_username = models.CharField(max_length=256, blank=True, null=True)
    post_date = models.DateTimeField()
    price = models.CharField(max_length=256, blank=True, null=True)
    likes = models.IntegerField()
    comments = models.IntegerField()
    is_ads = models.BooleanField(blank=True, null=True)
    is_video = models.BooleanField()
    is_single_product = models.BooleanField(blank=True, null=True)
    is_sold = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.caption

class PostSideCard(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    sidecard_len = models.IntegerField()
    display_url = models.CharField(max_length=256)
    is_video = models.BooleanField()
    video_url = models.CharField(max_length=700)

    def __str__(self):
        return str(self.post) + " " + str(self.sidecard_len)

class ProfileAnalytic(models.Model):
    created = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey("PostOwner", on_delete=models.CASCADE)
    followers = models.IntegerField()
    total_posts = models.IntegerField()

    def __str__(self):
        return self.profil