# Next

* analysis

  * include region breakdown trends for other phases besides total duration (excluding 'initiated')

* factors

  * file size with different orders of magnitude (eg/ 0.5 Mb, 5 Mb, 50 Mb)

    * report

        * is there an inconsistency between file size and any retrieval latency graphs?

        * expect: other steps besides 'fetching' should stay constant and 'fetching' should increase linearly with file size

    * collection

      * controller should perform several different runs for each file size with 'retriever' as mainplayer mode

      * logging should map CID to file size

        * EITHER

          * `more-logging` fork should be updated to include file size with CID with retrieval is initiated

        * OR

          * agent logs are made available to analysis (uploaded to loki DB and downloaded)

    * analysis

      * retrieval model should have a 'file size' field (default to 0.5 Mb)

      * log parsing should populate 'retrieval model' with file size

      * plot all trends for each file size

      * breakdown of bar charts for phase duration with three buckets (one for each file size)

  * uptime of the requesting peers being live in the network

    * report

      * how does agent 'uptime' effect duration of the different phases (especially 'getting_closest_peers')

    * experiment should send 'restart' signal to each instance of kubo periodically (every hour)

    * more-logging outputs 'uptime' along with CID when retrieval begins

    * analysis

      * retrieval model has an 'origin uptime' field

      * histogram plot: average duration of each phase for different uptime buckets based on a 5 min. increment

  * how long a file has been published for

    * analysis

      * for each phase a trend with a breakdown of 'publish age'

  * popularity

* share page

  * group / order related graphs and include headings for better readability

  * include `quick_stats`

  * plot certain `quick_stat` trends since beginning of time

* analysis

  * should differentiate between various 'factors/constants/controls' (otherwise they might be meaningless)

  * each graph (or section) should have a number of results used (sample size)

* final report

  * check out other final reports in network measurements repo

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
