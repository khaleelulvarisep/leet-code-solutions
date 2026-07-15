class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        st=startTime.split(':')
        ed=endTime.split(':')

        hr=(int(ed[0])-int(st[0]))*3600
        mt=(int(ed[1])-int(st[1]))*60
        sc=int(ed[2])-int(st[2])
        return hr+mt+sc
        

    


        