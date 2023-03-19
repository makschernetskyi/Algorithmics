string1 = "ATTGCACGACATAT"
string2 = "ATTCGACGACGTACC"


def levenstein_distance(str1, str2):
    if str1 == '' and str2 == '':
        return 0
    elif str1 == '' or str2 == '':
        return len(str1 or str2)

    if str1[-1:] == str2[-1:]:
        return levenstein_distance(str1[:-1],str2[:-1])
    else:
        m = min( levenstein_distance(str1,str2[:-1]),levenstein_distance(str1[:-1],str2),levenstein_distance(str1[:-1],str2[:-1]) )
        if str1[:-2] and str2[:-2]:
            m = min(m,levenstein_distance(str1[:-2],str2[:-2]))
        return m+1

if __name__ == "__main__":
    print(100 - (levenstein_distance(string1,string2)/len(string1))*100, '%')