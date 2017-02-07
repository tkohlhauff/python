from riotwatcher import RiotWatcher
w = RiotWatcher('b5b499ca-f687-4315-9121-14268f314fb0')
NUMBER_OF_GAMES=5
bonus=0
def main():
    summ=input("What is the summoner name?: ")
    me=w.get_summoner(name=summ)
    get_stats(me,summ)
def get_stats(me,summ):
    kills=0
    assists=0
    deaths=0
    cs=0
    tripK=0
    quadK=0
    pentaK=0
    ranked=w.get_match_history(summoner_id=me['id'],end_index=NUMBER_OF_GAMES)
    for x in range(0,5):
        assist=ranked['matches'][x]['participants'][0]['stats']['assists']
        bonusChk(assist)
        assists+=assist
        kill=ranked['matches'][x]['participants'][0]['stats']['kills']
        bonusChk(kill)
        kills+=kill
        deaths+=ranked['matches'][x]['participants'][0]['stats']['deaths']
        cs+=ranked['matches'][x]['participants'][0]['stats']['minionsKilled']
        tripK+=ranked['matches'][x]['participants'][0]['stats']['tripleKills']
        quadK+=ranked['matches'][x]['participants'][0]['stats']['quadraKills']
        pentaK+=ranked['matches'][x]['participants'][0]['stats']['pentaKills']
    fantasy_score(summ,assists,kills,deaths,cs,tripK,quadK,pentaK)
def bonusChk(x):
    global bonus
    if x>10:
        bonus+=2    
def fantasy_score(name,a,k,d,cs,tk,qk,pk):
    total=bonus+(tk*2)+(qk*5)+(pk*10)+(a*1.5)+(k*2)+(cs*.01)-(d*.5)
    kda=(k+a)/d
    avg=total/NUMBER_OF_GAMES
    print("Summary of last",NUMBER_OF_GAMES,"games")
    print(k," kills",'\n',
          d," deaths",'\n',
          a," assists",'\n',
          format(kda,".2f")," kda",'\n',
          cs," cs",sep='')
          
    print(name,"scored a total of",total,"fantasy points in the last 5 games.")
    print("They average",format(avg,".2f"),"points per game")
    newSumm()
def newSumm():
    again=input("Would you like to search a different summoner?: ")
    if again in ["Y","yes","Yes","y"]:
        main()
    else:
        print("Thank you for using the solo q fantasy search!")
        
main()
