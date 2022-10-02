Mitchell Rabushka

# Invoice Creator made with Django

## Link
https://inventabuild.github.io/crypto-api/

## Short Project Description

An Django based website with multiple databases and foreign keys for creating invoices from customer, item and pricing databases all created in the various apps in the program.

The website uses Django,Python, html, css and Javascript.

## Future upgrades:
1. Foreign key databases used in invoice_manager/invoice_new app will be loaded into API's for use with Javascript instead of the current method of loading the databases into JSON files for use with Javascript.
2. List paid and unpaid invoice in separate views.
3. Open invoices in a read only original format with a "paid" checkbox and "customer check #" input box to update the invoice when payment is made.
4. Create a Bill of Material app that calculates item pricing based on a list of components (and their pricing) used to manufacture the items, overhead and other data entered by the user.  The BOM app will automatically updates the customer pricing database so it will have up to date information for new invoices.
5. Make the company name header at the top of the invoice editable and allow for multiple companies to be stored and selected via a select dropdown list.
6. Create template literal in invoice_manager/invoice_view that will count through the rows to populate them instead of listing each row separately in the html area.

## User Stories
User Story 1, As someone interested in investing in cryptocurrencies, I want to obtain cryptocurrency prices without requiring an account sign-in, so I don't have to take time to sign-in for quotes.

User Story 2, As an investor in cryptocurrencies, I want a screen dedicated to cryptocurrency prices, so I don't get bombarded by adverstisements whenever I want to retrieve prices.

User Story 3, As an investor that uses the 200 day moving average for making investment decisions about cryptocurrencies, I wanted a screen that showed the 200 day moving average of cryptocurrencies, so I can save time.