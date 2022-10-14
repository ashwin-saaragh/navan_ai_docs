lines = [line.replace("\n","") for line in open("E:\DEV\\navan_ai_docs\prediction code\classes.names","r").readlines()]
classes = {i:lines[i] for i in range(len(lines))}
print(classes)

