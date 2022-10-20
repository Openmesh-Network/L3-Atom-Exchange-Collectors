from .coinbase import Coinbase
from .binance import Binance
from .binance_futures import BinanceFutures
from .apollox import ApolloX
from .dydx import Dydx
from .bitfinex import Bitfinex
from .gemini import Gemini
from .deribit import Deribit
from .bybit import Bybit
from .ftx import FTX
from .kraken import Kraken
from .kraken_futures import KrakenFutures

exch = [
    Coinbase,
    Binance,
    BinanceFutures,
    ApolloX,
    Dydx,
    Bitfinex,
    Gemini,
    Deribit,
    Bybit,
    FTX,
    Kraken,
    KrakenFutures
]

mapping = {
    e.name: e for e in exch
}
