from django.contrib.sitemaps import Sitemap
from connect.models import Question, Answer


class PostSitemap(Sitemap):
    def items(self):
        return Question.objects.all()  # Replace with your actual query for posts

    def items(self):
        return Answer.objects.all()
