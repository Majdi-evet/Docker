import graphene
import graphql_jwt
import testApp.schema
import users.schema


class Query(testApp.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)

class Mutation(users.schema.Mutation, testApp.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
   

schema = graphene.Schema(query=Query, mutation=Mutation)