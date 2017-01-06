def kartsuba(x,y, b=10):
	if (x<1000) or y<1000:
		return x*y
	else:
		m = max(len(str(x)),len(str(y)))
		m2 = m/2
		bm = b**m2
		high1, low1 = x/bm, x%bm
		high2, low2 = y/bm, y%bm
		print m2, bm
		z0 = kartsuba(low1,low2)
		z1 = kartsuba(low1+high1,low2+high2)
		z2 = kartsuba(high1,high2)
		return (z2*10**(2*m2))+((z1-z2-z0)*10**(m2))+(z0)

print kartsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)
