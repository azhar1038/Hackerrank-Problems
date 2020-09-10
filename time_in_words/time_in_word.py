def timeInWords(h, m):
    word = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half']
    after = m > 30
    to_past = 'past'
    if after:
        m = 60-m
        to_past = 'to'
    if m == 0:
        return f"{word[h-1]} o' clock"
    minute_word='minutes '
    if m == 1:
        minute_word='minute '
    elif m == 15 or m == 30:
        minute_word=''
    hour=word[h-1]
    if after:
        hour=word[h]
    return f"{word[m-1]} {minute_word}{to_past} {hour}" 

print(timeInWords(5, 59)) 