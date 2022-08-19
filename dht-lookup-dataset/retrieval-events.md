# Retrieval Events

## Milestones

The following is an ordered sequence of events for retrieval.

```
  retrieval_started_at: datetime
  get_providers_queries_started_at: Optional[datetime]
  found_first_provider_at: Optional[datetime]
  dial_started_at: Optional[datetime]
  connected_at: Optional[datetime]
  stream_opened_at: Optional[datetime]
  # there could be more than one provider
  received_first_HAVE_at: Optional[datetime]
  done_retrieving_at: Optional[datetime]
  finished_searching_providers_at: Optional[datetime]
```

## Phases

```
  INITIATED = 1
  GETTING_CLOSEST_PEERS = 2
  DIALING = 3
  FETCHING = 4
  DONE = 5
  DONE_WITHOUT_ASKING_PEERS = 6
```

## State Milestone Mapping

```
{
  GETTING_CLOSEST_PEERS: get_providers_queries_started_at,
  DIALING: dial_started_at,
  FETCHING: connected_at,
  DONE: done_retrieving_at | finished_searching_providers_at
  DONE_WITHOUT_ASKING_PEERS: done_retrieving_at | finished_searching_providers_at
}
```

## Phase Latency Calculation

```
{
  INITIATED: get_providers_queries_started_at - retrieval_started_at
  GETTING_CLOSEST_PEERS: dial_started_at - get_providers_queries_started_at,
  DIALING: connected_at - dial_started_at,
  FETCHING: done_retrieving_at - connected_at,
  DONE: done_retrieving_at | finished_searching_providers_at
}
```
