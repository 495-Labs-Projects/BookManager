import factory
from books.models import *
from django.utils import timezone


class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    first_name = "John"
    last_name = "Smith"


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = "Pearson"

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = "Cool Story"
    year_published = timezone.now().year

    # Sub Factories are used for One to Many relationships
    publisher = factory.SubFactory(PublisherFactory)

    # There's nothing sepcifically built in for Many to Many relationships
    # authors is a function instead of just a attribute and is called after the book is generated
    # All it does is goes through the list of authors and adds it to the book's authors list
    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for author in extracted:
                self.authors.add(author)
