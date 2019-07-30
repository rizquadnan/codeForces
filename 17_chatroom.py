chat = list(input())

output = "NO"
acc_chars = ['h', 'e', 'l', 'o']
if "h" in chat and "e" in chat and "l" in chat and "o" in chat and chat.count("l") >= 2:
    chat = [char for char in chat if char in acc_chars]
    acc_chat = []
    for char in chat:
        if char in acc_chat: 
            if char == 'l' and acc_chat.count('l') == 2:
                continue
            elif char == 'l' and acc_chat.count('l') < 2:
                pass
            else:
                continue
        if char == "h":
            if len(acc_chat) == 0:
                acc_chat.append(char)
            continue
        if char == "e":
            if len(acc_chat) == 1:
                acc_chat.append(char)
            continue
        if char == "l":
            if len(acc_chat) == 2:
                acc_chat.append(char)
            elif len(acc_chat) == 3:
                acc_chat.append(char)
            continue
        if char == "o":
            if len(acc_chat) == 4:
                acc_chat.append(char)
                output = "YES"
                break
    
print(output)