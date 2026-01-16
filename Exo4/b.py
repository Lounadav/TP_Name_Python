print("B1")
import a
def g():
    print("B2")
    a.f()
if __name__ == "__main__":
    print("B3")
    g()