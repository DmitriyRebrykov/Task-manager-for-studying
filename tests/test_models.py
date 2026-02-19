from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

from apps.main.models import Project, Task
from tests.base import BaseTestCase


class ProjectModelTest(BaseTestCase):


    def test_str_returns_project_name(self):
        self.assertEqual(str(self.project), "Test Project")


    def test_projects_ordered_alphabetically(self):
        Project.objects.create(name="Zebra", user=self.user)
        Project.objects.create(name="Alpha", user=self.user)
        names = list(
            Project.objects.filter(user=self.user).values_list("name", flat=True)
        )
        self.assertEqual(names, sorted(names))


    def test_created_at_set_on_create(self):
        self.assertIsNotNone(self.project.created_at)

    def test_updated_at_changes_after_save(self):
        old = self.project.updated_at
        self.project.name = "Renamed"
        self.project.save()
        self.project.refresh_from_db()
        self.assertGreaterEqual(self.project.updated_at, old)


    def test_cascade_delete_removes_tasks(self):
        task_pk = self.task.pk
        self.project.delete()
        self.assertFalse(Task.objects.filter(pk=task_pk).exists())

    def test_cascade_delete_with_user(self):
        project_pk = self.project.pk
        self.user.delete()
        self.assertFalse(Project.objects.filter(pk=project_pk).exists())

    def test_related_name_tasks(self):
        self.assertIn(self.task, self.project.tasks.all())


class TaskModelTest(BaseTestCase):


    def test_str_returns_task_and_project(self):
        expected = f"Task {self.task.name} for {self.project}"
        self.assertEqual(str(self.task), expected)


    def test_default_done_is_false(self):
        task = Task.objects.create(name="Fresh", project=self.project)
        self.assertFalse(task.done)

    def test_default_order_is_zero(self):
        task = Task.objects.create(name="Fresh", project=self.project)
        self.assertEqual(task.order, 0)

    def test_deadline_can_be_null(self):
        task = Task.objects.create(name="No deadline", project=self.project)
        self.assertIsNone(task.deadline)


    def test_tasks_ordered_by_order_then_name(self):
        Task.objects.all().delete()
        Task.objects.create(name="B", project=self.project, order=1)
        Task.objects.create(name="A", project=self.project, order=2)
        Task.objects.create(name="C", project=self.project, order=0)
        names = list(self.project.tasks.values_list("name", flat=True))
        self.assertEqual(names, ["C", "B", "A"])


    def test_clean_raises_for_past_deadline(self):
        past = timezone.now() - timedelta(hours=1)
        task = Task(name="Late", project=self.project, deadline=past)
        with self.assertRaises(ValidationError) as ctx:
            task.clean()
        self.assertIn("deadline", ctx.exception.message_dict)

    def test_clean_accepts_future_deadline(self):
        future = timezone.now() + timedelta(days=1)
        task = Task(name="Future", project=self.project, deadline=future)
        task.clean()

    def test_clean_accepts_no_deadline(self):
        task = Task(name="No deadline", project=self.project)
        task.clean()


    def test_created_at_set_on_create(self):
        self.assertIsNotNone(self.task.created_at)