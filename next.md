# Next

* outstanding features

  * trends: stability of measurements over time (ie/ is a node/region consistently involved in slow lookups?)

  * factors
    * geographic proximity

    * effects of file size

    * popularity

    * uptime of the requesting peers being live in the network

  * additionally, we could show the distribution of lookups in a specific probe, i.e. in a specific section of the network, in order to have a sense of the DHT lookup times to be expected for someone in the probe's premises.

  * each graph should have a number of results used

---

* look into why homepage is not loading from ipfs gateway

* terraform / setup
  * fix 'up.sh' key error
    * generate key if it does not exist

* in `ipfs-lookup-measurement/README'

    * outline the steps I took to get E2E working

      * run experiment

      * download logs, generate and share results

    * add 'logcli' as pre-req. to README before 'download'

    * remove old figs

    * ensure all 'config' options are documented

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
