# RFID-hand-tracker
Using RFID readers on a PRi 4 to track poker cards

## <u>Overview</u>
The main objective of this project is to track poker cards dealt to players using RFID technology. To accomplish that, 8 RFID readers were connected to the Raspberry Pi 4's IO ports and special poker cards with microchips inside them had to be bought to leverage the NFC technology. For now a breadboard is used to make the connections, but I am planning to design a PCB to replace the breadboard once I have finilized on the RFID readers' placement across the poker table. 

## <u>Motivation for the Project</u>
Every now and then, I gather with my friends and play poker. On January 2023, I had an interesting idea and decided to start logging the profit/loss of each player after each session. Soon enough I began to experiment with the data and I have now created an interractive dashboard (check my [Poker-Game-Analysis-using-Plotly-Dash](https://github.com/panstenos/Poker-Game-Analysis-using-Plotly-Dash) repo). Over the past year, there have been some devastating coolers, bluff-catcher hero calls, and generally multiple genious plays but also some extremely stupid actions. After each game we would always talk about the hands and the strategies followed in our poker dedicated whatsapp groupchat. It would be good though if we could have a replay of the action like a televised poker game. I quickly came to the realization that this was a tailored-fit project for my engineering and computing skills as well as my poker interests! 

## <u>Useful links</u>
Order Summary:
- [Breadboard + Jumper Cables](https://www.amazon.co.uk/dp/B0B5TCKTQH?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [Soldering pen](https://www.amazon.co.uk/Soldering-Electric-Switch-Adjustable-Temperature200%E2%84%83/dp/B09C7TMQGX/ref=sr_1_6?crid=348HET7OYKJLU&keywords=soldering+pen&qid=1702485501&s=industrial&sprefix=soldering+pen%2Cindustrial%2C72&sr=1-6)
- [Soldering wire](https://www.amazon.co.uk/Balala-Soldering-Repairing-Electronic-Components/dp/B07NT68DXP/ref=sr_1_4?crid=BXNHRILU2WSZ&keywords=soldering+iron+wire&qid=1702485541&s=industrial&sprefix=soldering+iron+wir%2Cindustrial%2C55&sr=1-4)
- [Desoldering pen](https://www.amazon.co.uk/dp/B00BG62F6E?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [RFID-RC522 readers](https://www.amazon.co.uk/dp/B074S9FZC5?ref=ppx_yo2ov_dt_b_product_details&th=1)
- [Raspberry Pi 4](https://www.amazon.co.uk/Raspberry-Pi-Model-4GB/dp/B09TTNF8BT/ref=sr_1_3?keywords=raspberry+pi+4&qid=1702485590&sr=8-3)
- [Micro HDMI to HDMI](https://www.amazon.co.uk/dp/B098XS9XS2?psc=1&ref=ppx_yo2ov_dt_b_product_details)
- [SD card](https://www.amazon.co.uk/Samsung-32GB-Memory-Micro-Adapter/dp/B06XFSZGCC/ref=sr_1_4?crid=1GBDG49DCK1S&keywords=samsung+micro+sd+card+32&qid=1702485942&sprefix=samsung+micro+sd+card+32%2Caps%2C75&sr=8-4)
- [Micro SD card reader](https://www.amazon.co.uk/dp/B00W02VHM6?psc=1&ref=ppx_yo2ov_dt_b_product_details)

- 
Software:
- [Raspberry Pi OS download](https://www.raspberrypi.com/software/)
- [Interface RFID module RC522 with Raspberry Pi 4](https://www.theengineeringprojects.com/2023/01/interface-rfid-module-rc522-with-raspberry-pi-4.html#:~:text=Wiring%20the%20RFID%20RC522&text=Simply%20connecting%207%20of%20the,SCK%20connects%20to%20Pin%2023.)
