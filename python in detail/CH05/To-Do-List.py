tasks = []

while True:
    task = input("Enter a task (or type 'quit' to stop): ")
    if task == 'quit':
        break
    tasks.append(task)

print("Your To-Do List:")
for task in tasks:
    print("- " + task)
