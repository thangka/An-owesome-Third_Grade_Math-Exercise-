#!/usr/bin/env python3


def solve():
    '''Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e - f - 11 + g * h / i - 10 = 66

    Bài toán lớp 3 có số đáp án khổng lồ
    (http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)
    '''

    result = None
    li = range(1, 10)
    result = len([[a, b, c, d, e, f, g, h, i] for a in li
                  for b in li for c in li for d in li for e in li
                  for f in li for g in li for h in li for i in li
                  if (a + d + 12 * e - f - 87) * c * i
                  + 13 * b * i + g * h * c == 0])
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
