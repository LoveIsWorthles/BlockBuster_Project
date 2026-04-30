from django.db import models


class Slider(models.Model):
    image_src = models.CharField(max_length=200, null=True, blank=True, default="")
    image_width = models.IntegerField(null=True, blank=True, default=0)
    image_height = models.IntegerField(null=True, blank=True, default=0)
    anchor_url = models.CharField(max_length=200, null=True, blank=True, default="")
    movie_genre = models.CharField(max_length=50, null=True, blank=True, default="")
    movie_title = models.CharField(max_length=100, null=True, blank=True, default="")
    lower_rating = models.CharField(max_length=5, null=True, blank=True, default="")
    upper_rating = models.CharField(max_length=5, null=True, blank=True, default="")

    def __str__(self):
        return str(self.movie_title)


class MovieTheater(models.Model):
    type = models.CharField(max_length=20, null=True, blank=True)
    img_src = models.CharField(max_length=200, null=True, blank=True)
    img_width = models.IntegerField(null=True, blank=True)
    img_height = models.IntegerField(null=True, blank=True)
    anchor_url = models.CharField(max_length=200, null=True, blank=True)
    movie_genre = models.CharField(max_length=50, null=True, blank=True)
    movie_title = models.CharField(max_length=100, null=True, blank=True)
    lower_rating = models.CharField(max_length=5, null=True, blank=True)
    upper_rating = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return str(self.movie_title)


class MovieTV(models.Model):
    type = models.CharField(max_length=20, null=True, blank=True)
    img_src = models.CharField(max_length=200, null=True, blank=True)
    img_width = models.IntegerField(null=True, blank=True)
    img_height = models.IntegerField(null=True, blank=True)
    anchor_url = models.CharField(max_length=200, null=True, blank=True)
    movie_genre = models.CharField(max_length=50, null=True, blank=True)
    movie_title = models.CharField(max_length=100, null=True, blank=True)
    lower_rating = models.CharField(max_length=5, null=True, blank=True)
    upper_rating = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return str(self.movie_title)


class Trailer(models.Model):
    trailer_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.trailer_url)


class TrailerItem(models.Model):
    img_src = models.CharField(max_length=200, null=True, blank=True)
    img_alt = models.CharField(max_length=100, null=True, blank=True)
    img_width = models.IntegerField(null=True, blank=True)
    img_height = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return str(self.description)


class News(models.Model):
    section = models.CharField(max_length=50, null=True, blank=True)
    img_src = models.CharField(max_length=200, null=True, blank=True)
    img_alt = models.CharField(max_length=100, null=True, blank=True)
    img_width = models.IntegerField(null=True, blank=True)
    img_height = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.title)


class Tweet(models.Model):
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.content)


class Celebrity(models.Model):
    anchor_url = models.CharField(max_length=200, null=True, blank=True)
    img_width = models.IntegerField(null=True, blank=True)
    img_height = models.IntegerField(null=True, blank=True)
    celebrity_url = models.CharField(max_length=200, null=True, blank=True)
    celebrity_name = models.CharField(max_length=100, null=True, blank=True)
    celebrity_type = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return str(self.celebrity_name)


class Advertisement(models.Model):
    section = models.CharField(max_length=20, null=True, blank=True)
    img_src = models.CharField(max_length=200, null=True, blank=True)
    img_width = models.IntegerField(null=True, blank=True)
    img_height = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.section)


class SocialLink(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    anchor_class = models.CharField(max_length=2, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    icon_class = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)