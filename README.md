# DeepThought Business Analytics Assignment Submission

This repository contains the target market profiling data (Part A) and the automated operational scale-up framework (Part B) for the Business Analytics Internship selection process at DeepThought.

## Part A: Sourcing & Profiling Methodology

### 1. Strategic Focus Parameters
* **Target Hub Focus:** Pune, Maharashtra. Selected due to its intensive concentration of advanced automotive toolrooms, custom engineering fabs, and specialty performance polymer clusters.
* **Industry Classifications Studied:**
  * **Basket C — Precision Auto Components & Engineering**
  * **Basket A — Performance Chemicals**

### 2. Systematic Sourcing & Data Extraction Funnel
1. **Corporate Registry Ingestion:** Queried active corporate listings via corporate tracking databases to isolate active private limited companies operating in Pune under relevant NIC manufacturing codes, keeping targets aligned with the ₹50Cr–₹500Cr revenue parameter.
2. **Regional Industrial Chamber Mapping:** Programmatically mapped the member indices of the **Mahratta Chamber of Commerce, Industries and Agriculture (MCCIA)** under advanced tooling and specialty chemical tracks.
3. **Operational Signaling Filters:** Monitored local job board platforms (Naukri, LinkedIn Jobs) to flag mid-market manufacturing companies in the Pune region actively searching for specialized system roles like "SAP Business One Administrator" or "Production Planner".

### 3. AI-Assisted Qualification & Verification Guardrails
* **Web Scraping Execution:** Raw data was parsed directly from the "Infrastructure", "Machinery Fleet", "Certifications", and "About Us" pages of targeted enterprise websites.
* **Schema-Constrained LLM Prompting:** Raw unstructured text blocks were routed through an automated prompt model to extract explicit facts corresponding to the six criteria.
* **Public Record Validation:** Financial bands, incorporation details, and directorship modifications were cross-verified using public regulatory data tools like Zauba Corp and Tofler.

---

## Part B: The 1,000-Company Scale-Up Proposal

### 1. Ingesting the Top-of-Funnel Universe
To deliver 1,000 highly qualified, verified "Federer" accounts within 30 days, we must initiate a top-of-funnel database of roughly **3,500 to 4,000 raw industrial prospects** to absorb a projected ~25-30% final verification yield.
* **Data Sources:** Execute systematic data extraction via the **Tofler / Zauba Corp API** to query all manufacturing firms across designated industrial clusters featuring an active revenue range between ₹50Cr and ₹500Cr.
* **Specialized Registries:** Extract member lists from the **Engineering Export Promotion Council (EEPC)** and the **Chemical Export Promotion Council (CHEMEXCIL)**.

### 2. Automated Multi-Stage Qualification Pipeline
* **Stage 1: The Gateway Script (Python):** Automatically pings candidate domains to weed out trading terms (*"wholesaler", "authorized dealer", "distributor"*).
* **Stage 2: Text Extraction & LLM Synthesis Engine:** Parses technical indicators (`C3` through `C8`) using the **Gemini 3.5 Flash API**.
* **Stage 3: Organizational Architecture Verification:** Run a script against the LinkedIn Talent Insights API to assess organizational structure and verify systems roles to confirm operational maturity.

### 3. 4-Week Phased Operational Blueprint
* **Week 1:** Configure python scraper frameworks and populate the initial pool of 3,500 raw industrial prospects.
* **Week 2:** Run the qualification scripts and execute regular expression filters to remove trading firms.
* **Week 3:** Isolate the mid-tier borderline profiles (scores between 55 and 75) and enrich missing data points via targeted LinkedIn and MCA directory lookups.
* **Week 4:** Perform final quality checks on the highest priority A-band accounts and generate personalized outreach hooks.
