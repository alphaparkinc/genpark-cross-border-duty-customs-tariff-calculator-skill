import json
from typing import Dict, Any, Optional

class CrossBorderDutyCustomsTariffCalculatorClient:
    """
    Production-grade global e-commerce customs duty and import tariff calculator.
    Applies destination de minimis rules and calculates total landed cost.
    """
    DE_MINIMIS_LIMITS = {
        "US": 800.0,
        "GB": 175.0,
        "DE": 160.0,
        "CA": 20.0,
        "AU": 650.0
    }

    TARIFF_RATES = {
        "8509": 0.045,  # Vacuum cleaners / electro-mechanical domestic appliances
        "8525": 0.030,  # Cameras / transmission apparatus
        "8504": 0.025   # Power stations / inverters
    }

    def calculate_customs_tariff(self, product_value_usd: float = 799.0, hs_code_prefix: str = "8509", destination_country: str = "GB", shipping_fee_usd: float = 45.0) -> Dict[str, Any]:
        dest = destination_country.upper()
        de_minimis = self.DE_MINIMIS_LIMITS.get(dest, 150.0)
        duty_exempt = (product_value_usd <= de_minimis)

        tariff_rate = self.TARIFF_RATES.get(hs_code_prefix, 0.04) if not duty_exempt else 0.0
        duty_amount = round(product_value_usd * tariff_rate, 2)

        # Import VAT (e.g. 20% UK, 19% DE)
        vat_rate = 0.20 if dest == "GB" else 0.19 if dest == "DE" else 0.08
        cif_value = product_value_usd + shipping_fee_usd + duty_amount
        import_vat = round(cif_value * vat_rate, 2)
        total_landed_cost = round(cif_value + import_vat, 2)

        return {
            "calculation_id": "trf_cst_7719",
            "product_value_usd": product_value_usd,
            "destination_country": dest,
            "hs_code_chapter": hs_code_prefix,
            "de_minimis_threshold_usd": de_minimis,
            "duty_exempt_status": duty_exempt,
            "applicable_tariff_rate": f"{tariff_rate*100:.1f}%",
            "customs_duty_amount_usd": duty_amount,
            "import_vat_amount_usd": import_vat,
            "shipping_fee_usd": shipping_fee_usd,
            "total_landed_cost_usd": total_landed_cost
        }
