def append_result(resu: None) -> None:
    with open("history.txt", "a") as file:
        file.write(str(resu))
        
def read_history() -> None:
    with open("history.txt", "r") as file:
        print("\n", "LOG OF OPERATIONS\n", file.read())
        