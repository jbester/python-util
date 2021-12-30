from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class symbol:
    """Unmodifiable comparable Symbol"""
    identifier: str
