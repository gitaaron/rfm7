# Oct. 11, 2022

* altered experiment controller to gather other measurements

  * agent uptime

  * filesize

  * health stats

  * publish age

* calcuating avg. total retrieval duration by filesize

  * low confidence in results since there seems to be no correlation between fetch duration and file size

* plotting a histogram of avg. total retrieval duration by agent uptime

  * also seems to have no correlation

Here are some plots fora recent ~36 hour period -

ipfs://bafybeibsstocvkks27iaeluhnnzxe2af5wqknsabphltjnelyaj4frc6ey/

Accompanying quick stats for a recent ~36 hour period -

```
{
    "num_retrievals": 3473,
    "has_file_size": 3466,
    "slow_retrievals (>4 sec.)": 499,
    "percent_retrievals_are_slow": "14.368%",
    "many_providers_count": 565,
    "single_provider_count": 2908,
    "average_providers_per_retrieval": 1.6435358479700548,
    "slow_many_providers": "12.2%",
    "slow_one_provider": "87.8%",
    "many_providers_slow_likelihood": "10.8%",
    "one_provider_slow_likelihood": "15.1%",
    "num_fpn": 2776,
    "num_non_fpn": 365,
    "avg_duration_fpn": "3.167 sec.",
    "avg_duration_non_fpn": "2.951 sec.",
    "fpn_slow_likelihood": "15.238%",
    "non_fpn_slow_likelihood": "12.055%",
    "phase_avg_duration": {
        "count": 3473,
        "TOTAL": "3.14 (sec.)",
        "INITIATED": "1.031 (sec.)",
        "GETTING_CLOSEST_PEERS": "0.899 (sec.)",
        "DIALING": "0.358 (sec.)",
        "FETCHING": "0.851 (sec.)"
    },
    "file_size_avg_duration": {
        "5242900": {
            "count": 346,
            "TOTAL": "2.904 (sec.)",
            "INITIATED": "1.028 (sec.)",
            "GETTING_CLOSEST_PEERS": "0.854 (sec.)",
            "DIALING": "0.349 (sec.)",
            "FETCHING": "0.673 (sec.)"
        },
        "52429000": {
            "count": 304,
            "TOTAL": "3.146 (sec.)",
            "INITIATED": "1.037 (sec.)",
            "GETTING_CLOSEST_PEERS": "0.914 (sec.)",
            "DIALING": "0.358 (sec.)",
            "FETCHING": "0.837 (sec.)"
        },
        "524290": {
            "count": 341,
            "TOTAL": "3.225 (sec.)",
            "INITIATED": "1.032 (sec.)",
            "GETTING_CLOSEST_PEERS": "0.965 (sec.)",
            "DIALING": "0.404 (sec.)",
            "FETCHING": "0.825 (sec.)"
        },
        "52429": {
            "count": 2475,
            "TOTAL": "3.159 (sec.)",
            "INITIATED": "1.031 (sec.)",
            "GETTING_CLOSEST_PEERS": "0.896 (sec.)",
            "DIALING": "0.354 (sec.)",
            "FETCHING": "0.879 (sec.)"
        },
        "null": {
            "count": 7,
            "TOTAL": "3.585 (sec.)",
            "INITIATED": "1.009 (sec.)",
            "GETTING_CLOSEST_PEERS": "0.645 (sec.)",
            "DIALING": "0.315 (sec.)",
            "FETCHING": "1.616 (sec.)"
        }
    },
    "uptime": {
        "count": 803,
        "total": 4827683.873598,
        "max": "12239.907 (sec.)",
        "min": "33.721 (sec.)",
        "avg_uptime": "6012.06 (sec.)"
    }
}
```


# Sep. 29, 2022

The following quick stats were generated on a 4 hour period.

```
{
    "num_retrievals": 343,
    "slow_retrievals (>4 sec.)": 56,
    "percent_retrievals_are_slow": "16.327%",
    "many_providers_count": 63,
    "single_provider_count": 280,
    "avg_providers_per_retrieval": 1.641,
    "slow_many_providers": "12.5%",
    "slow_one_provider": "87.5%",
    "many_providers_slow_likelihood": "11.1%",
    "one_provider_slow_likelihood": "17.5%",
    "percent_first_provider_nearest[fpn]": "87.941%",
    "num_fpns": 299,
    "num_non_fpns": 38,
    "avg_duration_fpns": "3.235 sec.",
    "avg_duration_non_fpns": "2.865 sec.",
    "fpn_slow_likelihood": "15.719%",
    "non_fpn_slow_likelihood": "15.789%"
}
```

The likelihood of a 'slow retrieval' is about the same for retrievals that occur from nearest neighbors vs non nearest neighbors, however, the average total duration is ~370ms slower for non nearest neighbor first providers.

The percent of retrievals that have a nearest first provider is ~87.9%.

This means that roughly 12% of retrievals that have relatively fast other phases could have a total duration improved by ~11.5%.

# Sep. 25, 2022

The experiment controller was altered to run two different 'main player' modes in conjunction with each other.  The 'main player' is either a publisher or a retriever of content and all other agents are the opposite.

In 'publisher' main player mode there are many 'retrievers' of the same CID at the same time (this was the classic setup) and in 'retriever' main player mode there are many 'publishers' of the same CID.

The 'retriever' mode was added to look at the effects of retrieving the same content from different providers in different regions.

Analysis of a 4 hour period (sample size of 23 'many provider' retrievals and 116 'single provider' retrievals) shows a 43.5% likelihood of a slow (>3 sec.) 'many provider' retrieval and 56% (>3 sec.) 'one provider' retrieval.  It might also be interesting to see how the same numbers are effected by different file sizes (currently using 0.5 MB size).

A trend for 'total duration' over time was also added for the last 4 hours and since the beginning of time which you can see here - ipfs://bafybeifds2cd6zmr2mohgyqwxm52zsrcnsjvamaiwz7bzuex2t3zel6cou/


# Sep. 15, 2022 

A `generate_share.sh` script was added that downloads logs for the last four hours and puts them into a directory index (along with older logs) so that the analysis script can be performed against them and the contents can be read from an html page published over IPFS.

An index of all snapshots can be found at `ipns://k51qzi5uqu5dhwn2mmkqzuf1owd1dp2sfnjxukykm82dr3r3cvckodk4ml8c40/`

# Aug. 27, 2022

I've completed a 'round' of the probe experiment without any errors except for an "address needed" report while performing a 'disconnect'.  

To get it working on my home network I applied the 'more-logging' changes to the latest kubo (0.14.0), go-bitswap, go-libp2p-kad-dht (to take advantage of hole punching since I'm behind a double nat).

Next I'll have a look at the logs generated to see if they can be used by python parsing scripts.


