from nex.common.storage import StorageAPI

class Token():
    """
    Basic settings for the NEP5 Token small neo and small crowdsale
    """

    name = 'small neo'

    symbol = 'SNEO'

    decimals = 8

    # This is the script hash of the address for the owner of the small neo token
    # This can be found in ``neo-python`` with the walet open, use ``wallet`` command
    owner = b'{5\x03\x11\xbc\x17\xc6I\x84\x06\x93\xcb\xe6.\x9f\xd0\x19\xb9\x11w'

    in_circulation_key = b'in_circulation'

    total_supply = 10000 * 10^8  # 1000 total supply 

    initial_amount = 6400 * 10^8 # 640 to owners 

    # for now assume .005 dollars per token, and one smallneo = $.005 * 1000
    tokens_per_neo = 200000 * 10^8 

    # for now assume 1 dollar per token, and one gas = $36 dollars * 10^8
    tokens_per_gas = 75000 * 10^8

    # maximum amount you can mint in the limited round ( 5 smallneo/person * 20000 Tokens/NEO * 10^8 )
    max_exchange_limited_round = 5 * 200000 * 10^8

    # when to start the crowdsale (TEST)
    block_sale_start = 1

    # when to end the initial limited round (TEST)
    limited_round_end = 1 + 504000000


    def crowdsale_available_amount(self):
        """

        :return: int The amount of tokens left for sale in the crowdsale
        """
        storage = StorageAPI()

        in_circ = storage.get(self.in_circulation_key)

        available = self.total_supply - in_circ

        return available


    def add_to_circulation(self, amount:int, storage:StorageAPI):
        """
        Adds an amount of token to circlulation

        :param amount: int the amount to add to circulation
        :param storage:StorageAPI A StorageAPI object for storage interaction
        """
        current_supply = storage.get(self.in_circulation_key)

        current_supply += amount

        storage.put(self.in_circulation_key, current_supply)



    def get_circulation(self, storage:StorageAPI):
        """
        Get the total amount of tokens in circulation

        :param storage:StorageAPI A StorageAPI object for storage interaction
        :return:
            int: Total amount in circulation
        """
        return storage.get(self.in_circulation_key)

