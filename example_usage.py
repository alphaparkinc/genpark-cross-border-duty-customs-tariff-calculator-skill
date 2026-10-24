import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import CrossBorderDutyCustomsTariffCalculatorClient

def main():
    client = CrossBorderDutyCustomsTariffCalculatorClient()
    res = client.calculate_customs_tariff(799.0, "8509", "GB", 45.0)
    print("=== Cross Border Duty & Customs Tariff Calculator Output ===")
    print(f"Product: ${res['product_value_usd']} to {res['destination_country']} (HS: {res['hs_code_chapter']})")
    print(f"Duty: ${res['customs_duty_amount_usd']} ({res['applicable_tariff_rate']}) | Import VAT: ${res['import_vat_amount_usd']}")
    print(f"Total Landed Cost: ${res['total_landed_cost_usd']} (Exempt: {res['duty_exempt_status']})")

if __name__ == '__main__':
    main()
