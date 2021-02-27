import configparser
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')
webhook_url_of_discord = config_ini['DISCORD']['WebhookURL'] # 通知用のURLを取得
