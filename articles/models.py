from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Article Title")
    category = models.CharField(max_length=100, verbose_name="Category")
    short_content = models.TextField(verbose_name="Short Description")
    long_content = models.TextField(verbose_name="Detailed Content")
    author = models.CharField(max_length=100, verbose_name="Author")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['title']