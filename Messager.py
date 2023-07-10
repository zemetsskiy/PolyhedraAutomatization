from web3 import Web3
from config.logger import logger

dst_addresses = {'bsc': '0xA98163227B85CcC765295Ce5C18E8aAD663De147',
                'polygon': '0xCcE1E39f2Ef1e69E6B61Cf79212E96C92C4aFf9a'}

lzdst_addresses = {'bsc': '0x39dad2E89a213626a99Ae09b808b4A79c0d3EC16',
                'polygon': '0x2647D579ebc9e1eC5e01c32030d8e69e4a678dEB'}

msg_sender_address = {'bsc': '0xfd3f4d96378072db0862a6f76cc258c2b7ea36cc',
                'polygon': '0xdB6fb08DD8Ce406DA8Ff53FAe65Bd374e3d68681'}

chain_ids = {'bsc': 3,
            'polygon': 4}

stargate_ids = {'bsc': 102,
                'polygon': 109}

fee = {'bsc': int(0.001*10**18),
        'polygon': int(0.5*10**18)}


class Messager:
    @staticmethod
    def messsage(private_key):
        abi = '[{"inputs":[{"internalType":"address","name":"_zkBridgeEntrypoint","type":"address"},{"internalType":"address","name":"_lzEndpoint","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":true,"internalType":"uint32","name":"dstChainId","type":"uint32"},{"indexed":true,"internalType":"address","name":"dstAddress","type":"address"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"string","name":"message","type":"string"}],"name":"LzMessageSend","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint64","name":"sequence","type":"uint64"},{"indexed":true,"internalType":"uint32","name":"dstChainId","type":"uint32"},{"indexed":true,"internalType":"address","name":"dstAddress","type":"address"},{"indexed":false,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"string","name":"message","type":"string"}],"name":"MessageSend","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint16","name":"chainId","type":"uint16"},{"indexed":false,"internalType":"uint256","name":"fee","type":"uint256"}],"name":"NewFee","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"account","type":"address"},{"indexed":false,"internalType":"bool","name":"zkBridgePaused","type":"bool"},{"indexed":false,"internalType":"bool","name":"layerZeroPaused","type":"bool"}],"name":"PauseSendAction","type":"event"},{"inputs":[],"name":"claimFees","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"string","name":"_message","type":"string"}],"name":"estimateLzFee","outputs":[{"internalType":"uint256","name":"nativeFee","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"","type":"uint16"}],"name":"fees","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"_srcChainId","type":"uint16"},{"internalType":"bytes","name":"_srcAddress","type":"bytes"}],"name":"forceResumeReceive","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"}],"name":"getConfig","outputs":[{"internalType":"bytes","name":"","type":"bytes"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"getSendVersion","outputs":[{"internalType":"uint16","name":"","type":"uint16"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"layerZeroPaused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"lzEndpoint","outputs":[{"internalType":"contract ILayerZeroEndpoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"lzChainId","type":"uint16"},{"internalType":"address","name":"lzDstAddress","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"string","name":"message","type":"string"}],"name":"lzSendMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"maxLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool","name":"zkBridgePaused_","type":"bool"},{"internalType":"bool","name":"layerZeroPaused_","type":"bool"}],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"dstAddress","type":"address"},{"internalType":"uint16","name":"lzChainId","type":"uint16"},{"internalType":"address","name":"lzDstAddress","type":"address"},{"internalType":"uint256","name":"nativeFee","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"string","name":"message","type":"string"}],"name":"sendMessage","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"},{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_configType","type":"uint256"},{"internalType":"bytes","name":"_config","type":"bytes"}],"name":"setConfig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_dstChainId","type":"uint16"},{"internalType":"uint256","name":"_fee","type":"uint256"}],"name":"setFee","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_maxLength","type":"uint256"}],"name":"setMsgLength","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setReceiveVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint16","name":"_version","type":"uint16"}],"name":"setSendVersion","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"zkBridgeEntrypoint","outputs":[{"internalType":"contract IZKBridgeEntrypoint","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"zkBridgePaused","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint16","name":"dstChainId","type":"uint16"},{"internalType":"address","name":"dstAddress","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"string","name":"message","type":"string"}],"name":"zkSendMessage","outputs":[],"stateMutability":"payable","type":"function"}]'
        web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))

        logger.info(f"Подключился к https://rpc.ankr.com/bsc")

        wallet_address = web3.eth.account.from_key(private_key).address
        wallet_balance = web3.eth.get_balance(wallet_address)

        logger.info(f"Адрес кошелька: {wallet_address}")
        logger.info(f"Баланс: {wallet_balance}")

        messager_contract = web3.eth.contract(address=Web3.to_checksum_address(msg_sender_address['bsc']),
                                              abi=abi)

        lz_id = stargate_ids['polygon']
        to_chain_id = chain_ids['polygon']
        from_chain_id = chain_ids['bsc']
        message = "Hello"
        dst_address = Web3.to_checksum_address(dst_addresses['polygon'])
        lzdst_address = Web3.to_checksum_address(lzdst_addresses['polygon'])


        tx = messager_contract.functions.zkSendMessage(to_chain_id, dst_address, wallet_address,
                                          message).build_transaction({
            'from': wallet_address,
            'value': fee['bsc'],

            'nonce': web3.eth.get_transaction_count(wallet_address),
            'gasPrice': int(1.5 * 10 ** 9)
        })

        signed_tx = web3.eth.account.sign_transaction(tx, private_key)
        raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_hash = web3.to_hex(raw_tx_hash)

        logger.info(f"Хеш транзакции: {tx_hash}")

        tx_receipt = web3.eth.wait_for_transaction_receipt(raw_tx_hash, timeout=300)

        if tx_receipt.status == 1:
            logger.info(f"Сообщение успешно отправлено.")
            logger.info(f"Транзакция: https://bscscan.com/tx/{tx_hash}\n'")

        else:
            logger.error("Произошла ошибка")



if __name__ == "__main__":
    with open("private_keys.txt", "r") as file:
        private_keys = [row.strip() for row in file]
    for pk in private_keys:
        Messager.messsage(pk)
