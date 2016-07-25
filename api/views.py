from proof.models import Theorem, Axiom, Definition, Statement, Argument, Book
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import renderers
from latex2mathml.converter import convert
from .serializers import (
                          TheoremSerializer, 
                          AxiomSerializer, 
                          DefinitionSerializer,
                          UserSerializer, 
                          GroupSerializer,
                          StatementSerializer,
                          ArgumentSerializer,
                          BookSerializer,
                  )

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ArgumentViewSet(viewsets.ModelViewSet):
    queryset = Argument.objects.all()
    serializer_class = ArgumentSerializer

class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class StatementHighlight(generics.GenericAPIView):
    queryset = Statement.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)
    def get(self, request, *args, **kwargs):
        statement = self.get_object()
        mathml = convert(statement.name)
        mathml = mathml.replace("<math>", '<math xmlns="http://www.w3.org/1998/Math/MathML">', 1)
        return Response({'name': mathml },template_name="statement.html")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DefinitionHighlight(generics.GenericAPIView):
    queryset = Definition.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        definition = self.get_object()
        return Response({'name': convert("\\sqrt{a}") },template_name="definition.html")


class DefinitionViewSet(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

class TheoremHighlight(generics.GenericAPIView):
    queryset = Theorem.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        theorem = self.get_object()
        return Response({'name': theorem.name },template_name="theorem.html")


class TheoremViewSet(viewsets.ModelViewSet):
    queryset = Theorem.objects.all()
    serializer_class = TheoremSerializer

class AxiomHighlight(generics.GenericAPIView):
    queryset = Axiom.objects.all()
    renderer_classes = (renderers.TemplateHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        axiom= self.get_object()
        return Response({'name': axiom.name },template_name="axiom.html")


class AxiomViewSet(viewsets.ModelViewSet):
    queryset = Axiom.objects.all()
    serializer_class = AxiomSerializer
