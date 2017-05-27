Feature: Confirming that selenium is set up correctly

	Scenario: check that we can confirm the title of the fPost home page
		When I go to the fPost home page
		Then I should see that the title is "fPost"