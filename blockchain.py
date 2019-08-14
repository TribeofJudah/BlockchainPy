#############################################################
# Author: Judah Masilela                                    #
# Date: 15 May 2018                                         #
#                                                           #
# Project:  Building a blockchain using Python              #
#                                                           #
#############################################################

#Initialize Blockchain as an empty array 
blockchain = []

def get_last_value():
    """Returns the value of the previous blockchain 
    """

    return blockchain[-1]

def add_value(transaction_amount, last_transaction=[1]):
    """
        Appends the new valueof the blockchain with the last value of the blockchain

        Arguments: 
            :transaction_amount: The new value that will be added to the blockchain 
            :last_transaction:   The previous value of the blockchain 
    """

    blockchain.append([last_transaction, transaction_amount])
    
def get_user_input():

    return float(input('Please insert the transaction amount: '))


# Acquiring user input 
tx_amount = get_user_input()
add_value(tx_amount)

tx_amount = get_user_input()
add_value(last_transaction=get_last_value(), transaction_amount=tx_amount)

tx_amount = get_user_input()
add_value(tx_amount, get_last_value())

print(blockchain)


