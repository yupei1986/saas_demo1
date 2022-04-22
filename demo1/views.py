from django.http import HttpResponse,JsonResponse
from demo1.models import Person




# Create your views here.
def list1(request):
    """
    首页123123213
    """
  #  return HttpResponse("123123123这是一个测试")

def list(request):
    """
    首页123123213
    """

    qs = Person.objects.values()
    retlist = list(qs)
    print(retlist)
    print('aaa')

    return JsonResponse({'a':'retlist'})