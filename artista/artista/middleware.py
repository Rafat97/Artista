class MainMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print(get_response)
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print(response)
        # Code to be executed for each request/response after
        # the view is called.

        return response
    def process_request(self, request):
        print("process_request")
        pass
    def process_view(self,request, view_func, view_args, view_kwargs):
        print("process_view")
        pass
        
    def process_exception(self,request, exception):
        print("process_exception")
        pass

    def process_template_response(self,request, response):
        print("process_template_response")
        pass    
