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


if __name__ == '__main__':
    unittest.main()
