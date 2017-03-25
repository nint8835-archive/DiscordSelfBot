from NintbotForDiscord.Launcher import FileBotLauncher
import os
# from pycallgraph import PyCallGraph, Config, GlobbingFilter
# from pycallgraph.output import GraphvizOutput

__author__ = 'Riley Flynn (nint8835)'

# module_filter = GlobbingFilter(exclude=[
#     "pycallgraph.*",
#     "asyncio.*",
#     "importlib.*",
#     "spec_from_file_location",
#     "module_from_spec",
#     "SourceFileLoader.*",
#     "_handle_fromlist",
#     "_find_and_load",
#     "_find_and_load*"
#     "__import__",
#     "cb",
#     "_gcd_import",
#     "_sanity_check"
#     "_lock_unlock_module",
#     "type.create_module",
#     "ExtensionFileLoader.*",
#     "type.create_module",
#     "type.exec_module",
#     "_load_unlocked",
#     "_new_module",
#     "cache_from_source"
# ])
#
# config = Config()
# config.trace_filter = module_filter
#
# out = GraphvizOutput()
# out.tool = "sfdp"
#
# with PyCallGraph(output=out, config=config):
#     launcher = FileBotLauncher(os.path.join("config.json"))

launcher = FileBotLauncher(os.path.join("config.json"))
