-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';

-- according to crime scene report description we know to look for witnesses' transcripts from interviews
SELECT name, transcript FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';

-- According to witness #1 (Ruth)   Eugene Raymond
SELECT activity, people.license_plate, name FROM people, bakery_security_logs WHERE people.license_plate = bakery_security_logs.license_plate
AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25;
-- Suspects According to witness #1: Vanessa (5P2BI95), Bruce (94KL13X), Barry (6P58WS2), Luca (4328GD8),
-- Sofia (G412CB7), Iman (L93JTIZ), Diana (322W7JE), Kelsey (0NTHK55)

-- According to witness #2 (Eugene)
SELECT name, transaction_type FROM people, bank_accounts, atm_transactions WHERE people.id = bank_accounts.person_id
AND atm_transactions.account_number = bank_accounts.account_number AND atm_transactions.month = 7 AND atm_transactions.day = 28
AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street';
--Suspects According to witness #2: Bruce, Brooke, Diana, Kenny, Iman, Luca, Taylor, Benista

-- According to witness #2 (Eugene)
SELECT caller, receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration <60;

UPDATE phone_calls set caller_name = people.name FROM people WHERE phone_calls.caller = people.phone_number;
UPDATE phone_calls set receiver_name = people.name FROM people WHERE phone_calls.receiver = people.phone_number;
