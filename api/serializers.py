from proof.models import Proof, Statement
from rest_framework import serializers

class StatementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statement
        fields = ('id',
                  'input_string',) 

class ProofSerializer(serializers.HyperlinkedModelSerializer):
    statements = serializers.ListField(child=serializers.CharField())
    reasons = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Proof
        fields = ('id',
                  'title',
                  'prove', 
                  'given',
                  'diagram',
                  'plan',        
                  'statements', 
                  'reasons',
                          )

