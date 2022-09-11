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
invoice_date
item_quantity
invoice_total
invoice_age
invoice_paid (yes/no)
invoice_customer_check_number
customer_po
```

