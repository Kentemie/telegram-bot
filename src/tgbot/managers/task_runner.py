from typing import Callable

from src.tgbot.managers.process_pool import ProcessPoolManager, process_pool_manager


class TaskRunner:
    def __init__(self, manager: ProcessPoolManager):
        self.manager = manager

    async def run_chart_generation(
        self,
        func: Callable,
        chart_type: str,
        data: dict,
    ) -> bytes:
        return await self.manager.run(func, chart_type, data)


task_runner = TaskRunner(process_pool_manager)
