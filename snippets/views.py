from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

'''
이 소스코드에서..
값: snippets 하나하나를 의미
'''


@csrf_exempt
def snippet_list(request):
    """
    1. GET: 값에 대한 리스트를 읽어온다
    2. POST: 값을 만든다.
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        # 리스트, 쿼리셋과 같은 여러개의 데이터를 가진 값에 대해 serialise
        # def many_init(cls, *args, **kwargs):
        # 얘까지 타고가면 알 수 있음.
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    1. GET: 특정 값을 가져온다.
    2. PUT: 값을 수정한다.
    3. DELETE: 값을 삭제한다.
    :param request:
    :param pk:
    :return:
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        # 지우고나서 No Content 인거냐?
        return HttpResponse(status=204)
