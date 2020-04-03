import graphene
import graphql_jwt
import graphql
from graphene_django.debug import DjangoDebug
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from . import forms

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'last_name',
            'first_name',
            'email',
            'last_login',
            'date_joined',
            'is_active',
            'groups',
        )

class RegistrationInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    first_name = graphene.String(required=True)
    last_name = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)

class Registration(graphene.Mutation):
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, input):
        form = forms.UserForm(data=input)
        if(form.is_valid()):
            user = get_user_model().objects.create_user(**form.cleaned_data)
        else: raise graphql.GraphQLError(
            message=dict(form._errors)
        )
        return Registration(user=user)

    class Arguments:
        input = RegistrationInput(required=True)

schema = ""
class ServiceField(graphene.ObjectType):
    sdl = graphene.String()

    def resolve_sdl(parent, _):
        string_schema = str(schema)
        string_schema = string_schema.replace("\n", " ")
        string_schema = string_schema.replace("type Query", "extend type Query")
        string_schema = string_schema.replace("schema {   query: Query   mutation: MutationQuery }", "")
        return string_schema

class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")
    _service = graphene.Field(ServiceField, name="_service", resolver=lambda x, _: {})
    is_authenticated = graphene.Boolean(
        resolver=lambda x, i: i.context.user.is_authenticated
    )
    me = graphene.Field(UserType, resolver=login_required(lambda _, i: i.context.user))

    def resolve_me(parent, info):
        return info.context.user

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()
    register = Registration.Field()
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query, mutation=Mutation)