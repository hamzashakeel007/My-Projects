-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
-- according to crime scene report description we know to look for witnesses' transcripts from interviews
SELECT transcript FROM interviews WHERE month = 7 AND day = 28 AND transcript LIKE '%bakery%';

