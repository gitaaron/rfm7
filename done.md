# Done

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
