from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100, default='Nicolas Garlinski')
    date = models.DateTimeField(auto_now_add=True)
    hero_image = models.URLField(blank=True)
    hero_image_alt = models.CharField(max_length=200, blank=True)
    is_new = models.BooleanField(default=False)
    nav_label = models.CharField(max_length=50)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class PostContent(models.Model):
    CONTENT_TYPES = [
        ('lead', 'Lead Paragraph'),
        ('text', 'Text Paragraph'),
        ('image', 'Image'),
        ('blockquote', 'Blockquote'),
    ]

    post = models.ForeignKey(Post, related_name='content', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=CONTENT_TYPES)
    text = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    image_alt = models.CharField(max_length=200, blank=True)
    blockquote_footer = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.post.title} - {self.type} ({self.order})'
