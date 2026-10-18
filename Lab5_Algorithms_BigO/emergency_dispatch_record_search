import time

import ss_inputs as ss_inputs

# Generate  the incident records
original_dataset = [
    ss_inputs.SEED_DIGIT * i
    for i in range(1, 11)
]

# Rotation point
rotation_point = ss_inputs.SEED_DIGIT

rotated_dataset = (
    original_dataset[rotation_point:]
    + original_dataset[:rotation_point]
)

# Target incident

incident_records = []

for i in range(1, 11):
    value = (
        (ss_inputs.SEED_DIGIT * i)
        + ss_inputs.NAME_LENGTH
        + (ss_inputs.ARTIST_LENGTH % 10)
    )
    incident_records.append(value)

target_incident = (
    (ss_inputs.ID_SUM + ss_inputs.ARTIST_SUM)
    % max(incident_records)
)

if target_incident not in original_dataset:
    target_incident = original_dataset[0]


def linear_search(data, target):
    comparisons = 0

    for index, value in enumerate(data):
        comparisons += 1

        if value == target:
            return index, comparisons

    return -1, comparisons


start = time.perf_counter()

position, comparisons = linear_search(
    rotated_dataset,
    target_incident
)

elapsed = time.perf_counter() - start

#--------------------
# ASSESSMENT DATA

print("\nASSESSMENT DATA")

print("\nOriginal Dataset")
print(original_dataset)

print("\nRotated Dataset")
print(rotated_dataset)

print("\nTarget Incident")
print(target_incident)

print("\nComparison Counts")
print(comparisons)

print("\nSearch Position")
print(position)

print("\nTime and Space Complexity")
print("Time : O(n)")
print("Space: O(1)")

#--------------------
# FINAL OUTPUT

print("\nFINAL OUTPUT")

if position != -1:
    print(
        f"Incident {target_incident} found "
        f"at position {position}"
    )
else:
    print("Incident not found")

print(f"Comparisons: {comparisons}")