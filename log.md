### July 23, 2024
* We want to determine what aspect the player needs to input to receive an output
    1. Drive
    2. Putting
    3. Approaching shot
    4. Scrambling

### July 25, 2024 
* Determined what User inputs are needed and what the output/target that we want
* However, user input does not immediately correlate to the target
    - the user inputs (AVG_FAIRWAY_HIT, AVG_DISTANCE) are needed to determine SG_DRIVER which will be used to predict the target
* The target/output is AVG_Stroke
    - to calcuate average stroke:
        * SG_DRIVER:
            - AVG_FAIRWAY_HIT
            - AVG_DISTANCE
        * SG_APPROACING:
            - %(7)
            - AVG_DISTANCE
        * SG_PUTTING:
            - 
            - 
        * SG_SCRAMBLING