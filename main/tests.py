from django.forms import model_to_dict
from django.test import TestCase

from main.models import Literature
from main.models.lifetime_love.models import Category
from main.models.lifetime_love.models import FigureCategory
from main.models.lifetime_love.models import Figure
from django.db.models import Q, OuterRef, Subquery, Sum


class TestCase1(TestCase):
    # qs = Literature.objects.filter(Q(lit_en_title__istartswith='S') | Q(lit_en_title__endswith='E'))
    # qs = Literature.objects.filter(lit_en_title__istartswith='S', lit_category='西方哲学')
    # qs = Literature.objects.filter(lit_id__lt=10)
    # qs = Literature.objects.filter(lit_id__lt=10).values('lit_en_title', 'lit_ch_title') # values之后直接就是json格式
    # qs = Literature.objects.filter(lit_id__lt=10) # values之后直接就是json格式

    # 找到每个作者的最早出版的一本书籍
    qs_book = Literature.objects.filter(fig_id=OuterRef("pk")).order_by("lit_published_date")

    qs = Figure.objects.all().annotate(
        earlyst = Subquery(
            qs_book.values('lit_id')[:1]
        )
    )



    print(qs)


    for lit in qs:
        print(model_to_dict(lit)) # model_to_dict 从model转成json格式
        # print(lit)

    # res = model_to_dict(Literature.objects.get(lit_id=1))
    # print(res)

