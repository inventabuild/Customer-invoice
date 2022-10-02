# Stopped at step 36 in OneNote
# Tables
```
CUSTOMER_MANAGER TABLE
customer_id
customer_name
customer_address
customer_city
customer_state
customer_country
customer_zip_code

ITEM_MANAGER TABLE
item_id
item_name
item_description
item_internal_cost

CUSTOMER_PRICING_MANAGER TABLE
customer_id (foreign key)
item_id (foreign key)
customer_pricing_id
customer_pricing

INVOICE_MANAGER
customer_id (foreign key)
customer_pricing_id (foreign key)
item_id (foreign key)
invoice_id
invoice_number
invoice_date
item_quantity
invoice_total
invoice_age
invoice_paid (yes/no)
invoice_customer_check_number
customer_po
```
```
Deprecated when address put in textarea
html
<!-- <div class="customer-mailing-address">
<span id="customer_mailing_address-name"></span>
<span id="customer_mailing_address-address"></span>
<span id="customer_mailing_address-city"></span>
<span id="customer_mailing_address-state"></span>
<span id="customer_mailing_address-zip_code"></span>
</div> -->
javascript
// document.getElementById("customer_mailing_address-name").innerHTML = js_json_customer_all[customerSelectObject.value-1].fields.name
// document.getElementById("customer_mailing_address-address").innerHTML = js_json_customer_all[customerSelectObject.value-1].fields.address
// document.getElementById("customer_mailing_address-city").innerHTML = js_json_customer_all[customerSelectObject.value-1].fields.city
// document.getElementById("customer_mailing_address-state").innerHTML = js_json_customer_all[customerSelectObject.value-1].fields.state
// document.getElementById("customer_mailing_address-zip_code").innerHTML = js_json_customer_all[customerSelectObject.value-1].fields.zip_code
```
```
Today's date from Raphael Balet (https://stackoverflow.com/questions/6982692/how-to-set-input-type-dates-default-value-to-today)
```