from django.conf import settings
from django.db import models

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.related_name
# The related_name attribute specifies the name of the reverse relation
# from the User model back to your model.
class Snippet(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        # related_name = 'snippet_set'
        # <이 클래스명의 소문자화_set>
    )
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField(default='')

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        `pygment` 라이브러리가 code snippet의 highlighted HTML 표현식을 만들어준다.
        :param args:
        :param kwargs:
        :return:
        """
        lexer = get_lexer_by_name(self.language)

        linenos = 'table' if self.linenos else False
        # linenos = self.linenos and 'table' or False

        options = {'title': self.title} if self.title else {}
        # options = self.title and {'title': self.title} or False

        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
