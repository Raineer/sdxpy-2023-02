# What happens when we run with or without the pre-definition while looping over globals?

name = None # This is the piece to toggle

for name in globals():
	print(name)


# If we do not define "name" first, then the "name" in the for loop appears to be treated as a global.
# As soon as "name" in the for loop takes a value, the value of the global dictionary changes.

# But, if name has a prior definition, the dictionary size is set and we are not creating a new entry.
