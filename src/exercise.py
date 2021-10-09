def main():
    #write your code below this line
    while True:
        text = input()
        if (text != ""):
            text_split = text.split()
            print(text_split[0])
        else:
            break


if __name__ == '__main__':
    main()
