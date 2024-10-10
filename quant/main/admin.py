from django.contrib import admin
from .models import cnn_news_model,bbc_news_model,yahoo_news_model

admin.site.register(cnn_news_model)
admin.site.register(bbc_news_model)
admin.site.register(yahoo_news_model)