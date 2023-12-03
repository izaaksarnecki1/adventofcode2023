def get_content(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    return content
        
if __name__ == '__main__':
    print("ran from file")