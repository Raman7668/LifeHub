import os

api_id = 22475741
api_hash = os.environ.get("API_HASH", "1a217be7la0225e0a678af286c211f8a")
bot_token = os.environ.get("BOT_TOKEN","7347353498:AAGgNzcVVGcEUoZSYAhghggmKpgX8_XUYvs")
auth_users = os.environ.get("AUTH_USERS", "6562642609")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "6562642609")
owner_users = [int(num) for num in osowner_users.split(",")]
