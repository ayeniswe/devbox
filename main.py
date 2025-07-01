import apps
from core.context import Context

import logging
import sys


logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    handlers=[
                        logging.StreamHandler(sys.stdout),
                        # logging.FileHandler("devbox.log")
                    ])

ctx = Context()
r = apps.loader(ctx)
app = r["vscode"]
app.install()
