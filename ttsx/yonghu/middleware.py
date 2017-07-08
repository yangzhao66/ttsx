#coding=utf-8
class Urlmiddleware:
    def process_request(self,request):
        if request.path not in ['/user/login_out/','/user/login/','/user/denglu/','/user/commit/','/user/register/']:
        #因为现在没有response  所以不能使用cookie
            request.session['url_path'] = request.get_full_path()
