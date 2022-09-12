# Done

# Monday Sep. 12, 2022


* get log generation (as working to date) set up on AWS and start sharing generated graphs (in fig. 9)

  * during `parse_log`

    * retrieve error: Illegal state transition from `State.GETTING_CLOSEST_PEERS` to `State.FETCHING`

      * should be in 'DIALING' phase
        * in order to get into 'DIALING' phase should be in `provider_peers`

          * in order to be in `provider_peers` must have `connected_to_provider`, `received_HAVE_from_provider` or `is_pvd_found`

            * `is_pvd_found` = "Found provider (\w+) for cid ([^\s]+) from (\w+)\((.+)\)"

            * `connected_to_provider` = "Connected to provider (\w+)\((.+)\) for cid ([^\s]+) from (\w+)\((.+)\)"

            * `receved_HAVE_from_provider` = "Got provider (\w+) for content (\w+)"

            * `is_pvd_found` line is not being generated properly
              * "Found provider {PROVIDER_ID} for cid .." is missing {PROVIDER_ID}

      * run using 'local remote' setup to verify problem is occuring during remote execution

      * add `{PROVIDER_ID}` to `is_pvd_found` line

      * take 'more-logging' on osx from ubuntu repo

        * compile with added line

      * run using 'local remote' setup to see if problem is fixed

        * log_parse should not produce errors "Illegal state transition" or "Not a match"

      * actual problem was in using `more-logging` form `wcgcyx` instead of `dennis-tra`


  * try generating graphs as already generated

    * try executing pre-exist 'dht-lookup-dataset' plots against new logs

    * try running analysis/plot.py

      * error parsing log lines (not expecting timestamp to start at line)

  * try calling 'download script'

  * see if I can use terraform scripts with my AWS account

    * error calling sts:GetCallerIdentity: InvalidClientTokenId: The security token included in the request is invalid
      * must enable regions in AWS account

    * agent does not load
      * can not connect to ec2 instance of test node
        * modify scripts to include my public ssh key

      * try running agent manually

        * looks like its failing without error message on key decoding (fixed in my ipfs-lookup-measurement fork)

        * modify terraform user script to use agent from my fork

  * sign up for individual AWS account and set it up with local dev machine (ubuntu)

    * get ec2 micro instance running and log into it

    * install AWS cli on villa and sign into personal account

    * install terraform cli on villa


  * clean up `ipfs-lookup-measurement` repo / push

    * stash docker stuff

    * remove debugging print statements

    * uncomment out code and see if 'clean' handler will work

* see `ipfs-lookup-measurement/analysis/download_logs.py` to see if it will work with docker containers

* run plotting scripts in rfm7 against new logs

  * see `ipfs-lookup-measurement/analysis/plot.py` to see if it covers all graphs in 'figure 9'

    * is it using 'model' in dht-lookup-dataset?

  * see `ipfs-lookup-measurement/analysis/download_logs.py` to see how logs are collected

  * in `dht-lookup-dataset/models/model_log_line.py` check "Finish searching providers for cid" regex to see if both logs (with and without ctx err) are parsed

* concurrent fmt.Print intermixes logs to the same line eg/

  ```2022-09-03T15:15:58.631408-04:00: Got 20 closest peers to cid QmbGrjHw9ZkcjRHXXv19CBG5eLdeJSy1nPx5DiYFBGjSME from QmUgmRxoLtGERot7Y6G7UyF6fwvnusQZfGR15PuE6pY3aB(go-ipfs/0.10.0/): QmYkQ9SxH71iT6AttBajMqrrkPx1rmm8eBnRuZuqWDLBxB 12D3KooWJy8Ekrz5pkqbjnCG47xT4ZrkhL5mitU2y4ausrcoyW4z 12D3KooWErrj9qY9QAzJY7EG9vxv3rfVZbDoABfm5dHoPmNctLZD 12D3KooWDNsqsvv97nu5CNAVQtbP1WCeUrnCtxFxuZWBjLadRdxW 12D3KooWJ6v3eqqgq9WueXvUnAgfheqiwdcRrjyQezwnaGbDNRRx 12D3KooWAJD2hSzusJFD1Dsrimqd1qrcaqcFWfyuhEEFPAr6zYTa 12D3KooWDe1McaYzuN98VNvy25w3cui3D6FFj2Wnh41EBs9jpmbE 12D3KooWAf5DpVm2C17DHevZoda8HpBeTCuXnrkwrPjWbULfLp2q 12D3KooWCXddJU6H5CTSf7TqbgwqLRfpnPWHBsYhfoCw1n6HWgEB 12D3KooWFszGtW9JUgGaT12PKqsxtrrQnJJuHAm43RGLschDSRig 12D3KooWBxbnC5NbzmbPxUsGd7B1tkb8XMvgr57EpWUX6pe3ZD6n 12D3KooWCcn28S1oKBwAsCsNaethb9cTn4LTwLhf5V5usYA92zVw 2022-09-03T15:15:58.631468-04:00: Bitswap connect to peer 12D3KooWFRD52ag1zLYsbGW3UkyDg3Y7R36Sq8FxrNacMUAyLinN```


## Sunday Sep. 4, 2022

* run probes using two nodes on same LAN but different hosts to generate logs (focus on figure 9)

  * ipfs lookup issue (times out)

    * controller should read key properly (same way as agent reads it)

    * get commented out code in 'agent' and 'controller' working

    * remove debugging logs

    * ipfs add/cat of random string using 'more-logging' does not work from shell (but latest version of kubo does work)

        * apply 'more-logging' edits to latest versions of kubo, go-libp2p-kad-dht and go-bitswap in order to:

            ```
              1. take advantage of hole punching

              2. building old versions of 'go-ipfs' fails ('quic-go' library doesn't build on Go v1.18 yet)
            ```

          * ensure all necessary logs are being written for 'more-logging' ports to latest versions

            * find log message that should be printed for each

            * fix 'log_parse' model

            * `finished_searching_providers_at` corresponding log does not appear to be anywhere in `more-logging`

              * "Finished searching providers for cid ${CID} ctx error: ${ERROR_MESSAGE:''}"

                should be

              * "Finish searching providers for cid ${CID} with ctx error: ${ERROR_MESSAGE:''}"

            * search for where log is generated in old versions of each repo and ensure it is also printed in new ports

            * manually verify all logs are printed in retriever

              * FIX: certain logs are missing timestamp at beginning (add in time.Now().Format(time.RFC3339Nano) to beginning of fmt.Println)

          * commit / publish new repos (kubo, go-libp2p-kad-dht, go-bitswap)


  * fix 'agent' loading issue
    * running agent before ipfs & not loading shell until api is called


  * fixed docker `/lib/x86_64-linux-gnu/libc.so.6: version ``GLIBC_2.32`` not found`
    * compiled agent from inside container

  * fixed host shell issue while loading 'IPFS' in 'handleGetID' handler by installing and running kubo locally

  * setup ubuntu server so that terraform m1 arch + docker networking is not an issue

  * run agents and monitor with docker

  * execute controller with node-list pointing to docker nodes

    * controller shows key error.. fixed by
        * output key with open-ssl instead of print from docker

        * remove '=' at end

    * @TODO err-msg encountered when dialing agent

  * build agent locally and run controller pointing to local agent

    * agent shows error with key (fixed by adding '=') to end


## Friday Aug. 19, 2022

* create dashboard mockup

  * create two views

    * select single region

    * selected single phase


* review python scripts

  * events (phases + milestones)

  * create a pie chart for slowest phases

  * create a bar chart for slowest regions

* regenerate figures 9(a-f) from [Design and Evaluation of IPFS: A Storage Layer for the Decentralized Web](http://bafybeidbzzyvjuzuf7yjet27sftttod5fowge3nzr3ybz5uxxldsdonozq.ipfs.localhost:8080/) using a subset of [dht-lookup-dataset](https://bafybeid7ilj4k4rq27lg45nceq4akdpetav6bcujgiym6vch5ml24tk2t4.ipfs.dweb.link) logs

  * convert histo/bar to CDF

  * generate all 6 graphs

    * figure out timeline of events

* submitted grant application

  * initial work plan

  * architecture diagram

  * thinking on 'popularity'

  * thinking on 'variance'
