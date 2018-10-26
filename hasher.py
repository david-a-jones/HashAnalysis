#modular hash to place into one of m buckets
def modHash(key, m):
	bytes = key.encode()
	numOfBytes = len(bytes)
	sum = 0
	for i in range(numOfBytes):
		b = bytes[i]
		sum = sum + b;
	return sum % m

#similar to modHash, but sum is done using longs (4 bytes at a time)
def foldHash(key, m):
	bytes = key.encode()
	numOfBytes = len(bytes)
	totalSum = 0
	i = 0
	while i < numOfBytes:
		try:
			b1 = bytes[i] << 24
		except IndexError:
			b1 = 0
		try:
			b2 = bytes[i+1] << 16
		except IndexError:
			b2 = 0
		try:
			b3 = bytes[i+2] << 8
		except IndexError:
			b3 = 0
		try:
			b4 = bytes[i+3]
		except IndexError:
			b4 = 0
		bytesSum = b1 + b2 + b3 + b4
		totalSum = totalSum + bytesSum
		i = i + 4
	return totalSum % m