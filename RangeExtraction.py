def solution(args):
    size = len(args)   
    sequencePos = []//1 if num is in a sequence, 0 if num is not in sequence
    
    prev = args[0]
    count = 0
    for i in args:
        if i!=prev:
            if i-prev == 1:
                if count==1:
                    sequencePos.append(1)
                sequencePos.append(1)
            else:
                if count==1:
                    sequencePos.append(0)
                sequencePos.append(0)
                
        prev = i  
        count+=1
    iterate = size
    ans = ""
    howManyCons = 0;
    
    while iterate > 0:
          iterate-=1
          
          seq = str(args[iterate])
          
          if sequencePos[iterate]==1:
              seq = "-"+ str(args[iterate])
              secondIter = iterate
              while secondIter >= 0:
                  howManyCons+=1
                  if sequencePos[secondIter]==0:
                      break;
                  
                  secondIter-=1
              if secondIter <0:
                  secondIter = 0
              seq = str(args[secondIter]) + seq
                            
              iterate = secondIter
              if howManyCons < 3:
                  
                  seq= str(args[iterate])+","+str(args[iterate+1])
                               
          howManyCons = 0
          
          ans = seq + ","+ ans 
        
    return ans[:-1]
