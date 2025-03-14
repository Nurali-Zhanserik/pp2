with open("default.txt", "a") as task:
    task.write("Something") # added one line 
with open("default.txt", "r") as task:
    
    count_line = sum(1 for line in task)
print(f"This file has {count_line} lines")        
