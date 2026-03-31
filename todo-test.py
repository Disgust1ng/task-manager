import unittest
from todo import add_task, list_tasks, remove_task

class TestTodo(unittest.TestCase):

    def test_add_task(self):
        add_task("Test task")
        self.assertIn("Test task", list_tasks())

    def test_remove_task(self):
        add_task("Task to remove")
        remove_task("Task to remove")
        self.assertNotIn("Task to remove", list_tasks())

if __name__ == "__main__":
    unittest.main()
