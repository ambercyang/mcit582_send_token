#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install py-algorand-sdk


# In[9]:


#!/usr/bin/python3

from algosdk.v2client import algod
from algosdk import mnemonic
from algosdk import transaction
from algosdk import account, encoding


# In[15]:


#Generating an account
#sk, address = account.generate_account()
#print("private key = ",sk)
#print("address:", address)
#Status: Code 200 success: "6STTP4HENIYTR4GPXMTLEFAWCEIZLAEBL6D6763JV5XVBPU4IJRA"
#Account be funded with 100 Algos


# In[34]:


import json
#algod_address = "https://testnet-algorand.api.purestake.io/ps2"
#algod_token = "B3SU4KcVKi94Jap2VXkK83xx38bsv95K5UZm2lab"
#client =algod.AlgodClient(algod_token, algod_address)
#account_info = client.account_info(address)


# In[20]:



#mnemonic.from_private_key(sk)
#'ship floor pattern transfer fiscal diamond maid raise never debate lemon brown siren upset gun sibling lend write cloth success glove shrug cattle ability ivory'
#mnemonic_secret = 'ship floor pattern transfer fiscal diamond maid raise never debate lemon brown siren upset gun sibling lend write cloth success glove shrug cattle ability ivory'
#sk = mnemonic.to_private_key(mnemonic_secret)
#pk = mnemonic.to_public_key(mnemonic_secret)
#print("my public key = ", pk)


# In[38]:


#Connect to Algorand node maintained by PureStake
#Connect to Algorand node maintained by PureStake
algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = "B3SU4KcVKi94Jap2VXkK83xx38bsv95K5UZm2lab"
#algod_token = 'IwMysN3FSZ8zGVaQnoUIJ9RXolbQ5nRY62JRqF2H'
headers = {
   "X-API-Key": algod_token,
}

acl = algod.AlgodClient(algod_token, algod_address, headers) #initiate the client
min_balance = 100000 #https://developer.algorand.org/docs/features/accounts/#minimum-balance

def send_tokens( receiver_pk, tx_amount ):
    params = acl.suggested_params()
    gen_hash = params.gh
    first_valid_round = params.first
    tx_fee = params.min_fee
    last_valid_round = params.last

    #Your code here
    #generate an account
    mnemonic_secret = 'ship floor pattern transfer fiscal diamond maid raise never debate lemon brown siren upset gun sibling lend write cloth success glove shrug cattle ability ivory'
    sk = mnemonic.to_private_key(mnemonic_secret)
    pk = mnemonic.to_public_key(mnemonic_secret)
    print("my public key = ", pk)
    account_info = algod_client.account_info(pk)
    
    
    #prepare and sign the transaction
    tx = transaction.PaymentTxn(pk,tx_free,first_valid_round,last_valid_round,gen_hash,reciver_pk,tx_amount)
    signed_tx = tx.sign(account_a_private_key)
    txid = algod_client.send_transaction(signed_tx)
    
    #send the signed transaction
    tx_confirm = acl.send_transaction(signed_tx, headers ={'content-type':'application/x-binary'})
    #acl.status_after_block(first_valid_round+2)
    print("sender_pk=",sender_pk)
    print("txid = ", txid)
    wait_for_confirmation(acl, txid)
    
    return sender_pk, txid


# In[4]:


# Function from Algorand Inc.
def wait_for_confirmation(client, txid):
    """
    Utility function to wait until the transaction is
    confirmed before proceeding.
    """
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print("Waiting for confirmation")
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print("Transaction {} confirmed in round {}.".format(txid, txinfo.get('confirmed-round')))
    return txinfo


# In[ ]:


send_tokens( receiver_pk, tx_amount )

