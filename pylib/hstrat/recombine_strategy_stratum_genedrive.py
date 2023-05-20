# from hstrat._auxiliary_lib import iter_monotonic_equivalencies

# this is an inefficient and inelegant implementation
from hstrat import hstrat


def recombine_strategy_stratum_genedrive(
    c1: hstrat.HereditaryStratigraphicColumn,
    c2: hstrat.HereditaryStratigraphicColumn,
) -> hstrat.HereditaryStratigraphicColumn:
    common_ranks = {*c1.IterRetainedRanks()} & {*c2.IterRetainedRanks()}
    younger, older = sorted([c1, c2], key=lambda c: c.GetNumStrataDeposited())

    store = hstrat.HereditaryStratumOrderedStoreList()
    for rank, differentia in older.IterRankDifferentiaZip():
        max_differentia = (
            max(differentia, younger.GetStratumAtRank(rank).GetDifferentia())
            if rank in common_ranks
            else differentia
        )
        stratum = hstrat.HereditaryStratum(
            differentia=max_differentia,
            deposition_rank=rank,
        )
        assert stratum.GetDifferentia() == max_differentia
        store.DepositStratum(stratum=stratum, rank=rank)

    return hstrat.HereditaryStratigraphicColumn(
        stratum_retention_policy=older._stratum_retention_policy,
        stratum_differentia_bit_width=older.GetStratumDifferentiaBitWidth(),
        stratum_ordered_store=(
            store,
            older.GetNumStrataDeposited(),
        ),
    )
