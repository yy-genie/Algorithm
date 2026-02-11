def solution(s):
    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for e in range(len(eng)):
        if eng[e] in s:
            idx = s.index(eng[e][0])
            new_s = s[:idx] + str(eng.index(eng[e])) + s[(idx+len(eng[e])):]
            s = new_s
        else:
            new_s = s
        if eng[e] in s:
            solution(new_s)
    return int(new_s)

s = '2three45sixseven'
print(solution(s))

### 아직 고치는 중