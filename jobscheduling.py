jobs = [
('J1', 2, 100),
('J2', 1, 50),
('J3', 2, 10),
('J4', 1, 20)
]

jobs.sort(key=lambda x: x[2], reverse=True)

slots = [False] * 2
result = []

for job in jobs:
    for j in range(min(1, job[1]-1), -1, -1):
        if not slots[j]:
            slots[j] = True
            result.append(job[0])
            break

print("Selected Jobs:", result)