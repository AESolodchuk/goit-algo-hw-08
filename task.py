import heapq


def min_cost_to_connect_cables(cable_lengths):
    if not cable_lengths:
        return 0

    # Ініціалізація мінімальної купи
    heapq.heapify(cable_lengths)
    print(cable_lengths)
    total_cost = 0

    # Об'єднання кабелів, поки в купі більше одного кабеля
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        cost = first + second
        total_cost += cost
        heapq.heappush(cable_lengths, cost)

    return total_cost


def merge_cables(cables: list, debug: bool = False) -> tuple:
    merge_order = []
    heap = cables.copy()
    heapq.heapify(heap)
    if debug:
        print("Початковий стан купи:")
        print(f"{heap}")
        print("Обрахунок витрат:")
        print(f"{'сума':>5} | {'відрізки '} | {'стан купи'}")

    total_cost = 0
    while len(heap) > 1:
        cost1, cost2 = heapq.heappop(heap), heapq.heappop(heap)
        total_cost += cost1 + cost2
        merge_order.append((cost1, cost2))
        heapq.heappush(heap, cost1 + cost2)
        if debug:
            print(f"{total_cost:^5} | {cost1:^3} + {cost2:^3} | {heap}")

    return merge_order, total_cost


if __name__ == "__main__":
    cables = [15, 4, 12, 6, 2]
    print(f"Відкрізки кабелів:\n{cables}")

    merge_order, total_cost = merge_cables(cables, debug=True)

    print(f"Порядок об'єднання кабелів: {merge_order}")
    print(f"Загальні витрати: {total_cost}")
    print(f"{cables = }")
