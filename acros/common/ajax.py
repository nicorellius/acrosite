import json

from django.http import HttpResponse

class AjaxResponseMixin(object):
    
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    
    def render_to_json_response(self, context, **response_kwargs):
        
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json'
        
        return HttpResponse(data, **response_kwargs)

    def form_invalid(self, form):
        
        print('inside form_invalid function')
        
        response = super(AjaxResponseMixin, self).form_invalid(form)
        
        if self.request.is_ajax():
            return self.render_to_json_response(form.errors, status=400)
        
        else:
            return response

    def form_valid(self, form):
        
        print('inside form_valid function')
        
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        
        response = super(AjaxResponseMixin, self).form_valid(form)
        
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            
            return self.render_to_json_response(data)
        
        else:
            return response