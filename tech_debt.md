# Next

  * 'Start listening at' log mechanism is not consistent with others

  * aws costs

    * remove timeout to avoid waste of ec2

    * reduce data transfer

      * is it coming from logging or file transfer?

        * if logging then reduce logging footprint to only necessary data

        * if file transfer then perform experiments with smaller file size more often


  * fix add `analysis` tests

  * calculate 'proximity' based on IP address instead of AWS region

  * add 'test' cmd line arg to 'generate-share' and if set:

    * skip download

    * skip publish to ipns

  * fix docker (and other places) nodes-list.out (new format)

  * change 'download' dir to somewhere besides 'tmp' so that logs are more easily retained

  * index page should sort by date printed instead of folder number

  * controller/config - should 3030 port be hardcoded when generating Host?

  * too many logs from `generate_share.sh`
    * analysis
      * print 'summary' instead of 'skipping'

  * experiment nodes seem to be going down unexpectedly

    * if a node is down (aka ID lookup fails)

      * add recovery routine

        * stop running experiment

        * terminate instance and recreate it

          * create 'terminate.sh' terraform that accepts NODE_NUM env var

          * call 'terminate.sh' from controller that passes in NODE_NUM env var

        * ensure refresh of 'nodes-list.out'

        * re-run experiment with refreshed 'nodes-list.out'

          * add in a 'wait-for-agents' that is run when controller first starts or is restarted

        * capture logs / healthcheck stats and send me an email


  * refactor: `analysis/plot_all.py`
    * all 'retrieval' filters should be part of 'ParsedLogFile' so that they are only performed once
    * get rid of `load_parsed_logs`
    * use 'ParsedLogFiles' instead of  List[ParsedLogFile]

  * refactor: `analysis/cdf_retrieval.py` to make use of `RetrievalPhase` enum

  * `generate_share.sh`
    * should call 'poetry install' then use `poetry run log_parse` and `poetry run plot_all`

---

  * ensure 'prod' logs are not conflicting with 'dev' location
    * search for `tmp/dht_lookup/logs` in project

  * log parsing should not parse the same log event twice

  * docker

    * should work in network without public access

    * add ipfs to controller to act as bootstrap server

    * agent docker-entry

      * depends on controller to be running first

      * gets peer id of controller

      * adds to its own bootstrap list


  * verification

    * compare `dht-lookup-dataset` scripts with orig to ensure no other `more-logging` fixes were applied

    * generate graphs using current logs and 'dht-lookup-dataset' to verify the generated logs are correct

  * terraform / setup

    * it should be possible to connect to each node created

  * in `generate_share.sh` shell script

    * log each step along with exit status

  * refactor: add phase calculation to 'retrieval' and 'pub' models
    * it may alrady exist (have a look at `duration_*`)
    * in publish see if there is a discrepancy between `find_node_started_at` and `provide_started_at` and if so then figure out what is happening before

  * probe health monitor

    * plot disk spage/memory/uptime for each probe in grafana dashboard

    * plot 'retrievals' or something similar in grafana


  * apply `more-logging` from `dennis-tra` instead of from `wcgcyx` to `go-libp2p-kad-dht`, `go-bitswap`, `kubo`

    * update terrform user script to pull from my repo again

    * test log output to ensure it is getting generated  properly

    * ensure all logs are being generated in 'more-logging' port

      * write a test to verify:

        * logs contains at least one proper retrieval and publication

        * all milestones are captured at least once for a single publication/retrieval

        * look at all 'regexes' parse by `log_parse` and ensure that each is matched at least once

  * get docker build working with ports of more-logging to latest versions of repos

    * run self contained (each container accesses each other over bridge)

      * make `controller` part of docker-compose

      * use bridge network so that each container can find one another

      * config bootstraps of kubo to talk to each other

      * verify its working as bootstrap by add/cat a file from one to another

      * try running `controller` and verify logs are generated


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

    * run test against 'docker' and ensure all necessary logs are generated

  * change logs from fmt.Print to use logger pkg?

  * issue with current 'more-logging' strategy

    * if an experiment fails then there is no log to indicate the experiment failed leaving the burden on the analysis to discard incomplete logs

    * benchmarking scripts are manually applied to code we are testing and it can become stale (we are benchmarking an old version)
