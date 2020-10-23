import json
from enum import IntEnum

from pkg_resources import resource_string

TELLOR_ABI = json.loads(resource_string('tellor', 'abi/tellor.json'))


class Network(IntEnum):
    MAINNET = 1
    RINKEBY = 4


TELLOR_ADDRESS = {
    Network.MAINNET: '0x0Ba45A8b5d5575935B8158a88C631E9F9C95a2e5',
    Network.RINKEBY: '0xFe41Cb708CD98C5B20423433309E55b53F79134a',
}

TELLOR_GENESIS = {
    Network.MAINNET: 8265522,
    Network.RINKEBY: 5067828,
}
