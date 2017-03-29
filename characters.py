class characters(object):
    def save(self,level,name,aType):
        f=open('savefile.txt','w')
        y=0
        for x in level:
            if y==0:
                f.write(self.level[y],'\n')
            if y==1:
                f.write(self.name[y],'\n')
            if y==2:
                f.write(self.aType[y],'\n')
            y+=1
            if y==3:
                y=0
        f.close()
    def load(self):
        x=0
        charArray=[]
        level=[]
        name=[]
        aType=[]
        characters=[]
        f=open('savefile.txt','r')
        for line in f:
            charArray.append(line)
        x=0
        for info in charArray:
            
            if x==0:
                level.append(info)
            if x==1:
                name.append(info)
            if x==2:
                aType.append(info)
            x+=1
            if x==3:
                x=0
        x=0
        for thing in level:
            level[x]=level[x].rstrip()
            name[x]=name[x].rstrip()
            aType[x]=aType[x].rstrip()
            x+=1
        return level,name,aType

    
            
