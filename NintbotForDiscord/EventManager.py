import traceback

from .Enums import EventTypes
from .Plugin import BasePlugin
import asyncio
__author__ = 'Riley Flynn (nint8835)'


class EventManager:

    def __init__(self, bot_instance):
        self._handlers = []
        self._bot = bot_instance
        self.loop = asyncio.get_event_loop()
        self.queue = asyncio.Queue(loop=self.loop)
        self.loop.create_task(self.event_handle_loop())

    async def event_handle_loop(self):
        """
        The main loop that dispatches incoming events to all registered handlers
        """
        while not self._bot.is_closed:
            handler = await self.queue.get()
            self._bot.logger.debug("{} items in event queue.".format(self.queue.qsize()))
            try:
                await asyncio.wait_for(handler["handler"](handler["args"]), timeout=self._bot.config["event_timeout"],
                                       loop = self.loop)
            except asyncio.TimeoutError:
                self._bot.logger.warning("Handling of {} event from plugin {} timed out.".format(handler["type"],
                                                                                                 handler["plugin"].manifest["name"]))

    def register_handler(self, event_type: EventTypes, event_handler, plugin: BasePlugin):
        """
        Registers an event handler
        :param event_type: The type of event this handler will handle
        :param event_handler: The coroutine that will handle this event
        :param plugin: The plugin instance that this module belongs to
        """
        self._handlers.append({"type": event_type, "handler": event_handler, "plugin": plugin})

    async def dispatch_event(self, event_type: EventTypes, **kwargs):
        """
        Adds an event to the event queue to be dispatched to all registered handlers
        :param event_type: The type of event to dispatch
        :param kwargs: The event arguments
        """
        new_args = kwargs
        new_args["bot"] = self._bot
        new_args["event_type"] = event_type
        for handler in self._handlers:
            if handler["type"] == event_type:
                # noinspection PyBroadException
                try:
                    await self.queue.put({"handler": handler["handler"],
                                          "type": event_type,
                                          "args": new_args,
                                          "plugin": handler["plugin"]})
                except:
                    traceback.print_exc(5)

        if event_type == EventTypes.COMMAND_SENT:
            await self._bot.CommandRegistry.handle_command(new_args["command_args"][0], new_args)

    def remove_handlers(self, plugin: BasePlugin):
        for handler in self._handlers:
            if handler["plugin"] == plugin:
                self._handlers.remove(handler)
