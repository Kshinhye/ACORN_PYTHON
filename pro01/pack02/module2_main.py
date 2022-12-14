#사용자 작성 모듈
print('뭔가를 하다가..')

#다른 모듈의 멤버 호출
list1=[1,3]
list2=[2,4]

import pack2.mymodimport pack02.mymodule1lipack02(list1,list2)
print(pack2.mymodule1.__pack02_)
print(pack2.mymodule1.__pack02_)

def abcd():
    if __name__ == '__main__':
        print('나는 메인 모듈이야')

abcd()
print('\n----같은 패키지에 있는 모듈 읽기----')
#가져오는 방법1
print('가격은{}원'.format(pack2.mymodule1.price))
#가져오는 방법2
from ppack02mymodule1 import price
print('가격은{}원'.format(price))
from pack2.mymodule1 import kbs,mbc
kbs()
mbc()

print('\n----다른 패키지에 있는 모듈 읽기----')
#가져오는 방법1
import etc.mymodule2
print(etc.mymodule2.Hap(5,3))
#가져오는 방법2
from etc.mymodule2 import Cha
print(Cha(5,3))

print('\n----다른 패키지(path가 설정 된)에 있는 모듈 읽기----')
'''
mymodule3은
C:\work\anaconda3\Lib\site-packages 여기에 있다
'''
#가져오는 방법1
import mymodule3
print(mymodule3.Gop(6, 3))
#가져오는 방법2
from mymodule3 import Nanugi
print(Nanugi(6, 3))























