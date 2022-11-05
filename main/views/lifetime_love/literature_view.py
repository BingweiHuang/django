import json

from django.core import serializers

from main.models import Literature

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

def change_type(byte):
    if isinstance(byte,bytes):
        return str(byte,encoding="utf-8")
    return json.JSONEncoder.default(byte)

class LiteratureView(APIView):
    # permission_classes = ([IsAuthenticated])


    def get(self, request):
        lit_id = int(request.GET.get('lit_id', 1))

        lit = Literature.objects.filter(lit_id=lit_id)

        print()


        # lit.lit_id
        # lit.lit_detail
        # lit.lit_category
        # lit.lit_ch_title
        # lit.lit_en_title
        # lit.lit_img_address
        # lit.lit_published_date
        # lit.lit_read_times
        # lit.author.fig_birthday
        # lit.author.fig_id
        # lit.author.fig_city
        # lit.author.fig_county
        # lit.author.fig_detail
        # lit.author.fig_ch_name
        # lit.author.fig_day_correction
        # lit.author.fig_deathday
        # lit.author.fig_en_name
        # lit.author.fig_gender
        # lit.author.fig_nationality
        # lit.author.fig_province


        # return Response({
        #     'lit_id': lit.lit_id,
        #     'lit_detail': lit.lit_detail,
        #     'lit_category': lit.lit_category,
        #     'lit_ch_title': lit.lit_ch_title,
        #     'lit_en_title': lit.lit_en_title,
        #     'lit_img_address': lit.lit_img_address,
        #     'lit_published_date': lit.lit_published_date,
        #     'lit_read_times': lit.lit_read_times,
        # })

        return Response({

        })