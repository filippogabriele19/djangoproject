from web3 import Web3


def sendTransaction(message):
    try:
        w3 = Web3(
            Web3.HTTPProvider(
                "https://ropsten.infura.io/v3/ea0c1c57fe284ba08f35594175b2dd72"
            )
        )
        address = "0xD38d13786D44cc74642CFc2dd34A2c5a7306b0EF"
        privateKey = (
            "0xc3fe88666de0bdba5b6aa0fd09df497526d3e96833806e38f40eada2de730a2b"
        )
        nonce = w3.eth.getTransactionCount(address)
        gasPrice = w3.eth.gasPrice
        value = w3.toWei(0.000001, "ether")
        signedTx = w3.eth.account.signTransaction(
            dict(
                nonce=nonce,
                gasPrice=gasPrice,
                gas=100000,
                to="0x0000000000000000000000000000000000000000",
                value=value,
                data=message.encode("utf-8"),
            ),
            privateKey,
        )

        tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
        txId = w3.toHex(tx)
        return txId
    except:
        return ""
