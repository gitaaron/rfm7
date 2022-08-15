import datetime
import json
from typing import List, Tuple, Dict

from models.model_log_line import LogLine
from models.model_retrieval import Retrieval
from models.model_publication import Publication


class LogFile:

    @staticmethod
    def parse(file: str) -> Tuple[Dict[str, Publication], Dict[str, Retrieval], List[str]]:
        print("Parsing", file)

        with open(file, 'r') as f:
            # CIDs that were not attempted to query
            unattempted_retrieval_cids: List[str] = []

            sealed_publications: dict[str, Publication] = {}
            sealed_retrievals: dict[str, Retrieval] = {}

            publications: dict[str, Publication] = {}
            retrievals: dict[str, Retrieval] = {}

            for idx, line in enumerate(reversed(f.readlines())):
                log = LogLine.from_dict(json.loads(line))
                if (pll := log.is_start_providing()) is not None:
                    publications[pll.cid] = Publication(
                        file, pll.cid, pll.timestamp)
                if (pll := log.is_start_getting_closest_peers()) is not None and pll.cid in publications:
                    publications[pll.cid].getting_closest_peers_started(
                        pll.timestamp)
                elif (pll := log.is_getting_closest_peers()) is not None and pll.cid in publications:
                    publications[pll.cid].find_node_query_started(
                        pll.remote_peer, pll.timestamp)
                elif (pll := log.is_got_closest_peers()) is not None and (
                        pll.cid in publications or pll.cid in retrievals):
                    if pll.cid in publications:
                        publications[pll.cid].find_node_query_ended(
                            pll.remote_peer, pll.timestamp, pll.closest_peers)
                    else:
                        retrievals[pll.cid].got_closer_peers_from(
                            pll.remote_peer, pll.timestamp, pll.closest_peers)
                elif (pll := log.is_error_getting_closest_peers()) is not None and pll.cid in publications:
                    publications[pll.cid].find_node_query_ended(
                        pll.remote_peer, pll.timestamp, [], pll.error_str)
                elif (pll := log.is_pvd_dht_walk_end()) is not None and pll.cid in publications:
                    publications[pll.cid].dht_walk_ended(
                        pll.timestamp, pll.closest_peers)
                elif (pll := log.is_add_provider_started()) is not None and pll.cid in publications:
                    publications[pll.cid].add_provider_started(
                        pll.remote_peer, pll.timestamp)
                elif (pll := log.is_add_provider_success()) is not None and pll.cid in publications:
                    publications[pll.cid].add_provider_success(
                        pll.remote_peer, pll.timestamp)
                elif (pll := log.is_add_provider_error()) is not None and pll.cid in publications:
                    publications[pll.cid].add_provider_error(
                        pll.remote_peer, pll.timestamp, pll.error_str)
                elif pll := log.is_get_provider_success():
                    if len(publications) == 1:
                        publications[list(publications.keys())[0]].get_provider_success(
                            pll.remote_peer, pll.timestamp)
                    else:
                        for cid in publications:
                            if pll.remote_peer in publications[cid].get_provider_queries:
                                print(
                                    f"Multiple publications going on: {pll.remote_peer.id} ({pll.remote_peer.agent_version}) "
                                    f"using CID: {cid} - {' '.join(list(publications.keys()))}"
                                )
                                publications[cid].get_provider_success(
                                    pll.remote_peer, pll.timestamp)
                                break
                            print(
                                f"not using peer {pll.remote_peer} for cid {cid}")
                elif (pll := log.is_get_provider_error()) is not None and pll.cid in publications:
                    publications[pll.cid].get_provider_error(
                        pll.remote_peer, pll.timestamp, pll.error_str)
                elif (pll := log.is_finish_providing()) is not None:
                    publications[pll.cid].seal(pll.timestamp)
                    sealed_publications[pll.cid] = publications[pll.cid]
                    del publications[pll.cid]

                elif (pll := log.is_start_retrieving()) is not None:
                    retrievals[pll.cid] = Retrieval(
                        file, pll.cid, pll.timestamp)
                elif (pll := log.is_start_searching_pvd()) is not None and pll.cid in retrievals:
                    retrievals[pll.cid].getting_provider_peers_started(
                        pll.timestamp)
                elif (pll := log.is_start_getting_providers()) is not None and pll.cid in retrievals:
                    retrievals[pll.cid].getting_providers_from(
                        pll.remote_peer, pll.timestamp)
                elif (pll := log.is_found_provider_entries()) is not None:
                    for cid in retrievals:
                        if pll.remote_peer in retrievals[cid].get_providers_queries:
                            retrievals[cid].found_providers_from(
                                pll.remote_peer, pll.timestamp, pll.count)
                            break
                elif (pll := log.is_pvd_found()) is not None and pll.cid in retrievals:
                    if retrievals[pll.cid].found_first_provider_at is None or retrievals[
                            pll.cid].found_first_provider_at > pll.timestamp:
                        retrievals[pll.cid].found_first_provider_at = pll.timestamp
                    retrievals[pll.cid].provider_record_storing_peers.add(
                        pll.remote_peer)
                    retrievals[pll.cid].provider_peers.add(pll.other_peer)
                elif (pll := log.is_bitswap_connect()) is not None:
                    for cid in retrievals:
                        if pll.remote_peer in retrievals[cid].provider_peers:
                            retrievals[cid].start_dialing_provider(
                                pll.remote_peer, pll.timestamp)
                            break
                elif (pll := log.is_bitswap_connected()) is not None:
                    for cid in retrievals:
                        if pll.remote_peer in retrievals[cid].provider_peers:
                            retrievals[cid].bitswap_connected(
                                pll.remote_peer, pll.timestamp)
                            break
                elif (pll := log.is_connected_to_pvd()) is not None and pll.cid in retrievals:
                    retrievals[pll.cid].connected_to_provider(
                        pll.remote_peer, pll.other_peer, pll.timestamp)
                elif (pll := log.is_got_provider()) is not None and pll.cid in retrievals:
                    retrievals[pll.cid].received_HAVE_from_provider(
                        pll.remote_peer, pll.timestamp)
                elif (pll := log.is_done_retrieving()) is not None and pll.cid in retrievals:
                    retrievals[pll.cid].done_retrieving(
                        pll.timestamp, pll.error_str)
                    if retrievals[pll.cid].marked_for_removal:
                        sealed_retrievals[pll.cid] = retrievals[pll.cid]
                        del retrievals[pll.cid]
                    else:
                        retrievals[pll.cid].marked_for_removal = True
                elif (pll := log.is_finish_searching_pvd()) is not None and pll.cid in retrievals:
                    retrievals[pll.cid].finish_searching_providers(
                        pll.timestamp, pll.error_str)
                    if retrievals[pll.cid].state == Retrieval.State.DONE_WITHOUT_ASKING_PEERS:
                        unattempted_retrieval_cids.append(pll.cid)
                    if retrievals[pll.cid].marked_for_removal:
                        sealed_retrievals[pll.cid] = retrievals[pll.cid]
                        del retrievals[pll.cid]
                    else:
                        retrievals[pll.cid].marked_for_removal = True

            return sealed_publications, sealed_retrievals, unattempted_retrieval_cids
