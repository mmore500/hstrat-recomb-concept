from ..hstrat import recombine_strategy_stratum_genedrive


def hstrat_mate_decorator(func):
    def wrapFunc(*args, **kwargs):
        i1, i2 = func(*args, **kwargs)
        child_annotation = recombine_strategy_stratum_genedrive(
            i1.hstrat_annotation,
            i2.hstrat_annotation,
        )
        i1.hstrat_annotation = child_annotation.CloneDescendant()
        i2.hstrat_annotation = child_annotation.CloneDescendant()
        return (i1, i2)

    return wrapFunc
