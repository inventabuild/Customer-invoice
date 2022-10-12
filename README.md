Mitchell Rabushka

# Invoice Creator made with Django

## Link
Branch
https://inventabuild.github.io/Customer-invoice/

## Short Project Description

An Django based website with multiple databases and foreign keys for creating invoices from customer, item and pricing databases all created in the various apps in the program.

The website uses Django,Python, html, css and Javascript.

## Future upgrades:
1. Foreign key databases used in invoice_manager/invoice_new app will be loaded into API's for use with Javascript instead of the current method of loading the databases into JSON files for use with Javascript.
2. List paid and unpaid invoice in separate views.
3. Open invoices in a read only original format with a "paid" checkbox and "customer check #" input box to update the invoice when payment is made.
4. Create a Bill of Material app that calculates item pricing based on a list of components (and their pricing) used to manufacture the items, overhead and other data entered by the user.  The BOM app will automatically updates the customer pricing database so it will have up to date information for new invoices.
5. Create template literal in invoice_manager/invoice_view that will count through the rows to populate them instead of listing each row separately in the html area.
6. Add invoice_date_closed to Invoice models and tie it to the date that the invoice_paid boolean checbox is checked.  The age (by days) will be calculated from the original invoice_date to the invoice_date_closed or the age counter will remain live if the invoice is still open (invoice_paid boolean checbox is unchecked).
7. Add the age counter (days old) to the invoice_list page and invoice_view for specific invoices.
8. Add the ability to search for open invoices vs closed invoices.
9. Create a search page in each app to search by number, name, etc.
10. Verify if pricing already exists when trying to create new customer pricing.
11. Increase padding / margin between table data on some of the apps and maybe include gridlines to separate items.
12. Make invoice print/save to a pdf when saving the invoice.  Try django library that can give this functionality.
13. Find best way to convert new invoice to pdf file when the page is saved.
14. Make several @media only screen to change formatting of elements as screen size changes.
15. Create a homepage w/ a nice background picture showing some of the things that can be done w/ the app.  Possibly make the links to the apps horizontal w/ a bootstrap navbar instead the current vertical listing.
16. Validate names for no commas so django doesn't throw an error.
17. Validate css.

## User Stories
User Story 1, As someone that creates invoices on the computer, I want to simplify the invoice creation process, so that I can automate invoicing.

User Story 2, As a company that creates invoices on a computer to send to customers, we want to access invoice data so that we save time.

User Story 3, As a company that needs to get paid on invoices sent to customers, we want to access payment term information, so that we can notify customers to pay us when an invoice gets older than 30 days.