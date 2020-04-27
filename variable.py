a = 3
b = 4.92
c = "itgenius"
print(a)
print(b)
print(c)


# combine word and var
# 1st concat String
print("price", b, "per unit available", a, "unit")

# 2nd String interpolation
print("price %.2f per unit available %d unit" % (b, a))

# 3rd Format String
print(f"Price {b} per unit Available {a} unit")
