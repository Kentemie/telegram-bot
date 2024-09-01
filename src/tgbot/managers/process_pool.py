import asyncio
import functools

from concurrent.futures import ProcessPoolExecutor


class ProcessPoolManager:
    def __init__(self, max_workers: int = None):
        self.executor = ProcessPoolExecutor(max_workers=max_workers)

    async def run(self, func, *args, **kwargs):
        loop = asyncio.get_running_loop()
        call = functools.partial(func, *args, **kwargs)

        return await loop.run_in_executor(self.executor, call)

    def shutdown(self):
        self.executor.shutdown()


process_pool_manager = ProcessPoolManager(3)
