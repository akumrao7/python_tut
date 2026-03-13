
# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt","rt") as fh:
        line1=fh.readline()
        line2 = fh.readline()


    print("Reading the content:")
    print(f"Line1: {line1.rstrip()}")
    print(f"Line2: {line2.rstrip()}")

except FileNotFoundError as e:
    print(f"Error: the file {e} not found.")


# Task 2: Write and Append Data to a File

fh=open("output.txt","at")
fh.write(input("\nEnter the text to write to the file:")+"\n")
print("Data successfully written to output.txt")
fh.write(input("\nEnter additional text to append:")+"\n")
print("Data successfully appended to output.txt")
fh.close()

with open("output.txt","rt") as fh:
    content=fh.read()

print(f"\nFinal content of the file:\n{content}")
