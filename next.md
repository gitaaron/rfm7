# Next

* run probes using two nodes on same LAN but different hosts to generate logs (focus on figure 9)

  * ipfs-lookup-measurement

    * get docker build working with ports of more-logging to latest versions of repos

      * bitswap is not included in Dockerfile

      * docker networking issue (multiaddrs are not using ip that is reachable on local network)

        * figure out which docker network (ipvlan?) works with latest kubo

        * add note or script to create proper docker network(s) for docker-compose

      * use compiled version instead of copied version of 'agent'

      * generate key and pass it in

      * commit / share docker related things

      * in node/Dockerfile

        * clean 'agent' so that it compiles proper binary for docker image

        * look into using a different more lightweight base image?

          * do we need loki/grafana?


  * E2E logs/plots for figure 9

    * see `ipfs-lookup-measurement/analysis/download_logs.py` to see if it will work with docker containers

      * otherwise see if it will work for downloading from each 'agent' host OS

      * run plotting scripts in rfm7 against new logs

        * see `ipfs-lookup-measurement/analysis/plot.py` to see if it covers all graphs in 'figure 9'

          * is it using 'model' in dht-lookup-dataset?

        * see `ipfs-lookup-measurement/analysis/download_logs.py` to see how logs are collected


  * ensure README in `ipfs-lookup-measurement` outlines the steps I took to get E2E working

  * ensure README in `rfm7/dht-lookup-dataset` outlines the steps I took to get E2E working

  * commit / share rfm7

    * ensure link to all repos from this rfm7 repo's README

    * groom 'next/questions'

* have a look at what logs are getting sent to loki/grafana 'monitor'

* in `dht-lookup-dataset/models/model_log_line.py` check "Finish searching providers for cid" regex to see if both logs (with and without ctx err) are parsed

* concurrent fmt.Print intermixes logs to the same line eg/

  ```2022-09-03T15:15:58.631408-04:00: Got 20 closest peers to cid QmbGrjHw9ZkcjRHXXv19CBG5eLdeJSy1nPx5DiYFBGjSME from QmUgmRxoLtGERot7Y6G7UyF6fwvnusQZfGR15PuE6pY3aB(go-ipfs/0.10.0/): QmYkQ9SxH71iT6AttBajMqrrkPx1rmm8eBnRuZuqWDLBxB 12D3KooWJy8Ekrz5pkqbjnCG47xT4ZrkhL5mitU2y4ausrcoyW4z 12D3KooWErrj9qY9QAzJY7EG9vxv3rfVZbDoABfm5dHoPmNctLZD 12D3KooWDNsqsvv97nu5CNAVQtbP1WCeUrnCtxFxuZWBjLadRdxW 12D3KooWJ6v3eqqgq9WueXvUnAgfheqiwdcRrjyQezwnaGbDNRRx 12D3KooWAJD2hSzusJFD1Dsrimqd1qrcaqcFWfyuhEEFPAr6zYTa 12D3KooWDe1McaYzuN98VNvy25w3cui3D6FFj2Wnh41EBs9jpmbE 12D3KooWAf5DpVm2C17DHevZoda8HpBeTCuXnrkwrPjWbULfLp2q 12D3KooWCXddJU6H5CTSf7TqbgwqLRfpnPWHBsYhfoCw1n6HWgEB 12D3KooWFszGtW9JUgGaT12PKqsxtrrQnJJuHAm43RGLschDSRig 12D3KooWBxbnC5NbzmbPxUsGd7B1tkb8XMvgr57EpWUX6pe3ZD6n 12D3KooWCcn28S1oKBwAsCsNaethb9cTn4LTwLhf5V5usYA92zVw 2022-09-03T15:15:58.631468-04:00: Bitswap connect to peer 12D3KooWFRD52ag1zLYsbGW3UkyDg3Y7R36Sq8FxrNacMUAyLinN```

  * change logs from fmt.Print to use logger pkg

* E2E log/plogging with terraform/AWS

* E2E log/plotting for 'publish' events

  * create a `publish-events.md` similar to `retrieval-events.md`

  * ensure all logs are being generated in 'more-logging' port

  * create plotting scripts for publish (simiar to `cdf-*` for retrieval)


* E2E logging test (see `rfm7/dht-lookup-dataset/[retrieval|publish]-events.md` for full list of logs that should be included

  * run test against 'docker' and ensure all necessary logs are generated (see if they already exist)

# Later

* create architecture diagram reflecting E2E solution

* determine if the size of data processed will be a problem and come up with alternatives

* dashboard mockup

  * add missing information

    * connection setup time

    * geolocation / ASN

    * proximity of fetch to provider

  * additional controls

    * select a specific node or region

* finish proposal

  * include dashboard mockup

  * problems

    * how much data will be processed?

      * in 7 days, 1 month, 1 years

  * requirements

  * plan (include new architecture diagram)

      * review todos here + in repo

  * alternatives

  * risks

  * re-read grant + RFM and update list of questions

    * there is also an 'ipfs design questions' in keep

* create a complete list of regions or availability zones to be deployed to

* investigate tooling

  * how to provide filters and selectors efficiently

    * utilize pre-existing python scripts and pre-generate data for plotting each graph

    * efficient queries of large log data sets

      * hadoop

      * spark

      * time series

        * timescale db

        * prometheus

      * redshift

      * big query db

      * snowflake

  * extensible dashboard

    * Jupyter

    * Grafana

    * Sisense (+ Grafana?)

    * Periscope


