istr = "hello"
hello = "-".join(istr)
print(hello)

string_to_center = "How are you? M fine!"

print(string_to_center.center(100, "*"))
print("    heya    ".lstrip() + "hi")
print("    heya    ".rstrip() + "hi")
print("    heya    ".strip() + "hi")

print("heya".zfill(43))

print("heya".rjust(43, "*"))


print("Buna %s, aici este un care de burta in %5.2f kg" % ("Vasile", 32.4))
print("Buna {nume}, aici este un care de burta in {kilo} kg".
      format(nume="Vasile", kilo=32.4))
print("Buna {0:s}, aici este un care de burta in {1:f} kg".
      format("Vasile", 32.434242424243566656666666666666))


print("..mic".lstrip())
