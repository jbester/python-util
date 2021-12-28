from dataclasses import dataclass


@dataclass(frozen=True, eq=True)
class Symbol:
    """Unmodifiable comparable Symbol"""
    symbol_id: str
