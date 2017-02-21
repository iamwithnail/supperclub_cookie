from test_plus.test import TestCase
from django.utils.text import slugify

class test_successful_event_creation(TestCase):

    def setUp(self):
        pass


    def test_event_create_success(self):
        from core.models import Event

        from datetime import datetime
        passing_event_fixture = {
                                 "date": datetime(2016,12,22),
                                 "location_title": "This is a fairly short title event",
                                 "location_code": "r4nd0mcode5",
                                 "picture_url": "http://www.wearesupperclub.co.uk/picture.jpg",
                                 }

        event = Event(**passing_event_fixture)
        event.save()
        #Can it create an object properly?
        self.assertIsInstance(event, Event)
        #Presumably then it's slugified the event url properly
        self.assertTrue(event.event_url == slugify(event.location_title+str(event.date)))

    def test_event_create_failure(self):
        from core.models import Event

        from datetime import datetime
        failing_numbers_event_fixture = {
            "date": datetime(0234, 12, 22),
            "location_title": 4,
            "location_code": 3,
            "picture_url": 1,
        }

        event = Event(**failing_numbers_event_fixture)
        #Trying to concatenate strings and ints breaks
        self.assertRaises(TypeError, event.save())
