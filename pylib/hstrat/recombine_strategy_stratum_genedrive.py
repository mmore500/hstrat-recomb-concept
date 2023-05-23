# from hstrat._auxiliary_lib import iter_monotonic_equivalencies
import random

# this is an inefficient and inelegant implementation
from hstrat import hstrat


def recombine_strategy_stratum_genedrive(
    c1: hstrat.HereditaryStratigraphicColumn,
    c2: hstrat.HereditaryStratigraphicColumn,
) -> hstrat.HereditaryStratigraphicColumn:
    younger, older = sorted([c1, c2], key=lambda c: c.GetNumStrataDeposited())
    assert younger.GetNumStrataDeposited() == older.GetNumStrataDeposited()

    store = hstrat.HereditaryStratumOrderedStoreList()
    for rank, differentia in older.IterRankDifferentiaZip():
        younger_stratum = younger.GetStratumAtRank(rank)
        younger_differentia = younger_stratum.GetDifferentia()
        younger_annotation = younger_stratum.GetAnnotation()

        older_stratum = older.GetStratumAtRank(rank)
        older_differentia = older_stratum.GetDifferentia()
        older_annotation = older_stratum.GetAnnotation()

        max_differentia = max(differentia, younger_differentia)
        stratum = hstrat.HereditaryStratum(
            differentia=max_differentia,
            deposition_rank=rank,
        )
        store.DepositStratum(stratum=stratum, rank=rank)

    return hstrat.HereditaryStratigraphicColumn(
        stratum_retention_policy=older._stratum_retention_policy,
        stratum_differentia_bit_width=older.GetStratumDifferentiaBitWidth(),
        stratum_ordered_store=(
            store,
            older.GetNumStrataDeposited(),
        ),
    )
