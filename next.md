# Next

* factors

  * filesize

    * collection

      * logging should map CID to file size

          * controller/agent outputs a single line with CID / size


          * agent logs are made available to analysis (uploaded to loki DB and downloaded)

            * `promtail config` includes `agent.log`

            * `download_logs.py` downloads `agent.log` along with `all.log`

---

            * analysis parses new filename to create proper regions

          * update cloud agents to upload new logs

            * terraform

              * update testing_node to refer to gitaaron repo's promtail


      * controller should perform several different runs for each file size (0.5, 5, 50 Mb) with 'retriever' in mainplayer mode

---

      * terraform
          * terminate/up all agent nodes

    * analysis

      * update `log_parse,plot_all,quick_stats` to look for new `ipfs_region.log` name
        * `ipfs_region.py` should be parsed first
        * `agent_region.py` should be parsed after so that it can find the retrieval model to update with file-size

      * log parsing should populate 'retrieval model' with file size

        * retrieval model should have a 'file size' field (default to 0.5 Mb)

        * for each region

            * load both ipfs and agent logs

            * read agent log and update to retrieval with corresponding CID

      * plot all trends for each file size

      * breakdown of bar charts for phase duration with three buckets (one for each file size)

      * create 'phase' pie chart for each possible filesize
        * ensure 'val' in pie chart is average instead of total (that should be explained somewhere)

    * report

        * is there any inconsistency between file size and any retrieval latency graphs?

        * expect: other steps besides 'fetching' should stay constant and 'fetching' should increase linearly with file size


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

  * geographic proxomity

    * see what happens when nodes are in the same region

  * popularity

  * node health stats (uptime/memory)

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
