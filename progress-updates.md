# Aug. 27, 2022

I've completed a 'round' of the probe experiment without any errors except for an "address needed" report while performing a 'disconnect'.  

To get it working on my home network I applied the 'more-logging' changes to the latest kubo (0.14.0), go-bitswap, go-libp2p-kad-dht (to take advantage of hole punching since I'm behind a double nat).

Next I'll have a look at the logs generated to see if they can be used by python parsing scripts.
