class BitcoinMainNet(object):
    """Bitcoin MainNet version bytes.

    From https://github.com/bitcoin/bitcoin/blob/v0.9.0rc1/src/chainparams.cpp
    """
    NAME = "Bitcoin Main Net"
    SCRIPT_ADDRESS = 0x05  # int(0x05) = 5
    PUBKEY_ADDRESS = 0x00  # int(0x00) = 0  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x0488ADE4  # Used to serialize private BIP32 addresses


class BitcoinTestNet(object):
    """Bitcoin TestNet version bytes.

    From https://github.com/bitcoin/bitcoin/blob/v0.9.0rc1/src/chainparams.cpp
    """
    NAME = "Bitcoin Test Net"
    SCRIPT_ADDRESS = 0xc4  # int(0xc4) = 196
    PUBKEY_ADDRESS = 0x6f  # int(0x6f) = 111
    SECRET_KEY = 0xEF      # int(0xef) = 239
    EXT_PUBLIC_KEY = 0x043587CF
    EXT_SECRET_KEY = 0x04358394


class LitecoinMainNet(object):
    """Litecoin MainNet version bytes

    Primary version bytes from:
    https://github.com/litecoin-project/litecoin/blob/master-0.8/src/base58.h

    Unofficial extended version bytes from
    https://bitcointalk.org/index.php?topic=453395.0
    """
    NAME = "Litecoin Main Net"
    SCRIPT_ADDRESS = 0x05  # int(0x05) = 5
    PUBKEY_ADDRESS = 0x30  # int(0x30) = 48
    SECRET_KEY = PUBKEY_ADDRESS + 128  # = int(0xb0) = 176

    # Unofficial extended version bytes taken from
    # https://bitcointalk.org/index.php?topic=453395.0
    EXT_PUBLIC_KEY = 0x019da462
    EXT_SECRET_KEY = 0x019d9cfe


class LitecoinTestNet(object):
    """Litecoin TestNet version bytes

    Primary version bytes from:
    https://github.com/litecoin-project/litecoin/blob/master-0.8/src/base58.h

    Unofficial extended version bytes from
    https://bitcointalk.org/index.php?topic=453395.0
    """
    NAME = "Litecoin Test Net"
    SCRIPT_ADDRESS = 0xc4  # int(0xc4) = 196
    PUBKEY_ADDRESS = 0x6f  # int(0x6f) = 111
    SECRET_KEY = PUBKEY_ADDRESS + 128  # = int(0xef) = 239

    # Unofficial extended version bytes taken from
    # https://bitcointalk.org/index.php?topic=453395.0
    EXT_PUBLIC_KEY = 0x0436f6e1
    EXT_SECRET_KEY = 0x0436ef7d


class DogecoinMainNet(object):
    """Dogecoin MainNet version bytes

    Primary version bytes from:
    https://github.com/dogecoin/dogecoin/blob/1.5.2/src/base58.h

    Unofficial extended version bytes from
    https://bitcointalk.org/index.php?topic=409731
    """
    NAME = "Dogecoin Main Net"
    SCRIPT_ADDRESS = 0x16  # int(0x16) = 22
    PUBKEY_ADDRESS = 0x1e  # int(0x1e) = 30
    SECRET_KEY = PUBKEY_ADDRESS + 128  # int(0x9e) = 158

    # Unofficial extended version bytes taken from
    # https://bitcointalk.org/index.php?topic=409731
    EXT_PUBLIC_KEY = 0x02facafd
    EXT_SECRET_KEY = 0x02fac398


class DogecoinTestNet(object):
    """Dogecoin TestNet version bytes

    Primary version bytes from:
    https://github.com/dogecoin/dogecoin/blob/1.5.2/src/base58.h

    Unofficial extended version bytes from
    https://bitcointalk.org/index.php?topic=409731
    """
    NAME = "Dogecoin Test Net"
    SCRIPT_ADDRESS = 0xc4  # int(0xc4) = 196
    PUBKEY_ADDRESS = 0x71  # int(0x71) = 113
    SECRET_KEY = PUBKEY_ADDRESS + 128  # int(0xf1) = 241

    # Unofficial extended version bytes taken from
    # https://bitcointalk.org/index.php?topic=409731
    EXT_PUBLIC_KEY = 0x0432a9a8
    EXT_SECRET_KEY = 0x0432a243


class ViacoinMainNet(object):
    """Viacoin MainNet version bytes.

    """
    NAME = "Viacoin Main Net"
    SCRIPT_ADDRESS = 0x21  # int(0x21) = 33
    PUBKEY_ADDRESS = 0x47  # int(0x47) = 71  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses


class BitcoinGoldMainNet(object):
    """Bitcoin Gold MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Bitcoin Gold Main Net"
    SCRIPT_ADDRESS = 0x17  # int(0x17) = 23
    PUBKEY_ADDRESS = 0x26  # int(0x26) = 38  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x0488ADE4  # Used to serialize private BIP32 addresses

class DashMainNet(object):
    """Dash MainNet version bytes.

    """
    NAME = "Dash Main Net"
    SCRIPT_ADDRESS = 0x10  # int(0x10) = 16
    PUBKEY_ADDRESS = 0x4C  # int(0x4C) = 76  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x02FE52F8  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394 # Used to serialize private BIP32 addresses

class ZCashMainNet(object):#TODO no good
    """ZCash MainNet version bytes.

    """
    NAME = "ZCash Main Net"
    SCRIPT_ADDRESS = [0x1C,0xBD]  # int(0x05) = 05
    PUBKEY_ADDRESS = [0x1C, 0xB8]  # int(0x00) = 00  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394 # Used to serialize private BIP32 addresses

class BitcoinCashMainNet(object):
    """Bitcoin Cash MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Bitcoin Cash Main Net"
    SCRIPT_ADDRESS = 0x05  # int(0x05) = 5
    PUBKEY_ADDRESS = 0x00  # int(0x00) = 0  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x0488ADE4  # Used to serialize private BIP32 addresses

class VertcoinMainNet(object):
    """Vertcoin MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Vertcoin Main Net"
    SCRIPT_ADDRESS = 0x05  # int(0x05) = 5
    PUBKEY_ADDRESS = 0x47  # int(0x47) = 71  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class PeercoinMainNet(object):
    """Peercoin MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Peercoin Main Net"
    SCRIPT_ADDRESS = 0x75  # int(0x75) = 117
    PUBKEY_ADDRESS = 0x37  # int(0x37) = 55  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0xE6E8E9E5  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class DigibyteMainNet(object):
    """Digibyte MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Digibyte Main Net"
    SCRIPT_ADDRESS = 0x05  # int(0x05) = 5
    PUBKEY_ADDRESS = 0x1E  # int(0x1E) = 30  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class PosWalletMainNet(object):
    """PosWallet MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "PosWallet Main Net"
    SCRIPT_ADDRESS = 0x55  # int(0x55) = 85
    PUBKEY_ADDRESS = 0x37  # int(0x37) = 55  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class PivXMainNet(object):
    """PivX MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "PivX Main Net"
    SCRIPT_ADDRESS = 0x0D  # int(0x0D) = 13
    PUBKEY_ADDRESS = 0x1E  # int(0x1E) = 30  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x022D2533  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class QtumMainNet(object):
    """Qtum MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Qtum Main Net"
    SCRIPT_ADDRESS = 0x32  # int(0x55) = 50
    PUBKEY_ADDRESS = 0x3A  # int(0x1C) = 58  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488B21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses


class StratisMainNet(object):
    """Stratis MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Stratis Main Net"
    SCRIPT_ADDRESS = 0x7D  # int(0x7D) = 125
    PUBKEY_ADDRESS = 0x3F  # int(0x3F) = 63  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488C21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class StealthcoinMainNet(object):
    """Stealthcoin MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Stealthcoin Main Net"
    SCRIPT_ADDRESS = 0x55  # int(0x55) = 85
    PUBKEY_ADDRESS = 0x3E  # int(0x3F) = 62  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x8F624B66  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class KomodoMainNet(object):
    """Komodo MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "Komodo Main Net"
    SCRIPT_ADDRESS = 0x55  # int(0x55) = 85
    PUBKEY_ADDRESS = 0x3C  # int(0x3C) = 60  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0xF9EEE48D  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses

class HCashMainNet(object):
    """HCash MainNet version bytes.
    from https://github.com/LedgerHQ/ledger-wallet-webtool/blob/master/src/Networks.js
    """
    NAME = "HCash Main Net"
    SCRIPT_ADDRESS = 0x64  # int(0x64) = 100
    PUBKEY_ADDRESS = 0x28  # int(0x28) = 40  # Used to create payment addresses
    SECRET_KEY = 0x80      # int(0x80) = 128  # Used for WIF format
    EXT_PUBLIC_KEY = 0x0488C21E  # Used to serialize public BIP32 addresses
    EXT_SECRET_KEY = 0x05358394  # Used to serialize private BIP32 addresses