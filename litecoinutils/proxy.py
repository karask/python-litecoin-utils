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

from litecoinrpc.authproxy import AuthServiceProxy

from litecoinutils.setup import get_network
from litecoinutils.constants import NETWORK_DEFAULT_PORTS


class NodeProxy:
    """Simple Bitcoin node proxy that can call all of Bitcoin's JSON-RPC functionality.

    Attributes
    ----------
    proxy : object
        a litecoinrpc AuthServiceProxy object
    """

    def __init__(self, rpcuser=None, rpcpassword=None, host=None, port=None):
        """Connects to node using credentials given

        Parameters
        ----------
        rpcuser : str
            as defined in litecoin.conf
        rpcpassword : str
            as defined in litecoin.conf
        host : str, optional
            host where the Bitcoin node resides; defaults to 127.0.0.1
        port : int, optional
            port to connect to; uses default ports according to network

        Raises
        ------
        ValueError
            if rpcuser and/or rpcpassword are not specified
        """

        if not rpcuser or not rpcpassword:
            raise ValueError('rpcuser or rpcpassword is missing')

        if not host:
            host = '127.0.0.1'

        if not port:
            port = NETWORK_DEFAULT_PORTS[get_network()]

        self.proxy = AuthServiceProxy("http://{}:{}@{}:{}".format(rpcuser, rpcpassword, host, port))


    def get_proxy(self):
        """Returns litecoinrpc AuthServiceProxy object"""
        return self.proxy

