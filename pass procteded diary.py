password = input("🔐 Enter diary password: ")
if password == "243114":
    with open("private_diary.txt", "a") as f:
        entry = input("Write your diary entry: ")
        f.write(entry + "\n")
    print("✅ Entry saved.")
else:
    print("❌ Wrong password.")
