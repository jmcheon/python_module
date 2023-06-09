from vector import Vector

if __name__ == "__main__":

	# when data is a list
	print("\n << when data is a list >>")
	print("\n << Column vector of shape n * 1 >>")
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
	print(Vector([[0.0], [-1.0], [2.0], [3.0]]).values)
#	Vector([[0], [1.0], [2.0], [3.0]])
#	Vector([[0.0, 1.0], [1.0], [2.0], [3.0]])
#	Vector([[], [1.0], [2.0], [3.0]])

	print("\n << Row vector of shape 1 * n >>")
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
	print(Vector([[0.0, -1.0, 2.0, 3.0]]).values)
	print(Vector([[-0.0, 1.0, 2.0, 3.0]]).values)
	#Vector([[0, 1.0, 2.0, 3.0]])
	#Vector([[[], 1.0, 2.0, 3.0]])
	#Vector([1.0, [0.0, 1.0, 2.0, 3.0]])
	#Vector([[]])


	# when data is a size
	print("\n << when data is a size >>")
	print(Vector(4).values)
	#print(Vector(-1).values)



	# when data is a tuple
	print("\n << when data is a tuple >>")
	print(Vector((4, 6)).values)
	print(Vector((0, 6)).values)
	print(Vector((1, 1)).values)
	#Vector((-1, 6))
	#Vector((1, 6.1))
	#Vector((4, 1))


	# dot product
	print("\n << dot product >>")
	v1 = Vector([[2.0, 3.0, 1.0]])
	v2 = Vector([[2.0], [3.0], [1.0]])
	#v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
	#v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
	print(v1)
	print(v1.dot(v2))

	# transpose
	print("\n << transpose >>")
	print(v1.T())
	print(v1.T().shape)
	print(v2.T())
	print(v2.T().shape)

	# division by scalar
	v3 = v1 / 2.0
	print(v3.values)
	v3 = Vector(4) / 2
	print(v3.values)
	v3 = Vector(4) / 3.14
	print(v3.values)
	#v3 = Vector(4) / 0
	#v3 = Vector(4) / None
	#v3 = None / Vector(4) 
	#v3 = 3 / Vector(4) 

	# addition by scalar
	v = Vector(4)
	v2 = Vector([[1.0], [1.0], [1.0], [1.0]])
	print((v + v2).values)
	print((1 + v2))
	print((v - v2).values != (v2 - v).values)

	# multiplication by scalar
	v = Vector(4)
	print(v * 4) 
	print(4.0 * v) 
	#v * "hello"
