from django.db import models

class cnn_news_model(models.Model):
    title = models.CharField(max_length= 100)
    summary = models.CharField(max_length= 100)
    url = models.CharField(max_length= 1000)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class bbc_news_model(models.Model):
    title = models.CharField(max_length= 100)
    summary = models.CharField(max_length= 100)
    url = models.CharField(max_length= 1000)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class yahoo_news_model(models.Model):
    title = models.CharField(max_length= 100)
    summary = models.CharField(max_length= 100)
    url = models.CharField(max_length= 1000)
    content = models.TextField()

    def __str__(self):
        return self.title