# Proposal

The following is a proposal for [RFM7: Distribution of DHT lookup times and breakdown of content routing latency](https://www.dgm.xyz/grants/cieOsJkIqWSQkk9obsrO) grant.

## Background / Prior Work


[`Design and Evaluation of IPFS: A Storage Layer for the Decentralized Web`](http://bafybeidbzzyvjuzuf7yjet27sftttod5fowge3nzr3ybz5uxxldsdonozq.ipfs.localhost:8080/) using a subset of [dht-lookup-dataset](https://bafybeid7ilj4k4rq27lg45nceq4akdpetav6bcujgiym6vch5ml24tk2t4.ipfs.dweb.link)

  * sample CDFs showing distribution of latency

  * link to DHT Measurements Dataset

[`DHT Measurements Dataset`](https://bafybeid7ilj4k4rq27lg45nceq4akdpetav6bcujgiym6vch5ml24tk2t4.ipfs.dweb.link)

  * contains python scripts

    * parsing logs into a more efficient data format

    * data modeling into 'retrieval' and 'publish' records

    * sample `plot_retrievals.py` that shows how the data can be analysed to produce a histogram showing distribution of latency

  * README contains links to other supporting work for generating logs

[`ipfs-lookup-measurement`](https://github.com/dennis-tra/ipfs-lookup-measurement)

  * sample terraform setup for probe orchestration

[`go-ipfs`](https://github.com/dennis-tra/go-ipfs/tree/more-logging) - Branch `more-logging`

[`go-libp2p-kad-dht`](https://github.com/dennis-tra/go-libp2p-kad-dht/tree/more-logging) - Branch `more-logging`

[`go-bitswap`](https://github.com/dennis-tra/go-bitswap/tree/more-logging) - Branch `more-logging`

@TODO - include architecture diagram along with writeup that describes how current E2E solution works

## Goal

To have a dashboard that enables protocol designers to better understand the performance of the IPFS DHT while downloading content so that they can use it to make better informed design decisions in the future

The dashboard should help uncover:

  * factors causing slowdowns

  * 'edge' locations (based on geography and network topology)
