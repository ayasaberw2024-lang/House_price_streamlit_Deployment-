# House_price_streamlit_Deployment-


##  How to Run

### 1. Clone the repo

git clone https://github.com/your-username/house-price.git
cd house-price



### 2. create an environment 
open terminal then choose CMD  write this command 

______________________________

conda create -p ./venv python=3.10

press yes 
then activate it 


conda activate ./venv 

this will create a conda env in ur project folder _ u can also check it out on anaconda 
________________________________


### 3. create a requirements.txt file and install all lib in it 
make sure the spelling is correct and u will find the lib in green 
then write the command 

pip install -r requirements.txt


ps: u can declare certain versions of the lib that is sutable for ur project 

use the command : 
pip list
to see them 
________________________________________________

### 4- lets create our notebook  u can use any platform u like 
#### the columns we use in train are 
OverallQual, GrLivArea, GarageArea, 1stFlrSF, FullBath,
YearBuilt, YearRemodAdd, MasVnrArea, Fireplaces,
BsmtFinSF1, LotFrontage, WoodDeckSF, OpenPorchSF,
LotArea, CentralAir
>>>>>>>>>


2- Binary / Categorical already encoded
CentralAir → 0 / 1  --> Y/N




### All categorical features were encoded using Label Encoding to convert them into numerical format suitable for XGBoost model training. Not optimal but womn't matter to xgnoost 
________________________
### 5.  save the model using joblib 
________________________
### 6. put the saved model in ur folder
________________________
### 7. create ur stremlitapp.py




run it using this commmand 


streamlit run streamlit_app.py


__________________________________
ctrl+c to close 
_____________________________
### Now push everything to the repo this will be our first version :D 


git add .
git status 

git commit m- "1 deploy using a streamlit app "

git push 

go to ur repo and check it 
________________________
### 8. deploy it 
