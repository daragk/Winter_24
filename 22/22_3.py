import re
import keyword

srt_kw = sorted(keyword.kwlist, key=len, reverse=True)
dr_stroka = 'There is another string with some keywords such as "pass", try not to fail it, please!'
for word in srt_kw:
    dr_stroka = re.sub(fr'\b({word})', 'kw', dr_stroka, flags=re.IGNORECASE)
print(dr_stroka)
