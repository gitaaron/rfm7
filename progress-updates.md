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


# Aug. 27, 2022

I've completed a 'round' of the probe experiment without any errors except for an "address needed" report while performing a 'disconnect'.  

To get it working on my home network I applied the 'more-logging' changes to the latest kubo (0.14.0), go-bitswap, go-libp2p-kad-dht (to take advantage of hole punching since I'm behind a double nat).

Next I'll have a look at the logs generated to see if they can be used by python parsing scripts.


