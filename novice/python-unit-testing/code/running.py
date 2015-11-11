def running(values):
   result = []
   lastval = 0
   for v in values:
      count = v + lastval
      lastval = count
      result.append(count)
   return result
