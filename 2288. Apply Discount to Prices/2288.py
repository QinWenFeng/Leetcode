class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sent = sentence.split(' ')
        for i, val in enumerate(sent):
            num = val.split("$")
            if(len(num) == 2):
                if(val == "${:s}".format(num[1])):
                    try:
                        int(num[1])
                        sent[i] = "${:.2f}".format(int(num[1]) - (int(num[1])*discount/100))
                    except:
                         pass
        return ' '.join(sent)