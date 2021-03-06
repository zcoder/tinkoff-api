from dataclasses import dataclass
from typing import Optional, List

from tinkoff.investments.model.base import (
    BaseModel,
    Currency,
    FigiName,
    TickerName,
)


@dataclass
class MarketInstrument(BaseModel):
    figi: FigiName
    ticker: TickerName
    lot: int
    name: str
    currency: Optional[Currency] = None
    isin: Optional[str] = None
    minPriceIncrement: Optional[float] = None


@dataclass
class MarketInstrumentList(BaseModel):
    total: int
    instruments: List[MarketInstrument]


__all__ = [
    'MarketInstrument',
    'MarketInstrumentList',
]
