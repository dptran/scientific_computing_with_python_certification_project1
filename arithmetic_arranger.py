def arithmetic_arranger(problems, *boolean):
    if len(problems) > 5:
        return "Error: Too many problems."
    first = []
    second = []
    operator = []
    spaces = []
    formula = ""
    
    for i in problems:
        x = i.split(" ")
        first.append(x[0])
        operator.append(x[1])
        second.append(x[2])

    for i in operator:
        if i != "+" and i != "-":
            return "Error: Operator must be '+' or '-'."
        
    for i in first:
        if len(i) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not i.isdigit():
            return "Error: Numbers must only contain digits."
        
    for i in second:
        if len(i) > 4:
            return "Error: Numbers cannot be more than four digits."
        elif not i.isdigit():
            return "Error: Numbers must only contain digits."
        
    for k in range(len(first)):
        if len(first[k]) > len(second[k]):
            spaces.append(int(len(first[k]) + 2))
        else:
            spaces.append(int(len(second[k]) + 2))
            
    count = len(spaces)
    
    for i in range(count - 1):
        for s in range(spaces[i] - len(first[i])):
            formula += " "
        formula += first[i] + "    "
    
    for s in range(spaces[-1] - len(first[-1])):
        formula += " "
    formula += first[-1]
    formula += "\n"
    
    for i in range(count - 1):
        formula += operator[i]
        for s in range(spaces[i] - len(second[i]) - 1):
            formula += " "
        formula += second[i] + "    "
        
    formula += operator[-1]
    for s in range(spaces[-1] - len(second[-1]) - 1):
        formula += " "
    formula += second[-1]
    formula += "\n"
    
    for i in range(count - 1):
        formula += f"{spaces[i] * '-'}"
        formula += "    "
        
    formula += f"{spaces[-1] * '-'}"
    if len(boolean) == 0:
        return formula
    elif boolean[0] == True:
        formula += "\n"
        cal = [eval(i) for i in problems]
        for i in range(count - 1):
            for s in range(spaces[i] - len(str(cal[i]))):
                formula += " "
            formula += str(cal[i]) + "    "
        
        for s in range(spaces[-1] - len(str(cal[-1]))):
            formula += " "
        formula += str(cal[-1])
        return formula