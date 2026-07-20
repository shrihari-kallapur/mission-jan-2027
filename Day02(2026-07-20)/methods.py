name = "Shrihari"
company = "NVIDIA"
message = """AI System Engineer"""

# Uppercase and Lowercase
print(name.upper())
print(company.lower())
print(message.title())

# Remove spaces
title = "   AI System Engineer   "
print(title.strip())

# Replace
text = "I like TensorFlow"
print(text.replace("TensorFlow", "PyTorch"))

# Split
sentence = "Python, SQL, Liunx"
print(sentence.split(", "))

# Join
skills = ["Python", "SQL", "Linux"]
print(" | ".join(skills))

# Find
text = "Artificial Intelligence"
print(text.find("Intelligence"))

# Count
text = "banana"
print(text.count("a"))
