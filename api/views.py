from proof.models import Proof, Statement
from rest_framework import viewsets
from .serializers import ProofSerializer, StatementSerializer

class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer

class ProofViewSet(viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer


