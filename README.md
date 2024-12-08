
### **Dataset Column Definitions**
1. **Date**  
    The date on which the match was played.
2. **HomeTeam**  
    The team playing at their home ground.
3. **AwayTeam**  
    The team playing away from home.

---
### **Match Outcomes**

4. **FTHG (Full-Time Home Goals)**  
    Total goals scored by the home team at full time.
5. **FTAG (Full-Time Away Goals)**  
    Total goals scored by the away team at full time.
6. **FTR (Full-Time Result)**  
    Result of the match:
    - **H**: Home win
    - **D**: Draw
    - **A**: Away win

---

### **Half-Time Statistics**

7. **HTHG (Half-Time Home Goals)**  
    Goals scored by the home team at half time.
8. **HTAG (Half-Time Away Goals)**  
    Goals scored by the away team at half time.
9. **HTR (Half-Time Result)**  
    Result at half time:
    - **H**: Home win at half time
    - **D**: Draw at half time
    - **A**: Away win at half time

---

### **Match Official**

10. **Referee**  
    The name of the referee officiating the match.

---

### **Shooting Statistics**

11. **HS (Home Shots)**  
    Total number of shots by the home team.
12. **AS (Away Shots)**  
    Total number of shots by the away team.
13. **HST (Home Shots on Target)**  
    Total number of shots on target by the home team.
14. **AST (Away Shots on Target)**  
    Total number of shots on target by the away team.

---

### **Corner Statistics**

15. **HC (Home Corners)**  
    Total number of corners taken by the home team.
16. **AC (Away Corners)**  
    Total number of corners taken by the away team.
    
---

### **Foul Statistics**

17. **HF (Home Fouls)**  
    Total number of fouls committed by the home team.
18. **AF (Away Fouls)**  
    Total number of fouls committed by the away team.
---

### **Card Statistics**

19. **HY (Home Yellow Cards)**  
    Total number of yellow cards received by the home team.
20. **AY (Away Yellow Cards)**  
    Total number of yellow cards received by the away team.
21. **HR (Home Red Cards)**  
    Total number of red cards received by the home team.
22. **AR (Away Red Cards)**  
    Total number of red cards received by the away team.

---

### **Cumulative Statistics**

23. **HTGS (Home Team Goals Scored)**  
    Total goals scored by the home team up to this match in the current season.
24. **ATGS (Away Team Goals Scored)**  
    Total goals scored by the away team up to this match in the current season.
25. **HTGC (Home Team Goals Conceded)**  
    Total goals conceded by the home team up to this match in the current season.
26. **ATGC (Away Team Goals Conceded)**  
    Total goals conceded by the away team up to this match in the current season.
27. **HTP (Home Team Points)**  
    Total points accumulated by the home team up to this match in the current season.
28. **ATP (Away Team Points)**  
    Total points accumulated by the away team up to this match in the current season.

---

### **Recent Form**

29. **HM1, HM2, HM3, HM4, HM5 (Home Team Last 5 Matches)**  
    Results of the home team's last 5 matches (e.g., **W** = Win, **D** = Draw, **L** = Loss).
30. **AM1, AM2, AM3, AM4, AM5 (Away Team Last 5 Matches)**  
    Results of the away team's last 5 matches.
31. **HTFormPtsStr (Home Team Form Points String)**  
    String representation of the home team's last 5 match results (e.g., **WWLDL**).
32. **ATFormPtsStr (Away Team Form Points String)**  
    String representation of the away team's last 5 match results.
33. **HTFormPts (Home Team Form Points)**  
    Total points earned by the home team in the last 5 matches.
34. **ATFormPts (Away Team Form Points)**  
    Total points earned by the away team in the last 5 matches.

---

### **Win/Loss Streaks**

35. **HTWinStreak3 (Home Team Win Streak 3)**  
    Indicates if the home team has won the last 3 matches (1 = Yes, 0 = No).
36. **HTWinStreak5 (Home Team Win Streak 5)**  
    Indicates if the home team has won the last 5 matches (1 = Yes, 0 = No).
37. **HTLossStreak3 (Home Team Loss Streak 3)**  
    Indicates if the home team has lost the last 3 matches (1 = Yes, 0 = No).
38. **HTLossStreak5 (Home Team Loss Streak 5)**  
    Indicates if the home team has lost the last 5 matches (1 = Yes, 0 = No).
39. **ATWinStreak3 (Away Team Win Streak 3)**  
    Indicates if the away team has won the last 3 matches (1 = Yes, 0 = No).
40. **ATWinStreak5 (Away Team Win Streak 5)**  
    Indicates if the away team has won the last 5 matches (1 = Yes, 0 = No).
41. **ATLossStreak3 (Away Team Loss Streak 3)**  
    Indicates if the away team has lost the last 3 matches (1 = Yes, 0 = No).
42. **ATLossStreak5 (Away Team Loss Streak 5)**  
    Indicates if the away team has lost the last 5 matches (1 = Yes, 0 = No).

---

### **Goal Differences and Points Differences**

43. **HTGD (Home Team Goal Difference)**  
    Goal difference for the home team up to this match (Goals Scored - Goals Conceded).
44. **ATGD (Away Team Goal Difference)**  
    Goal difference for the away team up to this match.
45. **DiffPts (Points Difference)**  
    Difference in points between the home team and the away team.
46. **DiffFormPts (Form Points Difference)**  
    Difference in form points between the home team and the away team.




## God Data

Rk -- **Rank**  
This is a count of the rows from top to bottom.  
It is recalculated following the sorting of a column.

Date -- Date listed is local to the match

xG -- Expected Goals  
xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

Cmp -- Passes Completed  
Includes live ball passes (including crosses) as well as corner kicks, throw-ins, free kicks and goal kicks.

TklW -- Tackles in which the tackler's team won possession of the ball

Subs -- Games as sub  
Game or games player did not start, so as a substitute

Recov -- Number of loose balls recovered

Live -- Live-ball Passes

GCA -- Goal-Creating Actions  
The two offensive actions directly leading to a goal, such as passes, take-ons and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.

TotDist -- Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction

SCA -- Shot-Creating Actions  
The two offensive actions directly leading to a shot, such as passes, take-ons and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.

Rec -- Number of times a player successfully received a pass

Comp -- Competition

GF -- Goals For

GA -- Goals Against

GD -- Goal Difference

Poss -- **Possession**  
Calculated as the percentage of passes attempted

G-PK -- Non-Penalty Goals

PK -- Penalty Kicks Made

PKatt -- Penalty Kicks Attempted

PKm -- Penalty Kicks Missed

xG -- Expected Goals  
xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

npxG -- **Non-Penalty Expected Goals**  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

xGD -- **Expected Goals Difference**  
xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

npxGD -- **Non-Penalty Expected Goals Difference**  
xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

xAG -- **Expected Assisted Goals**  
xG which follows a pass that assists a shot  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

xA -- **Expected Assists**  
The likelihood each completed pass becomes a goal assists  
given the pass type, phase of play, location and distance.  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.  
Minimum 30 minutes played per squad game to qualify as a leader

G-xG -- **Goals minus Expected Goals**  
xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

np:G-xG -- **Non-Penalty Goals minus Non-Penalty Expected Goals**  
xG totals include penalty kicks, but do not include penalty shootouts (unless otherwise noted).  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

A-xAG -- **Assists minus Expected Goals Assisted**  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.

npxG/Sh -- Non-Penalty Expected Goals per shot  
Provided by Opta.  
An underline indicates there is a match that is missing data, but will be updated when available.  
Minimum .395 shots per squad game to qualify as a leader

Sh -- Shots Total  
Does not include penalty kicks

G/Sh -- Goals per shot  
Minimum .395 shots per squad game to qualify as a leader

G/SoT -- Goals per shot on target  
Minimum .111 shots on target per squad game to qualify as a leader  
Note: Shots on target do not include penalty kicks

SoT -- Shots on Target  
Note: Shots on target do not include penalty kicks

SoT% -- Percentage of shots that are on target  
Minimum .395 shots per squad game to qualify as a leader  
Note: Shots on target do not include penalty kicks

Dist -- Average distance, in yards, from goal of all shots taken  
Minimum .395 shots per squad game to qualify as a leader  
Does not include penalty kicks

FK -- Shots from Free Kicks

Cmp -- Passes Completed  
Includes live ball passes (including crosses) as well as corner kicks, throw-ins, free kicks and goal kicks.

Att -- Passes Attempted  
Includes live ball passes (including crosses) as well as corner kicks, throw-ins, free kicks and goal kicks.

Cmp% -- Pass Completion Percentage  
Minimum 30 minutes played per squad game to qualify as a leader  
Includes live ball passes (including crosses) as well as corner kicks, throw-ins, free kicks and goal kicks.

KP -- Passes that directly lead to a shot (assisted shots)

1/3 -- Completed passes that enter the 1/3 of the pitch closest to the goal  
Not including set pieces

PPA -- Completed passes into the 18-yard box  
Not including set pieces

CrsPA -- Completed crosses into the 18-yard box  
Not including set pieces

PrgP -- Progressive Passes  
Completed passes that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch

TotDist -- Total distance, in yards, that completed passes have traveled in any direction

PrgDist -- Progressive Distance  
Total distance, in yards, that completed passes have traveled towards the opponent's goal. Note: Passes away from opponent's goal are counted as zero progressive yards.

Cmp -- Passes Completed  
Passes between 5 and 15 yards

Att -- Passes Attempted  
Passes between 5 and 15 yards

Cmp% -- Pass Completion Percentage  
Passes between 5 and 15 yards  
Minimum 30 minutes played per squad game to qualify as a leader

Cmp -- Passes Completed  
Passes between 15 and 30 yards

Att -- Passes Attempted  
Passes between 15 and 30 yards

Cmp% -- Pass Completion Percentage  
Passes between 15 and 30 yards  
Minimum 30 minutes played per squad game to qualify as a leader

Cmp -- Passes Completed  
Passes longer than 30 yards

Att -- Passes Attempted  
Passes longer than 30 yards

Cmp% -- Pass Completion Percentage  
Passes longer than 30 yards  
Minimum 30 minutes played per squad game to qualify as a leader

SCA -- Shot-Creating Actions  
The two offensive actions directly leading to a shot, such as passes, take-ons and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.

PassLive -- Completed live-ball passes that lead to a shot attempt

PassDead -- Completed dead-ball passes that lead to a shot attempt.  
Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks

TO -- Successful take-ons that lead to a shot attempt

Sh -- Shots that lead to another shot attempt

Fld -- Fouls drawn that lead to a shot attempt

Def -- Defensive actions that lead to a shot attempt

GCA -- Goal-Creating Actions  
The two offensive actions directly leading to a goal, such as passes, take-ons and drawing fouls. Note: A single player can receive credit for multiple actions and the shot-taker can also receive credit.

PassLive -- Completed live-ball passes that lead to a goal

PassDead -- Completed dead-ball passes that lead to a goal. Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks

TO -- Successful take-ons that lead to a goal

Sh -- Shots that lead to another goal-scoring shot

Fld -- Fouls drawn that lead to a goal

Def -- Defensive actions that lead to a goal

Carries -- Number of times the player controlled the ball with their feet

TotDist -- Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction

PrgDist -- Progressive Distance  
Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal

PrgC -- Carries that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any carry into the penalty area. Excludes carries which end in the defending 50% of the pitch

1/3 -- Carries that enter the 1/3 of the pitch closest to the goal

CPA -- Carries into the 18-yard box

Mis -- Number of times a player failed when attempting to gain control of a ball

Dis -- Number of times a player loses control of the ball after being tackled by an opposing player. Does not include attempted take-ons

Rec -- Number of times a player successfully received a pass

PrgR -- Progressive Passes Received  
Completed passes that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch

Rec -- Number of times a player successfully received a pass

PrgR -- Progressive Passes Received  
Completed passes that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area. Excludes passes from the defending 40% of the pitch

Carries -- Number of times the player controlled the ball with their feet

TotDist -- Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction

PrgDist -- Progressive Distance  
Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal

PrgC -- Carries that move the ball towards the opponent's goal line at least 10 yards from its furthest point in the last six passes, or any carry into the penalty area. Excludes carries which end in the defending 50% of the pitch

1/3 -- Carries that enter the 1/3 of the pitch closest to the goal

CPA -- Carries into the 18-yard box

Mis -- Number of times a player failed when attempting to gain control of a ball

Dis -- Number of times a player loses control of the ball after being tackled by an opposing player. Does not include attempted take-ons

Tkl -- Number of players tackled

TklW -- Tackles in which the tackler's team won possession of the ball

Def 3rd -- Tackles in defensive 1/3

Mid 3rd -- Tackles in middle 1/3

Att 3rd -- Tackles in attacking 1/3

Tkl -- Number of dribblers tackled

Att -- Number of unsuccessful challenges plus number of dribblers tackled

Tkl% -- **Percentage of dribblers tackled**  
Dribblers tackled divided by number of attempts to challenge an opposing dribbler  
Minimum .625 dribblers challenged per squad game to qualify as a leader

Lost -- Number of unsucessful attempts to challenge a dribbling player

Blocks -- Number of times blocking the ball by standing in its path

Sh -- Number of times blocking a shot by standing in its path

Pass -- Number of times blocking a pass by standing in its path

Int -- Interceptions

Tkl+Int -- Number of players tackled plus number of interceptions

Clr -- Clearances

Err -- Mistakes leading to an opponent's shot

Live -- Live-ball Passes

Dead -- Dead-ball Passes  
Includes free kicks, corner kicks, kick offs, throw-ins and goal kicks

FK -- Passes attempted from free kicks

TB -- Completed pass sent between back defenders into open space

Sw -- Passes that travel more than 40 yards of the width of the pitch

Crs -- Crosses

TI -- Throw-ins Taken

CK -- Corner Kicks

In -- Inswinging Corner Kicks

Out -- Outswinging Corner Kicks

Str -- Straight Corner Kicks

Off -- Offsides

Blocks -- Blocked by the opponent who was standing in the path

Subs -- Games as sub  
Game or games player did not start, so as a substitute

Mn/Sub -- Minutes Per Substitution  
Minimum 30 minutes played per squad game to qualify as a leader

Off -- Offsides

PKwon -- Penalty Kicks Won

PKcon -- Penalty Kicks Conceded

OG -- Own Goals

Recov -- Number of loose balls recovered
