import os
import asyncio

import uvloop

from ostiarius.app import create_app

if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = create_app()
    app.run(host="0.0.0.0", port=7777, debug=os.getenv("DEBUG", False))
