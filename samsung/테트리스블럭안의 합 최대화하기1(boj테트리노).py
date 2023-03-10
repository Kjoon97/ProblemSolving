import sys

sys.stdin = open("input.txt","r")
'''
문제: 
* n*m 격자위에 테트리스 올려놓아 블럭이 올려진 칸의 합의 최댓 값 구하기
'''
n, m  = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# 가능한 모든 모양을 정의해줍니다.
blocks = [
    [  [1, 1, 1, 1],
       [0, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [0, 1, 0, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 1, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 1, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [1, 0, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 0, 1, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 1, 0],
       [1, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 0, 0],
       [0, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [1, 1, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 0, 0, 0],
       [1, 1, 0, 0],
       [1, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [1, 1, 1, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [1, 1, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 0, 0] ],

     [ [0, 1, 0, 0],
       [1, 1, 1, 0],
       [0, 0, 0, 0],
       [0, 0, 0, 0] ]
]


def in_range(x,y):
    return 0 <= x <n and 0 <= y <m


def get_max_sum(x,y):
    max_sum =0
    for shape in blocks:
        sum_of_nums = sum([grid[x+dx][y+dy] for dx in range(4) for dy in range(4) if in_range(x+dx,y+dy) and shape[dx][dy]])
        max_sum = max(max_sum,sum_of_nums)

    return max_sum


ans = max([get_max_sum(i,j) for i in range(n) for j in range(m)])

print(ans)