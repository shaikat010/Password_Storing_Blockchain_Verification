from BlockchainDataBase.Blockchain import Blockchain

bc = Blockchain()

# Genesis block can only be inserted once
print(bc.validate_chain())

# This gives the block objects in the blockchain
print(bc.chain)

# adding a new block here
data = {"Data": 123}
bc.add_block(data)

# adding a new block here
data = {"Data": "3"}
bc.add_block(data)

# adding a new block here
data = {"Data": "4"}
bc.add_block(data)

# printing the blocks so far
#bc.print_blocks()

# This gives us a boolean value of whether out chain is valid or not
bc.validate_chain()

# This prints the database object
#print(bc.data_base)

# This is the status of the prints blocks function
print("These are the blocks")

# Gives us the length or the height of the chain
print(bc.print_blocks())

print(len(bc.chain))