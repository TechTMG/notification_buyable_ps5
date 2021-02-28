import os
import configparser
from discordwebhook import Discord

def notify_discord(buyable_ps5_site_name):
    config_ini = configparser.ConfigParser()
    config_ini.read('config.ini', encoding='utf-8')

    buyable_ps5_site_url = config_ini['SiteURL'][buyable_ps5_site_name]
    webhook_url_of_discord = os.environ['DISCORD_WEBHOOK'] # 通知用のURLを取得

    discord = Discord(url=webhook_url_of_discord)
    discord.post(content= buyable_ps5_site_name + "で ps5 買えるぞおお急げえええええええ！！！！\n" + buyable_ps5_site_url)
