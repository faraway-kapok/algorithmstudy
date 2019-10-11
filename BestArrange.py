"""
一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你每一个项目开始的时间和结束的时间，你来安排宣讲的日程
要求会议室进行的宣讲的场次，最多，返回这个最多宣讲场次
贪心策略
1.按照最早时间，错
2.按照时间短，错
3.按照哪个项目早结束，bingo，然后删除掉所有因为这个项目的开始无法进行的项目，
再次选择早结束的项目

"""

class program:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __lt__(self, other):
        return self.end < other.end

def bestArrange(programs, cur):
    sortedprograms = sorted(programs)
    result = 0
    for i in range(len(programs)):
        if cur <= sortedprograms[i].start:
            result += 1
            cur = sortedprograms[i].end
    
    return result

if __name__ == "__main__":
    starts = []