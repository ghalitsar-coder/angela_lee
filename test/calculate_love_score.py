# def calculate_love_score(name1, name2):
#     trueOccurs = {"T": 0, "R": 0, "U": 0, "E": 0}
#     loveOccurs = {"L": 0, "O": 0, "V": 0, "E": 0}
#     for char in trueOccurs.keys():
#         if char.lower() in name1:
#             trueOccurs[char] += 1
#         if char.lower() in name2:
#             trueOccurs[char] += 1

#     for char in loveOccurs.keys():
#         if char.lower() in name1:
#             loveOccurs[char] += 1
#         if char.lower() in name2:
#             loveOccurs[char] += 1
            
#     total = f"{sum(trueOccurs.values())}{sum(loveOccurs.values())}"
#     return total


# print(calculate_love_score("angela yu", "jack bauer"))


# * gpt
def calculate_love_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    true_score = sum(name1.count(char) + name2.count(char) for char in "true")
    love_score = sum(name1.count(char) + name2.count(char) for char in "love")
    return f"{true_score}{love_score}"

print(calculate_love_score("angela yu", "jack bauer"))