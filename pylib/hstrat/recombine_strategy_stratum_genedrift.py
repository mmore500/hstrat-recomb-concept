# from hstrat._auxiliary_lib import iter_monotonic_equivalencies
import random

# this is an inefficient and inelegant implementation
from hstrat import hstrat


def recombine_strategy_stratum_genedrift(
    c1: hstrat.HereditaryStratigraphicColumn,
    c2: hstrat.HereditaryStratigraphicColumn,
) -> hstrat.HereditaryStratigraphicColumn:
    common_ranks = {*c1.IterRetainedRanks()} & {*c2.IterRetainedRanks()}
    younger, older = sorted([c1, c2], key=lambda c: c.GetNumStrataDeposited())

    store = hstrat.HereditaryStratumOrderedStoreList()
    for rank, differentia in older.IterRankDifferentiaZip():
        younger_annotation = younger.GetStratumAtRank(rank).GetAnnotation()
        older_annotation = older.GetStratumAtRank(rank).GetAnnotation()
        younger_differentia = younger.GetStratumAtRank(rank).GetDifferentia()
        stratum = hstrat.HereditaryStratum(
            differentia=random.choice(
                [differentia] * (older_annotation + 1)
                + [younger_differentia] * (younger_annotation + 1)
            )
            if (older.GetNumStrataDeposited() - rank) < 16
            else random.choice([differentia, younger_differentia]),
            deposition_rank=rank,
            annotation=max(
                older_annotation,
                younger_annotation,
            )
            + 1
            if differentia == younger_differentia
            else 0,
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
