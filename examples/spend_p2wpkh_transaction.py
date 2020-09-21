# Copyright (C) 2018-2020 The python-litecoin-utils developers
#
# This file is part of python-litecoin-utils
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-litecoin-utils, including this file, may be copied,
# modified, propagated, or distributed except according to the terms contained
# in the LICENSE file.

from litecoinutils.setup import setup
from litecoinutils.utils import to_satoshis
from litecoinutils.transactions import Transaction, TxInput, TxOutput
from litecoinutils.keys import P2pkhAddress, PrivateKey
from litecoinutils.script import Script

def main():
    # always remember to setup the network
    setup('testnet')

    # the key that corresponds to the P2WPKH address
    priv = PrivateKey("cQQB9SYxT2gmT9TkVnyZNDvjEeheDoAXskPDhkhAh2d3RfoHxF2J")

    pub = priv.get_public_key()

    fromAddress = pub.get_segwit_address()
    print(fromAddress.to_string())

    # amount is needed to sign the segwit input
    fromAddressAmount = to_satoshis(0.95)

    # UTXO of fromAddress
    txid = 'e66a7a9cb04c57a2be1ce44306ccc8a58d48e3d831bc232567180eb7536ef8ea'
    vout = 1

    # change to same address
    toAddress = fromAddress

    # create transaction input from tx id of UTXO
    txin = TxInput(txid, vout)

    # the script code required for signing for p2wpkh is the same as p2pkh
    script_code = Script(['OP_DUP', 'OP_HASH160', pub.to_hash160(),
                          'OP_EQUALVERIFY', 'OP_CHECKSIG'])

    # create transaction output
    txOut = TxOutput(to_satoshis(0.949), toAddress.to_script_pub_key())

    # op_return
    op_return_cert_protocol = '1234567890'
    op_return_output = TxOutput(to_satoshis(0), Script(['OP_RETURN',
                                                        op_return_cert_protocol]))
    # create transaction without change output - if at least a single input is
    # segwit we need to set has_segwit=True
    tx = Transaction([txin], [txOut, op_return_output], has_segwit=True)

    print("\nRaw transaction:\n" + tx.serialize())

    sig = priv.sign_segwit_input(tx, 0, script_code, fromAddressAmount)
    tx.witnesses.append( Script([sig, pub.to_hex()]) )

    # print raw signed transaction ready to be broadcasted
    print("\nRaw signed transaction:\n" + tx.serialize())
    print("\nTxId:", tx.get_txid())


if __name__ == "__main__":
    main()
