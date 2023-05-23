def hstrat_mutate_decorator(func):
    def wrapFunc(*args, **kwargs):
        individuals = func(*args, **kwargs)
        for individual in individuals:
            individual.hstrat_annotation.DepositStratum(0)
            for z in individual.hstrat_annotations:
                z.DepositStratum(0)

        return individuals

    return wrapFunc
