import graphene

import forms.schema


class Query(forms.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)