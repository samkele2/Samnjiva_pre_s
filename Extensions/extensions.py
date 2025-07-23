mrt = input("File name:" )

mrt_l = mrt.lower().strip(" ")

if mrt_l.endswith(".gif"):
    print("image/gif")
elif mrt_l.endswith(".jpg") or mrt_l.endswith(".jpeg"):
    print("image/jpeg")
elif mrt_l.endswith(".png"):
    print("image/png")
elif mrt_l.endswith(".pdf"):
    print("application/pdf")
elif mrt_l.endswith(".txt"):
    print("text/plain")
elif mrt_l.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
