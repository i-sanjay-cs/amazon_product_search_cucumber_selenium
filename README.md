
---

# Scenario: Searching for Different Products after Login on Amazon

## Description:
This scenario outlines the steps to search for different products on the Amazon website after logging in.

## Steps:
1. **Given** I am on the Login page URL "https://www.amazon.in/"
    - Opens the browser and navigates to the Amazon login page.

2. **Then** I click on sign in button and wait for sign in page
    - Clicks on the sign-in button and waits for the sign-in page to load. Verifies if the sign-in page is displayed.

3. **Then** I should see Sign In Page
    - Verifies if the sign-in page is successfully displayed.

4. **When** I enter username as "username"
    - Enters the username in the provided field.

5. **When** I Click on Continue button
    - Clicks on the continue button to proceed with the login process.

6. **When** I enter password as "password"
    - Enters the password in the provided field.

7. **When** click on login button
    - Clicks on the login button to log into the account.

8. **Then** I am logged in
    - Verifies if the user is successfully logged in.

9. **Then** I search different "<products>" from the search bar
    - Searches for different products (laptops, pendrive, led tv) based on the value provided in the Examples table.

10. **Then** I exit the browser
    - Closes the browser session.

## Examples:
- **Products:**
  - laptops
  - pendrive
  - led tv

---

This documentation provides a clear outline of the scenario along with the steps involved in executing it. Each step is explained in detail to ensure clarity and understanding. Additionally, examples of different products are provided to demonstrate the flexibility of the scenario.
