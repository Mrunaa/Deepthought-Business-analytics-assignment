#!/usr/bin/env python3
"""
DeepThought Sourcing Pipeline Engine
Automated evaluation framework for screening B2B target prospects against the Federer Profile.
"""

class FedererSourcingEngine:
    def __init__(self, target_city: str, rejected_keywords: list):
        self.target_city = target_city.lower()
        self.rejected_keywords = [word.lower() for word in rejected_keywords]

    def evaluate_eligibility_gates(self, company_profile: dict) -> dict:
        location = company_profile.get("location", "").lower()
        web_text = company_profile.get("scraped_text", "").lower()
        
        if self.target_city not in location:
            return {"status": "FAIL", "reason": "Gate E2 Failure: Operational center outside target hub."}
            
        for keyword in self.rejected_keywords:
            if keyword in web_text:
                return {"status": "FAIL", "reason": f"Gate E1 Failure: Found trading keyword '{keyword}'."}
                
        if "service provider" in web_text and not any(w in web_text for w in ["factory", "plant", "manufacturing", "cnc"]):
            return {"status": "FAIL", "reason": "Gate E1 Failure: Pure service architecture without asset base."}

        return {"status": "PASS", "reason": "Passed eligibility screening gates."}

    def compute_federer_score(self, evaluation_metrics: dict) -> dict:
        weights = {
            "C3_differentiated": 20,
            "C4_decision_maker": 15,
            "C5_growing_sector": 15,
            "C6_growth_signals": 15,
            "C7_systems_maturity": 20,
            "C8_succession": 15
        }
        
        total_score = 0
        for criterion, weight in weights.items():
            rating = evaluation_metrics.get(criterion, "weak").lower()
            if rating == "strong":
                points = weight
            elif rating == "moderate":
                points = weight / 2
            else:
                points = 0
            total_score += points
            
        band = "A" if total_score >= 80 else ("B" if total_score >= 60 else "C")
        return {"total_score": total_score, "band": band}

if __name__ == "__main__":
    trader_keywords = ["distributor", "authorized dealer", "trader", "importer", "wholesaler"]
    engine = FedererSourcingEngine(target_city="Pune", rejected_keywords=trader_keywords)
    print("Sourcing pipeline engine initialized successfully.")
