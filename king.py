def king(korea, chosun):
    king_dict = dict()

    korea = korea.split(",")
    chosun = chosun.split(",")

    for kor in korea:
        king_dict[kor] = 1

    for cho in chosun:
        if king_dict.get(cho,0) >=1:
            king_dict[cho] = king_dict[cho] +1
        else:
            continue

    repeated_king = []
    for (k,v) in king_dict.items():
        if v >=2:
            repeated_king.append(k)
    
    count = 0
    for king in repeated_king:
        print(f"조선과 고려에 모두 있는 왕 이름 : {king}")
        cpint += 1
    print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")