from django.http import JsonResponse

# def result(code = 200,message = '',data = None):
#     json_dict = {'code': code, 'message': message, 'data': data}
#     return JsonResponse(json_dict)

# def show_success(data):
#     return result(200,'success',data)
#
# def show_error(code,message):
#     return result(code,message)
#
# def page_not_found(code = 404 ,message = 'action not found.' ,data = None):
#     return result(code, message, data)
#
# def params(request,key,tmp = None):
#     require = tmp == None
#     param = request.POST.get(key)
#     print(require)
#     if param == None:
#         if require == True:
#             print(1)
#             error(1001, key + ' is required.')
#
#         else:
#             param = tmp
#     return param


class HttpCode(object):
    success = 0
    error = 1


def result(code=HttpCode.success, message='', data=None, kwargs=None):
    json_dict = {'data': data, 'code': code, 'message': message}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})


def success(data=None):
    return result(code=HttpCode.success, message='OK', data=data)


def error(message='', data=None):
    return result(code=HttpCode.error, message=message, data=data)



