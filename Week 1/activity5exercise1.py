user_input = input("Type in a sentence:\n").lower()

a_count = user_input.count("a")
e_count = user_input.count("e")
i_count = user_input.count("i")
o_count = user_input.count("o")
u_count = user_input.count("u")
space_count = user_input.count(" ")
remainder = len(user_input) - a_count - e_count - i_count - o_count - u_count - space_count

print(f"A: {a_count * '*'}")
print(f"E: {e_count * '*'}")
print(f"I: {i_count * '*'}")
print(f"O: {o_count * '*'}")
print(f"U: {u_count * '*'}")

print(f"Other (non-space) Characters: {remainder}")
