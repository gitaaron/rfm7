# Next

* change 'download' dir to somewhere besides 'tmp' so that logs are retained

* plot trends of 'total duration' with a region breakdown

* outstanding features


  * factors

    * geographic proximity

        * investigate how blocks are fetched over bitswap in kubo

          * if more than one provider: how are blocks being downloaded?

            * potential options:

              * first provider that produces a 'HAVE' ?

              * first provider that produces a 'BLOCK' ?

              * all providers but different blocks at the same time ?

              * all providers any block?

          * what 'percentage' of content is typically fetched from 'first provider'

            * if typically majority is first provider I will focus on this

              OTHERWISE

            * intercept 'block' bitswap events and use those to determine % of content fetched by each provider

---

        * have a way to filter results based on 'player mode' type

        * better answer of 'where content is coming from'

          * try running agent 'ipfs' with debug level to see 'block' bitswap responses

            * add 'received block' event to python 'retrieve' model

            * compare 'num_providers' with more than one bitswap 'block'

          * try running dennis-tra `more-logging` with `host` setup

            OR

          * fix my port of `more-logging` so that they work with current parser

            * look at `dennis-tra` `more-logging`

            * use 'host' setup for testing

            * should be able to run `quick_stats`


        * analysis should be able to filter logs between controller publisher modes

        * analysis should be able to decider the peer id of the actual content provider from the 



      * analysis

          * new reports

            * percentage of runs where node fetches content from closest (geographically)

              * isClosestNeighbor (fetcher:region_1, provider:region_2, alternatives:[region_3, region_4...]) returns bool

              * getProximity (region_1, region_2) returns proximity

              * 'retrieval' model

                * getContentProvider (returns peer id of peer that provided content)

              * for a certain time period:

              * percentageOfCloseFetches(retrievals)

                * iterate over all 'retrievals'

                * determine if retrieve happened with 'isClosestNeighbor'

            * comparison of total latency / fetch latency between 'neighbor' fetches and 'long distance' fetches

          * breakdown reports by region

          * current analysis should continue to be performed against 1 publisher

    * effects of file size

    * popularity

    * uptime of the requesting peers being live in the network

  * additionally, we could show the distribution of lookups in a specific probe, i.e. in a specific section of the network, in order to have a sense of the DHT lookup times to be expected for someone in the probe's premises.

  * each graph should have a number of results used

  * trends: stability of regions over time


---

* look into why homepage is not loading from ipfs gateway

* terraform / setup
  * fix 'up.sh' key error
    * generate key if it does not exist

* in `ipfs-lookup-measurement/README`

    * outline the steps I took to get E2E working

      * run experiment

      * download logs, generate and share results

    * add 'logcli' as pre-req. to README before 'download'

    * remove old figs

    * ensure all 'config' options are documented


    * add "development with docker" section



* ensure README in `ipfs-lookup-measurement/analysis` is up to date

  * add sample logs to the 'analysis' folder so that it can be immediately run by someone checking out repo

* rename 'figs' to 'old/figs'

* determine timezone logs are generated as 

* commit / share rfm7

  * ensure link to all repos from this rfm7 repo's README is correct

* grant documentation

  * create architecture diagram reflecting current E2E solution

  * review grant / outline what is left for grant to be completed and what steps need to be taken to complete work

  * update ./later.md

  * update ./proposal.md

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

  * include a complete list of regions or availability zones that probes are deployed to
