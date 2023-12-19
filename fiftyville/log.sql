-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

-- according to crime scene report description we know to look for witnesses' transcripts from interviews
SELECT name, transcript FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- According to witness #1 (Ruth)
SELECT activity, people.license_plate, name FROM people, bakery_security_logs WHERE people.license_plate = bakery_security_logs.license_plate
AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;
-- Suspects According to witness #1: Vanessa (5P2BI95), Bruce (94KL13X), Barry (6P58WS2), Luca (4328GD8),
-- Sofia (G412CB7), Iman (L93JTIZ), Diana (322W7JE), Kelsey (0NTHK55)

-- According to witness #2 (Eugene)
SELECT name, transaction_type FROM people, bank_accounts, atm_transactions WHERE people.id = bank_accounts.person_id
AND atm_transactions.account_number = bank_accounts.account_number AND atm_transactions.month = 7 AND atm_transactions.day = 28
AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street';
--Suspects According to witness #2: Bruce, Brooke, Diana, Kenny, Iman, Luca, Taylor, Benista

-- According to witness #3 (Raymond)
SELECT caller_name, receiver_name,caller, receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration <60;

ALTER TABLE phone_calls ADD caller_name;
ALTER TABLE phone_calls ADD receiver_name;

UPDATE phone_calls SET caller_name = people.name FROM people WHERE phone_calls.caller = people.phone_number;
UPDATE phone_calls SET receiver_name = people.name FROM people WHERE phone_calls.receiver = people.phone_number;

SELECT caller_name, receiver_name,caller, receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration <60;
--Suspects (Accomplices) according to witness #3: Sofia (Jack), Kelsey (Larry)(Melissa), Bruce (Robin),
-- Taylor (James), Diana (Philip), Carina (Jacqueline), Kenny (Doris), Benista (Anna)

-- Checking the earliest flight the day after the robbery
SELECT id, hour, minute, origin_airport_id, destination_airport_id, city FROM flights, airports WHERE month = 7 AND day = 29
ORDER BY hour ASC LIMIT 1;

