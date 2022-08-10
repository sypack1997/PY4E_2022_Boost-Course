def count_word(file,word):
    count = 0
    for i in file:
        if word in i:
            count +=1
    return count

a = input("텍스트에 저장할 글을 입력하세요:")
b = input("갯수를 세아릴 글자를 입력하세요:")
with open("story.txt", "w", encoding = 'UTF-8') as file:
    file.write(a)
    print(count_word(a,b))