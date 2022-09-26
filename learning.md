* investigate how blocks are fetched over bitswap in kubo

  * if more than one provider: how are blocks being downloaded?

    * potential options:

      * first provider that produces a 'HAVE' ?

      * first provider that produces a 'BLOCK' ?

      * all providers but different blocks at the same time ?

      * all providers any block?

  * what 'percentage' of content is typically fetched from 'first provider'

    * if typically majority is first provider I will focus on this

      OTHERWISE

    * intercept 'block' bitswap events and use those to determine % of content fetched by each provider

        * better answer of 'where content is coming from'

          * try running agent 'ipfs' with debug level to see 'block' bitswap responses

            * add 'received block' event to python 'retrieve' model

            * compare 'num_providers' with more than one bitswap 'block'

          * try running dennis-tra `more-logging` with `host` setup

            OR

          * fix my port of `more-logging` so that they work with current parser

            * look at `dennis-tra` `more-logging`

            * use 'host' setup for testing

            * should be able to run `quick_stats`

