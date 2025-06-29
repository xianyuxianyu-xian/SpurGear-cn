# Author-Autodesk
# Description-Base Template for creating a Fusion Addin.

from . import commands
from .lib import fusionAddInUtils as futil
import adsk.core


def run(context):
    try:
        # Display a message when the add-in is manually run.
        if not context['IsApplicationStartup']:
            app = adsk.core.Application.get()
            ui = app.userInterface
            ui.messageBox('加载成功,在实体→创建下新建了正齿轮生成命令')

        # Run the start function in each command.
        commands.start()

    except:
        futil.handle_error('run')


def stop(context):
    try:
        # Remove all of the event handlers.
        futil.clear_handlers()

        # Run the stop function in each command.
        commands.stop()

    except:
        futil.handle_error('stop')