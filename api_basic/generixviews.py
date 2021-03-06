from rest_framework import  generics
from rest_framework import mixins
from .serializers import AricleSerializers
from .models import Aricle


class GenericApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = AricleSerializers
    queryset =Aricle.objects.all()
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retreive(request)
        else:
            return self.list(request)
        return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self, request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)



