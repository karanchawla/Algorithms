def kartsuba(x,y, b=10):
	if (x<1000) or y<1000:
		return x*y
	else:
		m = min(len(str(x)),len(str(y)))
		m2 = m/2
		bm = b**m2
		high1, low1 = x/bm, x%bm
		print high1, low1, high2, low2 
		z0 = kartsuba(low1,low2)
		z1 = kartsuba(low1+high1,low2+high2)
		z2 = kartsuba(high1,high2)
		return (z2*10**(2*m2))+((z1-z2-z0)*10**(m2))+(z0)
print kartsuba(12345,6789)
