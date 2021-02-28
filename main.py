from amazon import is_amazon_buyable
from rakuten import is_rakuten_buyable
from discord import notify_discord


def determine_and_notify_if_ps5_is_available_for_purchase_at_each_site():
    if(is_amazon_buyable()):
        notify_discord('amazon')

    if(is_rakuten_buyable()):
        notify_discord('rakuten')

if __name__ == '__main__':
    determine_and_notify_if_ps5_is_available_for_purchase_at_each_site()
