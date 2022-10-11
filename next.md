# Next

  * add some simulated logs and tests for analysis to validate calculations

  * analysis of retrieval duration vs publish age (how long a file was published for before it was retrieved)

  * certain plots / stats should be calculated with filesize / num providers held as constant

  * do plots for last 4 hours along with since start of time

---

* factors

  * agent uptime (uptime of the requesting peers being live in the network)

    * analysis

      * in `generate_*_parsed_log_files`

        * load `agent_info` and all agent logs files

        * for each agent log file

        * parse for `start_times`

        * update `model_agent` with a list of `start_times`

        * add a `latest_start_time_from(reference_time)` -> gives the latest time that does not exceed the referenc_time

      * each retrieval has an `agent_started_at` field

        * when a retrieval is created 

            * find `agent_started_at`

              * find agent by region

                  * 'Agents' has as 'lookup_by_region' method

              * invoke `latest_start_time_from(retrieval_started_at)`

            * pass in `agent_started_at` as a param to constructor

              * should accept a None type

        * add an `agent_uptime` field that calculates difference between `retrieval_started_at` and `agent_started_at`

      * calculate

        * max / min agent uptime in completed retrievals

        * num retrievals in various 'agent uptime' buckets

          * 0-60 min. spaced by 10 min.

          * 0-4 hrs. spaced by 1 hour

      * plot

        * for each phase

          * agent uptime in buckets (x-axis) and duration (y-axis)


    * report

      * how does agent 'uptime' effect duration of the different phases (especially 'getting_closest_peers')

    * experiment should send 'restart' signal to each instance of kubo periodically (every hour)

    * more-logging outputs 'uptime' along with CID when retrieval begins

    * analysis

      * retrieval model has an 'origin uptime' field

      * histogram plot: average duration of each phase for different uptime buckets based on a 5 min. increment


  * how long a file has been published for ('publish age')

    * analysis

      * calculate 'publish age' = difference of first publish end time and retrieval start time

        * need a way to correlate between a publish and a retrieve

          * since new CIDs are created for each `DoRun`

            * in `LogFile.parse`

              * create a 'Runs' model

                * map[CID:Run]

                  * Run

                    * first_publish

                    * list of publishes

              * when creating a new Publish

                  * update 'Runs' with new publish event

            * in `Runs` model

                * implement a `first_publish_date(CID)`

            * in LogFile.parse

              * when creating a new Retrieval or Publish

              * update Run 'publishers' and 'retrievals' list accordingly

          * in `helpers/calc` implement a `publish_age(retrieval, runs)`

    * analysis

      * quick stat

        * average/min/max publish age

        * average retrieval duration of average/min/max publish ages

      * plot
        * a cdf for each phase of retrieval duration with a breakdown of 'publish age'

  * agent health stats (`load_avg/memory`)

    * report

      * are there any anomolies in any of the `health stats`

      * how does any anomology effect total duration of retrieval

  * filesize

    * analysis

      * plot

        * breakdown of bar charts for phase duration with three buckets (one for each file size)

        * create 'phase' pie chart for each possible filesize

        * ensure 'val' in pie chart is average instead of total (that should be explained somewhere)

      * other charts may need to be filtered on filesize and num publishes


* share page

  * group / order related graphs and include headings for better readability

  * include `quick_stats`

  * plot certain `quick_stat` trends since beginning of time

--- before tuesday

* error messages
    * analysis

      * look into error statement

        ```
          not using peer QmZ3eUjBqpCe8tFX2Uc2QR2bmRgnvrgiADHeMkxBNAjs41 (go-ipfs/0.8.0/48f94e2) for cid Qmbe6f2sNtYGjjuCsxtDm17kCVBcgsFmnbGWAAHhVkGUDS
          Multiple publications going on: QmZ3eUjBqpCe8tFX2Uc2QR2bmRgnvrgiADHeMkxBNAjs41 (go-ipfs/0.8.0/48f94e2) using CID: QmdfAqTyGSi3Nhce9GBDDzXigyJN4ZXEwVuwE4CxTxwTjr - Qmbe6f2sNtYGjjuCsxtDm17kCVBcgsFmnbGWAAHhVkGUDS QmdfAqTyGSi3Nhce9GBDDzXigyJN4ZXEwVuwE4CxTxwTjr
        ```

  * `controller`
    * investigate the following error -
      ```
      2022-10-06T18:05:28.378Z        INFO    controller      simplenode/simplenode.go:76     Response of disconnection from http://node1:3031 is: + /app/kubo/cmd/ipfs/ipfs swarm peers
      ```


* controller

  * if running main loop from run.sh then delayed run will not completed

  * each run takes way too long

    * decrease number of loops for 'perform small' to 2

    * remove loop logic from `run.sh` and move it back to controller


* analysis

  * should differentiate between various 'factors/constants/controls' (otherwise they might be meaningless)

  * each graph (or section) should have a number of results used (sample size)

* final report

  * check out other final reports in network measurements repo

--- Monday

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

