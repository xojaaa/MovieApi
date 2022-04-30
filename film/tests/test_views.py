from django.test import TestCase, Client

from film.models import Actor, Movie


class TestMovieSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test Movie', imdb=1, year=2021)
        self.movie2 = Movie.objects.create(name='Test Movie2', imdb=10, year=1987)
        self.movie3 = Movie.objects.create(name='Test Movie3', imdb=7, year=1985)
        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 3)
        self.assertIsNotNone(data[0]['id'])
        self.assertEquals(data[0]['name'], 'Test Movie')

    def test_search(self):
        response = self.client.get('/movies/?search=Test')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 3)
        self.assertEquals(data[0]['name'], 'Test Movie')

    def test_ordering(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data

        self.assertEquals(len(data), 3)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data[0]['id'])

