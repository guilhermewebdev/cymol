import graphene
import graphql_jwt
from graphene_django.debug import DjangoDebug

schema = ""
class ServiceField(graphene.ObjectType):
    sdl = graphene.String()

    def resolve_sdl(parent, _):
        string_schema = str(schema)
        string_schema = string_schema.replace("\n", " ")
        string_schema = string_schema.replace("type Query", "extend type Query")
        string_schema = string_schema.replace("schema {   query: Query   mutation: MutationQuery }", "")
        return string_schema

class Service:
    _service = graphene.Field(ServiceField, name="_service", resolver=lambda x, _: {})

class Query(graphene.ObjectType, Service):
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query, mutation=Mutation)