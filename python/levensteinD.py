string1 = "ATTGCACGACATAT"
string2 = "ATTCGACGACGTACC"


#recursive approach

def D(str1, str2):
    if str1 == '' and str2 == '':
        return 0
    elif str1 == '' or str2 == '':
        return len(str1 or str2)

    if str1[-1:] == str2[-1:]:
        return D(str1[:-1],str2[:-1])
    else:
        m = min( D(str1,str2[:-1]),D(str1[:-1],str2),D(str1[:-1],str2[:-1]) )
        if str1[:-2] and str2[:-2]:
            m = min(m,D(str1[:-2],str2[:-2]))
        return m+1

if __name__ == "__main__":
    print(100 - (D(string1,string2)/len(string1))*100, '%')