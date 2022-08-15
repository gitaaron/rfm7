# DHT Lookup Measurement Data

This repository contains log files of an IPFS DHT lookup measurement and code to parse analyse them. 

The log files that were analysed for the publication reside in the [`./2022-01-16-data`](./2022-01-16-data/) subdirectroy. 

The same measurement run continued until the 22nd of January and the subdirectory [`./2022-01-22-data`](./2022-01-22-data/) contains log files until this date. 

These files contain the same logs as the ones until `2022-01-16` and were not yet analysed by us. We provide them here for completeness reasons.

## General

The code to set up the measurement as well as the IPFS modifications can be found in the following repositories:

- [`ipfs-lookup-measurement`](https://github.com/dennis-tra/ipfs-lookup-measurement)
- [`go-ipfs`](https://github.com/dennis-tra/go-ipfs/tree/more-logging) - Branch `more-logging`
- [`go-libp2p-kad-dht`](https://github.com/dennis-tra/go-libp2p-kad-dht/tree/more-logging) - Branch `more-logging`
- [`go-bitswap`](https://github.com/dennis-tra/go-bitswap/tree/more-logging) - Branch `more-logging`

### Measurement setup

We provisioned six virtual machines in six different regions using AWS. 

Namely, the t2.small machines run in `me_south_1` (Bahrain), `ap_southeast_2` (Sydney), `af_south_1` (Cape Town), `us_west_1` (N. California), `eu_central_1` (Frankfurt) and `sa_east_1` (Sao Paulo).

On each machine we installed and start a modified `go-ipfs v0.10.0` instance.

The modifications consist of additional log messages to gather more information about peer interactions (see above).

Next to each IPFS instance we install an agent that can control the instance and in turn accepts commands by a central controller.

The central controller instructs the IPFS instances, via the agents, to publish or retrieve carefully crafted CIDs into/from the network. Details can be found in the `ipfs-lookup-measurement` repository.

### Lookup Procedure

The controller starts with generating 0.5 of random data.

It then transfers this data to the first controlled IPFS instance and instructs it to announce to the IPFS network that it is in possession of this data.

This step resembles the content publication process.

As soon as this step has finished the controller instructs all remaining controlled IPFS instances to retrieve the CID of the random data.

This step involves finding the provider record, connecting to the provider (first controlled IPFS node) and then fetching the 0.5 of random data.

As soon as all remaining IPFS instances have completed this process the controller instructs them to disconnect from the provider.

This last step is done so that we avoid retrieving content through Bitswap during the next experiment, since peers would remain directly connected.

In other words, this would test the performance of Bitswap and not the DHT lookup process.

## Log Analysis

### Prerequisites

Install [`poetry`](https://python-poetry.org/) for python dependency management and then install the dependencies:

```shell
poetry install
```

Then start a poetry shell to have all the dependencies available:

```shell
poetry shell
```

### Parsing

We recommend parsing the log files and saving a concise version of the information next to the log files. To do that run:

```shell
python3 log_parse.py
```

This command will take each log file in the `2022-01-16` directory, parse it and create a new file next to it called `<LOG_FILE_NAME>.p` (suffix `.p`). This file can be loaded later on way quicker.

### Analysis

The file `plot_retrievals.py` shows an example of how the files are loaded and analysed:

```shell
python3 plot_retrievals.py
```
