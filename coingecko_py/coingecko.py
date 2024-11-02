from typing import Any, Optional

from coingecko_py import api
from coingecko_py.utils import (
    DEMO_COIN_GECKO_API_URL,
    CoinGeckoRequestParams,
    RequestsClient,
)


class CoinGecko:
    def __init__(self, api_key: str) -> None:
        http = RequestsClient(
            base_url=DEMO_COIN_GECKO_API_URL, headers={"x-cg-demo-api-key": api_key}
        )

        self.simple = api.SimpleClient(http)
        self.ping = api.PingClient(http)
        self.coins = api.CoinsClient(http)
        self.contract = api.ContractClient(http)
        self.assets = api.AssetPlatformsClient(http)
        self.categories = api.CategoriesClient(http)
        self.exchanges = api.ExchangesClient(http)
        self.derivatives = api.DerivativesClient(http)
        self.exchange_rates = api.ExchangeRatesClient(http)
        self.search_all = api.SearchClient(http)
        self.trending_search = api.TrendingClient(http)
        self.global_market = api.GlobalClient(http)

    def ping_check_server_status(self) -> dict:
        return self.ping.ping()

    def simple_coin_price_by_id(
        self, ids: str, vs_currencies: str, **kwargs: Any
    ) -> dict:
        params = {"ids": ids, "vs_currencies": vs_currencies, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}

        return self.simple.coin_price_by_id(request=request)

    def simple_coin_price_by_token(
        self, asset_id: str, contract_address: str, vs_currencies: str, **kwargs: Any
    ) -> dict:
        params = {
            "contract_address": contract_address,
            "vs_currencies": vs_currencies,
            **kwargs,
        }
        request: CoinGeckoRequestParams = {"params": params}

        return self.simple.coin_price_by_token(asset_id=asset_id, request=request)

    def simple_supported_vs_currencies(self) -> list:
        return self.simple.supported_vs_currencies()

    def coins_list(self, include_platform: bool = False) -> list:
        params = {"include_platform": include_platform}
        request: CoinGeckoRequestParams = {"params": params}

        return self.coins.coins_list(request=request)

    def coins_markets(self, vs_currency: str, **kwargs: Any) -> list:
        params = {"vs_currency": vs_currency, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}

        return self.coins.coins_markets(request=request)

    def coin_by_id(self, coin_id: str, **kwargs: Any) -> dict:
        request: CoinGeckoRequestParams = {"params": kwargs}

        return self.coins.coin_by_id(coin_id=coin_id, request=request)

    def coin_tickers_by_id(self, coin_id: str, **kwargs: Any) -> dict:
        request: CoinGeckoRequestParams = {"params": kwargs}

        return self.coins.coin_tickers_by_id(coin_id=coin_id, request=request)

    def coin_history_by_id(
        self, coin_id: str, snapshot_date: str, localization: bool = True
    ) -> dict:
        params = {"date": snapshot_date, "localization": localization}
        request: CoinGeckoRequestParams = {"params": params}

        return self.coins.coin_history_by_id(coin_id=coin_id, request=request)

    def coin_history_chart_by_id(
        self, coin_id: str, vs_currency: str, days: str = "1", **kwargs: Any
    ) -> dict:
        params = {"vs_currency": vs_currency, "days": days, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}

        return self.coins.coin_history_chart_by_id(coin_id=coin_id, request=request)

    def coin_history_chart_range_by_id(
        self,
        coin_id: str,
        vs_currency: str,
        from_timestamp: int,
        to_timestamp: int,
        precision: Optional[str] = None,
    ) -> dict:
        params = {
            "vs_currency": vs_currency,
            "from": from_timestamp,
            "to": to_timestamp,
        }

        if precision:
            params["precision"] = precision

        request: CoinGeckoRequestParams = {"params": params}

        return self.coins.coin_history_chart_range_by_id(
            coin_id=coin_id, request=request
        )

    def coin_ohlc_by_id(
        self,
        coin_id: str,
        vs_currency: str,
        days: str = "1",
        precision: Optional[str] = None,
    ) -> list:
        params = {"vs_currency": vs_currency, "days": days}

        if precision:
            params["precision"] = precision

        request: CoinGeckoRequestParams = {"params": params}

        return self.coins.coin_ohlc_by_id(coin_id=coin_id, request=request)

    def contract_coin_data_by_token_address(
        self, coin_id: str, contract_address: str
    ) -> dict:
        return self.contract.coin_data_by_token_address(
            coin_id=coin_id, contract_address=contract_address
        )

    def contract_coin_historical_chart_by_token_address(
        self,
        coin_id: str,
        contract_address: str,
        vs_currency: str,
        days: str = "1",
        **kwargs: Any,
    ) -> dict:
        params = {"vs_currency": vs_currency, "days": days, **kwargs}
        request: CoinGeckoRequestParams = {"params": params}

        return self.contract.coin_historical_chart_by_token_address(
            coin_id=coin_id, contract_address=contract_address, request=request
        )

    def contract_coin_historical_chart_range_by_token_address(
        self,
        coin_id: str,
        contract_address: str,
        vs_currency: str,
        from_timestamp: int,
        to_timestamp: int,
        precision: Optional[str] = None,
    ) -> dict:
        params = {
            "vs_currency": vs_currency,
            "from": from_timestamp,
            "to": to_timestamp,
        }

        if precision:
            params["precision"] = precision

        request: CoinGeckoRequestParams = {"params": params}

        return self.contract.coin_historical_chart_range_by_token_address(
            coin_id=coin_id, contract_address=contract_address, request=request
        )

    def assets_platforms(self, filters: Optional[str] = None) -> list:
        if not filters:
            return self.assets.asset_platforms()

        params = {"filters": filters}
        request: CoinGeckoRequestParams = {"params": params}

        return self.assets.asset_platforms(request=request)

    def categories_list(self) -> list:
        return self.categories.categories_list()

    def categories_with_markets(self, order: Optional[str] = None) -> list:
        if not order:
            return self.assets.asset_platforms()

        params = {"order": order}
        request: CoinGeckoRequestParams = {"params": params}

        return self.categories.categories_list_with_market_data(request=request)

    def exchanges_list(self, per_page: int = 100, page: int = 1) -> list:
        params = {"per_page": per_page, "page": page}
        request: CoinGeckoRequestParams = {"params": params}

        return self.exchanges.exchanges_list(request=request)

    def exchanges_list_id_map(self) -> list:
        return self.exchanges.exchanges_list_id_map()

    def exchange_by_id(self, exchange_id: str) -> dict:
        return self.exchanges.exchange_by_id(exchange_id=exchange_id)

    def exchange_tickers_by_id(self, exchange_id: str, **kwargs: Any) -> dict:
        request: CoinGeckoRequestParams = {"params": kwargs}

        return self.exchanges.exchange_tickers_by_id(
            exchange_id=exchange_id, request=request
        )

    def exchange_volume_chart_by_id(self, exchange_id: str, days: int = 1) -> dict:
        params = {"days": days}
        request: CoinGeckoRequestParams = {"params": params}

        return self.exchanges.exchange_volume_chart_by_id(
            exchange_id=exchange_id, request=request
        )

    def derivatives_ticker_list(self) -> list:
        return self.derivatives.ticker_list()

    def derivatives_exchanges_list_with_data(
        self, order: str = "open_interest_btc_desc", per_page: int = 100, page: int = 1
    ) -> list:
        params = {"order": order, "per_page": per_page, "page": page}
        request: CoinGeckoRequestParams = {"params": params}

        return self.derivatives.exchanges_list_with_data(request=request)

    def derivatives_exchange_by_id(
        self, exchange_id: str, include_tickers: Optional[str] = None
    ) -> dict:
        if not include_tickers:
            return self.derivatives.exchange_by_id(exchange_id=exchange_id)

        params = {"include_tickers": include_tickers}
        request: CoinGeckoRequestParams = {"params": params}

        return self.derivatives.exchange_by_id(exchange_id=exchange_id, request=request)

    def derivatives_exchanges_list_id_map(self) -> list:
        return self.derivatives.exchanges_list_id_map()

    def btc_exchange_rates(self) -> dict:
        return self.exchange_rates.btc_to_currency()

    def search(self, query: str) -> dict:
        params = {"query": query}
        request: CoinGeckoRequestParams = {"params": params}

        return self.search_all.search(request=request)

    def trending(self) -> dict:
        return self.trending_search.trending()

    def global_market_data(self) -> dict:
        return self.global_market.global_market()

    def global_defi_market_data(self) -> dict:
        return self.global_market.global_defi_market()
