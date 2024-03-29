from trains.models import Train

def dfs_path(graph, start, goal):
    
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == goal:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_]))

def get_graph(qs):
    graph = {}
    for q in qs:
        graph.setdefault(q.from_city.id, set())
        graph[q.from_city.id].add(q.to_city.id)
    return graph

def get_routes(request, form):
    context = {'form': form}
    qs = Train.objects.all().select_related('from_city', 'to_city')
    graph = get_graph(qs)
    data = form.cleaned_data
    from_city = data['from_city']
    to_city = data['to_city']
    cities = data['cities']
    traveling_time = data['traveling_time']
    all_ways = list(dfs_path(graph=graph, start=from_city.id, goal=to_city.id))

    if not len(list(all_ways)):
        raise ValueError('Route does not exist')
    
    if cities:
        _cities = [city.id for city in cities]
        right_ways = []
        for route in all_ways:
            if all(city in route for city in _cities):
                right_ways.append(route)
        if not right_ways:
            raise ValueError('Route throught these cities is impossible')
    else:
        right_ways = all_ways
    
    routes = []
    all_trains = {}

    for q in qs:
        all_trains.setdefault((q.from_city.id, q.to_city.id), [])
        all_trains[(q.from_city.id, q.to_city.id)].append(q)

    for route in right_ways:
        tmp = {}
        tmp['trains'] = []
        total_time = 0
        for i in range(len(route) - 1):
            qs = all_trains[(route[i], route[i+1])]
            q = qs[0]
            total_time += q.travel_time
            tmp['trains'].append(q)
        tmp['total_time'] = total_time
        if total_time <= traveling_time:
            routes.append(tmp)

    if not routes:
        raise ValueError('Travele time is longer than indicated')

    sorted_routes = []
    if len(routes) == 1:
        sorted_routes = routes
    else:
        times = list(set(r['total_time'] for r in routes))
        times = sorted(times)

        for time in times:
            for route in routes:
                if time == route['total_time']:
                    sorted_routes.append(route)

    context['routes'] = sorted_routes
    context['cities'] = {'from_city': from_city, 'to_city': to_city}
    return context