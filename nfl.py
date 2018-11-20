from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict
def main():
    curr_year=2017
    years={}
    z=0
    while z<=25:
        teams={}
        three_loss_teams={}
        changed_year=curr_year-z
        if changed_year<1994:
            raiders="Los Angeles Raiders"
            cardinals="Phoenix Cardinals"
            end_of_games=223
            wk3_start=26
            wk3_end=38
        elif changed_year<1995:
            rams="Los Angeles Rams"
            wk3_start=26
            wk3_end=42
        elif changed_year<1996:
            end_of_games=239
            wk3_start=26
            wk3_end=45
        elif changed_year<1997:
            texans="Houston Oilers"
        elif changed_year<1999:
            titans="Tennessee Oilers"
            wk3_start=28
            wk3_end=43
        elif changed_year<2000:
            end_of_games=247
        elif changed_year<2016:
            rams="St. Louis Rams"
        elif changed_year<2017:
            chargers="San Diego Chargers"
        else:
            chargers="Los Angeles Chargers"
            titans="Tennessee Titans"
            texans="Houston Texans"
            rams="Los Angeles Rams"
            raiders="Oakland Raiders"
            cardinals="Arizona Cardinals"
            wk3_start=30
            wk3_end=46
            end_of_games=256
        teams={"Philadelphia Eagles":0, "Atlanta Falcons":0,"Cincinnati Bengals":0,"Indianapolis Colts":0,"Baltimore Ravens":0,"Buffalo Bills":0,"Tampa Bay Buccaneers":0,"New Orleans Saints":0,"Pittsburgh Steelers":0,"Cleveland Browns":0,"New England Patriots":0,texans:0,"Miami Dolphins":0,titans:0,"Minnesota Vikings":0,"San Francisco 49ers":0,"Jacksonville Jaguars":0,"New York Giants":0,"Kansas City Chiefs":0,chargers:0,"Washington Redskins":0,cardinals:0,"Denver Broncos":0,"Seattle Seahawks":0,"Carolina Panthers":0,"Dallas Cowboys":0,"Green Bay Packers":0,"Chicago Bears":0,"New York Jets":0,"Detroit Lions":0,rams:0,raiders:0}
        link="https://www.pro-football-reference.com/years/"+str(changed_year)+"/games.htm"
        page=requests.get(link)
        soup=BeautifulSoup(page.content,"html5lib")
        losers=soup.find_all("td",class_="left")
        x=0
        y=0
        for td in losers:
            x+=1
            if x%4==0 and x/4<end_of_games:
                y+=1
                if td.string in teams:
                    teams[td.string]+=1
                if x>wk3_start*4 and x<wk3_end*4 and teams[td.string]==3:
                    three_loss_teams[td.string]=3
        for team in three_loss_teams:
            if team in teams:
                three_loss_teams[team]=teams[team]
        years.update({changed_year:three_loss_teams})
        z+=1
    plot(years)
    
    
def plot(years):
    plt.title("Teams Records after starting 0-3 (1992-2017)")
    plt.xlabel("Record")
    
    record=[]
    loss_dict={}
    for year in years:
        for team in years[year]:
            if years[year][team] in loss_dict:
                loss_dict[years[year][team]]+=1
            else:
                loss_dict[years[year][team]]=1
                record.append(years[year][team])
    record=sorted(record, reverse=True)
    str_record=[]
    for x in record:
        str_record.append(str(16-x)+"-"+str(x))
    od_loss_dict=OrderedDict(sorted(loss_dict.items(),reverse=True))
    num_time=[]
    for key, value in od_loss_dict.items():
        num_time.append(value)
    plt.ylabel("# of Teams (Total: "+str(sum(num_time))+")")
    plt.xticks(np.arange(len(record)),str_record)
    plt.yticks(np.arange(20))
    plt.bar(np.arange(len(record)),num_time)
    plt.show()
            
        
main()
