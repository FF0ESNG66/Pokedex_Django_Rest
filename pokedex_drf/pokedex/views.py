from .models import Pokedex
from .serializers import PokedexSerializer, PokedexUpdateSerializer
from rest_framework import generics
from api.authentication import CustomAuthentication
from api.permissions import UserPermissions, AllDenied, AllowAnyAuthenticated
from . import client
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView



# GET (List)  &  POST
class PokedexListCreateView(generics.ListCreateAPIView):
    serializer_class = PokedexSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [UserPermissions]
    
    def get_queryset(self):
        return Pokedex.objects.all().order_by('pokedex_num')


pokedex_list_create_view = PokedexListCreateView.as_view()



# GET (Detail)
class PokedexDetailView(generics.RetrieveAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [UserPermissions]
    lookup_url_kwarg = 'name'
    lookup_field = 'name__iexact'

pokedex_detail_views = PokedexDetailView.as_view()

# · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 
#  - Note -
# lookup_url_kwarg -> Will look for the kwarg defined. These kwargs are defined in the URL pattern that I wrote in urls.py
#                     so it is looking for (in this case) <str:name>. And that value will be searched in the field defined in lookup_field (name)
# · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · · 

# PUT (Update)
class PokedexUpdateView(generics.UpdateAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexUpdateSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [AllDenied]
    lookup_url_kwarg = 'name'
    lookup_field = 'name__iexact'

pokedex_update_view = PokedexUpdateView.as_view()



# DELETE (Destroy)
class PokedexDestroyView(generics.DestroyAPIView):
    queryset = Pokedex.objects.all()
    serializer_class = PokedexSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [AllDenied]
    lookup_url_kwarg = 'name'
    lookup_field = 'name__iexact'

pokedex_destroy_view = PokedexDestroyView.as_view()



# Algolia Search

class PokedexSearchView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [AllowAnyAuthenticated]
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        if not query:
             return Response({'error': 'A valid query parameter ("q") is required.'}, status=status.HTTP_400_BAD_REQUEST)
        results = client.perform_search(query)
        return Response({"hits":results})
    
# pokedex_search_view = PokedexSearchView.as_view()