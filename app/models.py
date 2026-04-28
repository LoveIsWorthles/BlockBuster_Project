from django.db import models


class Slider(models.Model):
    image_src = models.CharField(max_length=200, default="")
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    anchor_url = models.CharField(max_length=200, default="")
    movie_genre = models.CharField(max_length=20, default="")
    movie_title = models.CharField(max_length=100, default="")
    lower_rating = models.CharField(max_length=5, default="")
    upper_rating = models.CharField(max_length=5, default="")

    def __str__(self):
        return self.movie_title


class MovieTheater(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=20)
    movie_title = models.CharField(max_length=100)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title


class MovieTV(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=20)
    movie_title = models.CharField(max_length=100)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)

    def __str__(self):
        return self.movie_title


class Trailer(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class TrailerItem(models.Model):
    trailer = models.ForeignKey(Trailer, on_delete=models.CASCADE, related_name="items")
    img_src = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class News(models.Model):
    section = models.CharField(max_length=50)
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Tweet(models.Model):
    username = models.CharField(max_length=100)
    content = models.TextField()
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Celebrity(models.Model):
    name = models.CharField(max_length=100)
    img_src = models.CharField(max_length=200)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    img_src = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.link


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.name