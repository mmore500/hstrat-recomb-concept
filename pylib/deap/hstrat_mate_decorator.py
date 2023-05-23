import random

from ..hstrat import recombine_strategy_stratum_genedrive


def hstrat_mate_decorator(func):
    def wrapFunc(*args, **kwargs):
        i1, i2 = func(*args, **kwargs)
        child_annotation = recombine_strategy_stratum_genedrive(
            i1.species_annotation,
            i2.species_annotation,
        )
        i1.species_annotation = child_annotation.CloneDescendant()
        i2.species_annotation = child_annotation.CloneDescendant()

        i1.gene_annotation.DepositStratum(0)
        i2.gene_annotation.DepositStratum(0)

        g1 = i1.gene_annotation
        g2 = i2.gene_annotation
        assert g1.GetNumStrataDeposited() == g2.GetNumStrataDeposited()

        for idx in range(g1.GetNumStrataDeposited()):
            s1 = g1.GetStratumAtColumnIndex(idx)
            r1 = s1.GetDepositionRank()
            s2 = g2.GetStratumAtColumnIndex(idx)
            r2 = s1.GetDepositionRank()
            assert r1 == r2

            if g1.GetNumStrataDeposited() - r1 == 16:
                s1._annotation |= 1 << random.randrange(64)
            if g2.GetNumStrataDeposited() - r2 == 16:
                s2._annotation |= 1 << random.randrange(64)

            if s1.GetDifferentia() == s2.GetDifferentia():
                s1._annotation |= s2._annotation
                s2._annotation |= s1._annotation

        return (i1, i2)

    return wrapFunc
