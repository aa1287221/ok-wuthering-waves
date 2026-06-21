# EatBuffFoodTask.py
from qfluentwidgets import FluentIcon

from src.task.BaseWWTask import BaseWWTask, EAT_BUFF_FOOD_KEY


class EatBuffFoodTask(BaseWWTask):
    """Standalone: eat the configured drop-rate buff food once.

    Doubles as the live-tuning entry point for the shared eat_buff_food() hook.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = "食用增益料理"
        self.description = "在大世界自动打开背包，食用设定的增益料理（如糖醋里脊 +50% 声骸掉落）后返回。"
        self.icon = FluentIcon.DICTIONARY
        self.group_name = "强化声骸"
        self.supported_languages = ["zh_CN", "zh_TW"]
        self.add_buff_food_config()
        # Standalone task: enable by default so it acts when run directly.
        self.default_config[EAT_BUFF_FOOD_KEY] = True

    def run(self):
        self.eat_buff_food()
