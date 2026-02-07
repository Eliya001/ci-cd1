from app import greet

def test_greet():
    result = greet("Eliya")
    if result != "Hello Eliya!":
        raise Exception("Test failed")

    print("test passed!")

test_greet()
