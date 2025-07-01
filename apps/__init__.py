"""
This package contains all application deployment modules for DevBox.

Each submodule corresponds to a specific application and implements logic
to install, start, and manage the application's lifecycle across different
environments.
"""

import importlib
import os

from core.context import Context
from core.interfaces import AppProvider


def loader(ctx: Context) -> dict[str, AppProvider]:
    """
    Dynamically discovers and initializes all application classes within the apps package.

    Args:
        ctx (Context): The shared context instance used to configure each app.

    Returns:
        dict[str, AppProvider]: A dictionary mapping app names to their initialized instances.
    """
    apps_path = os.path.dirname(__file__)
    loaded_apps = {}
    for name in os.listdir(apps_path):
        full_path = os.path.join(apps_path, name)
        if os.path.exists(os.path.join(full_path, os.path.basename(__file__))):
            module_name = f"{os.path.basename(apps_path)}.{name}"
            print(module_name)
            module = importlib.import_module(module_name)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, AppProvider) and attr is not AppProvider:
                    loaded_apps[name.lower()] = attr(ctx)

    return loaded_apps