def hstrat_select_decorator(func):
    def wrapFunc(*args, **kargs):
        individuals = func(*args, **kargs)
        individuals = [*map(copy.copy, individuals)]
        for individual in individuals:
            individual.hstrat_annotation = (
                individual.hstrat_annotation.CloneDescendant()
            )
        return individuals

    return wrapFunc
