from web3 import Web3
import datetime
import os

INFURA_URL = os.environ.get('INFURA_URL')

provider = Web3.HTTPProvider(INFURA_URL)
w3 = Web3(provider)

latest_block = w3.eth.block_number
info = w3.eth.get_block(latest_block)

with open("README.md" , "w") as file:
    file.write(f'# CURRENT BLOCK NUMBER: {latest_block}\n')
    file.write("\n")
    for key, value in info.items():
        if key == "timestamp":
            value = datetime.datetime.fromtimestamp(int(value)).utcnow()
        if key == "transactions" or key == "logsBloom" or key == "uncles":
            continue
        if isinstance(value , bytes):
            value = value.hex()
        file.write(f'### {key}: {value}\n')