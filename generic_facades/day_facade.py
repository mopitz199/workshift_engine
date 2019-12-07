# make all type hints be strings and skip evaluating them
from __future__ import annotations

from typing import Any


class DayFacade():

    def __init__(
        self,
        day: Any
    ) -> None:
        self.day = day

    def is_working_day(
        self
    ) -> bool:
        return (self.day.starting_time is not None and
                self.day.ending_time is not None)
