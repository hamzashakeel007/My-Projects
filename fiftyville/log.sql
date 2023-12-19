-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- according to crime scene report description we know to look for the time and activity, and license_plate from bakery security log
SELECT activity, license_plate FROM bakery_security_log WHERE month = 7 AND day = 28 AND street = 'Humphrey Street'
AND hour = 10 AND minute = 15;
