with open('./codeabbey-tasks.txt', mode='a') as f:
    f.write("# codeabbey tasks record:\n\n")
    for i in range(1,146):
        f.write(f"- [ ] Task: {i}\n")
