from sys import stdin

start, end, stream_end = map(str, input().split())
start = int("".join(start.split(":")))
end = int("".join(end.split(":")))
stream_end = int("".join(stream_end.split(":")))
peopel = {}
count = 0

while(True):
  line = stdin.readline()
  if len(line) < 5: 
        break
    
  t, _id = map(str, line.split())
  t = int("".join(t.split(":")))
  
  if t <= start:
      peopel[_id] = 1
      
  elif end <= t <= stream_end:
    if peopel.get(_id) == 1:
      # 이미 카운팅 했음을 표시해준거임
      peopel[_id] = peopel[_id] + 1 
      count += 1
      
print(count)
