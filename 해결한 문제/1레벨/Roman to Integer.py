''' leetcode 문제 '''
class Solution:

    # 후에 계산된 문자들을 삭제합니다.
    def change_num(self, input_dict, s):
        for k in input_dict.keys():
            if k in s:
                self.ret += s.count(k) * input_dict[k]
                s = s.replace(k,'')
        return s

    def romanToInt(self, s: str) -> int:
        self.comb_num = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        self.one_num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        self.sum_num = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        self.ret = 0

        self.ret = 0
        # 문자열에 해당하는 값들을 추출합니다.
        # 2개가 합쳐진 문자부터 확인합니다.
        
        if len(s) == 1:
            return self.one_num[s]
        s = self.change_num(self.comb_num, s)
        if s:      
            self.change_num(self.one_num, s)

        return int(self.ret)

    # 2개 단위로 넘어가며 합쳐질 수 있는 단어를 찾습니다.( 앞, 뒤로 )
    def inOrder(self, s):
        self.ret = 0
        total_len = len(s)
        if total_len == 1:
            return self.sum_num[s]
        for i in range(total_len)[::2]:
            try:
                try:
                    self.ret += self.sum_num[s[i-1:i+1]]
                    self.ret -= self.sum_num[s[i-1]]
                    try:
                        self.ret += self.sum_num[s[i+1]]
                    except:
                        pass
                except:
                    self.ret += self.sum_num[ s[i:i+2] ]
            except:
                self.ret += self.sum_num[ s[i] ]
                try:
                    self.ret += self.sum_num[ s[i+1] ]
                except:
                    pass
        return self.ret

    # 하나씩 넘어가며 뒤에 있는 수와 합쳐질 수 있는지 확인합니다.
    # 합쳐진다면 cnt += 1 을 하여 계산한 문자는 넘어가도록 설정합니다.
    def inOrder_upgrade(self, s):
        self.ret = 0
        total_len = len(s)
        if total_len == 1:
            return self.sum_num[s]
        
        cnt = 0
        for i in range(total_len):
            i += cnt
            try:
                self.ret += self.sum_num[s[i:i+2]]
                cnt += 1
            except:
                try:
                    self.ret += self.sum_num[ s[i] ]
                except:
                    pass

        return self.ret

roman_int = Solution()

print( roman_int.inOrder("MCMXCIV") )
print( roman_int.romanToInt("MCMXCIV") )
print( roman_int.inOrder_upgrade('MCMXCIV'))