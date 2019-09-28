import graphene

from graphene_django.types import DjangoObjectType

from testApp.models import Testmodel


class testType(DjangoObjectType):
    class Meta:
        model = Testmodel
        
class Query(object):
    test = graphene.Field(testType, id=graphene.Int(), album=graphene.String(), song=graphene.String(), artist=graphene.String())
    all_test = graphene.List(testType)

    def resolve_all_test(self, info, **kwargs):
        return Testmodel.objects.all()

    def resolve_test(self, info, **kwargs):
        id = kwargs.get('id')
        album = kwargs.get('album')
        song = kwargs.get('song')
        artist = kwargs.get('artist')

        if id is not None:
            return Testmodel.objects.get(pk=id)

        if album is not None:
            return Testmodel.objects.get(album=album)
            
        if song is not None:
            return Testmodel.objects.get(song=song)

        if artist is not None:
            return Testmodel.objects.get(artist=artist)

        return None

   #create
class CreateTest(graphene.Mutation):
    id = graphene.Int()
    album = graphene.String()
    artist = graphene.String()
    song = graphene.String()

    class Arguments:
        album = graphene.String()
        artist = graphene.String()
        song = graphene.String()

    def mutate(self, info, album, artist, song):
        test = Testmodel(album=album, artist=artist, song=song)
        test.save()

        return CreateTest(
            id=test.id,
            album=test.album,
            artist=test.artist,
            song=test.song,
        )


#4
class Mutation(graphene.ObjectType):
    create_test = CreateTest.Field()