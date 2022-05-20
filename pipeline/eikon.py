"""
Wrapper for the Eikon API

df, err = ek.get_data(
    instruments = ['IBM'],
        fields = ['TR.PriceClose']
        )

        display(df)

        TODO: how to forward eikon ports through to WSL without elevated priviledges? cf. https://stackoverflow.com/a/69498558/1106271
"""
from typing import List

import eikon as ek


class Eikon:
    """Wrapper for the eikon api"""

    def __init__(self, api_path: str = "EIKON_KEY"):
        with open(api_path, "r") as eikon_file:
            ek.set_app_key(eikon_file.read())

    def get_reference(self, tickers: List[str], fields: List[str]):
        """get snapshot reference / fundamental data"""

        df, err = ek.get_data(instruments=tickers, fields=fields)
        return df

    def get_timeseries(self, **kwargs):
        """
        recover OHLC historical data

        :param rics: string or list of strings
        Single RIC or list of RICs to retrieve historical data for
        :param start_date: date from which to get values
        start_date string or datetime.datetime or datetime.timedelta
        Starting date and time of the historical range.
        The string format is %Y-%m-%dT%H:%M:%S, for example, 2016-01-20T15:04:05.
        datetime.timedelta is negative number of day relative to datetime.now().
        The default is datetime.now() + timedelta(-100).
        You can use the helper function get_date_from_today.
        end_date string or datetime.datetime or datetime.timedelta
        End date and time of the historical range.
        Possible string formats:
            %Y-%m-%d, for example, 2017-01-20
            %Y-%m-%dT%H:%M:%S, for example, 2017-01-20T15:04:05
            datetime.timedelta is negative number of day relative to datetime.now().
            The default is datetime.now().
            You can use the helper function get_date_from_today. See the Examples section
            for usage.
        :param interval: string Data interval. Possible values are tick, minute, hour, daily, weekly, monthly, quarterly, yearly.
            The default is daily.
            fields string or list of
            strings
            Use this parameter to filter the returned fields set. Available fields: TIMESTAMP,
            VALUE, VOLUME, HIGH, LOW, OPEN, CLOSE, COUNT.
            By default, all fields are returned.
            count int, optional Maximum number of data points retrieved.
            calendar string, optional Possible values: native, tradingdays, calendardays.
            corax string, optional Possible values: adjusted, unadjusted
            Eikon functions
        :param normalize: boolean If set to True, the function returns a normalized data frame with the following columns
        Date, Security, Field. If the value of this parameter is False, the returned data
        frame shape depends on the number of RICs and the number of fields in the response
        There are three different shapes:
            • One RIC and many fields
            • Many RICs and one field
            • Many RICs and many fields
            The default is False.
             This parameter has less precedence than the parameter rawOutput. That is, if
            rawOutput is set to True, the returned data is the raw data and this parameter
            is ignored.
        :param raw_output: boolean Set this parameter to True to get the data in JSON format. If set to False, the
            function returns a data frame which shape is defined by the normalize parameter.
            The default is False.
        :param debug: bool When set to True, the JSON request and response are printed.
            The default is False
        """
        df = ek.get_timeseries(**kwargs)
        return df
