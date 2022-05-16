"""
Wrapper for the Eikon API

df, err = ek.get_data(
    instruments = ['IBM'],
        fields = ['TR.PriceClose']
        )

        display(df)
"""
import eikon as ek


class Eikon:
    """Wrapper for the eikon api"""

    def __init__(self, api_path: str = "EIKON_KEY"):
        with open(api_path, "r") as eikon_file:
            ek.set_app_key(eikon_file.read())
