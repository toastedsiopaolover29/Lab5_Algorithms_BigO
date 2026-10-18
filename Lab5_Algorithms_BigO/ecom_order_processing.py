import time

import ss_inputs as ss_inputs

base_dataset = []

for i, letter in enumerate(
    ss_inputs.FAVORITE_ARTIST.replace(" ", "")[:10]
):
    value = (
    (ord(letter) - 64)
    + ss_inputs.SEED_DIGIT
    + ss_inputs.NAME_LENGTH
    + (ss_inputs.ID_SUM % 10)
    + (ss_inputs.ARTIST_LENGTH % 5)
)

    base_dataset.append(value)

sorted_data = sorted(base_dataset)

reverse_data = sorted(
    base_dataset,
    reverse=True
)

random_data = [
    base_dataset[3],
    base_dataset[7],
    base_dataset[1],
    base_dataset[4],
    base_dataset[0],
    base_dataset[8],
    base_dataset[2],
    base_dataset[5],
    base_dataset[6]
]


def bubble_sort(arr):
    data = arr.copy()

    comparisons = 0
    movements = 0

    for i in range(len(data)):
        for j in range(
            len(data)-1-i
        ):
            comparisons += 1

            if data[j] > data[j+1]:
                data[j], data[j+1] = (
                    data[j+1],
                    data[j]
                )

                movements += 1

    return (
        data,
        comparisons,
        movements
    )


def selection_sort(arr):
    data = arr.copy()

    comparisons = 0
    movements = 0

    for i in range(len(data)):
        min_idx = i

        for j in range(
            i + 1,
            len(data)
        ):
            comparisons += 1

            if data[j] < data[min_idx]:
                min_idx = j

        if min_idx != i:
            data[i], data[min_idx] = (
                data[min_idx],
                data[i]
            )

            movements += 1

    return (
        data,
        comparisons,
        movements
    )


def insertion_sort(arr):
    data = arr.copy()

    comparisons = 0
    movements = 0

    for i in range(1, len(data)):
        key = data[i]

        j = i - 1

        while j >= 0:
            comparisons += 1

            if data[j] > key:
                data[j+1] = data[j]
                movements += 1
                j -= 1
            else:
                break

        data[j+1] = key

    return (
        data,
        comparisons,
        movements
    )


def test_algorithm(
    algorithm,
    dataset
):
    start = time.perf_counter()

    result = algorithm(dataset)

    elapsed = (
        time.perf_counter()
        - start
    )

    return result, elapsed


conditions = {
    "Sorted": sorted_data,
    "Reverse": reverse_data,
    "Random": random_data
}

algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

# ----------------------------------------
# ASSESSMENT DATA

print("\nASSESSMENT DATA")

print("\nGenerated Order Dataset")
print(random_data)

for condition_name, dataset in conditions.items():

    print(
        f"\n===== {condition_name} DATA ====="
    )

    for algo_name, algo in (
        algorithms.items()
    ):
        (
            (sorted_result,
             comparisons,
             movements),
            elapsed
        ) = test_algorithm(
            algo,
            dataset
        )

        print(f"\n{algo_name}")

        print(
            "Comparisons:",
            comparisons
        )

        print(
            "Movements:",
            movements
        )

        print(
            "Execution Time:",
            f"{elapsed:.8f}"
        )

        print(
            "Sorted Correctly:",
            sorted_result
            ==
            sorted(dataset)
        )

print("\nBig O Analysis")

print("Bubble Sort    : O(n²)")
print("Selection Sort : O(n²)")
print("Insertion Sort : O(n²)")
print("Best Case Insertion Sort: O(n)")
print("Worst Case: O(n²)")

# ----------------------------------------
# FINAL OUTPUT

print("\nFINAL OUTPUT")

print("\nSorted Order Dataset")
print(sorted(random_data))

print("\nSummary")
print(
    "Insertion Sort is generally "
    "best for nearly sorted data."
)

print(
    "Bubble Sort and Selection "
    "Sort remain O(n²)."
)