from django.test import TestCase, Client
from django.contrib.auth.models import User
from apps.main.models import Project, Task


class BaseTestCase(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpass123",
        )
        self.other_user = User.objects.create_user(
            username="otheruser",
            email="other@example.com",
            password="testpass123",
        )
        self.project = Project.objects.create(name="Test Project", user=self.user)
        self.task = Task.objects.create(
            name="Test Task", project=self.project, order=0
        )
        self.done_task = Task.objects.create(
            name="Done Task", project=self.project, done=True, order=1
        )

    def login(self):
        self.client.force_login(self.user)