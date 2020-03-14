
# my_lambdata/my_mod.py

def check_nulls(n):
    return (n.isnull().sum()) 

# print("JUNK")
# print("GLOBAL SCOPE")

# y = float(input("PLEASE INPUT A NUMBER TO ENLARGE"))
# print(enlarge(y))

if __name__=="__main__":
    # only if run from the command line, invoke the following code:
    # otherwise, dont

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("PLEASE INPUT A NUMBER TO ENLARGE"))
    print(enlarge(y))