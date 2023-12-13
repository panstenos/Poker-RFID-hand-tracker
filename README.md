# RFID-hand-tracker
Using RFID readers on a PRi 4 to track poker cards

## <u>Overview</u>
The main objective of this project is to track poker cards dealt to players using RFID technology. To accomplish that, 8 RFID readers were connected to the Raspberry Pi 4's IO ports and special poker cards with microchips inside them had to be bought to leverage the NFC technology. For now a breadboard is used to make the connections, but I am planning to design a PCB to replace the breadboard once I have finilized on the RFID readers' placement across the poker table. 

## <u>Motivation for the Project</u>
Every now and then, I gather with my friends and play poker. On January 2023, I had an interesting idea and decided to start logging the profit/loss of each player after each session. Soon enough I began to experiment with the data and now I have created an interractive dashboard (check my [Poker-Game-Analysis-using-Plotly-Dash][https://github.com/panstenos/Poker-Game-Analysis-using-Plotly-Dash] repo)

## <u>About the dataset</u>
The dataset has around 900 rows and 12 features as follows:
1. Age: age of the patient [years]
1. Sex: sex of the patient [M: Male, F: Female]
1. ChestPainType: chest pain type [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
1. RestingBP: resting blood pressure [mm Hg]
1. Cholesterol: serum cholesterol [mm/dl]
1. FastingBS: fasting blood sugar [1: if FastingBS > 120 mg/dl, 0: otherwise]
1. RestingECG: resting electrocardiogram results [Normal: Normal, ST: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV), LVH: showing probable or definite left ventricular hypertrophy by Estes' criteria]
1. MaxHR: maximum heart rate achieved [Numeric value between 60 and 202]
1. ExerciseAngina: exercise-induced angina [Y: Yes, N: No]
1. Oldpeak: oldpeak = ST [Numeric value measured in depression]
1. ST_Slope: the slope of the peak exercise ST segment [Up: upsloping, Flat: flat, Down: downsloping]
1. HeartDisease: output class [1: heart disease, 0: Normal]

## <u>Source</u>
The dataset was obtained from Kaggle.
This dataset was created by combining different datasets already available independently but not combined before. In this dataset, 5 heart datasets are combined over 11 common features which makes it the largest heart disease dataset available so far for research purposes. The five datasets used for its curation are:

- Cleveland: 303 observations
- Hungarian: 294 observations
- Switzerland: 123 observations
- Long Beach VA: 200 observations
- Stalog (Heart) Data Set: 270 observations
- Total: 1190 observations
- Duplicated: 272 observations

*Final dataset: 918 observations*

