from django.shortcuts import render

from django.http import HttpResponse
from django.http import JsonResponse

import json


def index(request):
    return render(request, 'dbutil.html', {})


def covert_query(request):
    payload = request.POST
    db_query = payload['query']
    print(db_query)

    left_char_check = '('
    right_char_check = ')'
    db_q_ary_col = []
    result_json = []

    char_index = db_query.find(left_char_check, 1)

    while char_index > 0:
        end_char_index = db_query.find(right_char_check, char_index + 1)

        if end_char_index < 1:
            break
        if len(db_q_ary_col) == 0:
            db_q_ary_col = db_query[char_index + 1:end_char_index].split(',')
        else:
            dictionary = dict(zip(db_q_ary_col, db_query[char_index + 1:end_char_index].split(',')))
            str_x = '{'
            for key, value in dictionary.items():
                str_x = str_x + "'" + key.strip() + "':" + value.strip() + ','

            str_x = str_x[:-1] + '}'
            str_x = str_x.replace('NULL', 'null').replace('\'', '"')
            result_json.append(json.loads(str_x))

        char_index = db_query.find(left_char_check, end_char_index + 1)

    data = json.dumps(result_json, indent=4)
    return HttpResponse(data, content_type='application/json')
