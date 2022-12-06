from django.db import models

class PostOwner(models.Model):
    username = models.CharField(max_length=256,unique=True,primary_key=True)
    followers = models.IntegerField()
    total_post = models.IntegerField()

    def __str__(self):
        return f"{self.username} (followers: {self.followers}, total_post: {self.total_post})"

class Post(models.Model):
    shortcode = models.CharField(max_length=256,unique=True,primary_key=True)
    owner = models.ForeignKey("PostOwner", on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=256)
    img_url = models.CharField(max_length=700)
    caption = models.CharField(max_length=1200, blank=True, null=True)
    product_name = models.CharField(max_length=256, blank=True, null=True)
    product_label = models.CharField(max_length=256, blank=True, null=True)
    product_category = models.CharField(max_length=256, blank=True, null=True)
    seller_username = models.CharField(max_length=256, blank=True, null=True)
    seller_phonenumber = models.CharField(max_length=256, blank=True, null=True)
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
    video_url = models.CharField(max_length=700, blank=True, null=True)

    def __str__(self):
        return str(self.post) + " " + str(self.sidecard_len)

class ProfileAnalytic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey("PostOwner", on_delete=models.CASCADE)
    followers = models.IntegerField()
    total_post = models.IntegerField()

    def __str__(self):
        return f"{self.created.strftime('%Y-%m-%d_%T')} {self.profile.username} ({self.profile.followers}/{self.profile.total_post})"

class ScrapingHistory(models.Model):
    scraping_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey("PostOwner", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)