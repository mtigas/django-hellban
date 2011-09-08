from random import randint
from time import sleep
from django.http import HttpResponse, Http404

def _is_hellbanned(request):
    # TODO: test against request.user
    
    # TODO: test against IP address
    
    # TODO: other tests (user-agent, etc)
    
    return False

class HellBanMiddleware(object):
    def process_request(self, request):
        if _is_hellbanned(request):
            ban_type = randint(0,4)
            request.hellban = ban_type
            
            if ban_type == 1:
                print "request is being slowbanned"
                sleep(10)
            elif ban_type == 2:
                print "request is getting 404"
                raise Http404
            elif ban_type == 3:
                print "request is being whitescreened"
                return HttpResponse("", mimetype="text/plain")
            elif ban_type == 4:
                print "request is getting error"
                return HttpResponse("500 Internal Server Error", mimetype="text/plain", status=500)
        
    def process_response(self, request, response):
        ban_type = getattr(request, "hellban", 0)
        return response
