from proof.models import Theorem, Axiom, Definition, Statement, Argument, Book
from rest_framework import serializers
from django.contrib.auth.models import User, Group

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('axioms','definitions','theorems','citation','proofs','user')

class StatementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statement
        fields = ('name', 'statement', 'label','citation','user')


class ArgumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Argument
        fields = ('statement', 'given','prove','diagram',
                  'note','paragraph','statements','reasons','user')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class DefinitionSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='definition-highlight', format='html')
    class Meta:
        model = Definition
        fields = ('id',
                  'name',
                  'statement',
                  'highlight',
                          )


class AxiomSerializer(serializers.HyperlinkedModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='axiom-highlight', format='html')
    class Meta:
        model = Axiom
        fields = ('id',
                  'name',
                  'statement',
                  'highlight',
                          )


class TheoremSerializer(serializers.HyperlinkedModelSerializer):
    statements = serializers.ListField(child=serializers.CharField())
    reasons = serializers.ListField(child=serializers.CharField())
    highlight = serializers.HyperlinkedIdentityField(view_name='theorem-highlight', format='html')
    class Meta:
        model = Theorem
        fields = ('id',
                  'name',
                  'statement',
                  'prove', 
                  'given',
                  'diagram',
                  'plan',        
                  'statements', 
                  'reasons',
                  'highlight',
                          )

