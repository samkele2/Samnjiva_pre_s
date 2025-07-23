mrt = input("What's the Answer to the Great Question of Life, the Universe, and Everything?"  )
mrt_l = mrt.lower().strip(" ")

if mrt_l == "forty two" or mrt_l == "forty-two" or mrt_l == "42":
   print("Yes")
else:
   print("No")
    
