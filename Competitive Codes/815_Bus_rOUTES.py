def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    # 1) Create and adjencecy list relating stops with
    # bus routes: 1:{0}, 2:{0}, 7:{0, 1}, 3:{1}, 6:{1}
    routeList = collections.defaultdict(set)
    for bus, route in enumerate(routes):
        for stop in route:
            routeList[stop].add(bus)

    # 2) Created 'queue' and visited
    # set for BFS processing:
    queue = [(source, 0)]
    visited = set([source])

    # 3) Perform BFS processing:
    # Decide whether two buses are connected
    # by an edge. They are connected if they
    # share a common value in the set intersection:
    for curLoc, buses in queue:
        # Base case: Arrives
        # to desired bus stop:
        if curLoc == target:
            return buses

        # 4) Annotate numbers of buses
        # taken to get to current stop:
        for bus in routeList[curLoc]:
            for stop in routes[bus]:

                if stop not in visited:
                    queue.append((stop, buses + 1))
                    visited.add(stop)

            # 5) Clean route since
            # it was already visited:
            routes[bus] = []

    return -1