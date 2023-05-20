def hstrat_mutate_decorator(func):
    def wrapFunc(*args, **kwargs):
        individuals = func(*args, **kwargs)
        for individual in individuals:
            history.update([individual])
            individual.hstrat_annotation.DepositStratum()
        return individuals

    return wrapFunc
