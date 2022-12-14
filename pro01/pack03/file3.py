#동 이름을 입력해 해당 동 관련 우편번호 및 주소 출력

try:
    dong=input('동 이름 입력:')
    #print(dong)
    
    with open('zipcode.txt', mode='r', encoding='euc-kr') as f:  ##열고
        line=f.readline()  ##첫 줄 읽기
        #print(line)
        while line:  ##줄이 있을 때 까지 반복
            #lines=line.split('\t') #split은 list를 반환함
            lines=line.split(chr(9)) #tab키 아스키코드  ##짜르고
            #print(lines)
            if lines[3].startswith(dong):
                #print(lines)
                print('['+lines[0]+']'+lines[1]+' '+lines[2]+' '+lines[3]+' '+' '+lines[4]+' ')
            
            line=f.readline()
        
except Exception as e:
    print('err: ',e)