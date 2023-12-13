# RFID-hand-tracker
Using RFID readers on a PRi 4 to track poker cards

## <u>Overview</u>
The main objective of this project is to track poker cards dealt to players using RFID technology. To accomplish that, 8 RFID readers were connected to the Raspberry Pi 4's IO ports and special poker cards with microchips inside them had to be bought to leverage the NFC technology. For now a breadboard is used to make the connections, but I am planning to design a PCB to replace the breadboard once I have finilized on the RFID readers' placement across the poker table. 

## <u>Motivation for the Project</u>
Every now and then, I gather with my friends and play poker. On January 2023, I had an interesting idea and decided to start logging the profit/loss of each player after each session. Soon enough I began to experiment with the data and I have now created an interractive dashboard (check my [Poker-Game-Analysis-using-Plotly-Dash](https://github.com/panstenos/Poker-Game-Analysis-using-Plotly-Dash) repo). Over the past year, there have been some devastating coolers, bluff-catcher hero calls, and generally multiple genious plays but also some extremely stupid actions. After each game we would always talk about the hands and the strategies followed in our poker dedicated whatsapp groupchat. It would be good though if we could have a replay of the action like a televised poker game. I quickly came to the realization that this was a tailored-fit project for my engineering and computing skills as well as my poker interests! 

## <u>Useful links</u>
[Raspberry Pi OS download](https://www.theengineeringprojects.com/2023/01/interface-rfid-module-rc522-with-raspberry-pi-4.html#:~:text=Wiring%20the%20RFID%20RC522&text=Simply%20connecting%207%20of%20the,SCK%20connects%20to%20Pin%2023.)
[Interface RFID module RC522 with Raspberry Pi 4](https://www.theengineeringprojects.com/2023/01/interface-rfid-module-rc522-with-raspberry-pi-4.html#:~:text=Wiring%20the%20RFID%20RC522&text=Simply%20connecting%207%20of%20the,SCK%20connects%20to%20Pin%2023.)
