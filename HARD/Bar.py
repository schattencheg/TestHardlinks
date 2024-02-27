from datetime import datetime


class Bar:
    def __init__(self, time_start: datetime, time_end: datetime,
                 open: float, high: float, low: float, close: float,
                 volume: float, instrument: str = ""):
        self.time_start: datetime = time_start
        self.time_end: datetime = time_end
        self.open: float = open
        self.high: float = high
        self.low: float = low
        self.close: float = close
        self.volume: float = volume
        self.instrument: str = instrument

    @classmethod
    def set_empty(cls):
        time = datetime.min
        instance = cls(time, time, -1, -1, 100000.0, -1, 0, "")
        return instance

    @classmethod
    def from_bar(cls, bar):
        instance = cls(bar.time_start, bar.time_end, bar.open, bar.high, bar.low, bar.close, bar.volume, bar.instrument)
        return instance

    def __str__(self):
        return f"{self.time_start: %Y-%m-%d},{self.open},{self.high},{self.low},{self.close}"

    def to_string(self, price_decimal):
        return f"{self.time_start: %Y-%m-%d},{self.open:.{price_decimal}f},{self.high:.{price_decimal}f}," \
               f"{self.low:.{price_decimal}f},{self.close:.{price_decimal}f}"
