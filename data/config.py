from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
IP = env.str("ip")

ADMINS: list[int] = [5810990906, 1821539766]
