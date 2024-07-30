from gendiff.generate_diff import generate_diff

def main():
    file1 = 'tests/fixtures/file1.json'
    file2 = 'tests/fixtures/file2.json'
    diff = generate_diff(file1, file2)
    print(diff)

if __name__ == "__main__":
    main()