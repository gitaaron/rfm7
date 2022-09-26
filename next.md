# Next

* change 'download' dir to somewhere besides 'tmp' so that logs are more easily retained

* plot trends of different phases (excluding initial) with a region breakdown

* outstanding features

  * factors

    * geographic proximity

      * answer question 'is closest copy content generally being served' (assume closest copy is coming from first provider)

        * analysis should be able to decider the peer id of the actual content provider from the 

            * percentage of runs where node fetches content from closest (geographically)

              * isClosestNeighbor (fetcher:region_1, provider:region_2, alternatives:[region_3, region_4...]) returns bool

              * getProximity (region_1, region_2) returns proximity

              * 'retrieval' model

                * getContentProvider (returns peer id of peer that provided content)

              * for a certain time period:

              * percentageOfCloseFetches(retrievals)

                * iterate over all 'retrievals'

                * determine if retrieve happened with 'isClosestNeighbor'

          * generate new reports

            * percentage of 'closest neighbor' retrievals vs 'non nearest neighbor' retrievals

            * comparison of total latency / fetch latency between 'neighbor' fetches and 'long distance' fetches

    * file size (different orders of magnitude 0.5 Mb, 5 Mb, 50 Mb)

      * see if there is inconsistency between file size and any retrieval latency graphs

      * expect: other steps besides 'fetching' should stay constant and 'fetching' should increase linearly with file size

    * uptime of the requesting peers being live in the network

    * how long a file has been published for

      * for each phase a trend with a breakdown of 'publish age'

    * popularity

  * analysis should differentiate between various 'factors/constants/controls' (otherwise they might be meaningless)

  * each graph (or section) should have a number of results used

  * check out final reports in network measurements repo

---

* ipns link is not loading from ipfs gateway
  * simple way to build homepage somewhere with updated links


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
