# Next

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
