# encoding: utf-8
# Author: LW

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        read_str = "1"
        if n==1:
            return '1'

        for x in range(2,n+1):
            read_str =  self.read_str_fun(read_str)

        return read_str


    def read_str_fun(self,str_in):
        #print(str_in)
        tmp_list = list(str_in);
        tmp_list_len = len(tmp_list)
        read_str = ''
        temp_num_str = ''
        temp_num_cnt = 1
        for y in range(tmp_list_len):
            #print(tmp_list[y])
            if y ==0 :
                temp_num_str = tmp_list[y]
            else:
                if temp_num_str == tmp_list[y]:
                    temp_num_cnt += 1
                else:
                    read_str += str(temp_num_cnt) + temp_num_str
                    temp_num_str = tmp_list[y]
                    temp_num_cnt = 1

            if y == tmp_list_len -1:
                read_str += str(temp_num_cnt) + temp_num_str

        #print(read_str)
        return read_str





n = 4
print(Solution().countAndSay(n))
#print(Solution().read_str('1211'))
