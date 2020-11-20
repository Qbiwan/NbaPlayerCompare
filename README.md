# NBA Player-Compare App deployed on Heroku
Data is first webscrapped from [Basketball Reference](https://www.basketball-reference.com/players/) >> use pandas to pivot data for player comparison in each stat category >> plot each stat using seaborn >> served via streamlit and deployed on heroku.

## Demo


![Demo](Demo/demo.gif)

NBA Player Compare App is deployed on Heroku live at [HERE](https://nba-player-compare.herokuapp.com/)

## Directory

```
nba_player_compare
├── Demo                                         
│     └── demo.gif 
├── streamlit_app.py                          <- streamlit app                                 
├── Procfile                                  <- commands to be executed by heroku on app startup 
├── configuration.py                          <- config file for webscraping
├── .slugignore                               <- for specifying files NOT to upload to heroku  
├── requirements.txt                          <- heroku app dependencies  
├── setup.sh                                  <- shell script setup for heroku  
├── runtime.txt                               <- specify python version for heroku
└── README.md
```

## Libraries

- streamlit
- pandas
- seaborn

