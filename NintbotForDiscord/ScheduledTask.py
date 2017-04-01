import time

import discord
from discord.utils import find

from . import Bot
from .Plugin import BasePlugin
from . import Scheduler

__author__ = 'Riley Flynn (nint8835)'


class ScheduledTask:

    def __init__(self, delay: int = 30):
        self.created = time.time()
        self.delay = delay

    def check_task(self):
        return time.time() - self.created >= self.delay

    async def execute_task(self):
        pass


class RepeatingScheduledTask(ScheduledTask):

    def __init__(self, scheduler: "Scheduler.Scheduler", plugin: BasePlugin, delay: int = 30):
        ScheduledTask.__init__(self, delay)
        self.scheduler = scheduler
        self.plugin = plugin

    async def execute_task(self):
        self.created = time.time()
        self.scheduler.add_task(self, self.plugin)


class RepeatingScheduledTaskWrapper(RepeatingScheduledTask):

    def __init__(self, task: ScheduledTask, plugin: BasePlugin, scheduler: "Scheduler.Scheduler"):
        RepeatingScheduledTask.__init__(self, scheduler, plugin, task.delay)
        self.task = task
        self.scheduler = scheduler

    def check_task(self):
        return self.task.check_task()

    async def execute_task(self):
        await RepeatingScheduledTask.execute_task(self)
        await self.task.execute_task()


class MessageScheduledTask(ScheduledTask):

    def __init__(self, destination: discord.Object, message: str, bot_instance: "Bot.Bot", delay: int = 30):
        ScheduledTask.__init__(self, delay)
        self.destination = destination
        self.message = message
        self.bot = bot_instance

    async def execute_task(self):
        await self.bot.send_message(self.destination, self.message)


class RepeatingMessageScheduledTask(RepeatingScheduledTask, MessageScheduledTask):

    def __init__(self,
                 destination: discord.Object,
                 message: str,
                 bot_instance: "Bot",
                 scheduler: "Scheduler",
                 plugin: BasePlugin,
                 delay: int = 30):
        RepeatingScheduledTask.__init__(self, scheduler, plugin, delay)
        MessageScheduledTask.__init__(self, destination, message, bot_instance, delay)

    async def execute_task(self):
        await RepeatingMessageScheduledTask.execute_task(self)
        await MessageScheduledTask.execute_task(self)


class AddRoleScheduledTask(ScheduledTask):

    def __init__(self, user_id: str, server_id: str, role_id: str, bot_instance: "Bot.Bot", delay: int = 30):
        ScheduledTask.__init__(self, delay)
        self.user_id = user_id
        self.server_id = server_id
        self.role_id = role_id
        self.bot = bot_instance

    async def execute_task(self):
        await ScheduledTask.execute_task(self)
        server = find(lambda s: s.id == self.server_id, self.bot.servers)
        role = find(lambda r: r.id == self.role_id, server.roles)
        await self.bot.add_roles(server.get_member(self.user_id), role)


class RemoveRoleScheduledTask(ScheduledTask):

    def __init__(self, user_id: str, server_id: str, role_id: str, bot_instance: "Bot.Bot", delay: int = 30):
        ScheduledTask.__init__(self, delay)
        self.user_id = user_id
        self.server_id = server_id
        self.role_id = role_id
        self.bot = bot_instance

    async def execute_task(self):
        await ScheduledTask.execute_task(self)
        server = find(lambda s: s.id == self.server_id, self.bot.servers)
        role = find(lambda r: r.id == self.role_id, server.roles)
        await self.bot.remove_roles(server.get_member(self.user_id), role)


class GameUpdateScheduledTask(ScheduledTask):

    def __init__(self, game: str, bot: "Bot.Bot", delay: int = 30):
        ScheduledTask.__init__(self, delay)
        self.game = game
        self.bot = bot

    async def execute_task(self):
        await self.bot.change_presence(game=discord.Game(name=self.game))
