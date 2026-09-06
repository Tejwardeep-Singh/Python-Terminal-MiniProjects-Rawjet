# quize game

import random

print("Let's Start")
questions = {
    "1. What is the capital of India?\nA) Mumbai\nB) New Delhi\nC) Kolkata\nD) Chennai": "B",

    "2. Who is known as the Father of the Nation in India?\nA) Jawaharlal Nehru\nB) Sardar Patel\nC) Mahatma Gandhi\nD) Subhas Chandra Bose": "C",

    "3. Which planet is known as the Red Planet?\nA) Venus\nB) Mars\nC) Jupiter\nD) Mercury": "B",

    "4. What is the largest ocean in the world?\nA) Atlantic Ocean\nB) Indian Ocean\nC) Arctic Ocean\nD) Pacific Ocean": "D",

    "5. Who wrote the Indian national anthem 'Jana Gana Mana'?\nA) Bankim Chandra Chatterjee\nB) Rabindranath Tagore\nC) Sarojini Naidu\nD) Subhas Chandra Bose": "B",

    "6. Which is the largest state in India by area?\nA) Madhya Pradesh\nB) Maharashtra\nC) Rajasthan\nD) Uttar Pradesh": "C",

    "7. Which is the smallest state in India by area?\nA) Goa\nB) Sikkim\nC) Tripura\nD) Manipur": "A",

    "8. What is the national animal of India?\nA) Lion\nB) Elephant\nC) Bengal Tiger\nD) Leopard": "C",

    "9. What is the national flower of India?\nA) Rose\nB) Lotus\nC) Sunflower\nD) Jasmine": "B",

    "10. Which is the longest river in India?\nA) Yamuna\nB) Brahmaputra\nC) Godavari\nD) Ganga": "D",

    "11. Who was the first President of India?\nA) Dr. Rajendra Prasad\nB) Dr. S. Radhakrishnan\nC) Jawaharlal Nehru\nD) Zakir Husain": "A",

    "12. Who was the first Prime Minister of independent India?\nA) Sardar Vallabhbhai Patel\nB) Jawaharlal Nehru\nC) Lal Bahadur Shastri\nD) Rajendra Prasad": "B",

    "13. Which is the highest civilian award in India?\nA) Padma Shri\nB) Padma Bhushan\nC) Bharat Ratna\nD) Padma Vibhushan": "C",

    "14. Which Indian city is known as the Pink City?\nA) Jaipur\nB) Jodhpur\nC) Udaipur\nD) Bikaner": "A",

    "15. Which Indian city is known as the City of Lakes?\nA) Jaipur\nB) Udaipur\nC) Bhopal\nD) Chandigarh": "B",

    "16. Where is the headquarters of the Reserve Bank of India?\nA) New Delhi\nB) Kolkata\nC) Mumbai\nD) Chennai": "C",

    "17. Which is the largest desert in India?\nA) Thar Desert\nB) Ladakh Desert\nC) Rann of Kutch\nD) Spiti Desert": "A",

    "18. Which mountain range separates India from the Tibetan Plateau?\nA) Aravalli\nB) Western Ghats\nC) Himalayas\nD) Vindhyas": "C",

    "19. Which is the highest mountain peak in India?\nA) Mount Everest\nB) Kangchenjunga\nC) Nanda Devi\nD) Kamet": "B",

    "20. Which state is known as the 'Land of Five Rivers'?\nA) Haryana\nB) Rajasthan\nC) Punjab\nD) Himachal Pradesh": "C",

    "21. Who founded the Maurya Empire?\nA) Ashoka\nB) Chandragupta Maurya\nC) Bindusara\nD) Samudragupta": "B",

    "22. Who was the first emperor of the Mughal Empire in India?\nA) Akbar\nB) Humayun\nC) Babur\nD) Shah Jahan": "C",

    "23. Who built the Taj Mahal?\nA) Akbar\nB) Shah Jahan\nC) Aurangzeb\nD) Jahangir": "B",

    "24. In which year did India gain independence?\nA) 1945\nB) 1946\nC) 1947\nD) 1950": "C",

    "25. When was the Constitution of India adopted?\nA) 15 August 1947\nB) 26 January 1950\nC) 26 November 1949\nD) 2 October 1949": "C",

    "26. When did the Constitution of India come into effect?\nA) 15 August 1947\nB) 26 November 1949\nC) 26 January 1950\nD) 2 October 1950": "C",

    "27. Who is known as the Iron Man of India?\nA) Bhagat Singh\nB) Sardar Vallabhbhai Patel\nC) Subhas Chandra Bose\nD) Bal Gangadhar Tilak": "B",

    "28. Who gave the slogan 'Give me blood, and I will give you freedom'?\nA) Mahatma Gandhi\nB) Bhagat Singh\nC) Subhas Chandra Bose\nD) Jawaharlal Nehru": "C",

    "29. Who was the first woman Prime Minister of India?\nA) Sarojini Naidu\nB) Indira Gandhi\nC) Pratibha Patil\nD) Sucheta Kriplani": "B",

    "30. Which movement was launched by Mahatma Gandhi in 1942?\nA) Non-Cooperation Movement\nB) Civil Disobedience Movement\nC) Quit India Movement\nD) Swadeshi Movement": "C",

    "31. What is the chemical symbol for gold?\nA) Ag\nB) Au\nC) Gd\nD) Go": "B",

    "32. What is the chemical symbol for silver?\nA) Si\nB) S\nC) Ag\nD) Sr": "C",

    "33. Which gas is most abundant in Earth's atmosphere?\nA) Oxygen\nB) Carbon dioxide\nC) Nitrogen\nD) Hydrogen": "C",

    "34. What is the hardest natural substance on Earth?\nA) Iron\nB) Diamond\nC) Quartz\nD) Graphite": "B",

    "35. What is the SI unit of force?\nA) Joule\nB) Watt\nC) Newton\nD) Pascal": "C",

    "36. What is the SI unit of electric current?\nA) Volt\nB) Ampere\nC) Ohm\nD) Watt": "B",

    "37. Which organ pumps blood throughout the human body?\nA) Brain\nB) Liver\nC) Heart\nD) Kidney": "C",

    "38. Which is the largest organ of the human body?\nA) Liver\nB) Brain\nC) Skin\nD) Lungs": "C",

    "39. Which vitamin is mainly produced when human skin is exposed to sunlight?\nA) Vitamin A\nB) Vitamin B12\nC) Vitamin C\nD) Vitamin D": "D",

    "40. What is the boiling point of water at sea level?\nA) 50°C\nB) 75°C\nC) 100°C\nD) 120°C": "C",

    "41. Which planet is closest to the Sun?\nA) Venus\nB) Mercury\nC) Earth\nD) Mars": "B",

    "42. Which is the largest planet in our Solar System?\nA) Saturn\nB) Earth\nC) Jupiter\nD) Neptune": "C",

    "43. Which planet is famous for its prominent rings?\nA) Mars\nB) Saturn\nC) Uranus\nD) Neptune": "B",

    "44. How many planets are there in the Solar System?\nA) 7\nB) 8\nC) 9\nD) 10": "B",

    "45. What is Earth's natural satellite?\nA) Sun\nB) Mars\nC) Moon\nD) Venus": "C",

    "46. Which is the largest continent in the world?\nA) Africa\nB) Europe\nC) North America\nD) Asia": "D",

    "47. Which is the smallest continent?\nA) Europe\nB) Australia\nC) Antarctica\nD) South America": "B",

    "48. Which is the largest country in the world by area?\nA) Canada\nB) China\nC) Russia\nD) United States": "C",

    "49. Which is the smallest country in the world?\nA) Monaco\nB) Vatican City\nC) San Marino\nD) Liechtenstein": "B",

    "50. Which river is the longest in the world according to the commonly accepted measurement?\nA) Amazon\nB) Nile\nC) Yangtze\nD) Mississippi": "B",

    "51. Which country is known as the Land of the Rising Sun?\nA) China\nB) South Korea\nC) Japan\nD) Thailand": "C",

    "52. What is the capital of Australia?\nA) Sydney\nB) Melbourne\nC) Brisbane\nD) Canberra": "D",

    "53. What is the capital of Canada?\nA) Toronto\nB) Vancouver\nC) Ottawa\nD) Montreal": "C",

    "54. What is the capital of Japan?\nA) Kyoto\nB) Osaka\nC) Hiroshima\nD) Tokyo": "D",

    "55. What is the capital of France?\nA) Rome\nB) Madrid\nC) Paris\nD) Berlin": "C",

    "56. Which country gifted the Statue of Liberty to the United States?\nA) United Kingdom\nB) France\nC) Germany\nD) Spain": "B",

    "57. Which ocean lies between Africa and Australia?\nA) Atlantic Ocean\nB) Pacific Ocean\nC) Indian Ocean\nD) Arctic Ocean": "C",

    "58. Which is the coldest continent?\nA) Europe\nB) Asia\nC) Antarctica\nD) North America": "C",

    "59. Which country has the largest population in the world as of the 2020s?\nA) United States\nB) China\nC) India\nD) Indonesia": "C",

    "60. The Great Wall is located in which country?\nA) Japan\nB) China\nC) Mongolia\nD) South Korea": "B",

    "61. Which sport is associated with Wimbledon?\nA) Cricket\nB) Football\nC) Tennis\nD) Hockey": "C",

    "62. How many players are there in a cricket team?\nA) 9\nB) 10\nC) 11\nD) 12": "C",

    "63. Which country hosted the first modern Olympic Games in 1896?\nA) France\nB) Greece\nC) Italy\nD) United Kingdom": "B",

    "64. Who is known as the 'Flying Sikh' of India?\nA) Milkha Singh\nB) Kapil Dev\nC) Dhyan Chand\nD) P. T. Usha": "A",

    "65. Which sport uses the term 'love' for a score of zero?\nA) Cricket\nB) Tennis\nC) Football\nD) Badminton": "B",

    "66. The FIFA World Cup is associated with which sport?\nA) Basketball\nB) Football\nC) Tennis\nD) Rugby": "B",

    "67. Which Indian athlete won India's first individual Olympic gold medal?\nA) Neeraj Chopra\nB) Abhinav Bindra\nC) Sushil Kumar\nD) Leander Paes": "B",

    "68. Neeraj Chopra is associated with which sport?\nA) Wrestling\nB) Boxing\nC) Javelin throw\nD) Shooting": "C",

    "69. Which sport is played at the French Open?\nA) Tennis\nB) Cricket\nC) Golf\nD) Hockey": "A",

    "70. How many rings are there on the Olympic flag?\nA) 4\nB) 5\nC) 6\nD) 7": "B",

    "71. What does CPU stand for?\nA) Central Processing Unit\nB) Computer Processing Utility\nC) Central Program Unit\nD) Computer Primary Unit": "A",

    "72. What does RAM stand for?\nA) Read Access Memory\nB) Random Access Memory\nC) Rapid Access Module\nD) Run Access Memory": "B",

    "73. Which language is primarily used to structure web pages?\nA) Python\nB) HTML\nC) SQL\nD) C++": "B",

    "74. What does WWW stand for?\nA) World Wide Web\nB) World Web Window\nC) Wide World Web\nD) Web World Wide": "A",

    "75. Which company developed the Windows operating system?\nA) Apple\nB) Google\nC) Microsoft\nD) IBM": "C",

    "76. Which of these is an operating system?\nA) Linux\nB) Oracle\nC) Python\nD) Chrome": "A",

    "77. What is the full form of URL?\nA) Uniform Resource Locator\nB) Universal Reference Link\nC) Uniform Reference Location\nD) Universal Resource Locator": "A",

    "78. Which device is used to connect multiple devices within a local network?\nA) Switch\nB) Monitor\nC) Printer\nD) Scanner": "A",

    "79. Which protocol is commonly used to access websites securely?\nA) HTTP\nB) FTP\nC) HTTPS\nD) SMTP": "C",

    "80. What is the binary representation of decimal number 2?\nA) 01\nB) 10\nC) 11\nD) 100": "B",

    "81. What is the currency of Japan?\nA) Yuan\nB) Won\nC) Yen\nD) Ringgit": "C",

    "82. What is the currency of the United Kingdom?\nA) Euro\nB) Pound Sterling\nC) Dollar\nD) Franc": "B",

    "83. What is the currency of India?\nA) Rupee\nB) Taka\nC) Dinar\nD) Riyal": "A",

    "84. Which institution is responsible for monetary policy in India?\nA) SEBI\nB) RBI\nC) SBI\nD) NITI Aayog": "B",

    "85. What does GDP stand for?\nA) Gross Domestic Product\nB) General Domestic Production\nC) Gross Development Process\nD) Government Domestic Product": "A",

    "86. Which tax replaced many indirect taxes in India in 2017?\nA) VAT\nB) GST\nC) CST\nD) Excise Duty": "B",

    "87. What does GST stand for?\nA) General Sales Tax\nB) Goods and Services Tax\nC) Government Service Tax\nD) Goods Supply Tax": "B",

    "88. Which organization regulates the securities market in India?\nA) RBI\nB) SEBI\nC) IRDAI\nD) NABARD": "B",

    "89. What is the full form of ATM?\nA) Automatic Transfer Machine\nB) Automated Teller Machine\nC) Automatic Transaction Method\nD) Automated Transfer Method": "B",

    "90. Which is the central bank of India?\nA) State Bank of India\nB) Punjab National Bank\nC) Reserve Bank of India\nD) Bank of India": "C",

    "91. Which is the largest democracy in the world?\nA) United States\nB) India\nC) United Kingdom\nD) Canada": "B",

    "92. How many fundamental rights are currently guaranteed by the Constitution of India?\nA) 5\nB) 6\nC) 7\nD) 8": "B",

    "93. Who is the constitutional head of India?\nA) Prime Minister\nB) Chief Justice of India\nC) President\nD) Home Minister": "C",

    "94. The Parliament of India consists of which two houses?\nA) Lok Sabha and Rajya Sabha\nB) Vidhan Sabha and Vidhan Parishad\nC) Lok Sabha and Vidhan Sabha\nD) Rajya Sabha and Vidhan Parishad": "A",

    "95. What is the minimum age required to become the President of India?\nA) 25 years\nB) 30 years\nC) 35 years\nD) 40 years": "C",

    "96. What is the minimum voting age in India?\nA) 16 years\nB) 18 years\nC) 21 years\nD) 25 years": "B",

    "97. Which body conducts elections in India?\nA) Supreme Court\nB) Election Commission of India\nC) Parliament\nD) Ministry of Home Affairs": "B",

    "98. Who is the highest judicial authority in India?\nA) High Court\nB) Supreme Court\nC) Parliament\nD) District Court": "B",

    "99. Which article of the Indian Constitution deals with equality before law?\nA) Article 12\nB) Article 14\nC) Article 19\nD) Article 21": "B",

    "100. Which national day is celebrated in India on 26 January?\nA) Independence Day\nB) Gandhi Jayanti\nC) Republic Day\nD) Constitution Day": "C"
}

while True:

    name = input("\nEnter your name: ").strip()

    if not name:
        print("Please enter a valid name.")
        continue

    score = 0

    print("\n" + "=" * 50)
    print(f"Welcome, {name}!")
    print("You will be asked 5 randomly selected questions.")
    print("Each correct answer = 1 mark")
    print("Each wrong answer = 0 marks")
    print("=" * 50)

    # Randomly select 5 UNIQUE questions
    selected_questions = random.sample(list(questions.items()), 5)

    # Ask the 5 questions
    for question_number, (question, correct_answer) in enumerate(
        selected_questions, start=1
    ):

        print("\n" + "-" * 50)
        print(f"Question {question_number} of 5")
        print("-" * 50)

        print(question)

        # Take answer
        while True:
            answer = input("\nEnter your answer (A/B/C/D): ").strip().upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid answer! Please enter A, B, C, or D.")

        # Check answer
        if answer == correct_answer:
            print("Correct! ✓")
            score += 1
        else:
            print("Wrong! ✗")
            print(f"The correct answer was: {correct_answer}")

    # Calculate result
    percentage = (score / 5) * 100

    print("\n" + "=" * 50)
    print("              QUIZ RESULT")
    print("=" * 50)

    print(f"Candidate : {name}")
    print(f"Score     : {score}/5")
    print(f"Percentage: {percentage:.0f}%")

    # Grade
    if score == 5:
        grade = "Excellent"
    elif score == 4:
        grade = "Very Good"
    elif score == 3:
        grade = "Good"
    elif score == 2:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    print(f"Result    : {grade}")

    print("=" * 50)

    # Play again?
    again = input("\nDo you want to play again? (Y/N): ").strip().upper()

    if again != "Y":
        print("\nThank you for playing!")
        break
