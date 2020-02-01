import graphene
from graphene_django import DjangoObjectType

from .models import Form


class FormType(DjangoObjectType):
    class Meta:
        model = Form


class Query(graphene.ObjectType):
    forms = graphene.List(FormType)

    def resolve_forms(self, info, **kwargs):
        return Form.objects.all()