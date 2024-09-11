import sys
input = sys.stdin.readline

def set_lyric(num):
    if num == 1:
        return f'{num} bottle'
    elif num == 0:
         return 'no more bottles'
    else:
        return f'{num} bottles'

n = int(input())
cnt = n

while cnt >= 0:
    lyric = set_lyric(cnt)
    if cnt > 0:
        print(f'{lyric} of beer on the wall, {lyric} of beer.')
        cnt -= 1
        next_lyric = set_lyric(cnt)
        print(f'Take one down and pass it around, {next_lyric} of beer on the wall.\n')
    else:
        lyric = set_lyric(n)
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print(f'Go to the store and buy some more, {lyric} of beer on the wall.')
        break