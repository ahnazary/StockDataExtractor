"""
Moduel for the Ticker class
"""

from stockdex.config import VALID_DATA_SOURCES, VALID_SECURITY_TYPES
from stockdex.digrin_interface import Digrin_Interface
from stockdex.exceptions import WrongDataSource
from stockdex.justetf import JustETF
from stockdex.nasdaq_interface import NASDAQInterface
from stockdex.yahoo_api import YahooAPI
from stockdex.yahoo_web import YahooWeb

# def ticker_factory(data_source_class):
# #YahooAPI, JustETF, NASDAQInterface, Digrin_Interface, YahooWeb
#     class TickerFactory(data_source):
#         pass


class Ticker(YahooAPI, JustETF, NASDAQInterface, Digrin_Interface, YahooWeb):
    """
    Class for the Ticker
    """

    def __init__(
        self,
        ticker: str = "",
        isin: str = "",
        security_type: VALID_SECURITY_TYPES = "stock",
        data_source: VALID_DATA_SOURCES = "yahoo_api",
    ) -> None:
        """
        Initialize the Ticker class

        Args:
        ticker (str): The ticker of the stock
        isin (str): The ISIN of the etf
        security_type (str): The security type of the ticker
            default is "stock"
        """

        self.ticker = ticker
        self.isin = isin
        self.security_type = security_type
        self.data_source = data_source

        if not ticker and not isin:
            raise Exception("Please provide either a ticker or an ISIN")

        # super().__init__(ticker=ticker, isin=isin, security_type=security_type)

    @property
    def data_source(self):
        return self._data_source

    @data_source.setter
    def data_source(self, value):
        if value not in VALID_DATA_SOURCES.__args__:
            raise WrongDataSource(given_source=value)
        self._data_source = value

    def data_source_class(self):
        if self.data_source == "yahoo_web":
            return YahooWeb
        elif self.data_source == "yahoo_api":
            return YahooAPI
        elif self.data_source == "nasdaq":
            return NASDAQInterface
        elif self.data_source == "justetf":
            return JustETF
        elif self.data_source == "digrin":
            return Digrin_Interface
        else:
            raise WrongDataSource(given_source=self.data_source)
