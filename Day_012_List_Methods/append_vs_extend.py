# Difference between append() and extend()

languages_with_append = ["Python", "Java"]
languages_with_append.append(["C++", "JavaScript"])

print("Using append():")
print(languages_with_append)


languages_with_extend = ["Python", "Java"]
languages_with_extend.extend(["C++", "JavaScript"])

print("\nUsing extend():")
print(languages_with_extend)