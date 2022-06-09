def pali(a):
    return a==a[::-1]

a=str(input('enter string'))
fn=pali(a)

if fn:
    print('palindrome')
else:
    print('not palindrome..')