import asyncio

from NintbotForDiscord.ScheduledTask import ScheduledTask

__author__ = 'Riley Flynn (nint8835)'


class Scheduler:

    def __init__(self, bot_instance):
        self.bot = bot_instance
        self.tasks = []
        self.bot.EventManager.loop.create_task(self.handle_tasks())

    async def handle_tasks(self):
        """
        The loop that checks and executes tasks
        """
        while not self.bot.is_closed:

            for task in self.tasks[:]:
                if task["task"].check_task():
                    self.tasks.remove(task)
                    await task["task"].execute_task()

            await asyncio.sleep(1)

    def add_task(self, task_instance: ScheduledTask, plugin_info: dict):
        """
        Adds a new task to the task list
        :param task_instance: The task to add
        :param plugin_info: The plugin_data dictionary of the plugin that is adding the task
        """
        self.tasks.append({"task": task_instance,
                           "plugin": plugin_info})

    def remove_tasks_for_plugin(self, plugin_info: dict):
        """
        Removes all tasks for a plugin
        :param plugin_info: The plugin_data dictionary of the plugin that is adding the task
        """
        for task in self.tasks[:]:
            if task["plugin"] == plugin_info:
                self.tasks.remove(task)
