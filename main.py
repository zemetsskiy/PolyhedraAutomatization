from Bridger import Bridger
from Minter import Minter
from Messager import Messager
from config.logger import logger
import time


def rest(private_key):
    greenfield_minter = Minter(private_key, 'bsc', 'Greenfield Testnet')
    logger.info("Начинаю минтить Greenfield Testnet нфт")
    greenfield_minter.mint()
    time.sleep(5)

    zklight_minter = Minter(private_key, 'bsc', 'ZkLightClient')
    logger.info("Начинаю минтить ZkLightClient нфт")
    zklight_minter.mint()
    time.sleep(3)

    logger.info("Начинаю бриджить ZkLightClient нфт из BSC в OPBNB")
    zklight_bridger = Bridger(pk, 'ZkLightClient', 'bsc', 'opbnb')
    zklight_bridger.bridge()

    opbnb_minter = Minter(private_key, 'bsc', 'ZkBridge on opBNB')
    logger.info("Начинаю минтить ZkBridge on opBNB нфт")
    opbnb_minter.mint()

    time.sleep(5)

    mainnetalpha_minter = Minter(private_key, 'core', 'Mainnet Alpha')
    logger.info("Начинаю минтить Mainnet Alpha нфт")
    mainnetalpha_minter.mint()
    time.sleep(5)

    logger.info("Начинаю бриджить ZkBridge on opBNB нфт из BSC в OPBNB")
    opbnb_bridger = Bridger(pk, 'ZkBridge on opBNB', 'bsc', 'opbnb')
    opbnb_bridger.bridge()

    time.sleep(7)
    logger.info("Начинаю бриджить Mainnet Alpha нфт из CORE в POLYGON")
    core_bridger = Bridger(pk, 'Mainnet Alpha', 'core', 'polygon')
    core_bridger.bridge()

    time.sleep(11)
    logger.info("Начинаю отправлять сообщение")
    Messager.messsage(private_key)





    pandra_bnb_minter = Minter(private_key, 'bsc', 'Pandra')
    logger.info("Начинаю минтить CodeConqueror нфт")
    pandra_bnb_minter.mint()
    time.sleep(3)

    pandra_pol_minter = Minter(private_key, 'polygon', 'Pandra')
    logger.info("Начинаю минтить PixelProwler нфт")
    pandra_pol_minter.mint()
    time.sleep(5)

    pandra_core_minter = Minter(private_key, 'core', 'Pandra')
    logger.info("Начинаю минтить MelodyMaven нфт")
    pandra_core_minter.mint()
    time.sleep(5)

    pandra_celo_minter = Minter(private_key, 'celo', 'Pandra')
    logger.info("Начинаю минтить EcoGuardian нфт")
    pandra_celo_minter.mint()
    time.sleep(5)





    time.sleep(2)
    logger.info("Начинаю бриджить CodeConqueror нфт из BSC в CORE")
    pandra_bsc_bridger = Bridger(pk, 'Pandra', 'bsc', 'core')
    pandra_bsc_bridger.bridge()

    time.sleep(2)
    logger.info("Начинаю бриджить PixelProwler нфт из POLYGON в BSC")
    pandra_polygon_bridger = Bridger(pk, 'Pandra', 'polygon', 'bsc')
    pandra_polygon_bridger.bridge()

    time.sleep(2)
    logger.info("Начинаю бриджить MelodyMaven нфт из CORE в POLYGON")
    pandra_core_bridger = Bridger(pk, 'Pandra', 'core', 'polygon')
    pandra_core_bridger.bridge()



def work(private_key):

    time.sleep(2)
    logger.info("Начинаю бриджить EcoGuardian нфт из CELO в BSC")
    pandra_celo_bridger = Bridger(pk, 'Pandra', 'celo', 'bsc')
    pandra_celo_bridger.bridge()


if __name__ == "__main__":
    with open("private_keys.txt", "r") as file:
        logger.info("Считываю приватники")
        private_keys = [private_key.strip() for private_key in file]

    logger.info(f"Приступаю к минту нфт")
    for pk in private_keys:
        work(pk)