#first 7-digit palindromic prime found in consecutive digets of pi
def ispalindrome(word):
    return word == word[::-1]

def arccot(x, unity):
    sum = xpower = unity // x
    n = 3
    sign = -1
    while 1:
        xpower = xpower // (x*x)
        term = xpower // n
        if not term:
            break
        sum += sign * term
        sign = -sign
        n += 2
    return sum

def pi(digits):
    unity = 10**(digits + 10)
    pi = 4 * (4*arccot(5, unity) - arccot(239, unity))
    return pi // 10**10

def isprime(num):
    if num < 2:
        return False
    else:
    	for div in range(2, (num/2)+1):
    		if num%div==0:
    			return False
    	else:
    		return True

pietep=str(pi(15000))
pie = pietep[1:]
startpos =0
done=False

while not done:
    if len(pie) >= startpos+7:
        pal = pie[startpos:startpos+7]
        if ispalindrome(pal) and isprime(int(pal)):
            print pal
            done = True
        else:
            startpos += 1
    else:
        done = True

print "None"