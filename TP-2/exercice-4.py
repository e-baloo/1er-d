
def func(A, B):
    C = (A and not B) or (not A and B)
    print("A = {0} / B = {1} / C = {2}".format(A, B, C))

func(True, True)
func(True, False)
func(False, True)
func(False, False)
