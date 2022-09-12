# Next

* get log generation (as working to date) set up on AWS and start sharing generated graphs (in fig. 9)

  * use current logs to create all fig. 9 graphs (priority is retrieval / dht lookup)

    * events for retrieval

      * overall retrieval duration = content_fetch_duration + dht_walks_duration | done_retrieving_at - retrieval_started_at

      * dht_walks_duration = found_first_provider_at - retrieval_started_at

      * content_fetch_duration = done_retrieving_at - dial_started_at ?

    * events for publish

    * for 'publish' find proper events for each phase

    * seperate line for each graph by region

    * plot all graphs using both old logs and newly generated logs to verify newly generated look right

  * generate graphs using current logs and 'dht-lookup-dataset' to verify the generated logs are correct

  * get E2E working

    * analysis scripts

      * compare `dht-lookup-dataset` scripts with orig to ensure no other `more-logging` fixes were applied

      * add a 'main' file that invokes all scripts

      * accept cmd line -o arg and if it exists then write png to disk instead of displaying

      * make `log_parse` and `cdf_plot_*` all use common 'logs' location/filenames

      * move 'dht-lookup-dataset' scripts over to 'ipfs-lookup-measurement' repo

    * write a script that reads entire log and prints start/end date of log (assuming first/last lines are latest/oldest)

    * download script

      * ensure 'download script' only downloads logs for previous two days

      * download script downloads each log file with proper region name and places it somewhere accessible by plot
        * map download log to region (eg/ `0.log` -> `af_south_east.log`)

      * download scripts fixes

        * add 'logcli' as pre-req. to README before 'download'

        * update 'os.put.env' to use monitor ip out from terraform

  * terraform / setup
    * fix 'up.sh' key error
      * generate key if it does not exist

* ensure everything is shared properly

  * generate graphs periodically from AWS probe logs (run on local dev machine; output should be a graph for a time period eg/ hourly+daily)

    * create a `generate_graphs` script that

      * calls `download_logs` from each instance in AWS

        * uses `nodes-list.out` to connect to each instance

      * downloads the log from each instance on AWS and writes to a local log file based on region name

      * calls `parse` on each region log to generate output readable by models

      * calls `generate_graphs` that outputs a png along with a metadata file

        /graphs

          /1/graph.png

          /1/meta.json { time_generated, time_range }

      * calls `share_graph`

        * adds png to IPFS

        * generates an html page

          * lists out graphs

              * image

              * time generated

              * time range of logs

        * adds the html page to IPFS/IPNS

      * log each step along with exit status

    * add `generate_graphs` script to cron task to download logs and generate the graph hourly

    * do same thing for all graphs (publish + phases)


  * ensure README in `ipfs-lookup-measurement/analysis` is up to date

  * ensure README in `ipfs-lookup-measurement` outlines the steps I took to get E2E working

  * commit / share rfm7

    * ensure link to all repos from this rfm7 repo's README is correct

* E2E log/plotting for 'publish' events

  * create a `publish-events.md` similar to `retrieval-events.md`


  * create plotting scripts for publish (simiar to `cdf-*` for retrieval)


* E2E logging test (see `rfm7/dht-lookup-dataset/[retrieval|publish]-events.md` for full list of logs that should be included

  * run test against 'docker' and ensure all necessary logs are generated (see if they already exist)

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
