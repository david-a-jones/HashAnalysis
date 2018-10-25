#modular hash to place into one of m buckets
def modHash(key, m):
	bytes = key.encode()
	numOfBytes = len(bytes)
	sum = 0
	for i in range(numOfBytes):
		b = bytes[i]
		sum = sum + b;
	return sum % m

def modMultiHash(key, m):
	bytes = key.encode()
	numOfBytes = len(bytes)
	prod = 0

	for i in range(numOfBytes):
		b = bytes[i]
		prod = prod * b;
	return prod % m