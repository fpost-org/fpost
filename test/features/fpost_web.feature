Feature: Testing web ui

Scenario: Testing web ui
  Given website "http://127.0.0.1:5000"
  Then title becomes "fPost"