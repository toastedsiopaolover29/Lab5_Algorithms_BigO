import time

import ss_inputs as ss_inputs

# Dataset A
dataset_a = sorted([
    ss_inputs.SEED_DIGIT * i + ss_inputs.ID_SUM
    for i in range(5)
])

# Dataset B
dataset_b = sorted([
    ss_inputs.ARTIST_LENGTH * i + ss_inputs.NAME_LENGTH
    for i in range(5)
])


def merge_sorted_lists(a, b):
    i = 0
    j = 0

    merged = []
    comparisons = 0

    while i < len(a) and j < len(b):
        comparisons += 1

        if a[i] <= b[j]:
            merged.append(a[i]) 
            i += 1
        else:
            merged.append(b[j])
            j += 1

    merged.extend(a[i:])
    merged.extend(b[j:])

    return merged, comparisons


start = time.perf_counter()

consolidated_dataset, comparisons = (
    merge_sorted_lists(
        dataset_a,
        dataset_b
    )
)

elapsed = time.perf_counter() - start

ordering_verified = (
    consolidated_dataset ==
    sorted(consolidated_dataset)
)

# ----------------------------------------
# ASSESSMENT DATA

print("\nASSESSMENT DATA")

print("\nDepartment A Dataset")
print(dataset_a)

print("\nDepartment B Dataset")
print(dataset_b)

print("\nConsolidated Dataset")
print(consolidated_dataset)

print("\nNumber of Records Before and After Consolidation")
print(
    f"Before: {len(dataset_a)+len(dataset_b)}"
)
print(
    f"After : {len(consolidated_dataset)}"
)

print("\nComparison Count")
print(comparisons)

print("\nOrdering Verification")
print(ordering_verified)

print("\nTime and Space Complexity")
print("Time : O(n)")
print("Space: O(n)")

# ----------------------------------------
# FINAL OUTPUT

print("\nFINAL OUTPUT")

print(
    "\nFinal Consolidated "
    "Enrollment Dataset"
)

print(consolidated_dataset)