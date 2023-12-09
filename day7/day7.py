def get_content(filename: str) -> str:
    with open(filename, "r") as f:
        content = f.read()
    return content


def main():
    filename = "day7/day7test.txt"
    content = get_content(filename)
    print(content)
    
    
if __name__ == "__main__":  
    main()  