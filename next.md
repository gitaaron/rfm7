# Next

* run probes using two nodes on same LAN but different hosts to generate logs (focus on figure 9)

  * setup ubuntu server so that terraform m1 arch + docker networking is not an issue

    * install from ISO

    * install docker

    * clone ipfs-lookup-measurement repo

    * try running docker-compose up on it

  * after review (test)

    * rand.seed should be called in 'simplenode.go' when generating 0.5 MB random byte array ?

* code review repos for generating logs

  * what is missing from logs to ensure all data for necessary measurements is complete?

    * how is file advertised by publishers directly to retrievers? custom pubsub protocol?

* create architecture diagram reflecting E2E solution

* determine if the size of data processed will be a problem and come up with alternatives

* mockup

  * add missing information

    * connection setup time

    * geolocation / ASN

    * proximity of fetch to provider

  * additional controls

    * select a specific node or region

# Later

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

* prep for meeting tomorrow

  * re-read grant + RFM and update list of questions

    * there is also an 'ipfs design questions' in keep

* create a complete list of regions or availability zones to be deployed to

--- Later

* dashboard mockup

  * create two views

    * single region

    * single phase

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


