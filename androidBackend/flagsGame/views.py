from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse
from .models import DublinFlags

# Import the serializers
from .serializers import DublinFlagsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView

class FlagsList(ListAPIView):

        queryset = DublinFlags.objects.all()
        serializer_class = DublinFlagsSerializer




# def allFlags(request):
#     all_flags = DublinFlags.objects.all()
#
#     # all_flags = {"positions": [[53.267685, -6.119695],
#     #              [53.268288, -6.115382],
#     #              [53.270912, -6.120339],
#     #              [53.269751, -6.121927],
#     #              [53.308807, -6.215731],
#     #              [53.309126, -6.219639],
#     #              [53.307005, -6.222331],
#     #              [53.308125, -6.223103],
#     #              [53.309266, -6.225442],
#     #              [53.308960, -6.222579],
#     #              [53.307646, -6.226012],
#     #              [53.308043, -6.230304],
#     #              [53.309832, -6.229102],
#     #              [53.311056, -6.224049],
#     #              [53.307542, -6.217093],
#     #              [53.305920, -6.217340],
#     #              [53.305067, -6.219411],
#     #              [53.304682, -6.221407],
#     #              [53.302994, -6.219692],
#     #              [53.306535, -6.228262],
#     #              [53.308567, -6.226857],
#     #              [53.307069, -6.219542]]}
#
#     return HttpResponse(json.dumps(all_flags))

