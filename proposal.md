# Distribution of DHT lookup times and Breakdown of Content Routing Latency

## How do you plan to approach this project? What are your initial ideas for how to approach the design, architecture, and solution implementation for the project?

Please see the attached Figma files for a proposed architecture.  The technologies I intend to lean on are K8s for controlling the 'probe' nodes and libp2p for invoking the DHT with appopriate hooks for logging the appropriate events (each log will have a timestamp).

After each run, the logs will be uploaded to a centralized 'log collector' and analyzed / interpreted into a CDF format that the dashboard can then interpret.

Architecture: https://www.figma.com/file/P2OFIBo9iibkIpYJ3XKj0e/DHT-measurements-architecture?node-id=0%3A1

## Milestone Notes

### Detailed breakdown of methodology plan

The deliverable of this milestone will be to clarify on what will be delivered and how it will be implemented.

  * review of prior work

  * a mockup of the dashboard (non-interactive)

    * grafana?

  * CDF data definition + fixtures (aka dummy data)

  * hopefully some initial POCs can also be provided but most importantly the necessary technology will be understood

    * libp2p libraries / hooks

    * terraform / k8s methodology

### Experiment Scripts / POC

There will be working prototypes of:

  * interactive dashboard with all controls using 'dummy data'

  * probe publisher / retriever

    * given a file the retriever will download the file from the publisher over the public IPFS network and each will record the appropriate logs in order to make all latency measurements as laid out in the requirements

  * controller

      * a README demonstrating how to run the controller

        * provides a sample of config data

      * generates a random files and passes it to each peer

### Initial Results / Proof of Concept

  * dashboard showing actual results (not dummy data)

  * controller

      * how 'popularity' is made deterministic

        * defining as 'how many other peers asked for the same file'

        * perhaps use a staged approach where a new random file is generated for each retriever

        * each retriever is instructed to download a new file that was used in the previous stage

        * popularity of the file would then correspond to the stage it is at (the third stage = popularity of 3)

        * file allocation in each stage is randomized to provide better sampling



### Reproducible Experiments & Stable Results

  * the bar chart might be converted to a candlestick plot to show variance over time

  * scheduling of batch jobs

    * experient initiator

    * log analyzer

### Final Report

  * final architecture diagram documenting all technology / implementation steps taken

  * shortcomings of current system design (if any)

  * interpretation of results

  * 'edge' locations (based on geography and network topology)
