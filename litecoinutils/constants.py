# Copyright (C) 2018-2020 The python-litecoin-utils developers
#
# This file is part of python-litecoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-litecoin-utils, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from decimal import Decimal

# TODO organise constants in sections

NETWORK_DEFAULT_PORTS = { 'mainnet': 9332,
                          'testnet': 19332,
                          'regtest': 19443 }

NETWORK_WIF_PREFIXES = { 'mainnet': b'\xB0',
                         'testnet': b'\xef',
                         'regtest': b'\xef' }

NETWORK_P2PKH_PREFIXES = { 'mainnet': b'\x30',
                           'testnet': b'\x6f',
                           'regtest': b'\x6f' }

NETWORK_P2SH_PREFIXES = { 'mainnet': b'\x32',
                          'testnet': b'\x3A',
                          'regtest': b'\x3A' }

NETWORK_SEGWIT_PREFIXES = { 'mainnet' : 'ltc',
                            'testnet' : 'tltc',
                            'regtest' : 'ltcrt' }

P2PKH_ADDRESS = "p2pkh"
P2SH_ADDRESS = "p2sh"
P2WPKH_ADDRESS_V0 = "p2wpkhv0"
P2WSH_ADDRESS_V0 = "p2wshv0"

SIGHASH_ALL = 0x01
SIGHASH_NONE = 0x02
SIGHASH_SINGLE = 0x03
SIGHASH_ANYONECANPAY = 0x80

TYPE_ABSOLUTE_TIMELOCK = 0x101
TYPE_RELATIVE_TIMELOCK = 0x201
TYPE_REPLACE_BY_FEE    = 0x301

DEFAULT_TX_LOCKTIME = b'\x00\x00\x00\x00'

EMPTY_TX_SEQUENCE = b'\x00\x00\x00\x00'
DEFAULT_TX_SEQUENCE = b'\xff\xff\xff\xff'
ABSOLUTE_TIMELOCK_SEQUENCE = b'\xfe\xff\xff\xff'

REPLACE_BY_FEE_SEQUENCE = b'\x01\x00\x00\x00'


# TX version 2 was introduced in BIP-68 with relative locktime -- tx v1
# does not support relative locktime
DEFAULT_TX_VERSION  = b'\x02\x00\x00\x00'

SATOSHIS_PER_BITCOIN = 100000000
NEGATIVE_SATOSHI = -1

