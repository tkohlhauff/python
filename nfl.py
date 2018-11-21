from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt
import numpy as np
from collections import OrderedDict
def main():
    curr_year=2017
    years={}
    mod_years={}
    z=0
    while z<=25:
        teams={}
        three_loss_teams={}
        mod_three_loss_teams={}
        changed_year=curr_year-z
        lose_score=[]
        win_score=[]
        mod=[]
        if changed_year<1996:
            wk3_start=26
            wk3_end=40
        elif changed_year<1999:
            wk3_start=29
            wk3_end=43
        else:
            wk3_start=30
            wk3_end=46
        teams={}
        mod_teams={}
        link="https://www.pro-football-reference.com/years/"+str(changed_year)+"/games.htm"
        page=requests.get(link)
        soup=BeautifulSoup(page.content,"html5lib")
        losers=soup.find_all("td",attrs={"data-stat":"loser"})
        x=0
        y=0
        loser_points=soup.find_all("td",attrs={"data-stat":"pts_lose"})
        winner_points=soup.find_all("td",attrs={"data-stat":"pts_win"})
        for score in loser_points:
            if x<len(loser_points)-12:
                lose_score.append(int(score.string))
            x+=1
        x=0
        for score in winner_points:
            if x<len(loser_points)-12:
                win_score.append(int(score.string))
            x+=1
        x=0
        for score in win_score:
            mod.append(win_score[x]-lose_score[x])
            x+=1
        x=0
        for td in losers:
            if x<len(losers)-12:
                if td.string in teams:
                    teams[td.string]+=1
                    if x<wk3_start:
                        mod_teams[td.string]+=mod[x]
                    elif x<wk3_end:
                        mod_teams[td.string]+=mod[x]
                    if teams[td.string]==3 and x<wk3_end:
                        three_loss_teams[td.string]=1
                        mod_three_loss_teams.update({td.string:round(float(mod_teams[td.string])/3,2)})
                else:
                    teams.update({td.string:1})
                    mod_teams.update({td.string:mod[x]})
            x+=1
        for team in three_loss_teams:
            if team in teams:
                three_loss_teams[team]=teams[team]
        years.update({changed_year:three_loss_teams})
        mod_years.update({changed_year:mod_three_loss_teams})
        z+=1

    plot(years,mod_years)
    
    
def plot(years,mod_years):
    str_record=[]
    x=16
    for year in years:
        for team in years[year]:
            annotation=team+":"+str(16-years[year][team])+"-"+str(years[year][team])+"("+str(mod_years[year][team])+")"
            plt.plot(mod_years[year][team],(16-years[year][team]),'bo')
    while x>=0:
        str_record.append(str(16-x))
        x-=1
    plt.ylabel("Wins")
    plt.xlabel("Avg. Margin of Defeat Over First 3 Games")
    plt.yticks(np.arange(17),str_record)
    plt.show()
            
        
main()
