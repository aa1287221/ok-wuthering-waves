import types
import unittest
from src.task import BaseWWTask as M


class TestBuffFoodConfig(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(M.EAT_BUFF_FOOD_KEY, 'Eat Buff Food Before Farming')
        self.assertEqual(M.BUFF_FOOD_NAME_KEY, 'Buff Food Name')

    def test_add_buff_food_config_populates_dicts(self):
        stub = types.SimpleNamespace(default_config={}, config_description={})
        M.BaseWWTask.add_buff_food_config(stub)
        self.assertEqual(stub.default_config[M.EAT_BUFF_FOOD_KEY], False)
        self.assertEqual(stub.default_config[M.BUFF_FOOD_NAME_KEY], '糖醋里脊')
        self.assertIn(M.EAT_BUFF_FOOD_KEY, stub.config_description)
        self.assertIn(M.BUFF_FOOD_NAME_KEY, stub.config_description)


class TestEatBuffFoodGuard(unittest.TestCase):
    def _stub(self, enabled):
        calls = []
        stub = types.SimpleNamespace(
            config={M.EAT_BUFF_FOOD_KEY: enabled, M.BUFF_FOOD_NAME_KEY: '糖醋里脊'},
            ensure_main=lambda *a, **k: calls.append('ensure_main'),
            log_info=lambda *a, **k: calls.append('log'),
            _eat_buff_food_navigate=lambda *a, **k: calls.append('nav'),
        )
        return stub, calls

    def test_noop_when_disabled(self):
        stub, calls = self._stub(False)
        M.BaseWWTask.eat_buff_food(stub)
        self.assertEqual(calls, [])           # nothing happens

    def test_runs_navigation_when_enabled(self):
        stub, calls = self._stub(True)
        M.BaseWWTask.eat_buff_food(stub)
        self.assertIn('nav', calls)

    def test_navigation_failure_is_swallowed(self):
        stub, calls = self._stub(True)
        def boom(*a, **k):
            raise RuntimeError('anchor not found')
        stub._eat_buff_food_navigate = boom
        # must NOT raise — buff is an enhancement, never crashes the farm
        M.BaseWWTask.eat_buff_food(stub)
        self.assertIn('log', calls)


from config import config
from ok.test.TaskTestCase import TaskTestCase
from src.task.EatBuffFoodTask import EatBuffFoodTask

config['debug'] = True


class TestEatBuffFoodTask(TaskTestCase):
    task_class = EatBuffFoodTask
    config = config

    def test_task_has_buff_config(self):
        self.assertIn(M.EAT_BUFF_FOOD_KEY, self.task.default_config)
        self.assertEqual(self.task.default_config[M.BUFF_FOOD_NAME_KEY], '糖醋里脊')
        self.assertTrue(self.task.default_config[M.EAT_BUFF_FOOD_KEY])  # standalone defaults ON


if __name__ == '__main__':
    unittest.main()
