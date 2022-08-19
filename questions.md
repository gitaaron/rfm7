# Questions

* grant/rfm clarifications

  * what am I choosing?

    * "ideally, we should have the option (e.g., in a dashboard-style tool) to chose to see the distribution of DHT lookups of the last 7 days, which will output a histogram with the time invested to perform a lookup in the DHT by the different probes."

  * does 'buckets' here mean delay range (eg/ 0-500ms)?

    * "We have a dashboard, or a range of plots that show different buckets with the number of requests for the different delays for a specific period of time."

  * performance in data processing or performance that might effect the accuracy of measurements?

    * "The project description above includes several items that need to be measured and benchmarked. In this milestone we need to dive deep into each of these items and surface details that might change performance drastically."

* paper clarifications

  * after 'announce' does it matter what order the retriever probes fetch the file?

* how often should the reports be generated?

* is the last 7 days all that will be needed or do you foresee a longer time range?

* if performance in data processing becomes a concern, is there a database (time series or log based) you prefer?
  * mention [unified data warehouse](https://www.notion.so/Unified-Data-Warehouse-878763d3643e47859bbd887143811e0c)

* is there a web based data viz library you might prefer (I have experience with D3)

* is running the probes on AWS sufficient for 'different vantage points'?
  * work on performing last mile or at home studies

* can I get verification that the 'infra as code' tool I should be using is weave over terraform?

  * is there a document somewhere outlining the reasoning for this shift?

* is it possible to get access to AWS or other cloud resources?

  * otherwise reduce scope?

    * can PL simply provide a log (CID over pubsub) I can listen for and collect to generate reports?

  * handoff will be 'infra as code' scripts PL runs on their own infra?

* factors

  * is 'number of seeds' a good measure for 'popularity'

  * geolocation/ASN (maxmind geolite2 API OK?)

  * what does 'connection setup time' mean?

  * any suggestions on how to measure and visualize 'proximity' between fetch and provider?

    * only applies to 'retrieve' and not 'publish'?

    * select a region and scatter plot

      * x-axis is geographic distance

      * y-axis is phase duration

---

* after code review

  * is there a way to tell all retrieval events apply to the same event sequence?
    the same CID could have been requested by different clients
    ( eg/ line 39-41  in plot_total_retrievals)

    * perhaps log an 'attempt ID' ?

    * workaround - ensure each CID is attempted only once in each log file and consider each file a single attempt

  * if 'DONE' is associated with `done_retrieving_at` and `finished_searching_providers_at` does that mean `finished_searching_providers` is only set if no providers were found?

