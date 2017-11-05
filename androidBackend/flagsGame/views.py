from django.shortcuts import render

# Create your views here.

import json
from django.http import HttpResponse

def allFlags(request):
    all_flags = {"positions": [[53.267685, -6.119695],
                 [53.268288, -6.115382],
                 [53.270912, -6.120339],
                 [53.269751, -6.121927],
                 [53.308807, -6.215731],
                 [53.309126, -6.219639],
                 [53.307005, -6.222331]]}

    return HttpResponse(json.dumps(all_flags))

