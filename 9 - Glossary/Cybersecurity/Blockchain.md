Tags: [[netsec]]

The Blockchain is a network based construct that relies on decentralization of the transactional record keeping, known as the **Open Public Ledger**

# Open Public Ledger

This is a record copied across all nodes in the network, relying on the fundamentally impossible nature of faking or forging transactions at scale.

The ledger is composed of blocks which are just batches of data, and each new block is concatenated, denoting an update to the state of the ledger. Each block contains hashes of information, which is how state can be known to be immutable. Updates to the chain are broadcasted at scale and require validation to be accepted. New blocks in the chain also contain references to previous chains, which establishes chronological order.

Transactional recording is done through broadcasting where the addition is done and at what time.  This is done through cracking some puzzle, at which point the network is signaled that some block is ready to be added. This is called **Proof of Work**. At that point, the other nodes in the network will use some agreed upon mechanism to ensure that the transaction is valid, and if so, will add it to the ledger.
