# Aug. 27, 2022

I've completed a 'round' of the probe experiment without any errors except for an "address needed" report while performing a 'disconnect'.  

To get it working on my home network I applied the 'more-logging' changes to the latest kubo (0.14.0), go-bitswap, go-libp2p-kad-dht (to take advantage of hole punching since I'm behind a double nat).

Next I'll have a look at the logs generated to see if they can be used by python parsing scripts.

# Sep. 25, 2022

The experiment controller was altered to run two different 'main player' modes in conjunction with each other.  The 'main player' is either a publisher or a retriever of content and all other agents are the opposite.

In 'publisher' main player mode there are many 'retrievers' of the same CID at the same time (this was the classic setup) and in 'retriever' main player mode there are many 'publishers' of the same CID.

The 'retriever' mode was added to look at the effects of retrieving the same content from different providers in different regions.

Analysis of a 4 hour period (sample size of 23 'many provider' retrievals and 116 'single provider' retrievals) shows a 43.5% likelihood of a slow (>3 sec.) 'many provider' retrieval and 56% (>3 sec.) 'one provider' retrieval.  It might also be interesting to see how the same numbers are effected by different file sizes (currently using 0.5 MB size).

A trend for 'total duration' over time was also added for the last 4 hours and since the beginning of time which you can see here - ipfs://bafybeifds2cd6zmr2mohgyqwxm52zsrcnsjvamaiwz7bzuex2t3zel6cou/